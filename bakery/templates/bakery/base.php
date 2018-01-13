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
                <li><a href="{% url 'liked_list'%}">Liked recipes</a></li>
              </ul>
              <form class="navbar-form navbar-left" action="">
                 <div class="input-group">
                   <input type="text" class="form-control" placeholder="Search">
                   <div class="input-group-btn">
                     <button class="btn btn-default" type="submit">
                       <i class="glyphicon glyphicon-search"></i>
                     </button>
                   </div>
                 </div>
               </form>
              <ul class="nav navbar-nav navbar-right">
                {% if user.is_authenticated %}
                  <li><a href="{% url 'profiles'%}" data-toggle="modal"><span class="glyphicon glyphicon-user"></span> Profile</a></li>
                  <li><a href="{% url 'logout' %}" data-toggle="modal"><span class="glyphicon glyphicon-off"></span> logout</a></li>
                {% else %}
                <li><a href="{% url 'registration_form'%}" data-toggle="modal"><span class="glyphicon glyphicon-user"></span> Sign Up</a></li>
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
        </div>
        <!-- log in field-->
        <!--
				<div class="modal fade" id="login" role="dialog">
					<div class="modal-dialog modal-sm">
					  <div class="modal-content">
						<div class="modal-header">
						  <button type="button" class="close" data-dismiss="modal">&times;</button>
						  <h4 class="modal-title">Log in</h4>
						</div>
						<div class="modal-body">
							<form>
								  <div class="form-group">
									<label for="user">Username</label>
									<input type="username" class="form-control" name="user" required>
								  </div>
								  <div class="form-group">
									<label for="pwd">Password</label>
									<input type="password" class="form-control" name="pwd" required>
								  </div>
								  <div class="checkbox">
									<label><input type="checkbox">Remember me</label>
								  </div>
								  <button type="submit" class="button" onClick="login(this.form)">Log in</button>
							</form>
						</div>
					  </div>
					</div>
				  </div>
        -->
				  <!-- sign in field-->
          <!--
				<div class="modal fade" id="signin" role="dialog">
					<div class="modal-dialog modal-sm">
					  <div class="modal-content">
						<div class="modal-header">
						  <button type="button" class="close" data-dismiss="modal">&times;</button>
						  <h4 class="modal-title">Sign in</h4>
						</div>
						<div class="modal-body">
							<form>
								  <div class="form-group">
									<label for="email">Email address</label>
									<input type="email" class="form-control" id="email" required>
								  </div>
								  <div class="form-group">
									<label for="pwd">Password</label>
									<input type="password" class="form-control" id="pwd" required>
								  </div>
								  <div class="checkbox">
									<label><input type="checkbox">Remember me</label>
								  </div>
								  <button type="submit" class="button" onClick="alert('you can't sign in at the moment')">sign in</button>
							</form>
						</div>
					  </div>
					</div>
        </div> -->
    </body>
</html>
