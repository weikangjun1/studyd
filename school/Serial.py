from rest_framework import serializers

from .models import students


class studentSerial(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = '__all__'
