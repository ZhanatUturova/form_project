from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback
from django.views import View
# Create your views here.

class FeedBackView(View):
    def get(self, request):
        form = FeedbackForm()  # здесь форма пустая
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request):
        form = FeedbackForm(request.POST)  # здесь форма заполнена данными
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
        return render(request, 'feedback/feedback.html', context={'form': form})


class DoneView(View):
    def get(self, request):
        return render(request, 'feedback/done.html')


class FeedBackUpdateView(View):

    def post(self, request, id_feedback: int):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(request.POST, instance=feed)       # instance означает, что мы работает с уже существующей записью
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/{id_feedback}')
        return render(request, 'feedback/feedback.html', context={'form': form})

    def get(self, request, id_feedback: int):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})


# def index(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)       # здесь форма заполнена данными
#         if form.is_valid():
#             print(form.cleaned_data)
#
#             # feed = Feedback(              так нужно писать, когда формы не основаны на моделях
#             #     name=form.cleaned_data['name'],
#             #     surname=form.cleaned_data['surname'],
#             #     feedback=form.cleaned_data['feedback'],
#             #     rating=form.cleaned_data['rating'],
#             # )
#             # feed.save()
#
#             form.save()
#             return HttpResponseRedirect('/done')
#     else:
#         form = FeedbackForm()           # здесь форма пустая
#     return render(request, 'feedback/feedback.html', context={'form': form})

# def done(request):
#     return render(request, 'feedback/done.html')


# def update_feedback(request, id_feedback: int):
#     feed = Feedback.objects.get(id=id_feedback)
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST, instance=feed)       # instance означает, что мы работает с уже существующей записью
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(f'/{id_feedback}')
#     else:
#         form = FeedbackForm(instance=feed)
#     return render(request, 'feedback/feedback.html', context={'form': form})