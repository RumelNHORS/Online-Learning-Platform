from rest_framework import serializers
# from .models import Course, Enrollment
from courses import models as courses_model


# Serializer for Course model, used to serialize/deserialize Course objects
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = courses_model.Course
        fields = '__all__'

# Serializer for Enrollment model, used to serialize/deserialize Enrollment objects
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = courses_model.Enrollment
        fields = '__all__'
