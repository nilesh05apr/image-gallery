from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.Homepage,name='homepage'),
    path('posts',views.display_post,name='display_post'),
    path('add',views.manage_post, name='manage_post'),
    path('<int:p_id>',views.display_post,name='delete'),
]