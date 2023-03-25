from dataclasses import fields
from django.shortcuts import render
from .forms import PostForm

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post

from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class AddStencilView(CreateView):
    form = PostForm
    mydict = {
        'form':form
    }
    model = Post
    template_name = 'stencil_new.html'
    comment = ['manufacture_date', 'stencil_number', 'revision', 'ZLNumber', 'material', 'manufacture_number', 'thickness', 'author']
    fields = ['manufacture_date', 'stencil_number', 'revision', 'ZLNumber', 'material', 'manufacture_number', 'thickness', 'author']
    success_url = reverse_lazy('success')


class SuccessView(ListView):
    model = Post
    template_name = 'success.html'
    
