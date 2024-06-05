from django.shortcuts import render, redirect

from process.forms import ProcessForm
from process.models import Process


# Create your views here.


def create_process(request, *args, **kwargs):
    user_permision = request.user.get_user_permissions()
    print(user_permision)
    create_form = ProcessForm(request.POST or None)
    if create_form.is_valid():
        Process.objects.create(
            name=create_form.cleaned_data.get('name'),
            date=create_form.cleaned_data.get('date'),
            customer=create_form.cleaned_data.get('customer'),
        )
        return redirect(f"admin/process/process")
    context = {
        'create_form': create_form,
    }
    return render(request, 'create_process.html', context)
