from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage


def home(request, c_slug=None):
    c_page = None
    prod = None

    if c_slug != None:
        c_page = get_object_or_404(catgry, slug=c_slug)
        prod = products.objects.filter(category=c_page, available=True)
    else:
        prod = products.objects.all().filter(available=True)
    ct = catgry.objects.all()

    paginator = Paginator(prod, 3)  # creating a paginator object,I'm telling paginator to paginate prod queryset in pages of 2
    try:
        page = int(request.GET.get('page', '1'))  # getting the desired page number from url
    except:
        page = 1
    try:
        page_obj = paginator.page(page)  # returns the desired page object,i.e combine all data into page object
    except(EmptyPage, InvalidPage):  # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'pr': prod, 'ctg': ct, 'po': page_obj})


def prod_detail(request, c_slug, prod_slug):
    try:
        prod = products.objects.get(category__slug=c_slug, slug=prod_slug)
    except Exception as e:
        raise e
    return render(request, 'items.html', {'pr': prod})


def searching(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = products.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request, 'search.html', {'qr': query, 'pr': prod})

# Create your views here.
