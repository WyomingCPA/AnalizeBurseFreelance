from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .models import FreelanceAds, FreelanceAdsHide, FreelanceAdsOverdue

from datetime import datetime, timedelta


@login_required(login_url='/accounts/signin/')
def read_advert(request):
    hide_adds = FreelanceAdsHide.objects.filter(user=request.user).values('ads_item')
    oeverdue_ads = FreelanceAdsOverdue.objects.filter(user=request.user).values('ads_item')
    list_ads =  FreelanceAds.objects.exclude(id__in=hide_adds)

    delta = datetime.now() - timedelta(hours=5)
    list_ads = list_ads.filter(time_parsing__gte=delta).exclude(id__in=oeverdue_ads)
     

    paginator = Paginator(list_ads, 50)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'dashboard/advert_table.html', {'list_ads': contacts,})


@login_required(login_url='/accounts/signin/')
def action_advert(request):
    if request.method == 'POST':
        pointer_user = request.POST.getlist('pointer_user[]')
        for item in pointer_user:
            ads = FreelanceAds.objects.get(id=int(item)) 
            hide = FreelanceAdsHide(user = request.user, ads_item = ads, )
            hide.save()
 
    return redirect('/ads/')

