from django.shortcuts import render, redirect, get_object_or_404
from shop.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist


def cart_details(request, totl=0, count=0, ct_items=None):
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
        ct_items = items.objects.filter(cart=ct, active=True)
        for i in ct_items:
            totl += (i.prodt.price * i.quntity)
            count += i.quntity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'ci': ct_items, 'to': totl, 'cn': count})


def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def add_cart(request, product_id):
    prod = products.objects.get(id=product_id)
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct = cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items = items.objects.get(prodt=prod, cart=ct)
        if c_items.quntity < c_items.prodt.stock:
            c_items.quntity += 1
            c_items.save()
    except ObjectDoesNotExist:
        c_items = items.objects.create(prodt=prod, quntity=1, cart=ct)
        c_items.save()
    return redirect('CartDetails')
def min(request,product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(products, id=product_id)
    ct_items = items.objects.get(prodt=prod, cart=ct)
    if ct_items.quntity > 1:
        ct_items.quntity-=1
        ct_items.save()
    else:
        ct_items.delete()
    return redirect('CartDetails')
def Delete(request,product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(products, id=product_id)
    ct_items = items.objects.get(prodt=prod, cart=ct)
    ct_items.delete()
    return redirect('CartDetails')


# Create your views here.
