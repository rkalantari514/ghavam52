from django.contrib.auth.decorators import login_required, permission_required
from django.http import FileResponse
from django.shortcuts import render, redirect
from django.utils.timezone import now

from cash.models import Gardesh, PivGardesh
from custom_login.models import MyUser, UserLog
from report.models import ZoneHesab, Product_Corection, Send_Parti, Master_Piv, Cash, Piv_Product_Taraz, Taraz_Bedehi, \
    Seller_Corection
from gharardad.forms import GharardadForm, SoratForm, AttachForm
from gharardad.models import Gharardad, Sorat, Attachement


@login_required(login_url='/login')
@permission_required('gharardad.view_gharardad')
def Gharardads(request, *args, **kwargs):
    user_permision = request.user.get_user_permissions()
    print(user_permision)
    zone_code = kwargs['zone_code']
    zone = ZoneHesab.objects.get(zone_code=zone_code)
    user_id = request.user.id
    user = MyUser.objects.get(id=user_id)
    UserLog.objects.create(
        user=user,
        page='قراردادها',
        zone=zone
    )
    projects = Product_Corection.objects.order_by('product_nick_name').filter(zone=zone)
    gharardads = Gharardad.objects.filter(zone=zone)
    context = {
        'zone': zone,
        'projects': projects,
        'gharardads': gharardads,
        'zone_code': zone_code,
        'user_permision': user_permision
    }
    return render(request, 'gharardads.html', context)


