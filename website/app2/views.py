from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from .models import Post
from .forms import PostForm


def manage_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            imageFile = request.FILES['image']
            Name = request.POST.get('name')
            instance = Post(image=imageFile,name=Name)
            instance.save()
            return redirect('display_post')
    else:
        form = PostForm()
    return render(request,'app2/post_form.html',{'form': form})


def display_post(request):
    posts = Post.objects.all()
    return render(request,'app2/display.html',{'posts': posts})
    

def delete_post(request,p_id = None):
    post = Post.objects.get(id=p_id).delete()
    posts = Post.objects.all()
    return render(request,'app2/display.html',{'posts': posts})


def increment_likes(request,p_id = None):
    post = Post.objects.get(id=p_id)
    post.likes += 1
    post.save()
    posts = Post.objects.all()
    return render(request,'app2/display.html',{'posts':posts})