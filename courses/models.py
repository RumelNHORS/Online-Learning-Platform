from django.db import models
    

# Model representing a Course
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    price = models.FloatField()
    currency = models.CharField(max_length=3, default='USD')  # Assuming currency code is 3 characters long

    def __str__(self):
        return f"{self.id} - {self.title} - {self.price} - {self.currency}"
    

# Model representing Enrollment of a student in a course
class Enrollment(models.Model):
    student_name = models.CharField(max_length=100)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} - {self.student_name} - {self.course_name.title}"
