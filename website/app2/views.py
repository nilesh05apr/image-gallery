from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from .models import Post
# Create your views here.

def display(request):
    return render(request,'app2/index.html')

class Home(TemplateView):
    template_name = 'index.html'

def file_upload(request):
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        Post.objects.create(image=my_file)
        return HttpResponse('')
    return JsonResponse({'post':'false'})
