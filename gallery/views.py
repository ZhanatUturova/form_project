from django.shortcuts import render
from django.views import View

# Create your views here.
class GalleryView(View):
    def get(self, request):
        return render(request, 'gallery/load_file.html')

    def post(self, request):
        pass