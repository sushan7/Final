from django.shortcuts import render
from django.http import HttpResponse
from . models import restoinfo

# Create your views here.

def index(request):
	all_resto = restoinfo.objects.all()
    #return HttpResponse("<h2> hdhdg </h2>")
    return render(request,"restoreview/index.html",{'restos': all_resto})

def addresto(request):
    return render(request,"restoreview/add_resto.html")

def add_resto_form_submission(request):
   print("the form is submitteds")
   restoname = request.POST["resto_name"]
   restotype = request.POST["resto_type"]
   restooreview = request.POST["resto_review"]
   restodetail = request.POST["resto_detail"]

   resto_info = restoinfo(resto_name = restoname,resto_type = restotype,resto_review = restooreview,resto_detail = restodetail)
   resto_info.save()
   return render(request,"restoreview/add_resto.html")

# def add_resto_form_submission(request):
# 	if form .is_valid():
# 		text= form.cleaned_data['resto_name']
# 		text1= form.cleaned_data['resto_review']
# 		text2= form.cleaned_data['resto_type']
# 		text3= form.cleaned_data['resto_detail']
# 	return render(request,text, text1, text2, text3)
