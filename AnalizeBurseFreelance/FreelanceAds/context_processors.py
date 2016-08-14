from .models import FreelanceAdsHide
import datetime


def CountTodayHidden(request):
    count_today_hidden = FreelanceAdsHide.objects.filter(user=request.user, time_check__gte=datetime.date.today()).count()
    return { "count_today_hidden": count_today_hidden }