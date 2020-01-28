from django import forms

from .models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('name', 'surname', 'date_of_birth', 'login',)
