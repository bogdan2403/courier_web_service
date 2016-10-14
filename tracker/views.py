from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from tracker.models import User, Tracker


@login_required(login_url='/authorization/log_error/')
def index(request):
    return redirect('/tracker/trackers/')


@login_required(login_url='/authorization/log_error/')
def trackers(request, page=1):

    try:
        user = User.objects.get(id=request.user.id)
    except:
        return redirect('/admin')
    if request.user.id == user.id:
        page = int(page)
        user_by_id = []
        for u in Tracker.objects.all().filter(user_id=user.id).reverse():
            user_by_id.append(u)
        p = Paginator(user_by_id, 5)
        page1 = p.page(page)
        context = {
            'trackers': page1,
            'paginator': p,
            'page': page,
        }
        return render(request, 'tracker/trackers.html', context)
    message = 'У вас немає доступу до даної сторінки'
    context = {
        'message': message,
    }
    return render(request, 'tracker/access_error.html', context)


def tracker(request, track_id):
    user_id = Tracker.objects.get(id=track_id).user_id.id
    if request.user.id == user_id:
        track = Tracker.objects.get(pk=int(track_id))
        context = {
            'ob': track,
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
