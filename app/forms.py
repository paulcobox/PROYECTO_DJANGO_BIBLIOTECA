from django import forms
from .models import Author

# Ejemplos
# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)
#     email = forms.EmailField(label='Email')

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        