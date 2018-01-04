from django.db import models
from django.utils import timezone


class Recipes(models.Model):
    bakeChoices = (('CAKES', 'cakes & cupcakes'),
     ('PIES', 'pies'), ('COOKIES', 'cookies'), ('OTHER', 'other'))

    title= models.CharField(max_length=30)
    imageDir = models.CharField(max_length=100)
    caption = models.CharField(max_length=40)
    text = models.TextField(max_length=200, default="")
    bakeType = models.CharField(max_length=10, choices=bakeChoices, default="CAKES")
    serve = models.CharField(max_length=2)
    prepTime = models.CharField(max_length=20)
    cookTime = models.CharField(max_length=30)
    kcal = models.CharField(max_length=10, default=0)
    fat = models.CharField(max_length=10, default=0)
    carbs = models.CharField(max_length=10, default=0)
    sugar = models.CharField(max_length=10, default=0)
    protein = models.CharField(max_length=10, default=0)
    salt = models.CharField(max_length=10, default=0)
    ingredients = models.TextField(max_length=9000)
    recipe = models.TextField(max_length=9000)
    rating = models.IntegerField(default=0)
    numberOfVotes = models.IntegerField(default=0)
    totalRating = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.created_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title
 
class Comment(models.Model):
    Ratings = [
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
            ]
    recipe = models.ForeignKey('bakery.Recipes', related_name='comments')
    name = models.CharField(max_length=200)
    text = models.TextField()
    rate = models.CharField(max_length=1, choices=Ratings, default="0")
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    
class NewUsers(models.Model):
   author = models.CharField(max_length=200)
   email = models.CharField(max_length=200)
   password = models.CharField(max_length=50)

   def publish(self):
        self.save()


   def __str__(self):
        return self.author
