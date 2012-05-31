from django import forms

class LoginForm(forms.Form):
  username = forms.CharField(label="Your DCE")
  password = forms.CharField(widget=forms.PasswordInput, label="Your RIT Password")
