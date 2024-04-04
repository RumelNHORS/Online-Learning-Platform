from django.urls import path
from courses import views


# URL patterns for API endpoints
urlpatterns = [
    # Endpoint for listing courses
    path('courses_list/', views.CourseListAPIView.as_view(), name='course_list'),
    
    # Endpoint for creating a new course
    path('course_create/', views.CourseCreateAPIView.as_view(), name='course_create'),
    
    # Endpoint for retrieving, updating, or deleting a specific course
    path('course/<int:pk>/', views.CourseDetailAPIView.as_view(), name='course_detail'),
    
    # Endpoint for creating a new enrollment
    path('enrollments/', views.EnrollmentCreateAPIView.as_view(), name='enrollment_create'),
    
    # Endpoint for listing all enrollments
    path('enrollments_list/', views.EnrollmentListAPIView.as_view(), name='enrollment_list'),
]
