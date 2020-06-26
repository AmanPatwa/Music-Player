from django import forms
from .models import Song

class SongForm(forms.ModelForm):
    """Form definition for Song."""

    class Meta:
        """Meta definition for Songform."""

        model = Song
        fields = ('song_title','audio_file')