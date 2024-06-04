from django.shortcuts import render, redirect

# Create your views here.
from sale.forms import KindeForm, ProducerForm
from sale.models import Kinde_Kala, Producer


def create_kind(request, *args, **kwargs):
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

def edit_kind(request, *args, **kwargs):
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
def delete_kind(request, *args, **kwargs):
    user_permision = request.user.get_user_permissions()
    print(user_permision)
    kindid = kwargs['kindid']
    todelete = Kinde_Kala.objects.filter(id=kindid).last()
    todelete.delete()
    return redirect(f"/admin/sale/kinde_kala")



def create_producer(request, *args, **kwargs):
    user_permision = request.user.get_user_permissions()
    print(user_permision)
    create_form = ProducerForm(request.POST or None)
    if create_form.is_valid():
        Producer.objects.create(
            active=create_form.cleaned_data.get('active'),
            name=create_form.cleaned_data.get('name'),
            address=create_form.cleaned_data.get('address'),
            email=create_form.cleaned_data.get('email'),
            phone=create_form.cleaned_data.get('phone'),
        )
        return redirect(f"/admin/sale/producer")
    context = {
        'create_form': create_form,
    }
    return render(request, 'create_producer.html', context)




def edit_producer(request, *args, **kwargs):
    user_permision = request.user.get_user_permissions()
    print(user_permision)
    proid = kwargs['proid']
    to_edit = Producer.objects.filter(id=proid).last()

    create_form = ProducerForm(request.POST or None, initial={
        'active': to_edit.active,
        'name': to_edit.name,
        'address': to_edit.address,
        'phone': to_edit.phone,
        'email': to_edit.email,
    }
                            )
    context = {
        'create_form': create_form,
    }
    if create_form.is_valid():
        to_edit.active = create_form.cleaned_data.get('active')
        to_edit.name = create_form.cleaned_data.get('name')
        to_edit.address = create_form.cleaned_data.get('address')
        to_edit.email = create_form.cleaned_data.get('email')
        to_edit.phone = create_form.cleaned_data.get('phone')
        to_edit.save()
        return redirect(f"/admin/sale/producer")
    context = {
        'create_form': create_form,

    }
    return render(request, 'create_producer.html', context)


def delete_producer(request, *args, **kwargs):
    user_permision = request.user.get_user_permissions()
    print(user_permision)
    proid = kwargs['proid']
    todelete = Producer.objects.filter(id=proid).last()
    todelete.delete()
    return redirect(f"/admin/sale/producer")
