import re

from django import forms
from django.core.exceptions import ValidationError


class OpportunityEnquiryForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    surname = forms.CharField(max_length=100, label="Surname")
    company_name = forms.CharField(max_length=150, label="Company Name")
    company_email = forms.EmailField(max_length=254, label="Company Email")
    company_telephone = forms.CharField(max_length=30, label="Company Telephone")
    message = forms.CharField(widget=forms.Textarea, max_length=5000, label="Message")
    website = forms.CharField(required=False, widget=forms.TextInput, label="Website")

    def clean_company_telephone(self):
        telephone = self.cleaned_data["company_telephone"].strip()
        digits = re.sub(r"\D", "", telephone)
        if not re.fullmatch(r"\+?[\d\s().-]+", telephone) or not 7 <= len(digits) <= 15:
            raise ValidationError("Enter a valid telephone number.")
        return telephone

    def clean_website(self):
        if self.cleaned_data["website"].strip():
            raise ValidationError("Unable to process this enquiry.")
        return ""