@login_required(login_url='/login')
@permission_required('gharardad.view_gharardad')
def Gharardad_detail(request, *args, **kwargs):
    user_permision = request.user.get_user_permissions()
    zone_code = kwargs['zone_code']
    gh_no = kwargs['gh_no']

    zone = ZoneHesab.objects.get(zone_code=zone_code)
    user_id = request.user.id
    user = MyUser.objects.get(id=user_id)
    UserLog.objects.create(
        user=user,
        page='جزئیات قرارداد',
        zone=zone
    )
    projects = Product_Corection.objects.order_by('product_nick_name').filter(zone=zone)
    gh = Gharardad.objects.filter(pk=gh_no).last()
    sorats = Sorat.objects.filter(gharardad=gh).order_by('peymankar_date').all()

    sorats_k = Sorat.objects.filter(gharardad=gh, sorat_kind__sorat_kind__contains="کارکرد").order_by('peymankar_date').all()
    sorats_t = Sorat.objects.filter(gharardad=gh, sorat_kind__sorat_kind__contains="تعدیل").order_by('peymankar_date').all()



    sumk = 0
    for so in sorats_k:
        if so.sorat_no == "1":
            so.peymankar_price = so.peymankar_total_price
            so.moshaver_price = so.moshaver_total_price
            so.karfarma_price = so.karfarma_total_price
            so.save()
            sumk = so.karfarma_total_price

        if so.sorat_no != "1" :
            so.peymankar_price = so.peymankar_total_price - sumk
            if so.peymankar_total_price == 0:
                so.peymankar_price = 0

            so.moshaver_price = so.moshaver_total_price - sumk
            if so.moshaver_total_price == 0:
                so.moshaver_price = 0

            so.karfarma_price = so.karfarma_total_price - sumk
            if so.karfarma_total_price == 0:
                so.karfarma_price = 0
            so.save()
            sumk = so.karfarma_total_price

    sumk = 0
    for so in sorats_t:
        if so.sorat_no == "1":
            so.peymankar_price = so.peymankar_total_price
            so.moshaver_price = so.moshaver_total_price
            so.karfarma_price = so.karfarma_total_price
            so.save()
            sumk = so.karfarma_total_price

        if so.sorat_no != "1":

            so.peymankar_price = so.peymankar_total_price - sumk
            if so.peymankar_total_price == 0:
                so.peymankar_price=0

            so.moshaver_price = so.moshaver_total_price - sumk
            if so.moshaver_total_price == 0:
                so.moshaver_price = 0

            so.karfarma_price = so.karfarma_total_price - sumk
            if so.karfarma_total_price == 0:
                so.karfarma_price = 0

            so.save()
            sumk = so.karfarma_total_price




    # sorats=Sorat.objects.last()
    mandeh_day = 0

    project_priod = gh.gharardad_end_date - gh.gharardad_date
    past_time = (now().date() - gh.gharardad_date)
    if gh.is_end:
        past_time = gh.khateme_date - gh.gharardad_date
    time_pish = past_time / project_priod * 100
    past_time = past_time.days
    time_pish1 = 0
    time_pish2 = 0
    if time_pish <= 100:
        time_pish1 = round(time_pish)
        time_pish = 100
    if time_pish > 100:
        time_pish1 = 100
        time_pish2 = round(time_pish - time_pish1)

    cash_gh_k = 0
    cash_gh_k_25 = 0
    cash_tadil_k = 0
    cash_tafavot_k = 0
    cash_0 = 0

    for so in sorats:

        if so.sorat_kind.sorat_kind == "کارکرد" or so.sorat_kind.sorat_kind == "قطعی":
            cash_gh_k += so.karfarma_price

        if so.sorat_kind.sorat_kind == "تعدیل":
            cash_tadil_k += so.karfarma_price

        if so.sorat_kind.sorat_kind == "ما به التفاوت":
            cash_tafavot_k += so.karfarma_price

    if cash_gh_k > gh.gharardad_price:
        cash_gh_k_25 = cash_gh_k - gh.gharardad_price
        cash_gh_k = gh.gharardad_price
    else:
        cash_0 = gh.gharardad_price - cash_gh_k

    cash_tolal_k = cash_gh_k + cash_gh_k_25 + cash_tadil_k + cash_tafavot_k + cash_0
    cash_tolal_kk = cash_gh_k + cash_gh_k_25 + cash_tadil_k + cash_tafavot_k

    cash_gh_k_100 = round(cash_gh_k / cash_tolal_k * 100)
    cash_gh_k_25_100 = round(cash_gh_k_25 / cash_tolal_k * 100)
    cash_tadil_k_100 = round(cash_tadil_k / cash_tolal_k * 100)
    cash_tafavot_k_100 = round(cash_tafavot_k / cash_tolal_k * 100)
    cash_0_100 = round(cash_0 / cash_tolal_k * 100)
    cash_tolal_k_100 = cash_gh_k_100 + cash_gh_k_25_100 + cash_tadil_k_100 + cash_tafavot_k_100 + cash_0_100

    timeline = []
    for so in sorats:
        if so.peymankar_price != 0 or so.moshaver_price != 0 or so.karfarma_price != 0:
            num = so.sorat_no
        if so.peymankar_price != 0:
            a = so.peymankar_price
            b = so.peymankar_date
            timeline.append((num, b, a, "پیمانکار", "primary"))
        if so.moshaver_price != 0:
            a = so.moshaver_price
            b = so.moshaver_date
            timeline.append((num, b, a, "مشاور", "info"))
        if so.karfarma_price != 0:
            a = so.karfarma_price
            b = so.karfarma_date
            timeline.append((num, b, a, "کارفرما", "success"))

    sum_peymankar = 0
    for so in sorats:
        sum_peymankar += so.peymankar_price

    attachment = Attachement.objects.filter(gharardad=gh).all()
    seller = gh.seller.seller_from_parti
    product = gh.product.product_from_parti

    partis = Send_Parti.objects.order_by('date').filter(zone=zone, seller=seller, product=product)



    gharardads = Gharardad.objects.filter(seller=gh.seller, product=gh.product)
    gh_count = gharardads.count()
    other_gh = False
    if gh_count > 1:
        other_gh = True

    cashflow = Gardesh.objects.filter(seller2=gh.seller.seller_from_parti, product2=gh.product.product_from_parti,
                                      zone=zone).order_by('-pk')

    taraz = Taraz_Bedehi.objects.filter(seller2=gh.seller.seller_from_parti, product2=gh.product.product_from_parti,
                                        zone=zone).last()
    print('*-*-*-----------------')
    # print(gh.seller.seller_from_parti)
    # print(gh.product.product_from_parti)
    # print(taraz)
    # print(taraz)
    # print(taraz)

    # cashflow=Cash.objects.all()[200:1020:50]

    cash_table = []
    e = 0
    g = 0
    h = "واریز وجه"

    sum_cash = 0
    sum_cash_pish = 0
    f = 0
    for i in cashflow:
        a = i.date
        b = i.sharh
        c = i.bedehkar
        d = i.bestankar
        j = False
        k = False
        l = False
        m = False
        if ((i.moeen == 130161) and (not 'كسورات' in b) and (not 'حسن انجام' in b) and (not 'پيش پرداخت' in b) and (not 'کسورات' in b) and (c > 1)):
            sum_cash = sum_cash + c
            j = True
        if ((i.moeen == 130161) and ('اصلاح' in b) and (d > 1)):
            sum_cash = sum_cash - d
            k = True
        if ((i.moeen == 170111) and (c > 1)):
            sum_cash_pish = sum_cash_pish + c
            l = True

        if ((i.moeen == 170111) and (d > 1) and ('اصلاح' in b)):
            sum_cash_pish = sum_cash_pish - d
            m = True

        e = sum_cash
        f = sum_cash_pish
        if (c + d == 0):
            continue

        cash_table.append((a, b, c, d, e, f, g, h, j, k, l, m, i.moeen))

    total_cash = e
    total_pish = f
    if PivGardesh.objects.filter(seller2=gh.seller.seller_from_parti, product2=gh.product.product_from_parti,
                                 zone=zone).last() is not None:
        mandeh_day = PivGardesh.objects.filter(seller2=gh.seller.seller_from_parti,
                                               product2=gh.product.product_from_parti,
                                               zone=zone).last().mandeh_day
    tashkis = True
    if taraz is not None:
        if taraz.bedehkar > 5:
            tashkis = False

    context = {
        'projects': projects,
        'gh': gh,
        'zone_code': zone_code,
        'sorats': sorats,
        'timeline': timeline,
        'sum_peymankar': sum_peymankar,
        'zone': zone,
        'past_time': past_time,
        'time_pish': time_pish,
        'time_pish1': time_pish1,
        'time_pish2': time_pish2,

        'cash_tolal_k': cash_tolal_k,
        'cash_tolal_kk': cash_tolal_kk,
        'cash_gh_k': cash_gh_k,
        'cash_gh_k_25': cash_gh_k_25,
        'cash_tadil_k': cash_tadil_k,
        'cash_tafavot_k': cash_tafavot_k,

        'cash_gh_k_100': cash_gh_k_100,
        'cash_gh_k_25_100': cash_gh_k_25_100,
        'cash_tadil_k_100': cash_tadil_k_100,
        'cash_tafavot_k_100': cash_tafavot_k_100,
        'cash_0_100': cash_0_100,

        'cash_tolal_k_100': cash_tolal_k_100,
        'user_permision': user_permision,

        'attachment': attachment,
        'partis': partis,
        'gharardads': gharardads,
        'other_gh': other_gh,

        'cash_table': cash_table,
        'total_cash': total_cash,
        'total_pish': total_pish,
        'taraz': taraz,
        'mandeh_day': mandeh_day,
        'tashkis': tashkis,

    }

    return render(request, 'gharardad_detail.html', context)
    # return render(request, 'test.html')


