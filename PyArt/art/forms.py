from django import forms
from . import models

class ArtUploadForm(forms.ModelForm):
    class Meta: 
        fields = ('name', 'description', 'picture', 'taking_request')
        model = models.Art

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['picture'].label = 'Art'
        self.fields['taking_request'].label = 'Are you taking request for this Art?'