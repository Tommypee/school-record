from django.urls import path
from department.views import homepage, new_department , delete_department, update_department











urlpatterns = [
    path('department', homepage, name='d_homepage'),
    path('add-new-department', new_department, name='add_department'),
    path('dept-delete/<int:id>/', delete_department, name='delete_department'),
    path('dept-update/<int:id>/', update_department, name='update_department'),
]