from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse


# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=20, validators=[MinLengthValidator(3)])
    surname = models.CharField(max_length=60)
    feedback = models.TextField()
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.name} {self.surname}'

    def get_absolute_url(self):
        return reverse('feedback-detail', args=[str(self.id)])
