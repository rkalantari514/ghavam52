from django.shortcuts import render

# Create your views here.


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
