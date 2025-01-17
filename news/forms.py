from .models import Articles
from django.forms import ModelForm, TextInput, Textarea, NumberInput
 
class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text','price']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
        
            "anons": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Anons'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Full text'
            })
        }