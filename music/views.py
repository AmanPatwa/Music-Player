from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Album,Song
from .forms import SongForm
from django.db.models import Q

# def detail(request, pk):
#     album = get_object_or_404(Album,pk = pk)
#     return render(request,'music/detail.html',{album:album})
AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg','mp4']
# class IndexView(ListView):
#     template_name = 'music/index.html'
#     model = Album
#     context_object_name = 'albums'


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

def add_song(request, album_id):
    sform = SongForm(request.POST or None, request.FILES or None)
    album = get_object_or_404(Album,pk = album_id)
    if sform.is_valid():
        song = sform.save(commit = False)
        song.album = album
        song.audio_file = request.FILES['audio_file']
        file_type = song.audio_file.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in AUDIO_FILE_TYPES:
            context = {
                'album': album,
                'form': sform,
                'error_message': 'Audio file must be WAV, MP3, or OGG',
            }
            return render(request, 'music/add_song.html', context)
        song.file_type = file_type
        song.save()
        context = {
            'album':album
        }
        return redirect('music:detail', pk = album.pk)
    context = {
        'form' : sform,
        'album' : album
    }
    return render(request,'music/add_song.html',context)

def delete_song(request,album_id,song_id):
    album = get_object_or_404(Album,pk=album_id)
    song = Song.objects.get(pk=song_id)
    song.delete()
    return render(request,'music/detail.html',{'album':album}) 

def favourite_song(request,album_id,song_id):
    album = get_object_or_404(Album,pk=album_id)
    song = Song.objects.get(pk=song_id)
    if song.is_favourite:
        song.is_favourite = False
    else:
        song.is_favourite = True
    song.save()
    return redirect('music:detail',pk = album.pk)

def favourite_album(request,album_id):
    album = Album.objects.get(pk=album_id)
    if album.is_favourite:
        album.is_favourite = False
    else:
        album.is_favourite = True
    album.save()
    return redirect('music:index')

def songs(request,type):
    try:
        song_ids = []
        for album in Album.objects.all():
            for song in album.song_set.all():
                song_ids.append(song.id)
        song = Song.objects.filter(pk__in = song_ids)
        if type == 'fav':
            song = song.filter(is_favourite = True)
    except Album.DoesNotExist:
        song = []
    return render(request,'music/songs.html',{
        'songs': song,
        'type' : type
    })

def index(request):
    albums = Album.objects.all()
    songs = Song.objects.all()
    query = request.GET.get('q')
    if query:
        albums = albums.filter(
            Q(album_title__icontains = query) |
            Q(artist__icontains = query)
        ).distinct()
        songs = songs.filter(
            song_title__icontains = query
        ).distinct()
        return render(request, 'music/index.html',{
            'albums':albums,
            'songs' : songs
        })
    else:
        return render(request, 'music/index.html', {'albums': albums})

