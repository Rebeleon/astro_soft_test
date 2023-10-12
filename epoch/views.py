from django.http import JsonResponse
import time


def data(request):
    current_time = int(time.time() * 1000)
    response_data = {"ts": current_time}
    return JsonResponse(response_data)
