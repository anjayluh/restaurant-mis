from rest_framework import routers
from core.menu.viewsets import MenuViewSet
from core.user.viewsets import UserViewSet
from core.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet

router = routers.SimpleRouter()
# menu
router.register(r"menu", MenuViewSet, basename="menu")

# AUTHENTICATION
router.register(r"auth/login", LoginViewSet, basename="auth-login")
router.register(r"auth/register", RegistrationViewSet, basename="auth-register")
router.register(r"auth/refresh", RefreshViewSet, basename="auth-refresh")

# USER
router.register(r"user", UserViewSet, basename="user")

urlpatterns = [*router.urls]

