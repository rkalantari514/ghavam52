from django import forms
from django.forms import ModelChoiceField
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime

from sale.models import Customer


class ProcessForm(forms.Form):
    customer = ModelChoiceField(
        widget=forms.Select(
            attrs={
                'placeholder': 'مشتری',
                'class': 'selectpicker mr-sm-2',
                'data-live-search' : "true",
            }),
        queryset=Customer.objects.filter(active=True),
        label='مشتری',
        required=True,
        empty_label='مشتری را انتخاب کنید',
    )



    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'نام فرآیند', 'class': 'form-control'}),
        label=' نام فرآیند',

    )



    date = forms.DateField(
        widget=forms.DateInput(),
    )







    def __init__(self, *args, **kwargs):
        super(ProcessForm, self).__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(
            label=('تاریخ فرآیند'),
            widget=AdminJalaliDateWidget
        )


