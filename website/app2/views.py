from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from .models import Post
from .forms import PostForm
from django.forms import modelformset_factory

# Create your views here.



class Home(TemplateView):
    template_name = 'index.html'

def file_upload(request):
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        Post.objects.create(image=my_file)
        return HttpResponse('')
    return JsonResponse({'post':'false'})

def manage_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None)
        if form.is_valid():
            imageFile = form.cleaned_data['image']
            name = form.cleaned_data['name']
            Post.objects.create(image=imageFile,name=name)
            form.save()
    else:
        form = PostForm()
    return render(request,'app2/index.html',{'form': form})