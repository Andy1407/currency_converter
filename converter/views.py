from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse


def index(request):
    if 'course' in request.GET and 'coursecurrency' in request.GET and 'input' in request.GET and 'from' in request.GET\
            and 'to' in request.GET:
        course = float(request.GET['course'])
        courseCurrency = request.GET['coursecurrency']
        inputConverter = float(request.GET['input'])
        fromConverter = request.GET['from']
        toConverter = request.GET['to']

        if fromConverter == courseCurrency:
            result = {'result': str(inputConverter/course)}

        elif toConverter == courseCurrency:
            result = {'result': str(inputConverter*course)}
        else:
            result = {'result': 'error'}

    else:
        result = {'result': 'error'}

    return JsonResponse(result)

# Create your views here.
