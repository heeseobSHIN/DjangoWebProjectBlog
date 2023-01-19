from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    #path('', views.index),
    path("", views.PostList.as_view()),
    path("detail/<int:pk>/", views.PostDetail.as_view(), name = 'detail'),
    path("mypage/", views.MyPageList.as_view(), name='mypage'),
    #path("mypage/", views.Mypage),
    path("username/", views.UserDetail.as_view()),
    path("search/", views.SearchResult),
    path("user_detail/<int:pk>/", views.UserDetail.as_view()),
    path("detail/<int:pk>/edit/", views.postUpdate.as_view(), name= 'update_post'),
    # path("detail/<int:pk>/edit/", views.EditPostF, name= 'update_post'),
    path("create/", views.PostCreate.as_view(), name='create'),
    path("user_detail/<int:pk>/update/", views.UserUpdate.as_view(), name='create'),
]
