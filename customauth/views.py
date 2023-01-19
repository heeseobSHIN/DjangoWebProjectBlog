from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserForm

def signup_inpage(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            nickname = form.cleaned_data.get('nickname')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, email = email, nickname = nickname,  password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'auth/signup_page.html', {'form': form})


