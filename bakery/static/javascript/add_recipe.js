//CSRF debug
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


var RecipeViewModel = function () {
    var self = this;

    //values of the input fields
    self.newTitle = ko.observable("");
    self.newImageDir = ko.observable(null);
    self.newCaption = ko.observable("");
    self.newText = ko.observable("");
    self.newBakeType = ko.observable("");
    self.newServe = ko.observable("");
    self.newPrepTime = ko.observable("");
    self.newCookTime = ko.observable("");
    self.newKcal = ko.observable("");
    self.newFat = ko.observable("");
    self.newCarbs = ko.observable("");
    self.newSugar = ko.observable("");
    self.newProtein = ko.observable("");
    self.newSalt = ko.observable("");
    self.newIngredients = ko.observable("");
    self.newRecipe = ko.observable("");




    //submit the recipe
    self.submitRecipe = function () {
        //URL
        var reader = new FileReader();

        reader.addEventListener("load", function () {
            var recipe = {
                title: self.newTitle(),
                imageDir: reader.result,
                caption: self.newCaption(),
                bakeType: self.newBakeType(),
                text: self.newText(),
                bakeType: self.newBakeType(),
                serve: self.newServe(),
                prepTime: self.newPrepTime(),
                cookTime: self.newCookTime(),
                kcal: self.newKcal(),
                fat: self.newFat(),
                carbs: self.newCarbs(),
                sugar: self.newSugar(),
                protein: self.newProtein(),
                salt: self.newSalt(),
                ingredients: self.newIngredients(),
                recipe: self.newRecipe(),

            }
            $.post("http://starpower.pythonanywhere.com/recipes/", recipe())
                .then(function (data) {
                    window.location.replace("/recipe/" + data.pk)
                })
                .fail(function (data) {
                    console.error(data);
                }).done();
            clear(); //clear the input fields after submitting

        }, false);
        reader.readAsDataURL(self.newImageDir())


    }

    //function that clears the input field
    function clear() {
        self.newTitle("");
        self.newImageDir(null);
        self.newCaption("");
        self.newText("");
        self.newServe("");
        self.newPrepTime("");
        self.newCookTime("");
        self.newKcal("");
        self.newFat("");
        self.newCarbs("");
        self.newSugar("");
        self.newProtein("");
        self.newSalt("");
        self.newIngredients("");
        self.newRecipe("");
    }
}


ko.bindingHandlers.fileUpload = {
    init: function (element, valueAccessor) {
        $(element).change(function () {
            valueAccessor()(element.files[0]);
        });
    },
    update: function (element, valueAccessor) {
        if (ko.unwrap(valueAccessor()) === null) {
            $(element).wrap('<form>').closest('form').get(0).reset();
            $(element).unwrap();
        }
    }
};

ko.applyBindings(new RecipeViewModel());
