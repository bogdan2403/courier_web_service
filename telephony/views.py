from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render
from telephony.models import Call
from tracker.models import User, Tracker
from django.core.exceptions import ObjectDoesNotExist


def call_me_page(request):
    if request.user.is_superuser:
        call = Call.objects.all().order_by('-pk')
        context = {
            'all_call': call,
        }
        return render(request, 'telephony/calls.html', context=context)
    else:
        message = 'У вас немає доступу до даної сторінки'
        context = {
            'message': message,
        }
        return render(request, 'tracker/access_error.html', context)


# AJAX зпити
def add_call(request, user_id, tracker_id):
    try:
        new_call = Call(user_id=User.objects.get(id=user_id), track_id=Tracker.objects.get(id=tracker_id))
        new_call.save()
    except ObjectDoesNotExist:
        return HttpResponse(0)
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
