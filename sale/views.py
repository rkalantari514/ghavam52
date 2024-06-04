from django.shortcuts import render, redirect

# Create your views here.
from sale.forms import KindeForm
from sale.models import Kinde_Kala


def creatkind(request, *args, **kwargs):
    user_permision = request.user.get_user_permissions()
    print(user_permision)

    create_form = KindeForm(request.POST or None)
    context = {
        'create_form': create_form,

    }
    if create_form.is_valid():
        Kinde_Kala.objects.create(
            active=create_form.cleaned_data.get('active'),
            name=create_form.cleaned_data.get('name'),
        )
        # return redirect(f"/")
    context = {
        'create_form': create_form,

    }
    return render(request, 'create_kinde.html', context)



