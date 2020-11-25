from django.shortcuts import render,redirect
from testApp.models import Employee
from testApp.forms import EmployeeForm
# Create your views here.
def ret_view(request):
    employee=Employee.objects.all()
    return render(request,'testApp/index.html',{'employee':employee})

def create_view(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST) #get the data from the form
        if form.is_valid():#basic authentication
            form.save()#save the data from the form
        return redirect('/r')#return to homepage after submitting the form
    return render(request,'testApp/create.html',{'form':form})

def delete_view(request,id):
    employee=Employee.objects.all().get(id=id)
    employee.delete()
    return redirect('/r')
