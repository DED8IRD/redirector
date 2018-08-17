from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import random

from .models import URL, SavedLink
from .forms import URLForm

def index(request):
    link = None
    error = None
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            if not url.startswith('http'):
                url = 'http://' + url   
            try:         
                validate = URLValidator(schemes=('http', 'https'))
                validate(url)
                link = url_map(url)
            except (ValueError, ValidationError):
                error = f'Invalid URL: {url}'

    context = {
        'form': URLForm(),
        'link': link, 
        'error': error,
    }
    return render(request, 'URLshortener/index.html', context)


@login_required
def links(request):
    context = {
        'links': SavedLink.objects.filter(user=request.user),
        'base': settings.BASE_URL
    }
    return render(request, 'URLshortener/user_links.html', context)


def shortened_redirect(request, code):
    url = get_object_or_404(URL, code=code)
    url.access_count += 1
    url.save()
    return redirect(url.url)


@login_required
def save_link(request, code):
    url = get_object_or_404(URL, code=code)
    SavedLink(url=url, user=request.user).save()
    return redirect('URLshortener:links')


@login_required
def delete_link(request, pk):
    get_object_or_404(SavedLink, pk=pk).delete()
    return redirect('URLshortener:links')


def url_map(url):
    if URL.objects.filter(url=url).exists():
        return URL.objects.get(url=url)
    else:
        code = shorten_url(url)
        new_url = URL(url=url, code=code)
        new_url.save()
        return new_url


def shorten_url(url):
    valid_chars = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
    while True:
        code = ''.join(random.choices(valid_chars, k=6))
        if not URL.objects.filter(code=code).exists():
            return code