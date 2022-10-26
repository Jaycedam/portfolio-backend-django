from rest_framework import serializers
from .models import Project, Area

class ProjectSerializer(serializers.ModelSerializer):
    # custom field to display name of the area
    area = serializers.CharField(read_only=True, source="id_area.name")

    class Meta:
        model = Project
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'