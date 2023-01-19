from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView
from django.utils.text import slugify
from django.views.generic.detail import SingleObjectMixin
from customauth import views
from .models import Post, User, Category
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.core.exceptions import PermissionDenied
from datetime import *
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import CommentForm
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse



class PostList(ListView):
    model = Post # 해당 html 템플릿에서 클래스 이름으로 수정하면 자동으로 표기
    ordering = '-created_at'
    template_name = '/blog/post_list.html'
   #(템프릿 호출 안해도 post_list.html을 자동으로 찾는다.)\
    
    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count']= Post.objects.filter(category = None).count()
        context['current_page'] = 'blog'
        return context
    
    
class PostDetail(DetailView):
    model = Post 
    ordering = '-pk'
   
    
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        context['current_page'] = 'blog'
        context['comment_form'] = CommentForm
        return context
    
    
        
        

    

       
    
class UserDetail(DetailView):
    model = User
    ordering = '-updated_at'
    template_name= 'blog/user_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(UserDetail, self).get_context_data()
        context['current_user'] = 'user.username'
        context['comment_form'] = CommentForm
        return context
    
    
# def UserDeatil(request):
#     return render(
#         request,
#         template_name= 'C:/Users/starc/JAP_IT/djangoWebTeam/jp_portfolio/templates/blog/user_detail.html'
#     )

def SearchResult(request):
    return render(
        request,
        template_name= 'blog/search_result.html'
    )
    


class MyPageList(ListView):
    
    template_name = 'blog/Mypage.html'
    # p = Post.objects.all()
    context_object_name = 'mypage_list'
    
    
    
    
    # def get_context_data(self, **kwargs):
    #     context = super(MyPageList, self).get_context_data()
        
    #     context['myinfo'] = Post.objects.all()
    #     context['current_page'] = 'blog'
        
    #     return context
    
    def get_queryset(self, **kwargs):       
        queryset = Post.objects.filter(username_id = self.request.user.pk)   
        print(queryset)    
        return queryset
    
   

class postUpdate(UpdateView):
    model = Post
    fields = ['title','content','head_image', 'file_upload', 'content_image', 'category', 'tags', ]
    # success_url = reverse_lazy('/blog/')
    template_name= 'blog/post_edit.html'
    
    
    
    def form_valid(self, form):
        messages.success(self.request, "The post was updated successfully.")
        return super(postUpdate,self).form_valid(form)
    
    


class PostCreate(CreateView):
    model = Post
    fields = ['title','content','head_image','file_upload', 'content_image', 'category', 'tags']
    # success_url = reverse_lazy('tasks')
    template_name= 'blog/post_create.html'
    
   
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The post was created successfully.")
        return super(PostCreate,self).form_valid(form)
    
    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)
    
    
class UserUpdate(UpdateView):
    model = User
    fields = ['username','email', 'nickname', 'user_icon', 'intro']
    # success_url = reverse_lazy('/blog/')
    template_name= 'blog/intro_update.html'
    
    def form_valid(self, form):
        messages.success(self.request, "The post was updated successfully.")
        return super(UserUpdate,self).form_valid(form)
