from django.test import TestCase

# Create your tests here.
<<<<<<< HEAD
=======
from django.views.decorators.clickjacking import XFrameOptionsMiddleware
from django.middleware.csrf import CsrfViewMiddleware

class XCTOMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-Content-Type-Options'] = "nosniff"
        return response



class MyMiddleware(CsrfViewMiddleware):
    def process_view(self, request, callback, callback_args, callback_kwargs):
        response = super().process_view(request, callback, callback_args, callback_kwargs)
        if request.method == "POST":
            if request.COOKIES.get("csrftoken", "") != request.POST.get("csrfmiddlewaretoken", ""):
                return self._reject(request, 'CSRF cookie not set.')
        return response

>>>>>>> 1cb3347 (Parcheo1S)
