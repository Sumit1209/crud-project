from django.shortcuts import render,HttpResponse
from .models import Student
from datetime import datetime


from datetime import datetime

# Create your views here.
def index (request):
    return render(request,'index.html')

def all_emp (request):
    emps= Student.objects.all()
    context = {
        'emps':emps
    }
    print(context)

    
  
    return render(request,'view_all_emp.html',context)

def add_emp (request):
    if request.method =='POST' :
        student_name=request.POST.get('Student_name')
        salary = request.POST.get('salary')
        dep = request.POST.get('dep')
        
        bonus = request.POST.get('bonus')
        phone = request.POST.get('phone')
        
        role = request.POST.get('role')
        add_emp = Student(student_name=student_name, salary=salary, bonus=bonus, phone=phone, dep = dep, role = role, hire_date = datetime.now())
        add_emp.save()
        return HttpResponse('Employee added Successfully')
    elif request.method =='GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An Exception Occured! Employee Has Not Been Added")

def remove_emp (request):
    return render(request,'remove_emp.html')

def filter_emp (request):
    return render(request,'filter_emp.html')