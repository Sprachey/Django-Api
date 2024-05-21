from django.http import JsonResponse


def home(request):
    data = {"name" : "Sheikh"}
    return JsonResponse(data) 