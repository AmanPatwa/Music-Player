from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'music'
urlpatterns = [
    path('',views.IndexView.as_view(),name = 'index'),
    path('<int:pk>/',views.AlbumDetailView.as_view(),name = 'detail'),
    path('album/add/',views.AlbumCreateView.as_view(),name = "add-album"),
    path('album/update/<int:pk>',views.AlbumUpdateView.as_view(),name = "update-album"),
    path('album/<int:pk>/delete/',views.AlbumDeleteView.as_view(),name = "delete-album"),
]
