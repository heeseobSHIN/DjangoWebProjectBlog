from django.db import models
from django.contrib.auth.models import AbstractUser
# from .forms import forms







class User(AbstractUser):
    username = models.CharField(max_length=10, name='username', unique=True, null= False)
    password = models.CharField(max_length=300, name='password1', null= False)
    email = models.EmailField(max_length=40, name='email', unique=True, null= False)
    nickname = models.CharField(max_length=8, name='nickname', null= True)
    user_icon = models.ImageField(upload_to='blog/images/user_icon/%Y/%m/%d/',null=True, blank=True)
    intro = models.TextField(null=True, blank=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return f'{self.username}'
    
    def get_absolute_url(self):
        return f'/blog/user_detail/{self.pk}/'
    
    def sample_view(request):
        current_user = request.user
        return current_user
    


