from django import forms
from . import models

class LoginForm(forms.Form):
    class Meta:
        model = models.