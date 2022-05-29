from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)       # здесь форма заполнена данными
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/done')
    form = FeedbackForm()           # здесь форма пустая
    return render(request, 'feedback/feedback.html', context={'form': form})

def done(request):
    return render(request, 'feedback/done.html')