@login_required(login_url='/login')
@permission_required('gharardad.view_gharardad')
def Sorats(request, *args, **kwargs):
    user_permision = request.user.get_user_permissions()
    zone_code = kwargs['zone_code']

    zone = ZoneHesab.objects.get(zone_code=zone_code)
    user_id = request.user.id
    user = MyUser.objects.get(id=user_id)
    UserLog.objects.create(
        user=user,
        page='صورت وضعیت ها',
        zone=zone
    )



    sorats = Sorat.objects.order_by('-peymankar_date').all()
    # sorats=Sorat.objects.last()
    context = {
        'zone_code': zone_code,
        'sorats': sorats,

        'zone': zone,

        'user_permision': user_permision,

    }

    return render(request, 'sorats.html', context)


@login_required(login_url='/login')
@permission_required('gharardad.add_gharardad')
def CreateGharardad(request, *args, **kwargs):
    user_permision = request.user.get_user_permissions()
    print(user_permision)
    zone_code = kwargs['zone_code']
    zone = ZoneHesab.objects.get(zone_code=zone_code)
    projects = Product_Corection.objects.order_by('product_nick_name').filter(zone=zone)
    create_form = GharardadForm(request.POST or None)
    gharardads = Gharardad.objects.filter(zone=zone)
    context = {
        'create_form': create_form,
        'projects': projects,
        'gharardads': gharardads,
        'zone_code': zone_code,
    }
    if create_form.is_valid():
        Gharardad.objects.create(
            zone=zone,
            product=create_form.cleaned_data.get('product'),
            seller=create_form.cleaned_data.get('seller'),
            subject=create_form.cleaned_data.get('subject'),
            gharardad_no=create_form.cleaned_data.get('gharardad_no'),
            gharardad_date=create_form.cleaned_data.get('gharardad_date'),
            gharardad_end_date=create_form.cleaned_data.get('gharardad_end_date'),
            gharardad_price=create_form.cleaned_data.get('gharardad_price'),
            is_end=create_form.cleaned_data.get('is_end'),
            khateme_date=create_form.cleaned_data.get('khateme_date'),
        )
        return redirect(f"/gh/{zone_code}")
    context = {
        'create_form': create_form,
        'projects': projects,
        'gharardads': gharardads,
        'zone_code': zone_code,
        'user_permision': user_permision,

    }
    return render(request, 'create_gharardad.html', context)


