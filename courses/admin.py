from django.contrib import admin
# from .models import Course, Enrollment
from courses import models as cource_model

admin.site.register(cource_model.Course)
admin.site.register(cource_model.Enrollment)
