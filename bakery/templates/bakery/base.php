{% load staticfiles %}

<html>
    <head>
        <title>The Little Bakery</title>

        <meta http-equiv="Content-Type" content="text/html; charset=windows-1252">

        <meta name="viewport" content="width=device-width,initial-scale=1.0">
         <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
        <!-- jQuery library -->
        <script src="{% static 'downloads/jquery.min.js.download' %}"></script>
        <script src="{% static 'jquery/jquery.min.js' %}"></script>
        <script src="{% static 'jquery/jquery.js' %}"></script>
        <script src="{% static 'javascript/javascript.js' %}"></script>

        <!-- Latest compiled JavaScript -->
        <script src="{% static 'downloads/bootstrap.min.js.download' %}"></script>
        <!-- stylesheet -->
        <link rel="stylesheet" href="{% static 'css/stylesheet.css' %}">
        <!-- Font -->
        <link href="https://fonts.googleapis.com/css?family=Sofia" rel="stylesheet">
        <script>
            $(document).ready(function(){
                $("#commenters").on("click", ".reply", function(event){
                    event.preventDefault();
                    var form = $("#postcomment").clone(true);
                    form.find('.parent').val($(this).parent().parent().attr('id'));
                    $(this).parent().append(form);
                });
            });
        </script>
    </head>
    <body>
        <div class='header'>
          <div id="header-bar">
            <p class="banner-text"><a href="{% url 'index'%}">The Little Bakery</a></p>
          </div>
          <nav class="navbar navbar-style"  data-spy="affix" data-offset-top="100">
            <div class="container-fluid">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="{% url 'index'%}">The Little Bakery</a>
            </div>
            <div class="collapse navbar-collapse" id="myNavbar">
              <ul class="nav navbar-nav">
                <li><a href="{% url 'cakes_cupcakes'%}">Cakes & Cupcakes</a></li>
                <li><a href="{% url 'pies'%}">Pies</a></li>
                <li><a href="{% url 'cookies'%}">Cookies</a></li>
                <li><a href="{% url 'baked-goods'%}">Other Baked goods</a></li>
                {% if user.is_authenticated %}
                    <li><a href="{% url 'users'%}">Users</a></li>
                {%else%}
                  <li><a href="{% url 'liked_list'%}">Liked recipes</a></li>
                {% endif %}
                  <li><a href="{% url 'add_recipe'%}">Submit you own recipe</a></li>
              </ul>
              <form class="navbar-form navbar-left" action="">
                 <div class="input-group">
                   <form method="get" action="/search/">
                       <input type="text" placeholder=" Search for recipes" name="q" id="id_q" value="{{ query }}"/>
                       <input class="search-but" type="submit" value="Search" />
                    </form>
                 </div>
               </form>

              <ul class="nav navbar-nav navbar-right">
                {% if user.is_authenticated %}


                  <li><a href="{% url 'userProfile' user.username %}" data-toggle="modal"><span class="glyphicon glyphicon-user"></span> Profile</a></li>
                  <li><a href="{% url 'logout' %}" data-toggle="modal"><span class="glyphicon glyphicon-off"></span> logout</a></li>
                {% else %}
                <li><a href="{% url 'registration_form' %}" data-toggle="modal"><span class="glyphicon glyphicon-user"></span> Sign Up</a></li>
                <li><a href="{% url 'login_page' %}" data-toggle="modal"><span class="glyphicon glyphicon-log-in"></span> Login</a></li>
                {% endif %}
              </ul>
            </div>
            </div>
          </nav>
        </div>
        <div class="content container">


            {% block content %}
            {% endblock %}
            <!-- Knockout -->
            <script src="{% static 'javascript/knockout-3.4.2.js' %}"></script>
            <!-- JavaScript to add recipe -->
            <script src="{% static 'javascript/add_recipe.js' %}"></script>
            <!-- stylesheet -->
        </div>

    </body>
</html>
