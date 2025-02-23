from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from.forms import SignUpForm ,AddRecordForm
from .models import Student

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Student  # Make sure Student is imported from your models

def home(request):
    # Retrieve all student records from the database.
    students = Student.objects.all()

    # Check if the user is submitting the login form.
    if request.method == "POST":
        username = request.POST.get('username')  # Use .get() to avoid KeyError
        password = request.POST.get('password')

        if username and password:  # Ensure both fields are filled
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You Have Been Logged In')
                return redirect('home')  # Redirect after login success
            else:
                messages.error(request, ' Username or Password Incorrect')
        else:
            messages.error(request, 'Please enter both username and password.')

        return redirect('home')  # Redirect to avoid form re-submission

    return render(request, 'home.html', {'students': students})



def logout_user(request):
    logout(request)
    messages.success(request ,'You have been logged out....')
    return redirect ('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request , user)

            messages.success(request, 'You Have Successfully Registered !')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})



def record_detail(request ,pk):
    
    # If user is Logged In
    
    if request.user.is_authenticated:

    # check Record

        records = Student.objects.get(id=pk)

        return render(request, 'records.html', {'records': records})

    else:
          messages.success(request, 'You Have To Logging In To View Records')
          return redirect('home')


    # DELETE RECORD

def delete_detail(request ,pk):
    if request.user.is_authenticated:
       delete_student = Student.objects.get(id=pk)
       delete_student.delete()
       messages.success(request, ' Record Deleted Sucessfully')
       return redirect('home')

    else:
      messages.success(request, ' You must be logged in First ')
      return redirect('home')
    
    # ADDING RECORDS

def add_record(request):

    form =AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record=form.save()
                messages.success(request,"Recorded Added Successfully")
                return redirect('home')
                
        return render(request, 'add_record.html', {'form':form})

    else:
                messages.success(request,"You Must Be Logged In First")
                return redirect('home')


def update_record(request,pk):
    if request.user.is_authenticated:
        currrent_student= Student.objects.get(id=pk)
        form =AddRecordForm(request.POST or None, instance= currrent_student)
        if form.is_valid():
            form.save()
            messages.success(request,"Updated Successfully")
            return redirect('home')

        return render(request, 'update_record.html', {'form':form})
    
    else:

                messages.success(request,"You Must Be Logged In First")
                return redirect('home')


    
    