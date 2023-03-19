from django.shortcuts import render,HttpResponse,redirect
from emp_app.models import Employee, Department, Role
from .forms import EmployeeForm
# Create your views here.
def home(request):
    return render(request, 'home.html')
def view_all(request):
    emps=Employee.objects.all()
    return render(request, 'view_all.html',{'emps':emps})

def add(request):
    if request.method=='POST':
        fn=request.POST['first_name']
        ln=request.POST['last_name']
        salary=request.POST['salary']
        dep = Department.objects.get(id=int(request.POST['dept']))
        # dep=request.POST['dept']
        # rol=request.POST['role']
        rol = Role.objects.get(id=int(request.POST['role']))
        bonus=request.POST['bonus']
        phno=request.POST['phone']
        
        user = Employee(first_name=fn, last_name=ln, salary=salary, dept=dep, role=rol, bonus=bonus, phone=phno)
        user.save() 
        return redirect('/add/')
    elif request.method=="GET":
        departments = Department.objects.all()
        roles = Role.objects.all()
        context = {
            "departments": departments,
            "roles" :roles
        }
        return render(request, 'add.html', context)
    else:
        return HttpResponse("Exception occurred could not add employee")

def edit(request, id):
    emp=Employee.objects.get(id=id)
    if request.method=='GET':
        return render(request,'edit.html',{'emp':emp})
    else:
        emp.fn=request.POST['first_name']
        emp.ln=request.POST['last_name']
        emp.salary=request.POST['salary']
        emp.dep=request.POST['dept']
        emp.rol=request.POST['role']
        emp.bonus=request.POST['bonus']
        emp.phno=request.POST['phone']
        emp.save()
        return redirect('home')

# def remove(request,id):
#     Employee.objects.get(id=id).delete()
#     return redirect('view-all')