from django import forms


class TicketForm(forms.Form):

    subject = forms.CharField(max_length=255, required=False)
    message = forms.CharField(widget=forms.Textarea, required=False)
    attachment = forms.FileField(required=False)
    priority = forms.ChoiceField(required=False, choices=[
        ('l', 'پایین'),
        ('n', 'متوسط'),
        ('h', 'بالا'),
        ('c', 'بسیار مهم'),
    ])