@login_required(login_url='/login')
@permission_required('gharardad.change_gharardad')
def EditGharardad(request, *args, **kwargs):
    user_permision = request.user.get_user_permissions()
    zone_code = kwargs['zone_code']
    zone = ZoneHesab.objects.get(zone_code=zone_code)
    projects = Product_Corection.objects.order_by('product_nick_name').filter(zone=zone)
    gharardads = Gharardad.objects.filter(zone=zone)

    gh_no = kwargs['gh_no']

    to_edit = Gharardad.objects.filter(pk=gh_no).last()

    create_form = GharardadForm(request.POST or None,
                                initial={
                                    'product': to_edit.product,
                                    'seller': to_edit.seller,
                                    'subject': to_edit.subject,
                                    'gharardad_no': to_edit.gharardad_no,
                                    'gharardad_date': to_edit.gharardad_date,
                                    'gharardad_end_date': to_edit.gharardad_end_date,
                                    'gharardad_price': to_edit.gharardad_price,
                                    'is_end': to_edit.is_end,
                                    'khateme_date': to_edit.khateme_date,
                                }
                                )

    context = {
        'create_form': create_form,
        'projects': projects,
        'gharardads': gharardads,
        'zone_code': zone_code,

    }
    if create_form.is_valid():
        to_edit.product = create_form.cleaned_data.get('product')
        to_edit.seller = create_form.cleaned_data.get('seller')
        to_edit.subject = create_form.cleaned_data.get('subject')
        to_edit.gharardad_no = create_form.cleaned_data.get('gharardad_no')
        to_edit.gharardad_date = create_form.cleaned_data.get('gharardad_date')
        to_edit.gharardad_end_date = create_form.cleaned_data.get('gharardad_end_date')
        to_edit.gharardad_price = create_form.cleaned_data.get('gharardad_price')
        to_edit.is_end = create_form.cleaned_data.get('is_end')
        to_edit.khateme_date = create_form.cleaned_data.get('khateme_date')

        to_edit.save()
        return redirect(f"/gh/{zone_code}/{gh_no}")

    context = {
        'create_form': create_form,
        'projects': projects,
        'gharardads': gharardads,
        'zone_code': zone_code,
        'user_permision': user_permision,

    }
    return render(request, 'create_gharardad.html', context)


