from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        # later on, should really be more like "fields = ['name', 'desc', 'topic'] etc"
        fields = "__all__"
        exclude = ["host", "participants"]
