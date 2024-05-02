from django.forms import ModelForm

# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User, Survey


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["name", "username", "email", "password1", "password2"]


class RoomForm(ModelForm):
    class Meta:
        model = Room
        # later on, should really be more like "fields = ['name', 'desc', 'topic'] etc"
        fields = "__all__"
        exclude = ["host", "participants"]


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["avatar", "name", "username", "email", "bio"]
        
        
class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fields = ["q1", "q2"]
