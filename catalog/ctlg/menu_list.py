from catalog.ctlg.models import Category


def gener():
    i = -1
    my_list = []
    for index in Category.objects.filter(sub__isnull=True):
        my_list.append(recurfunc(index, i))
    return my_list


def recurfunc(sub, i):
    child = []
    i += 1
    for index in sub.categories.all():
        child.append(recurfunc(index, i))
    return {'main': sub, 'children': child, 'margin_left': i}


def listgener(my_list, new_list):
    for index in my_list:
        children = index.pop('children')
        new_list.append(index)
        listgener(children, new_list)