from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from courses import models as courses_model
from courses import serializers as courses_serializer

# API view for listing courses with optional filtering by instructor, price, and duration
class CourseListAPIView(generics.ListAPIView):
    # Serializer class for Course model
    serializer_class = courses_serializer.CourseSerializer

    def get_queryset(self):
        # Retrieves all courses
        queryset = courses_model.Course.objects.all()  
        # Filters by instructor if provided
        instructor = self.request.query_params.get('instructor')
        # Filters by price if provided
        price = self.request.query_params.get('price')  
        # Filters by duration if provided
        duration = self.request.query_params.get('duration')

        if instructor:
            # Filters courses by instructor
            queryset = queryset.filter(instructor__icontains=instructor)  
        if price:
            # Filters courses by price
            queryset = queryset.filter(price=float(price))  
        if duration:
            # Filters courses by duration
            queryset = queryset.filter(duration=int(duration))  

        # Returns filtered queryset
        return queryset


# API view for creating a new course
class CourseCreateAPIView(generics.CreateAPIView):
    serializer_class = courses_serializer.CourseSerializer 

    def create(self, request, *args, **kwargs):
        # Retrieves course title from request data
        title = request.data.get('title')
        if courses_model.Course.objects.filter(title=title).exists():
            # Checks if a course with the provided title already exists
            return Response({"message": "A course with this title already exists."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)  # Serializes request data
        serializer.is_valid(raise_exception=True)  # Validates serializer data
        self.perform_create(serializer)  # Creates new course
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

# API view for retrieving, updating, or deleting a specific course
class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = courses_model.Course.objects.all() 
    serializer_class = courses_serializer.CourseSerializer 


# API view for creating a new enrollment
class EnrollmentCreateAPIView(generics.CreateAPIView):
    queryset = courses_model.Enrollment.objects.all() 
    serializer_class = courses_serializer.EnrollmentSerializer 


# API view for listing all enrollments
class EnrollmentListAPIView(generics.ListAPIView):
    queryset = courses_model.Enrollment.objects.all() 
    serializer_class = courses_serializer.EnrollmentSerializer