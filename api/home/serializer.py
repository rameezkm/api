from rest_framework import serializers

from . models import Api

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model=Api
        fields=['id','name','product','desc']