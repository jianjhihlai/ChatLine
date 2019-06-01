from django.utils.deprecation import MiddlewareMixin

class DisableCsrfCheck(MiddlewareMixin):

    def process_request(self, request):
        attr = '_dont_enforce_csrf_checks'
        if not getattr(request, attr, False):
            setattr(request, attr, True)