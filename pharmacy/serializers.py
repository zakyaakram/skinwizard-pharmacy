from rest_framework import serializers
from .models import Medicine



class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'  # this already includes `is_available`
