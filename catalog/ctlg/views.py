from django.template import loader, RequestContext
from django.http.response import HttpResponse
from catalog.ctlg.models import Unit
from catalog.ctlg.breadcrumbs import get_allunits, get_unit, get_cat1, get_cat2, get_cat3
from catalog.ctlg.paginator import paginator


def search(request):
    if 'q' in request.GET:
        term = request.GET['q']
    search_list = Unit.objects.filter(name__icontains=term)
    pag_list = paginator(search_list, request)
    t = loader.get_template("category_list.html")
    c = RequestContext(request, {'Unit_list': pag_list, 'term': term})

    return HttpResponse(t.render(c))


def base(request):
    unit_list = Unit.objects.all()
    pag_list = paginator(unit_list, request)
    t = loader.get_template("category_list.html")
    c = RequestContext(request, {'Unit_list': pag_list})

    return HttpResponse(t.render(c))


def my_cat1(request, cat1):
    my_list = []
    my_links = get_cat1(cat1)
    unit_list = get_allunits(my_links[-1], my_list)
    pag_list = paginator(unit_list, request)
    t = loader.get_template("category_list.html")
    c = RequestContext(request, {'Unit_list': pag_list, 'link_list': my_links})

    return HttpResponse(t.render(c))


def my_cat2(request, cat1, cat2):
    my_list = []
    my_links = get_cat2(cat1, cat2)
    unit_list = get_allunits(my_links[-1], my_list)
    pag_list = paginator(unit_list, request)
    t = loader.get_template("category_list.html")
    c = RequestContext(request, {'Unit_list': pag_list, 'link_list': my_links})

    return HttpResponse(t.render(c))


def my_cat3(request, cat1, cat2, cat3):
    my_list = []
    my_links = get_cat3(cat1, cat2, cat3)
    unit_list = get_allunits(my_links[-1], my_list)
    pag_list = paginator(unit_list, request)
    t = loader.get_template("category_list.html")
    c = RequestContext(request, {'Unit_list':  pag_list, 'link_list': my_links})

    return HttpResponse(t.render(c))


def units3(request, cat1, cat2, cat3, unit):
    my_links = get_cat3(cat1, cat2, cat3)
    prod = get_unit(unit)
    t = loader.get_template("detail_unit.html")
    c = RequestContext(request, {'prod':  prod, 'link_list': my_links})

    return HttpResponse(t.render(c))


def units2(request, cat1, cat2, unit):
    my_links = get_cat2(cat1, cat2)
    prod = get_unit(unit)
    t = loader.get_template("detail_unit.html")
    c = RequestContext(request, {'prod':  prod, 'link_list': my_links})

    return HttpResponse(t.render(c))


def units1(request, cat1, unit):
    my_links = get_cat1(cat1)
    prod = get_unit(unit)
    t = loader.get_template("detail_unit.html")
    c = RequestContext(request, {'prod':  prod, 'link_list': my_links})

    return HttpResponse(t.render(c))
