from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.sessions.models import Session
from django.dispatch import receiver
from .models import UserSession




@receiver(user_logged_in)
def single_session(sender, request, user, **kwargs):
    old = UserSession.objects.filter(user=user).first()
    if old and old.session_key != request.session.session_key:
        Session.objects.filter(session_key=old.session_key).delete()
    UserSession.objects.update_or_create(
        user=user, defaults={"session_key": request.session.session_key}
    )


@receiver(user_logged_out)
def clear_session(sender, request, user, **kwargs):
    if user:
        UserSession.objects.filter(user=user).delete()