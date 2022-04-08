from django.shortcuts import HttpResponse


def api_root(request):
    return HttpResponse('Backend Assessment API - Sarah Shamsi')