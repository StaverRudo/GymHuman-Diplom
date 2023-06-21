from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'content-coments__form-main__coment'})
    )

    class Meta:
        model = Comment
        fields = ['text']

        def __init__(self, *args, **kwargs):
            super(CommentForm, self).__init__(*args, **kwargs)
            self.fields['text'].widget.attrs.update({'class': 'content-coments__btn'})    

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    email = forms.EmailField(label='Email')
    subject = forms.CharField(label='Заголовок', max_length=100)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)
