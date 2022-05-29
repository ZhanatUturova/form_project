from django import  forms

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=7, min_length=2, error_messages={
        'max_length': 'Слишком много символов',
        'min_length': 'Слишком мало символов',
        'required': 'Укажите хотя бы 1 символ',
    })
    surname = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))
    rating = forms.IntegerField(label='Рейтинг', max_value=5, min_value=1)