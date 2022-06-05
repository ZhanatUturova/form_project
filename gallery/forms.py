from django import forms
from .models import Gallery


class GalleryUploadForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'

        labels = {  # назначаем названия полей, чтобы не было как в моделях
            'image': 'Картинка',
        }
