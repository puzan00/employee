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
    if request.method=="GET":
        departments = Department.objects.all()
        roles = Role.objects.all()
        context = {
            "departments": departments,
            "roles" :roles
        }
        return render(request, 'add.html', context)
    elif request.method=='POST':
        fn=request.POST['first_name']
        ln=request.POST['last_name']
        salary=request.POST['salary']
        dep = Department.objects.get(id=int(request.POST['dept']))
        rol = Role.objects.get(id=int(request.POST['role']))
        bonus=request.POST['bonus']
        phno=request.POST['phone']
        user = Employee(first_name=fn, last_name=ln, salary=salary, dept=dep, role=rol, bonus=bonus, phone=phno)
        user.save() 
        print(dep, rol)
        return redirect("/view-all/")
    else:
        return HttpResponse("Exception occurred could not add employee")

def delete(request, id):
    emp = Employee.objects.get(id = id)
    emp.delete()
    return redirect("/view-all/")

def edit(request, id):
    if request.method == 'GET':
        emp = Employee.objects.get(id = id)
        departments = Department.objects.all()
        roles = Role.objects.all()
        context = {
            'emp' : emp,
            'departments' : departments,
            'roles' : roles
        }
        print(emp.dept.id)
        return render(request, 'edit.html', context)
    elif request.method == "POST":
        # print("department ", request.POST['dept'])
        emp = Employee.objects.get(id = id)
        emp.first_name = request.POST['first_name']
        emp.last_name = request.POST['last_name']
        emp.salary = request.POST['salary']
        emp.dept = Department.objects.get(id=int(request.POST['dept']))
        emp.role = Role.objects.get(id=int(request.POST['role']))
        emp.bonus = request.POST['bonus']
        emp.phone = request.POST['phone']
        emp.save()
        return redirect("/view-all/")