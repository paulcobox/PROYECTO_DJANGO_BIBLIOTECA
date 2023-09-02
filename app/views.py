from django.shortcuts import render, redirect
from django.urls import reverse # Flask -> url_for
from django.views.decorators.http import require_http_methods
from .forms import AuthorForm


# Create your views here.
@require_http_methods(['GET', 'POST']) #este decoraror me permite recibir mas de un metodo http
def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('biblioteca:index'))
    else:
        form = AuthorForm()

    return render(request, 'author/test.html', {
        'form': form
    })
