from django import forms

class MailForm(forms.Form):
    text = forms.CharField(label='Текст', max_length=100, widget=forms.Textarea)
    time = forms.IntegerField(label='Время отправки,сек', min_value=0)