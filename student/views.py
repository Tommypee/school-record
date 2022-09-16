from django.shortcuts import render, redirect
from student.forms import StudentForm
from django.urls import reverse
from student.models import Student
from django.contrib import messages

# Create your views here.

def homepage(request):
    schools = Student.objects.all()
    context = {
        'students': schools
    }
    return render(request, 'student/index.html', context)

def new_student(request):
    form = StudentForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect(reverse('add_student'))
    return render(request, 'student/add.html', context)

def delete_student(request, id):
    school = Student.objects.get(id=id)
    school.delete()
    messages.success(request, 'student record deleted')
    return redirect(reverse('s_homepage'))


def update_student(request, id):
    school = Student.objects.get(id=id)

    form = StudentForm(request.POST or None, request.FILES or None, instance = school)

    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        messages.success(request, 'student record updated')
        return redirect(reverse("s_homepage"))
    return render(request, "student/update.html", context)
       
