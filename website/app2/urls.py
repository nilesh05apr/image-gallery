from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.display_post,name='display_post'),
    path('add',views.manage_post, name='manage_post'),
    path('<int:p_id>',views.delete_post,name='delete'),
    path('like/<int:p_id>',views.increment_likes,name='like')
]