@login_required(login_url='/login')
@permission_required('gharardad.delete_gharardad')
def DeleteGharardad(request, *args, **kwargs):
    zone_code = kwargs['zone_code']
    gh_no = kwargs['gh_no']
    Gharardad.objects.filter(pk=gh_no).delete()
    return redirect(f'/gh/{zone_code}')


@login_required(login_url='/login')
@permission_required('gharardad.add_sorat')
def CreateSorat(request, *args, **kwargs):
    user_permision = request.user.get_user_permissions()
    zone_code = kwargs['zone_code']
    gh_no = kwargs['gh_no']
    zone = ZoneHesab.objects.get(zone_code=zone_code)
    projects = Product_Corection.objects.order_by('product_nick_name').filter(zone=zone)
    create_form = SoratForm(request.POST or None, request.FILES or None,
                            initial={
                                'product': "",
                                'seller': "",
                                'year': "1401",
                            }

                            )
    gharardad = Gharardad.objects.filter(zone=zone, id=gh_no).last()

    context = {
        'zone_code': zone_code,
        'zone': zone,
        'projects': projects,
        'create_form': create_form,
        'gharardad': gharardad,
        'user_permision': user_permision,

    }

    if create_form.is_valid():

        Sorat.objects.create(
            zone=zone,
            gharardad=gharardad,
            sorat_no=create_form.cleaned_data.get('sorat_no'),
            sorat_kind=create_form.cleaned_data.get('sorat_kind'),
            peymankar_date=create_form.cleaned_data.get('peymankar_date'),
            peymankar_total_price=create_form.cleaned_data.get('peymankar_total_price'),
            moshaver_date=create_form.cleaned_data.get('moshaver_date'),
            moshaver_total_price=create_form.cleaned_data.get('moshaver_total_price'),
            moshaver_no=create_form.cleaned_data.get('moshaver_no'),
            karfarma_date=create_form.cleaned_data.get('karfarma_date'),
            karfarma_total_price=create_form.cleaned_data.get('karfarma_total_price'),
            sorat_form=create_form.cleaned_data.get('form_file')
        )
        return redirect(f"/gh/{zone_code}/{gh_no}")

    return render(request, 'create_sorat.html', context)


