from django.urls import path
from .views import posts, post_add, post_detail, post_update, post_delete

app_name = 'main'
urlpatterns = [
    path('', posts, name='posts'),
    path('posts/', post_add, name='create_post'),
    path('posts/<int:pk>/', post_detail, name='post_detail'),
    path('posts/<int:pk>/update/', post_update, name='post_update'),
    path('posts/<int:pk>/delete/', post_delete, name='post_delete'),
]


