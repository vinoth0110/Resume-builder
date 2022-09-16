from django.shortcuts import render
from.models import Profile
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io

#import wkhtmltopdf
# Create your views here.

def accept(request):
    print("before request")
    if request.method=="POST":
        name=request.POST.get("Name","")
        phone = request.POST.get("phone", "")
        email = request.POST.get("email", "")
        degree = request.POST.get("degree", "")
        university = request.POST.get("university", "")
        skills = request.POST.get("skills", "")
        about_you = request.POST.get("about_you", "")
        previous_work = request.POST.get("previous_work", "")
        print("inside request")
        profile=Profile.objects.create(name=name,phone=phone,email=email,degree=degree,university=university,skills=skills,about_you=about_you,previous_work=previous_work)
        profile.save()


    return render(request,"design/accept.html")


def resume(request,id):
    user_profile=Profile.objects.get(pk=id)
    template = loader.get_template("design/resume.html")
    html = template.render({'user_profile': user_profile})
    return render(request,"design/resume.html",{'user_profile':user_profile})

    option={
        'page-size':'letter',
        'encoding':'UTF-8'

    }
    pdf=pdfkit.from_string(html,False,option)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment'
    return response

def list(request):
    profile=Profile.objects.all()
    return render(request,"design/list.html",{'profile':profile})


    config=pdfkit.configuration(wkhtmltopdf="C:\Program Files\wkhtmltopdf")
    pdfkit.from_url("http://www.google.com/","google.pdf",configuration=config)
    #return render(request,"design/resume.html",{'user_Profile':user_Profile})
def next(request):
    return render(request,"design/next.html")