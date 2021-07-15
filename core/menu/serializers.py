from rest_framework import serializers
from core.menu.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["id", "name", "description", "price", "created_on", "updated_on"]

