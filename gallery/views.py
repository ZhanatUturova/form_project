from django.shortcuts import render
from django.views import View
from .forms import GalleryUploadForm
from django.http import HttpResponseRedirect


def storage_file(file):
    with open(f'gallery_tmp/{file.name}', 'wb+') as new_file:
        for chunk in file.chunks():
            new_file.write(chunk)


class GalleryView(View):
    def get(self, request):
        form = GalleryUploadForm()
        return render(request, 'gallery/load_file.html', {'form': form})

    def post(self, request):
        form = GalleryUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # storage_file(request.FILES['image'])      # можно так обращаться
            storage_file(form.cleaned_data['image'])    # и так тоже можно обращаться
            return HttpResponseRedirect('load_image')
        return render(request, 'gallery/load_file.html', {'form': form})
