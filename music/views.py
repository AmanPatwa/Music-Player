from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Album,Song

# def index(request):
#     all_albums = Album.objects.all()
#     context = {
#         'albums':all_albums
#     }
#     return render(request,'music/index.html',context)

# def detail(request, pk):
#     album = get_object_or_404(Album,pk = pk)
#     return render(request,'music/detail.html',{album:album})

class IndexView(ListView):
    template_name = 'music/index.html'
    model = Album
    context_object_name = 'albums'


class AlbumDetailView(DetailView):
    model = Album
    context_object_name = 'album'
    template_name = "music/detail.html"


class AlbumCreateView(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']
    template_name = "music/album_form.html"


class AlbumUpdateView(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']
    template_name = "music/album_form.html"

class AlbumDeleteView(DeleteView):
    model = Album
    success_url = '/music/'

def add_song(request):
    pass