from RestAPI.models import *
from rest_framework import serializers

class makananSerializers(serializers.ModelSerializer):
    class Meta:
        model = makanan
        fields = "__all__" 