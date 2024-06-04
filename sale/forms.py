from django import forms
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from django.forms import ModelChoiceField, ModelMultipleChoiceField




class KindeForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'دسته بندی کالا', 'class': 'form-control'}),
        label=' نوع',
    )

    active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
        ),
        label=' فعال است؟',
    )