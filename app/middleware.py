from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class AuthUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            if request.session['username']:
                print('------     Middleware running      ------')
            else:
                HttpResponseRedirect(reverse)
        except Exception as e:
            print(e)
            HttpResponseRedirect(reverse("app:login"))
        return None
