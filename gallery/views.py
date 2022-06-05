from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .forms import GalleryUploadForm
from django.http import HttpResponseRedirect
from .models import Gallery


class ListGallery(ListView):
    model = Gallery
    template_name = 'gallery/list_file.html'
    context_object_name = 'records'


class CreateGalleryView(CreateView):
    model = Gallery
    # form_class = GalleryUploadForm  # если писать так, надо в файле forms сделать наследование от ModelFolm
    fields = '__all__'      # если писать так, forms менять не надо
    template_name = 'gallery/load_file.html'
    success_url = '/load_image'
