from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Review, STATUS_CHOICES, ACTIVE
from webapp.forms import ReviewForm
from django.http import Http404


def index_review_view(request, *args, **kwargs):
    reviews = Review.objects.filter(status=ACTIVE).order_by('-created')
    return render(request, 'index.html', context={
        'reviews': reviews,
    })


def review_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = ReviewForm()
        return render(request, 'create.html', context={'form': form})
    elif request.method == 'POST':
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            review = Review.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text'])
            return redirect('index')
        else:
            return render(request, 'create.html', context={'form': form})
