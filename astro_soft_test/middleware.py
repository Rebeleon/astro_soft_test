from epoch.models import LogEntry


class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        log_entry = LogEntry(
            ip_address=request.META.get('REMOTE_ADDR'),
            user_agent=request.META.get('HTTP_USER_AGENT'),
            accept_language=request.META.get('HTTP_ACCEPT_LANGUAGE')
        )
        log_entry.save()

        response = self.get_response(request)
        return response
