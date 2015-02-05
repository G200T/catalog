from catalog.ctlg.models import Category, Unit
from operator import attrgetter
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


# need fix
def get_cat3(cat):
    my_links = []
    line = cat[0:-1].split('/')
    try:
        for index, string in enumerate(line):
            if index == 0:
                my_links.append(Category.objects.get(sub__isnull=True, slug=string))
            else:
                my_links.append(Category.objects.get(slug=string))
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