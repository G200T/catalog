from catalog.ctlg.models import Category


def get_cat3(cat1, cat2, cat3):
    lvl1 = Category.objects.get(sub__isnull=True, slug=cat1)
    lvl2 = Category.objects.get(sub=lvl1, slug=cat2)
    lvl3 = Category.objects.get(sub=lvl2, slug=cat3)
    my_links = [lvl1, lvl2, lvl3]

    return my_links


def get_cat2(cat1, cat2):
    lvl1 = Category.objects.get(sub__isnull=True, slug=cat1)
    lvl2 = Category.objects.get(sub=lvl1, slug=cat2)
    my_links = [lvl1, lvl2]

    return my_links


def get_cat1(cat1):
    lvl1 = Category.objects.get(sub__isnull=True, slug=cat1)
    my_links = [lvl1]

    return my_links


def get_unit(sub, my_list):
    for unit in sub.units.all():
        my_list.append(unit)
    for index in sub.categories.all():
        get_unit(index, my_list)

    return my_list
