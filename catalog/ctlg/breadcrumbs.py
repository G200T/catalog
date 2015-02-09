from catalog.ctlg.models import Category
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist



def get_cat(cat):
    my_links = []
    line = cat[0:-1].split('/')
    try:
        for index, string in enumerate(line):
            if index == 0:
                my_links.append(Category.objects.get(sub__isnull=True, slug=string))
            else:
                my_links.append(Category.objects.get(sub=my_links[-1], slug=string))
    except ObjectDoesNotExist:
        raise Http404

    return my_links