from django.forms import ModelForm
from .models import FeedBack


class FeedbackForm(ModelForm):
    class Meta:
        model = FeedBack
        fields = ['text']
        labels = {
            'text': 'Текст',
        }
        help_text = {
            'text': 'Напишите здесь свой положительный (или нет) отзыв.',
        }
