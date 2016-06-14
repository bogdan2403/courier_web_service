from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import auth

from tracker.models import User, Tracker


def index(request):
    if not request.user.is_authenticated():
        return redirect('/authorization/log_error/')
    return redirect('tracker/trackers/')

@login_required(login_url='/authorization/log_error/')
def trackers(request, page=1):
    user_name = auth.get_user(request).username
    user_id = auth.get_user(request).id
    try:
        user = User.objects.get(id=user_id)
    except:
        return redirect('/admin')
    if str(user_name) == str(user):
        user_id = int(user_id)
        page = int(page)
        user_by_id = Tracker.objects.all().filter(user_id=user_id)
        name = User.objects.get(pk=user_id).first_name
        p = Paginator(user_by_id, 2)
        page1 = p.page(page)
        context = {
            'user_name': user_name,
            'name': name,
            'trackers': page1,
            'paginator': p,
            'page': page,
            'user_id': user_id,
        }
        return render(request, 'tracker/trackers.html', context)
    message = 'У вас немає доступу до даної сторінки'
    context = {
            'user_name': user_name,
            'message': message,
    }
    return render(request, 'tracker/access_error.html', context)


def tracker(request, track_id):
    user_name = auth.get_user(request).username
    user_id = Tracker.objects.get(id=track_id).user_id
    if str(user_name) == str(User.objects.get(id=user_id.id)):
        track = Tracker.objects.get(pk=int(track_id))
        context = {
            'user_name': user_name,
            'ob': track,
        }
        return render(request, 'tracker/tracker.html', context)
    message = 'У вас немає доступу до даної сторінки'
    context = {
        'user_name': user_name,
        'message': message,
    }
    return render(request, 'tracker/access_error.html', context)