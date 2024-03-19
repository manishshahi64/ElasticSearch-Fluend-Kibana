from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentAttendance

def save_attendance(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            standard = request.POST.get('standard')
            roll_number = request.POST.get('rollNumber')
            date = request.POST.get('date')
            attendance = StudentAttendance(name=name, standard=standard, roll_number=roll_number, date=date)
            attendance.save()
            return render(request,'save_attendance.html',{'message':'Sucessful'})
            
        return render(request,'save_attendance.html',{'message':'Invalid'})
    except Exception as error:
        print(error)
def show_attendance(request):
    try:
        attendance_records = StudentAttendance.objects.all()
        return render(request, 'show_attendance.html', {'attendance_records': attendance_records})
    except Exception as error:
        print(error)
