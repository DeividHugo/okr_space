from apps.accounts.utils import set_current_user
from django.utils.deprecation import MiddlewareMixin

class CurrentUserMiddleware(MiddlewareMixin):
    
    def process_request(self, request):
        current_user = getattr(request, 'user', None)
        set_current_user(current_user)
