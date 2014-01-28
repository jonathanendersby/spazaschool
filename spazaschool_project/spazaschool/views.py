from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from models import PageCopy

def landing(request):
    copy = PageCopy.objects.get(slug="landing").html_copy

    return render(
        request, 'spazaschool/landing.html',
        {'copy': copy, }
    )
