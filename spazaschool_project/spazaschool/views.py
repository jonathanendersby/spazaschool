from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, \
    logout as auth_logout

from models import PageCopy, Module, ModuleSection


def landing(request):
    copy = PageCopy.objects.get(slug="landing").html_copy

    modules = Module.objects.all().filter(published=True).\
        order_by('sort_order')

    return render(
        request, 'spazaschool/landing.html',
        {
            'copy': copy,
            'modules': modules,
        }
    )


def login(request):
    if request.method == "POST":
        msisdn = '+27' + request.POST.get('phone_number')[1:]

        user = authenticate(msisdn=msisdn,
                            password=request.POST.get('password'))

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect(reverse('landing'))
            else:
                messages.add_message(request, messages.ERROR,
                                     'Login Failed - Account Disabled')

        else:
            messages.add_message(request, messages.ERROR,
                                 'Login Failed - Invalid Login')

    return render(
        request, 'spazaschool/login.html')


def logout(request):
    auth_logout(request)
    return redirect(reverse('landing'))


def register(request):
    copy = PageCopy.objects.get(slug="landing").html_copy

    return render(
        request, 'spazaschool/landing.html',
        {'copy': copy, }
    )