@login_required(login_url='/login')
@permission_required('gharardad.change_sorat')
def EditSorat(request, *args, **kwargs):
    user_permision = request.user.get_user_permissions()
    zone_code = kwargs['zone_code']
    gh_no = kwargs['gh_no']
    so_no = kwargs['so_no']

    zone = ZoneHesab.objects.get(zone_code=zone_code)
    projects = Product_Corection.objects.order_by('product_nick_name').filter(zone=zone)
    gharardad = Gharardad.objects.filter(zone=zone, id=gh_no).last()
    sorat = Sorat.objects.filter(zone=zone, id=so_no).last()

    create_form = SoratForm(request.POST or None, request.FILES or None,
                            initial={
                                'sorat_kind': sorat.sorat_kind,
                                'sorat_no': sorat.sorat_no,
                                'peymankar_date': sorat.peymankar_date,
                                'peymankar_total_price': sorat.peymankar_total_price,
                                'moshaver_date': sorat.moshaver_date,
                                'moshaver_no': sorat.moshaver_no,
                                'moshaver_total_price': sorat.moshaver_total_price,
                                'karfarma_date': sorat.karfarma_date,
                                'karfarma_total_price': sorat.karfarma_total_price,
                                'form_file': sorat.sorat_form,
                            }
                            )
    context = {
        'zone_code': zone_code,
        'zone': zone,
        'projects': projects,
        'create_form': create_form,
        'gharardad': gharardad,
        'user_permision': user_permision,

    }

    if create_form.is_valid():
        # sumk = 0
        # s = str(create_form.cleaned_data.get('sorat_kind'))
        # try:
        #     if "ق" in s:
        #         print(create_form.cleaned_data.get('sorat_kind'))
        #         so_pish = Sorat.objects.filter(zone=zone, gharardad=gharardad,
        #                                        sorat_kind__sorat_kind__contains="ق").last()
        #         sumk = so_pish.karfarma_total_price
        #     if "ل" in s:
        #         so_pish = Sorat.objects.filter(zone=zone, gharardad=gharardad,
        #                                        sorat_kind__sorat_kind__contains="ل").last()
        #         sumk = so_pish.karfarma_total_price
        # except:
        #     pass

        # pey_price = int(create_form.cleaned_data.get('peymankar_total_price')) - sumk
        # mos_price = int(create_form.cleaned_data.get('moshaver_total_price')) - sumk
        # kar_price = int(create_form.cleaned_data.get('karfarma_total_price')) - sumk



        sorat.sorat_kind = create_form.cleaned_data.get('sorat_kind')
        sorat.sorat_no = create_form.cleaned_data.get('sorat_no')
        sorat.peymankar_date = create_form.cleaned_data.get('peymankar_date')
        sorat.peymankar_total_price = create_form.cleaned_data.get('peymankar_total_price')
        sorat.moshaver_date = create_form.cleaned_data.get('moshaver_date')
        sorat.moshaver_total_price = create_form.cleaned_data.get('moshaver_total_price')
        sorat.moshaver_no = create_form.cleaned_data.get('moshaver_no')
        sorat.karfarma_date = create_form.cleaned_data.get('karfarma_date')
        sorat.karfarma_total_price = create_form.cleaned_data.get('karfarma_total_price')
        sorat.sorat_form = create_form.cleaned_data.get('form_file')

        # sorat.peymankar_price =pey_price
        # sorat.moshaver_price =mos_price
        # sorat.karfarma_price =kar_price


        sorat.save()
        return redirect(f"/gh/{zone_code}/{gh_no}")

    return render(request, 'create_sorat.html', context)


@login_required(login_url='/login')
@permission_required('gharardad.delete_sorat')
def DeleteSorat(request, *args, **kwargs):
    zone_code = kwargs['zone_code']
    gh_no = kwargs['gh_no']
    so_no = kwargs['so_no']
    zone = ZoneHesab.objects.get(zone_code=zone_code)
    Sorat.objects.filter(zone=zone, id=so_no).delete()
    return redirect(f'/gh/{zone_code}/{gh_no}')


@login_required(login_url='/login')
@permission_required('gharardad.add_attachement')
def CreateAttach(request, *args, **kwargs):
    # user_permision = request.user.get_user_permissions()
    # print(user_permision)
    zone_code = kwargs['zone_code']
    gh_no = kwargs['gh_no']
    gharardad = Gharardad.objects.filter(id=gh_no).last()
    zone = ZoneHesab.objects.get(zone_code=zone_code)
    create_form = AttachForm(request.POST or None, request.FILES or None)
    context = {
        'create_form': create_form,
        'zone_code': zone_code,
    }

    if create_form.is_valid():
        Attachement.objects.create(
            zone=zone,
            gharardad=gharardad,
            a_kind=create_form.cleaned_data.get('a_kind'),
            a_describe=create_form.cleaned_data.get('a_describe'),
            a_file=create_form.cleaned_data.get('a_file'),
            a_expire=create_form.cleaned_data.get('a_expire'),

        )
        return redirect(f"/gh/{zone_code}/{gh_no}")
    context = {
        'create_form': create_form,
        'zone_code': zone_code,

    }
    return render(request, 'create_attachment.html', context)


