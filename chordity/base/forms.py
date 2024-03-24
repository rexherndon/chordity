from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        # later on, should really be more like "fields = ['name', 'desc', 'topic'] etc"
        fields = "__all__"
        exclude = ["host", "participants"]
        

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']