from django import forms


class TicketForm(forms.Form):

    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    attachment = forms.FileField()
    priority = forms.ChoiceField(choices=[
        ('l', 'پایین'),
        ('n', 'متوسط'),
        ('h', 'بالا'),
        ('c', 'بسیار مهم'),
    ])
