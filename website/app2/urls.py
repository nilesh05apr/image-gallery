from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.manage_post, name="manage_post"),
]