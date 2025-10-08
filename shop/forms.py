from django import forms
from .models import SupportMessage

PRICE_CHOICES = [
    ('0-25', 'Under $25'),
    ('25-50', '$25 to $50'),
    ('50-100', '$50 to $100'),
    ('100+', 'Over $100'),
]

class FilterForm(forms.Form):
    q = forms.CharField(required=False, label='Search')
    category = forms.CharField(required=False)
    price = forms.ChoiceField(choices=[('', 'Any price')] + PRICE_CHOICES, required=False)



from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'address', 'city', 'zip', 'payment_method']
        widgets = {
            'payment_method': forms.Select(attrs={'class': 'form-select'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'zip': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SupportMessageForm(forms.ModelForm):
    class Meta:
        model = SupportMessage
        fields = ['subject', 'message']
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Describe your issue...'}),
        }