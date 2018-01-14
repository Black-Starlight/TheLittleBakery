from django.db import models
from django.utils import timezone
from django.core.validators import validate_comma_separated_integer_list
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Recipes(models.Model):
    bakeChoices = (('CAKES', 'cakes & cupcakes'),
     ('PIES', 'pies'), ('COOKIES', 'cookies'), ('OTHER', 'other'))

    title= models.CharField(max_length=30)
    imageDir = models.TextField(null=True, blank=True)
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
    content = models.TextField(default='empty')
    date = models.DateTimeField(default=timezone.now)
    path = models.CharField(validators=[validate_comma_separated_integer_list], blank=True, editable=False, max_length=50)
    depth = models.PositiveSmallIntegerField(default=0)

    def __unicode__(self):
        return self.content


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    favs = models.ForeignKey(Recipes, related_name='%(class)s_favorites', on_delete=models.CASCADE, blank=True, null=True)
    made = models.ForeignKey(Recipes, related_name='%(class)s_made', on_delete=models.CASCADE, blank=True, null=True)
    friends = models.ForeignKey(User, related_name='%(class)s_friends', on_delete=models.CASCADE, blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

    def __str__(self):
        return self.text

    
