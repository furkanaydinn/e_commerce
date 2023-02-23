from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name','email','message')
        widgets = {
            'name': TextInput(attrs = {
                'id': "name",
                'name': "name",
                'placeholder': 'Name'
            }),
            'email': EmailInput(attrs = {
                'id': "email",
                'name': "email",
                'placeholder': 'Email'
            }),
            'message': Textarea(attrs = {
                'id': "message",
                'name': "message",
                'placeholder': 'Message'
            })
        }
