from catalog.ctlg.menu_list import listgener, gener


def menu(request):
    my_list = gener()
    new_list = []
    listgener(my_list, new_list)

    return {'cat_list': new_list}

