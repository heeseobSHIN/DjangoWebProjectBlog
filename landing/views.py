from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.utils.text import slugify
from blog.models import Post, User, Category
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.core.exceptions import PermissionDenied
from datetime import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# def landing(request):
#     return render(
#         request,
#        'main/landing.html',
#     )
    
class Landing(ListView):
    model = Post # 해당 html 템플릿에서 클래스 이름으로 수정하면 자동으로 표기
    ordering = '-created_at'
    template_name = 'main/landing.html'
   #(템프릿 호출 안해도 post_list.html을 자동으로 찾는다.)\
    
    def get_context_data(self, **kwargs):
        context = super(Landing, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count']= Post.objects.filter(category = None).count()
        context['current_page'] = 'blog'
        return context
    
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

