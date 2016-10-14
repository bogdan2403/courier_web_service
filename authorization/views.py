from django.shortcuts import redirect, HttpResponse, render
from django.contrib import auth
from authorization.forms import UserRegistrationForm


# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/tracker/')


def login(request):
    if request.POST:
        username = request.POST.get('user', '')
        password = request.POST.get('pass', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponse(1)
        return HttpResponse(0)


def reg(request, errors=''):
    # перервірка чи авторизований користувач
    # авторизований не може потрапити на сторінку з реєстацією
    if request.user.is_authenticated():
        return redirect('/tracker/')
    context = {
        'form': UserRegistrationForm,
        'errors': errors,
    }
    return render(request, 'authorization/reg.html', context=context)


def add_reg(request):
    if request.POST:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.position_lat = 49.2339846
            new_user.position_long = 28.4138335
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('/tracker/')
        else:
            return reg(request, form.errors)


def log_error(request):
    if not request.user.is_authenticated():
        return render(request, 'authorization/error.html')
    else:
        return redirect('/tracker/')
