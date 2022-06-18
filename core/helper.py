from django.http import JsonResponse

def create_response(data, message, status_code):
    result = {
        "status_code": status_code,
        "message": message,
        "data": data
        }
    return JsonResponse(result)
