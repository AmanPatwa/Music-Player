from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'music'
urlpatterns = [
    path('',views.index,name = 'index'),
    path('<int:pk>/',views.AlbumDetailView.as_view(),name = 'detail'),
    path('album/add/',views.AlbumCreateView.as_view(),name = "add-album"),
    path('album/update/<int:pk>',views.AlbumUpdateView.as_view(),name = "update-album"),
    path('album/<int:pk>/delete/',views.AlbumDeleteView.as_view(),name = "delete-album"),
    path('<int:album_id>/song/add/',views.add_song,name = 'add-song'),
    path('<int:album_id>/song/delete/<int:song_id>',views.delete_song,name = 'remove-song'),
    path('<int:album_id>/song/favourite/<int:song_id>',views.favourite_song,name = 'favourite-song'),
    path('album/favourite/<int:album_id>',views.favourite_album,name = 'favourite-album'),
    path('songs/<str:type>',views.songs,name = 'songs'),

]
