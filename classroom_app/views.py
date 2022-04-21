from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from classroom_app.forms import LoginRegister, StudentRegister, ComplaintRegister, Notification_add
from classroom_app.models import Complaint, Notifications, Student


def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_home')
            elif user.is_student:
                return redirect('student_home')
        else:
            messages.info(request, 'INVALID CREDENTIALS')

    return render(request, 'login.html')


def student_register(request):
    user_form = LoginRegister()
    stud_form = StudentRegister()
    if request.method == 'POST':
        user_form = LoginRegister(request.POST)
        stud_form = StudentRegister(request.POST)
        if user_form.is_valid() and stud_form.is_valid():
            user = user_form.save(commit=False)
            user.is_student = True
            user.save()
            stud = stud_form.save(commit=False)
            stud.user = user
            stud.save()
            messages.info(request, 'student Register Successful')
            return redirect('login')
    return render(request, 'student_register.html', {'user_form': user_form, 'stud_form': stud_form})


# def complaint(request):
# form=ComplaintRegister()
def complaint_add(request):
    form = ComplaintRegister()
    u = request.user
    if request.method == 'POST':
        form = ComplaintRegister(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request,"complaint registered successfully")
            return redirect('complaint_view')
        else:
            form = ComplaintRegister()
    return render(request, 'complaint_add.html', {'form': form})

def complaint_view(request):
    data = Complaint.objects.all()
    context = {
        'data': data
    }
    return render(request, 'complaint_view.html',context)

def admin_home(request):
    return render(request, 'admin_home.html')

def student_home(request):
    return render(request, 'student_home.html')

def notification_add(request):
    form = Notification_add()
    a = request.user
    if request.method == 'POST':
        form = Notification_add(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = a
            obj.save()
            messages.info(request,"notification registered successfully")
            return redirect('notification_add')
        else:
            form = Notification_add()
    return render(request, 'notification_add.html', {'form': form})

def notification_view(request):
    data = Notifications.objects.all()
    context = {
        'data': data
    }
    return render(request, 'notification_view.html',context)
def student_reg_view(request):
    data = Student.objects.all()
    context = {
        'data':data
    }
    return render(request,'student_reg_view.html',context)

def update_view(request,id):
    obj = Student.objects.get(id=id)
    form =StudentRegister(request.POST or None,instance= obj)
    if form.is_valid():
        form.save()
        return redirect('student_reg_view')
    return render (request,'update.html',{'form':form})
def delete_view(request,id):
    obj = Student.objects.get(id=id)
    if request.method=='POST':
        obj.delete()
        return redirect('student_reg_view')
    return render(request,'delete.html')



