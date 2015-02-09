from operator import attrgetter
from catalog.ctlg.models import Unit
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


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