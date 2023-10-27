from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse
from appointment.models import UserDat
# from .models import UserDat





# def index1(request):

#     all_data = categories.objects.all()
#     all_course = courses.objects.all().prefetch_related('cat_id')
#     data = {"data":all_data,"course_data":all_course}
#     return render(request,'admin/course.html',data)

# def index(request):
#     all_data = UserDat.objects.all()
#     data = {"user_data": all_data}
#     return render(request,"doctor-profile-settings.html",data)


def UserData(request):
   if request.method == "POST":
       
      first_name = request.POST.get('first_name')
      last_name = request.POST.get('last_name')
      email = request.POST.get('email')
      password = request.POST.get('password')
      
      UserData_obj = UserDat()
      UserData_obj.first_name= first_name
      UserData_obj.last_name = last_name
      UserData_obj.email = email
      UserData_obj.password = password
      UserData_obj.save()
     
      return redirect('user_insert') 
   else:
      all_data = UserDat.objects.all()
      data = {"user_data": all_data}
      

   return render(request, "doctor-profile-settings.html",data)
   
   
   
   
      # messages.success(request,'Your data saved! Thank you.')
      # return redirect('user_index')   
   # return render(request,"doctor-profile-settings.html")
   

# def input_view(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('user_name')
#         user_email = request.POST.get('user_email')

#         if user_name and user_email:
#             UserData.objects.create(user_name=user_name, user_email=user_email)

#     return render(request, 'input.html')

# def display_data(request):
#     data = UserData.objects.all()
#     return render(request, 'display.html', {'data': data})
