from django.shortcuts import render
from testApp.models import Employee
# Create your views here.
def ret_view(request):
    employee=Employee.objects.all()
    return render(request,'testApp/index.html',{'employee':employee})