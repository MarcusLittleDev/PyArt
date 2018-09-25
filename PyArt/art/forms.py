from django import forms
from . import models

class ArtForm(forms.ModelForm):
    taking_request = forms.BooleanField(required=False, initial=False)
    # taking_request.widget = forms.FileInput(attrs={'multiple':True})
    class Meta: 
        fields = ('name', 'description', 'taking_request')
        model = models.Art

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['taking_request'].label = 'Are you taking request for this Art?'

class PictureForm(forms.ModelForm):
    picture = forms.ImageField(required=True,
                                widget=forms.FileInput(attrs={'multiple':True}))
    class Meta:
        fields = ('picture',)
        model = models.Picture

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['picture'].label = 'Image'
