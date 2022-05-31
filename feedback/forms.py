from django import forms
from .models import Feedback


# class FeedbackForm(forms.Form):
#     name = forms.CharField(label='Имя', max_length=7, min_length=2, error_messages={
#         'max_length': 'Слишком много символов',
#         'min_length': 'Слишком мало символов',
#         'required': 'Укажите хотя бы 1 символ',
#     })
#     surname = forms.CharField()
#     feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))
#     rating = forms.IntegerField(label='Рейтинг', max_value=5, min_value=1)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        # fields = ['name', 'surname', 'feedback', 'rating']  # какие поля надо отобразить
        fields = '__all__'      # если все поля надо отобразить пишем так
        # exclude = ['rating']        # какие поля надо исключить

        labels = {      #  назначаем названия полей, чтобы не было как в моделях
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Рейтинг',
        }

        error_messages = {          # переопределяем сообщения об ошибках
            'name': {
                'max_length': 'Слишком много символов',
                'min_length': 'Слишком мало символов',
                'required': 'Поле не должно быть пустым',
            },
            'surname': {
                'max_length': 'Слишком много символов',
                'min_length': 'Слишком мало символов',
                'required': 'Поле не должно быть пустым',
            },
        }

