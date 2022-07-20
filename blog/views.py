from operator import truediv
from django.shortcuts import render,get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render (request, 'blog/home.html', context)

class PostListView(ListView):                                       #used to create list views on our website
    model = Post                                                    #model on which itertions will be done, here(post table)
    template_name = 'blog/home.html'                                #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'                                   #name for the variable our logic will be looping over, the default name is object
    ordering = ['-date_posted']                                     #ordering the posts according to the latest to oldest posts
    paginate_by=2                                                   #this will provide pagination to our website, also this will pass some parameters the html file that is called from here that is pagination object, is_paginated etc

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'
    context_object_name = 'posts'
    paginate_by = 2
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):                                   #used to create detailed views on the website
    model = Post                                                    #model from which details will be gathered

class PostCreateView(LoginRequiredMixin,CreateView):                                   #used to make create views on our website 
    model = Post                                                    #model on which the new item(here post) will be created, basically this tells to which model we should save our newly created post, like title, content
    fields = ['title','content']                                    #these are the fields our form will have to create a new post

    def form_valid(self, form):
        form.instance.author = self.request.user                    #sets the author of the for the current isntance equal to current user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):                                                            #this function is run every time an update request if made to check if the uer updateding the post is the author of the post
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url= '/'
    def test_func(self):                                                            #this function is run every time an update request if made to check if the uer updateding the post is the author of the post
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render (request, 'blog/about.html', {'title':'About'})
