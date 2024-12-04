from django import forms

class ContractForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ваше имя")
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea, label="Сообщения")
    subscribe = forms.BooleanField(required=False, label="Подписаться на рассылку")
