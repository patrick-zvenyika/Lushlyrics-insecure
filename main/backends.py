from django.contrib.auth.backends import BaseBackend
from .models import playlist_user

class PlaylistUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = playlist_user.objects.get(username=username)
            # Implement your authentication logic here, e.g., check password
            if user.check_password(password):
                return user
        except playlist_user.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return playlist_user.objects.get(pk=user_id)
        except playlist_user.DoesNotExist:
            return None
