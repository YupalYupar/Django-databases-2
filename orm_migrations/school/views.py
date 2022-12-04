from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.prefetch_related('teachers').all()
    context = {'object_list':students}
    return render(request, template, context)
