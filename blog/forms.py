from .models import BlogComment
from django.forms import ModelForm, TextInput, EmailInput, Textarea


class CommentForm(ModelForm):
    class Meta:
        model = BlogComment
        fields = ['name','email','phone','comment']
        widgets = {
            'name': TextInput(attrs = {
                'id': "name",
                'name': "name",
                'placeholder': 'İsim'
            }),
            'email': EmailInput(attrs = {
                'id': "email",
                'name': "email",
                'placeholder': 'Mail adresi'
            }),
            'phone': TextInput(attrs = {
                'id': "phone",
                'name': "phone",
                'placeholder': 'Telefon Numarası'
            }),
            'comment': Textarea(attrs = {
                'id': "comment",
                'name': "comment",
                'placeholder': 'Mesajınız'
            })
        }