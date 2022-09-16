from django.shortcuts import render,redirect
from department.forms import DepartmentForm
from department.models import Department
from django.urls import reverse
from django.contrib import messages

import school


def homepage(request):
    schools = Department.objects.all()
    context = {
        'departments': schools
    }
    return render(request, 'department/index.html', context)


def new_department(request):
    form = DepartmentForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect(reverse('add_department'))
    return render(request, 'department/add.html', context)

def delete_department(request, id):
    school = Department.objects.get(id=id)
    school.delete()
    messages.success(request, 'Deleted')
    return redirect(reverse('d_homepage'))


def update_department(request, id):
    school = Department.objects.get(id=id)
    form = DepartmentForm(request.POST or None, request.FILES or None, instance = school)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        messages.success(request, 'department record updated')
        return redirect(reverse("d_homepage"))
    return render(request, "department/update.html", context)
    