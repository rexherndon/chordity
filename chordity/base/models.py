from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    
    # path for default image is at static\images
    avatar = models.ImageField(null=True, default="avatar.svg")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] # required for superuser creation

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class Message(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # w/ CASCADE, if a room gets deleted, all the children (ie. - messages) will also get deleted
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    # only returns first 50 characters when initially viewing
    def __str__(self):
        return self.body[0:50]

    # unneeded boilerplate?
    # class Meta:
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    # unneeded boilerplate?
    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
    

# survey
# id - auto generated

class Survey(models.Model):
    
    # on a scale from 1 to 5, how much do you like this app?
    q1 = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    # do you want to provide any additional comments or feedback to help improve the application?
    q2 = models.TextField()
    