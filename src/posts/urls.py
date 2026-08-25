from django.urls import path
from posts.views import BlogHome, BlogPostCreate, BlogPostDetail, BlogPostUpdate,BlodPostDelete
 # from django.contrib.auth.decorators import login_required 

app_name = 'posts'

urlpatterns = [
    path('',BlogHome.as_view(),name='home'),
    # path('create/',login_required(BlogPostCreate.as_view()),name='create'),  > premiere methode pour restreindre l'acces à une page
    path('create/',BlogPostCreate.as_view(),name='create'),
    path('edit/<str:slug>/',BlogPostUpdate.as_view(),name='edit'),
    path('<str:slug>/',BlogPostDetail.as_view(),name='post'),
    path('delete/<str:slug>/',BlodPostDelete.as_view(),name='delete'),
]