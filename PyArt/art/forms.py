from django import forms
from . import models

class ArtUploadForm(forms.ModelForm):
    class Meta: 
        fields = ('name', 'description', 'taking_request')
        model = models.Art

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['taking_request'].label = 'Are you taking request for this Art?'

class PictureForm(forms.ModelForm):
    class Meta:
        fields = ('picture',)
        model = models.Picture

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['picture'].label = 'Image'
