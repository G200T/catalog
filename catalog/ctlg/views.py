from django.template import loader, RequestContext
from django.http.response import HttpResponse
from catalog.ctlg.models import Unit
from catalog.ctlg.breadcrumbs import get_allunits, get_unit, get_cat3
from catalog.ctlg.paginator import paginator


def search(request):
    if request.method == 'POST' and request.is_ajax():
        term = request.POST['line']
        t = loader.get_template("ajaxtemplate.html")
        search_list = Unit.objects.filter(name__icontains=term)
        pag_list = paginator(search_list, request)
        c = RequestContext(request, {'Unit_list':  pag_list})

    return HttpResponse(t.render(c))


def base(request):
    unit_list = Unit.objects.all()
    pag_list = paginator(unit_list, request)
    t = loader.get_template("category_list.html")
    c = RequestContext(request, {'Unit_list': pag_list})

    return HttpResponse(t.render(c))


def my_cat(request, cat):
    my_list = []
    my_links = get_cat3(cat)
    unit_list = get_allunits(my_links[-1], my_list)
    pag_list = paginator(unit_list, request)
    t = loader.get_template("category_list.html")
    c = RequestContext(request, {'Unit_list':  pag_list, 'link_list': my_links})

    return HttpResponse(t.render(c))


def units(request, unit, cat):
    my_links = get_cat3(cat)
    prod = get_unit(unit)
    t = loader.get_template("detail_unit.html")
    c = RequestContext(request, {'prod':  prod, 'link_list': my_links})
    return HttpResponse(t.render(c))