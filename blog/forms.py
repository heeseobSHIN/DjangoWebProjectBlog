from django import forms
from .models import Comment, Post
from django import forms

class CommentForm(forms.ModelForm):
    
    class meta:
        model = Comment
        filed = ('content', )
        
class PostCreateForm(forms.Form):
    email = forms.EmailField(label="이메일")
    password1 = forms.CharField(widget=forms.PasswordInput)

    

    class Meta(forms.Form):
        model = Post
       # user = User.objects.get(pk=post_mortem['username'])
        fields = ['username','email', 'nickname', 'user_icon', 'intro', 'password']
        
        widgets = {
            'password' : forms.PasswordInput(attrs={'class':'form-control', 'value': '','type':'hidden'}),
            'username' : forms.TextInput(attrs={'class':'form-control', 'value': '','id':'current_user','type':'hidden'}),
            }
