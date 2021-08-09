from django.contrib.auth import get_user_model
from .models import UsuarioWeb


class AuthenticationEmailBackend(object):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)

        except UserModel.DoesNotExist:
            return None
        else:
            if getattr(user, 'is_active', False) and user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        try:
            return UsuarioWeb.objects.get(pk=user_id)
        except UsuarioWeb.DoesNotExist:
            return None