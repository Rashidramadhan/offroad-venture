from django import forms
from offroad_safari.models import GuestEnquiryModel


class GuestEnquiryForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    package = forms.CharField()
    news_letter = forms.BooleanField(required=False)
    enquiry_message = forms.CharField(widget=forms.Textarea)