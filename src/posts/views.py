
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from posts.models import BlogPost



class BlogHome(ListView):
    model = BlogPost
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset        
        return queryset.filter(published=True)
    
@method_decorator(login_required, name='dispatch') # seconde methode pour restreindre l'acces à un page
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = 'posts/blogpost_create.html'
    fields = ['title', 'content', ]

@method_decorator(login_required, name='dispatch')
class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = 'posts/blogpost_edit.html'
    fields = ['title', 'content', 'published', ]


class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = 'post'

@method_decorator(login_required, name='dispatch')
class BlodPostDelete(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('posts:home')
    context_object_name = 'post'
