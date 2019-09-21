from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import Review, STATUS_CHOICES, ACTIVE
from django.http import Http404


def index_review_view(request, *args, **kwargs):
    reviews = Review.objects.filter(status=ACTIVE).order_by('-created')
    return render(request, 'index.html', context={
        'reviews': reviews,
    })
