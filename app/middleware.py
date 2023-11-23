# middleware.py
from django.utils.deprecation import MiddlewareMixin
from django.contrib.sessions.models import Session
from .models import Visitor
from django.utils import timezone

# class VisitorMiddleware(MiddlewareMixin):
#     def process_request(self, request):
#         # Récupérer l'adresse IP du visiteur
#         ip_address = request.META.get('REMOTE_ADDR')

#         # Récupérer l'agent utilisateur du visiteur
#         user_agent = request.META.get('HTTP_USER_AGENT')

#         # Enregistrer les informations dans la base de données
#         Visitor.objects.create(ip_address=ip_address, user_agent=user_agent)
class VisitorMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Check if the user is anonymous and has no active session
        if not request.user.is_authenticated and not request.session.exists(request.session.session_key):
            request.session.create()

        # Count visitors
        total_visitors = Session.objects.filter(expire_date__gte=timezone.now()).count()
        request.visitor_count = total_visitors