from django.http import request
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    TemplateView, ListView, DeleteView, DetailView, CreateView, UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
# Create your views here.

class AboutView(TemplateView):
    template_name = 'appOne/about.html'
    def get(self,request):
        return render(request,'appOne/about.html',{'insert_me':'<will not convert to html code>'})


class PostListView(ListView):
    # template_name = 'posts.html'
    model = Post

    # sql query
    # lte is less than or equal to
    # field lookups in documnentation
    # ? https://docs.djangoproject.com/en/3.1/topics/db/queries/
    # * files__lookuptype=value eg:- published_date__lte=timeone.now()
    # * which is equals to the following sql query
    # ? SELECT * FROM Post WHERE published_date <= CURDATE() ORDER BY published_date;

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'appOne/post_detail.html'
    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'appOne/post_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class PostDraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = '/appone/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')

# --------------------------------------------------------
# --------------------------------------------------------


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def add_comments_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'appOne/comment_form.html', {'form': form})


@login_required
def comment_approved(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    # the above line is must as we delete the comment Django will not know where to redirect
    comment.delete()
    return redirect('post_detail', pk=post_pk)


@login_required
def comment_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish
    return redirect('post_detail', pk=pk)
