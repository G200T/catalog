from catalog.ctlg.models import Category, Unit
from operator import attrgetter
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
import re


def get_cat3(cat):
    my_links = []
    p = re.compile(r'/')
    line = p.split(cat[0:-1])
    line.reverse()
    try:
        for index in line:
            my_links.append(Category.objects.get(slug=index))
    except ObjectDoesNotExist:
        raise Http404

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