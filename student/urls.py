from django.urls import path
from student.views import homepage, new_student, delete_student, update_student

urlpatterns = [
    path('student',homepage, name='s_homepage'),
    path('add-new-student', new_student, name='add_student'),
    path('delete/<int:id>/', delete_student, name='delete_student'),
    path('update/<int:id>/', update_student, name='update_student'),
]
