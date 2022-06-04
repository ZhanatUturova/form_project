from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView


# class FeedBackView(FormView):
#     # в шаблоне html надо обязательно обращаться к переменной form!
#     form_class = FeedbackForm  # оператор вызова не нужен!
#     template_name = 'feedback/feedback.html'
#     success_url = '/done'  # URL куда должно быть перенаправление при успешной обработке формы
#
#     # описываем тут, что нужно делать с данными, которые мы получили в форме
#     def form_valid(self, form):
#         form.save()  # проверка на валидность не нужна. Тут форма уже точно валидна
#         return super(FeedBackView, self).form_valid(form)


class FeedBackView(CreateView):
    # в шаблоне html надо обязательно обращаться к переменной form!
    model = Feedback
    # fields = ['name', 'surname', 'feedback']    # список полей, которые надо отобразить в форме (может вызвать ошибку, если не написать обязательное поле по модели
    # fields = '__all__'          # чтобы отображались все поля
    # fields надо прописывать если не использовать form_class!
    form_class = FeedbackForm  # оператор вызова не нужен!
    template_name = 'feedback/feedback.html'
    success_url = '/done'  # URL куда должно быть перенаправление при успешной обработке формы


class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Ivan'
        context['date'] = '23.04.2022'
        return context


class FeedBackUpdateView(View):

    def post(self, request, id_feedback: int):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(request.POST,
                            instance=feed)  # instance означает, что мы работает с уже существующей записью
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/{id_feedback}')
        return render(request, 'feedback/feedback.html', context={'form': form})

    def get(self, request, id_feedback: int):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})


class ListFeedBack(ListView):
    template_name = 'feedback/list_feedback.html'
    model = Feedback

    # название ключа для контекста.
    context_object_name = 'all_feedbacks'  # если не написать, будет по-умолчанию object_list

    # можно отфильтровать queryset
    def get_queryset(self):
        queryset = super().get_queryset()  # по-умолчанию берет model.objects.all()
        filter_qs = queryset.filter(rating__gt=3)
        return filter_qs


# class DetailFeedBack(TemplateView):
#     template_name = 'feedback/detail_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         id_feedback = kwargs['id_feedback']
#         one_feedback = Feedback.objects.get(id=id_feedback)
#         context['one_feedback'] = one_feedback
#         return context

class DetailFeedBack(DetailView):  # в urls обязательно должно быть <int:pk> или слаг!
    template_name = 'feedback/detail_feedback.html'
    model = Feedback

    # название ключа атоматически берется из названия модели только маленькими буквами. Можно переопределить
    # context_object_name = 'one_feedback'  # по-умолчанию можно еще обращаться как object
