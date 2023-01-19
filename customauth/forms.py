from pdb import post_mortem
from django import forms
from django.contrib.auth.forms import UserCreationForm
#from .models import User
from django.contrib.auth import get_user_model
from .models import User



    

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    password1 = forms.CharField(widget=forms.PasswordInput)

    

    class Meta(UserCreationForm.Meta):
        model = User
       # user = User.objects.get(pk=post_mortem['username'])
        fields = ["username","email", "nickname",]
        
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'username' : forms.TextInput(attrs={'class':'form-control', 'value': '','id':'current_user','type':'hidden'}),
            }
