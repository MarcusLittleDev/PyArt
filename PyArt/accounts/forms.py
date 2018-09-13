from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms

class UserCreateForm(UserCreationForm):
    email = forms.CharField(max_length=255, required=True)
    class Meta: 
        fields = ('username', 'email', 'password1', 'password2')
        model = User

        def __init__(self, *args, **kwargs):
            super().__init__(self, *args, **kwargs) 
            self.fields['username'].label = 'Display Name'
            self.fields['email'].label = 'Email Address'  

class UpdateProfileForm(forms.ModelForm):
    email = forms.CharField(max_length=255, required=True)
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')

        def __init__(self, *args, **kwargs):

            super(UpdateProfileForm, self).__init__(*args, **kwargs) 
            self.fields['username'].label = 'Display Name'
            self.fields['email'].label = 'Email Address'  

    def clean(self):
        username = self.cleaned_data['email']
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exclude(email=self.initial['email']).exists():
            raise forms.ValidationError("A user with that email already exists")

        if User.objects.filter(username=username).exclude(username=self.initial['username']).exists():
            raise forms.ValidationError("A user with that email already exists")

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User



