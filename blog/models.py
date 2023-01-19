from datetime import *
from django.utils import timezone
from django.db import models
import os
from customauth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_delete


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode = True)
    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'
    
    
    # class Meta:
    #     verbose_name_plural = 'Tag' # 이름 재설정

class Category(models.Model):
    name = models.CharField(max_length=50, unique= True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode = True)
    
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'
    
    
    class Meta:
        verbose_name_plural = 'Categories' # 이름 재설정
    
    
now = timezone.now()

class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    head_image = models.ImageField(upload_to='blog/images/head_images/%Y/%m/%d/',null=True, blank=True)
    file_upload = models.FileField(upload_to='blog/files/add_file/%Y/%m/%d', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.ForeignKey(User, null= False ,blank=True ,on_delete=models.CASCADE)
    content_image = models.ImageField(upload_to='blog/images/content_images/%Y/%m/%d/',null=True, blank=True)
    pub_date = models.DateTimeField('PUBLISH DATE', default=timezone.now)
    mod_date = models.DateTimeField('MODIFY DATE', auto_now=True)
    category = models.ForeignKey(Category, null= True ,blank=True ,on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank= True) #null은 default로 True
    like = models.IntegerField(null=True, blank=True, )
    
    
    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/blog/detail/{self.pk}/'
    
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
    
    def get_previous(self):
        return self.get_previous_by_mod_date()

    def get_next(self):
        return self.get_next_by_mod_date()
    
    def sample_view(request):
        current_user = request.user
        return current_user


@receiver(post_delete, sender=Post)
def submission_delete(sender, instance, **kwargs):
    instance.head_image.delete(False)



class Comment(models.Model):
    
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.ForeignKey(User, null = True, on_delete=models.SET_NULL)
    title = models.ForeignKey(Post, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'[{self.pk}][{self.post.pk}] {self.author}'
    
    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'
    