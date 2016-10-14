from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect

from tracker.models import Tracker


@login_required(login_url='/authorization/log_error/')
def trackers(request, page=1):
    if request.user.is_superuser:
        return redirect('/admin')
    p = Paginator(Tracker.objects.all().filter(user_id=request.user.id), 5)
    page1 = p.page(str(page))
    context = {
        'trackers': page1,
        'paginator': p,
        'page': int(page),
    }
    return render(request, 'tracker/trackers.html', context)


@login_required(login_url='/authorization/log_error/')
def tracker(request, track_id):
    try:
        track_for_user = Tracker.objects.get(id=track_id)
    except Tracker.DoesNotExist:
        raise Http404("Трекер не існує")
    if request.user.id == track_for_user.user_id.id:
        context = {
            'ob': track_for_user,
        }
        return render(request, 'tracker/tracker.html', context)
    message = 'У вас немає доступу до даної сторінки'
    context = {
        'message': message,
    }
    return render(request, 'tracker/access_error.html', context)


def confirm(request, track_id):
    track = Tracker.objects.get(id=track_id)
    track.is_confirm = True
    track.save()
    return HttpResponse(1)