@login_required(login_url='/login')
@permission_required('gharardad.change_attachement')
def EditAttach(request, *args, **kwargs):
    user_permision = request.user.get_user_permissions()
    print(user_permision)
    zone_code = kwargs['zone_code']
    gh_no = kwargs['gh_no']
    at_no = kwargs['at_no']
    gharardad = Gharardad.objects.filter(id=gh_no).last()
    zone = ZoneHesab.objects.get(zone_code=zone_code)
    atach = Attachement.objects.filter(id=at_no).last()
    create_form = AttachForm(request.POST or None, request.FILES or None,
                             initial={
                                 'a_kind': atach.a_kind,
                                 'a_describe': atach.a_describe,
                                 'a_file': atach.a_file,
                                 'a_expire': atach.a_expire,
                             })
    context = {
        'create_form': create_form,
        'zone_code': zone_code,
        'atach': atach,
    }

    if create_form.is_valid():
        atach.a_kind = create_form.cleaned_data.get('a_kind')
        atach.a_describe = create_form.cleaned_data.get('a_describe')
        atach.a_file = create_form.cleaned_data.get('a_file')
        atach.a_expire = create_form.cleaned_data.get('a_expire')
        atach.save()
        return redirect(f"/gh/{zone_code}/{gh_no}")
    context = {
        'create_form': create_form,
        'zone_code': zone_code,
        'atach': atach,
    }
    return render(request, 'create_attachment.html', context)


@login_required(login_url='/login')
@permission_required('gharardad.delete_attachement')
def DeleteAttach(request, *args, **kwargs):
    zone_code = kwargs['zone_code']
    gh_no = kwargs['gh_no']
    at_no = kwargs['at_no']
    zone = ZoneHesab.objects.get(zone_code=zone_code)
    Attachement.objects.filter(zone=zone, id=at_no).delete()
    return redirect(f'/gh/{zone_code}/{gh_no}')


def Mporg(request, *args, **kwargs):
    masrers = Master_Piv.objects.all()
    print(masrers)
    for i in masrers:
        day = i.update_time.date()
        print(day)

    return render(request, 'mporg.html')


@login_required(login_url='/login')
@permission_required('gharardad.view_gharardad')
def seller_producrt(request, *args, **kwargs):
    zone_code = kwargs['zone_code']
    zone = ZoneHesab.objects.filter(zone_code=zone_code).last()
    projects = Product_Corection.objects.order_by('product_nick_name').filter(zone=zone)
    sell_pro = PivGardesh.objects.filter(zone=zone, moeen='130161').all()

    context = {
        'sell_pro': sell_pro,
        'projects': projects,
        'zone_code': zone_code,
    }
    return render(request, 'sell-pro.html', context)


