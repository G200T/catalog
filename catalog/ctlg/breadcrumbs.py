from catalog.ctlg.models import Category, Unit
from operator import attrgetter
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


def get_cat3(cat1, cat2, cat3):
    try:
        lvl1 = Category.objects.get(sub__isnull=True, slug=cat1)
        lvl2 = Category.objects.get(sub=lvl1, slug=cat2)
        lvl3 = Category.objects.get(sub=lvl2, slug=cat3)
    except ObjectDoesNotExist:
        raise Http404

    my_links = [lvl1, lvl2, lvl3]

    return my_links


def get_cat2(cat1, cat2):
    try:
        lvl1 = Category.objects.get(sub__isnull=True, slug=cat1)
        lvl2 = Category.objects.get(sub=lvl1, slug=cat2)
    except ObjectDoesNotExist:
        raise Http404

    my_links = [lvl1, lvl2]

    return my_links


def get_cat1(cat1):
    try:
        lvl1 = Category.objects.get(sub__isnull=True, slug=cat1)
    except ObjectDoesNotExist:
        raise Http404
    my_links = [lvl1]

    return my_links


def get_allunits(sub, my_list):
    for unit in sub.units.all():
        my_list.append(unit)
    for index in sub.categories.all():
        get_allunits(index, my_list)
    my_list.sort(key=attrgetter('name'))

    return my_list

def get_unit(unit):
    try:
        prod = Unit.objects.get(slug=unit)
    except ObjectDoesNotExist:
        raise Http404

    return prod