from django.shortcuts import render
from testApp.models import Employee
from testApp.forms import EmployeeForm
# Create your views here.
def ret_view(request):
    employee=Employee.objects.all()
    return render(request,'testApp/index.html',{'employee':employee})

def create_view(request):
    form=EmployeeForm()
    return render(request,'testApp/create.html',{'form':form})