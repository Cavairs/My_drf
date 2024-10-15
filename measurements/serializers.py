from rest_framework import serializers
from .models import Project, Measurement




class MeasurementSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Measurement   
        fields = ['value', 'created_at']  




class ProjectSerializer(serializers.ModelSerializer):  
    measurements = MeasurementSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'measurements']  

