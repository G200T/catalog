from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginator(unit_list, page):
    paginator = Paginator(unit_list, 12)
    try:
        unit_list = paginator.page(page)
    except PageNotAnInteger:
        unit_list = paginator.page(1)
    except EmptyPage:
        unit_list = paginator.page(paginator.num_pages)

    return unit_list