@login_required(login_url='/login')
@permission_required('gharardad.view_gharardad')
def seller_producrt_detail(request, *args, **kwargs):
    user_permision = request.user.get_user_permissions()
    zone_code = kwargs['zone_code']
    zone = ZoneHesab.objects.get(zone_code=zone_code)
    user_id = request.user.id
    user = MyUser.objects.get(id=user_id)
    UserLog.objects.create(
        user=user,
        page='جزئیات پروژه/پیمانکار',
        zone=zone
    )

    ghardesh_no = kwargs['ghardesh_no']

    product = PivGardesh.objects.filter(pk=ghardesh_no).last().product
    seller = PivGardesh.objects.filter(pk=ghardesh_no).last().seller






    try:
        seller2 = Seller_Corection.objects.filter(seller_from_taraz=seller).last().seller_from_parti
    except:
        pass

    try:
        seller20=[]
        for s in (Seller_Corection.objects.filter(seller_from_taraz=seller)):
            seller20.append(s.seller_from_parti)
    except:
        pass

    try:
        product20=[]
        for p in (Product_Corection.objects.filter(product_from_taraz=product)):
            product20.append(p.product_from_parti)
    except:
        pass



    for i in seller20:
        print(i)


    product2 = Product_Corection.objects.filter(product_from_taraz=product).last().product_from_parti
    projects = Product_Corection.objects.order_by('product_nick_name').filter(zone=zone)

    try:
        # partis = Send_Parti.objects.order_by('date').filter(zone=zone, seller=seller2, product=product2)
        # partis = Send_Parti.objects.order_by('date').filter(zone=zone, seller__in=seller20, product=product2)
        partis = Send_Parti.objects.order_by('date').filter(zone=zone, seller__in=seller20, product__in=product20)
    except:
        partis = Send_Parti.objects.order_by('date').filter(zone=202, seller='pskd', product=product2)

    gharardads = Gharardad.objects.filter(seller__seller_from_taraz=seller, product__product_from_taraz=product)
    other_gh = True

    cashflow = Gardesh.objects.filter(seller=seller, product=product, zone=zone).order_by('-pk')

    taraz = Taraz_Bedehi.objects.filter(seller=seller, product=product, zone=zone).last()
    # cashflow=Cash.objects.all()[200:1020:50]

    cash_table = []
    e = 0
    g = 0
    h = "واریز وجه"

    sum_cash = 0
    sum_cash_pish = 0
    f = 0
    for i in cashflow:
        a = i.date
        b = i.sharh
        c = i.bedehkar
        d = i.bestankar
        j = False
        k = False
        l = False
        m = False
        if ((i.moeen == 130161) and (not 'كسورات' in b) and (not 'حسن انجام' in b) and (not 'پيش پرداخت' in b) and (not 'کسورات' in b) and (c > 1)):
            sum_cash = sum_cash + c
            j = True
        if ((i.moeen == 130161) and ('اصلاح' in b) and (d > 1)):
            sum_cash = sum_cash - d
            k = True
        if ((i.moeen == 170111) and (c > 1)):
            sum_cash_pish = sum_cash_pish + c
            l = True

        if ((i.moeen == 170111) and (d > 1) and ('اصلاح' in b)):
            sum_cash_pish = sum_cash_pish - d
            m = True

        e = sum_cash
        f = sum_cash_pish
        if (c + d == 0):
            continue

        cash_table.append((a, b, c, d, e, f, g, h, j, k, l, m, i.moeen))

    total_cash = e
    total_pish = f
    mandeh_day = 0

    if PivGardesh.objects.filter(seller=seller, product=product, zone=zone).last() is not None:
        mandeh_day = PivGardesh.objects.filter(seller=seller, product=product, zone=zone).last().mandeh_day
    tashkis = True
    if taraz is not None:
        if taraz.bedehkar > 5:
            tashkis = False
    context = {
        'projects': projects,
        'zone_code': zone_code,
        'seller': seller,
        'product': product,
        'zone': zone,
        'user_permision': user_permision,
        'partis': partis,
        'gharardads': gharardads,
        'other_gh': other_gh,
        'cash_table': cash_table,
        'total_cash': total_cash,
        'total_pish': total_pish,
        'taraz': taraz,
        'mandeh_day': mandeh_day,
        'tashkis': tashkis,

    }

    return render(request, 'sell-pro-detail.html', context)
    # return render(request, 'test.html')


@login_required(login_url='/login')
@permission_required('gharardad.view_gharardad')
def Expire_date(request, *args, **kwargs):
    user_permision = request.user.get_user_permissions()
    zone_code = kwargs['zone_code']
    zone = ZoneHesab.objects.get(zone_code=zone_code)
    projects = Product_Corection.objects.order_by('product_nick_name').filter(zone=zone)

    files = Attachement.objects.filter(zone=zone)
    print(files)

    for file in files:

        if file.a_expire is not None:
            a = file.a_expire
            b = now().date()
            c = a - b
            c = c.days
            if file.a_until_day != c:
                file.a_until_day = c
                file.save()

            print(now().date())
            print(file.a_expire)
            print(c)
            print(file.a_until_day)

    context = {
        'zone': zone,
        'projects': projects,
        'files': files,
        'zone_code': zone_code,
        'user_permision': user_permision,
    }
    return render(request, 'expire-date.html', context)
