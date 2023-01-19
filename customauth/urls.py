from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views



app_name = 'customauth'  #the weird code
urlpatterns = [
    
    #path('signin/', views.signIn),
    # path('signup/', views.signUp),
    path('signup/', views.signup_inpage, name='signup'),
    #path('signup/', include(signup_inpage))
    path('signin/', auth_views.LoginView.as_view(template_name='auth/signin.html'), name='signin'),
]