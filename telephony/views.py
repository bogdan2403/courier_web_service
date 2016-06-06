from django.contrib import auth
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from telephony.models import Call
from tracker.models import User, Tracker


def call_me_page(request, page=1):
    user_name = auth.get_user(request).username
    page = int(page)
    call = reversed(Call.objects.all())
    p = Paginator(list(call), 10)
    page1 = p.page(page)
    context = {
        'user_name': user_name,
        'all_call': page1,
        'paginator': p,
        'page': page,
        'len_calls': Call.objects.count()
    }
    return render(request, 'telephony/calls.html', context=context)


# AJAX зпити
def add_call(request, user_id, tracker_id):
    new_call = Call(user_id=User.objects.get(id=user_id), track_id=Tracker.objects.get(id=tracker_id))
    new_call.save()
    return HttpResponse(1)


def check_new_call(request, len_obj):
    if int(len_obj) == Call.objects.count():
        return HttpResponse(0)
    else:
        return HttpResponse(1)


def change_call(request, call_id):
    call = Call.objects.get(id=call_id)
    call.is_called = True
    call.save()
    return HttpResponse(1)


def clear_all(request):
    for call in Call.objects.all():
        call.delete()
    return HttpResponse(1)
