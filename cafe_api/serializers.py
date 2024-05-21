from rest_framework import serializers
from .models import Cafe

class CafeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Cafe
        fields = "__all__"

        