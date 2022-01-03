from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Main,Contact
from .track2 import *

# main pager
def home(request):
  #user register form
  if request.method == 'POST' and 'MainForm' in request.POST:
    main = Main()
    name = request.POST.get('Name')
    email = request.POST.get('Email')
    if Main.objects.filter(email=email).exists():
        return render(request, 'main/used.html')
    mobile = request.POST.get('Mobile')
    #validate mobile number
    if len(mobile) != 10:
      messages.warning(request, f'Please enter a valid mobile number')
      return redirect('yoga-home')
    if Main.objects.filter(mobile=mobile).exists():
        return render(request, 'main/used.html')
    main.name = name
    main.email = email
    main.mobile = mobile
    main.save()
    return render(request,'main/demo.html')
  
  #contact section form
  if request.method == 'POST' and 'ContactForm' in request.POST:
    contact = Contact()
    name = request.POST.get('name')
    email = request.POST.get('email')
    comment = request.POST.get('comment')
    contact.name = name
    contact.email = email
    contact.comment = comment
    contact.save()
    return render(request,'main/success.html')
  
  # model start/stop
  if request.method == 'POST' and 'start' in request.POST:
    start()
  if request.method == 'POST' and 'stop' in request.POST:
    close()

  return render(request,'main/home.html')

# Admin
# admin pass-> bharat1234