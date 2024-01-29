from . import views
from django.urls import path


urlpatterns=[

    path('create_post.html/', views.create_post, name='create_post'),
    path('display_posts.html/', views.display_posts, name='display_posts'),

    path('post/<int:pk>/', views.posts, name='posts'),
    path('', views.index, name='index'),
    
    
]