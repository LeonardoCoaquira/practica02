from django.shortcuts import render, get_object_or_404
from django.shortcuts import get_object_or_404

from .models import *

# Create your views here.
def index(request):
    post_list = Post.objects.order_by('titulo')[:6]
    categorias_list = Categoria.objects.all()
    context = {
        'posts': post_list,
        'categorias': categorias_list
    }
    return render(request,'index.html',context)


def post(request, post_id):
    post = get_object_or_404(Post, pk=producto_id)
    categorias_list = Categoria.objects.all()
    return render(request,'post.html',{'post':post,'categorias': categorias_list})

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(pk=categoria_id)
    lista_posts = categoria.post_set.all()
    lista_categorias = Categoria.objects.all()

    context = {
        'posts': lista_posts,
        'categorias':lista_categorias,
        'categoria':categoria
    }
    
    return render(request,'index.html',context)