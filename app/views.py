from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *

# Create your views here.
def Student(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        FD=StudentForm(request.POST)
        if FD.is_valid():
            return HttpResponse(str(FD.cleaned_data))
    
    
    
    return render(request,'student.html',d)
