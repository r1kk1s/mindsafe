from django.http import JsonResponse


JSON_DUMPS_PARAMS = {
    "ensure_ascii": False
}

def ret(json_object, status=200):
    """Отдает JSON с правильными HTTP заголовками и в читаемом
    в браузере виде в случае с кириллицей."""
    return JsonResponse(
        json_object,
        status=status,
        safe=not isinstance(json_object, list),
        json_dumps_params=JSON_DUMPS_PARAMS
    )


def error_response(exception):
    """Форматирует HTTP ответ с описанием ошибки и Traceback'om"""
    res = {"errorMessage": str(exception),
           "traceback": traceback.format_exc()}
    return ret(res, status=400)


def base_view(fn):
    """Декоратор для всех вьюшек, обрабатывающий исключения"""
    @functools.wraps(fn)
    def inner(request, *args, **kwargs):
        try:
            with transaction.atomic():
                return fn(request, *args, **kwargs)
        except Exception as e:
            return error_response(e)
    return inner