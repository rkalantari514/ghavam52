from django.shortcuts import render, redirect

# Create your views here.
from sale.forms import KindeForm
from sale.models import Kinde_Kala


def creatkind(request, *args, **kwargs):
    user_permision = request.user.get_user_permissions()
    print(user_permision)
    create_form = KindeForm(request.POST or None)
    if create_form.is_valid():
        Kinde_Kala.objects.create(
            active=create_form.cleaned_data.get('active'),
            name=create_form.cleaned_data.get('name'),
        )
        return redirect(f"/admin/sale/kinde_kala")
    context = {
        'create_form': create_form,
    }
    return render(request, 'create_kinde.html', context)

def editkind(request, *args, **kwargs):
    user_permision = request.user.get_user_permissions()
    print(user_permision)
    kindid = kwargs['kindid']
    to_edit = Kinde_Kala.objects.filter(id=kindid).last()

    create_form = KindeForm(request.POST or None, initial={
        'active': to_edit.active,
        'name': to_edit.name,
    }
                            )
    context = {
        'create_form': create_form,
    }
    if create_form.is_valid():
        to_edit.active = create_form.cleaned_data.get('active')
        to_edit.name = create_form.cleaned_data.get('name')
        to_edit.save()
        # return redirect(f"/")
    context = {
        'create_form': create_form,

    }
    return render(request, 'create_kinde.html', context)
def deletekind(request, *args, **kwargs):
    user_permision = request.user.get_user_permissions()
    print(user_permision)
    kindid = kwargs['kindid']
    todelete = Kinde_Kala.objects.filter(id=kindid).last()
    todelete.delete()
    return redirect(f"/admin/sale/kinde_kala")
