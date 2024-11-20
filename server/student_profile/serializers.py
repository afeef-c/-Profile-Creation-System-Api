from rest_framework import serializers
from .models import StudentProfile
from .validators import validate_password

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['name', 'email', 'phone', 'password']

    def validate_password(self, value):
        validate_password(value)
        return value
