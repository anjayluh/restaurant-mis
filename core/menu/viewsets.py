from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from core.menu.models import Menu
from core.menu.serializers import MenuSerializer


class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [OrderingFilter]
    ordering_fields = ["updated_on"]
    ordering = ["-updated_on"]

    def get_queryset(self):
        return Menu.objects.all()
