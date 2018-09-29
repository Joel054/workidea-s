from django.forms import ModelForm

from core.models import Notification


class FormNotification(ModelForm):
    class Meta:
        model = Notification
        fields = ["__all__"]
