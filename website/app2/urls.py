from django.urls import path, include
from . import views
urlpatterns = [
    path('home',views.display_post,name='display_post'),
    path('',views.manage_post, name="manage_post"),
]