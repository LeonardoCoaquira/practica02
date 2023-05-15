from django.urls import path,include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'post',views.PostViewSet,basename='post')

urlpatterns = [
    path('',views.IndexView.as_view()),
    path('categoria',views.CategoriaView.as_view()),
    path('categoria/<int:categoria_id>',views.CategoriaDetailView.as_view()),
    path('admin/',include(router.urls)),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:post_id>/', views.PostDetailView.as_view(), name='post-detail'),
]