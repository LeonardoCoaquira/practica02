from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets

from blog.models import Categoria,Post
from .serializers import (
    CategoriaSerializer,
    PostSerializer
)

class IndexView(APIView):
    
    def get(self,request):
        lista_categorias = Categoria.objects.all()
        serializer_categoria = CategoriaSerializer(lista_categorias,many=True)
        return Response(serializer_categoria.data)
    
class CategoriaView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    lookup_url_kwarg  = 'categoria_id'
    serializer_class = CategoriaSerializer
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    lookup_url_kwarg = 'post_id'
    serializer_class = PostSerializer