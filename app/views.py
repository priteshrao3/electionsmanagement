from django.shortcuts import render
from django.views import View
from .models import ServicePage, MainSlider, ClintProfile, Gallery, Testomonials, BlogPost, NewsPage, PollingResult, ElectionResult, ElectionResultDetails, ElectionSeatsAndParty, UpcommingElectionResult, CabinetMember
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.
class HomePage(View):
    template_name = ''
    def get(self, request):
        service = ServicePage.objects.all()
        mainslider = MainSlider.objects.all()
        clintprofile = ClintProfile.objects.all()
        gallery = Gallery.objects.all()
        testo = Testomonials.objects.all()
        news =NewsPage.objects.all()
        blogpost = BlogPost.objects.all()
        polling = PollingResult.objects.all()
        elections = ElectionResult.objects.all()
        upcommingelections = UpcommingElectionResult.objects.all()
        member = CabinetMember.objects.all()

        return render(request, self.template_name, {
            'services':service, 'slider':mainslider, 'clintprofile':clintprofile,'gallery':gallery,
            'testo':testo, 'news':news, 'blogpost':blogpost, 'polling':polling, 'elections':elections, 
            'upcommingelections':upcommingelections, 'member':member})
    


    def post(self, request):

        username = 'Name: '
        useremail = 'Email: '
        userphone = 'Phone No.: '

        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        mobile = request.POST['mobile']
        message = request.POST['message']
        send_mail(
            subject,
            username+name +'\n'+'\n'+   useremail+email +'\n'+'\n'+  userphone+mobile +'\n'+'\n'+ message,
            settings.EMAIL_HOST_USER,
            ['devloperpritesh@gmail.com'],
            fail_silently=False,
        )
        messages.success(request,'Message send Successfull')
        return render(request, self.template_name)



# News Page view
class News(View):
    def get(self, request, new):
        service = ServicePage.objects.all()
        news_title = new.replace('-', ' ')
        newsall = NewsPage.objects.all()
        news = NewsPage.objects.get(title=news_title)
        return render(request, 'newsdetails.html', {'new':news, 'newsall':newsall, 'services':service})

  
       
# Profile Page view
class Profile(View):
    def get(self, request, prof):
        service = ServicePage.objects.all()
        profile_title = prof.replace('-', ' ')
        clintprofile = ClintProfile.objects.all()
        clintprofiles=ClintProfile.objects.get(title=profile_title)  
        return render(request, 'profiledetails.html', {'profile':clintprofiles, 'clintprofile':clintprofile, 'services':service})




# Service Page view
class Services(View):
    def get(self, request, servd):
        serv_title = servd.replace('-', ' ')
        service = ServicePage.objects.all()
        services=ServicePage.objects.get(Service_Title=serv_title)  
        return render(request, 'services.html', {'serv':services, 'services':service})
    

    def post(self, request, servd):
        serv_title = servd.replace('-', ' ')
        service = ServicePage.objects.all()
        services=ServicePage.objects.get(Service_Title=serv_title) 

        username = 'Name: '
        useremail = 'Email: '
        userphone = 'Phone No.: '

        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        mobile = request.POST['mobile']
        message = request.POST['message']
        send_mail(
            subject,
            username+name +'\n'+'\n'+   useremail+email +'\n'+'\n'+  userphone+mobile +'\n'+'\n'+ '\n'+message,
            settings.EMAIL_HOST_USER,
            ['devloperpritesh@gmail.com'],
            fail_silently=False,
        )
        messages.success(request,'Message send Successfull')
        return render(request, 'services.html', {'serv':services, 'services':service})


# Blog Pages View
class Blogs(View):
    def get(self, request, blog):
        service = ServicePage.objects.all()
        blog_title = blog.replace('-', ' ')
        allblogs = BlogPost.objects.all()
        blog=BlogPost.objects.get(title=blog_title)  
        return render(request, 'profiledetails.html', {'blogs':allblogs, 'blog':blog, 'services':service})


# Polling View
class Poling(View):
    def get(self, request, stat):
        service = ServicePage.objects.all()
        state_title = stat.replace('-', ' ')
        pollings = PollingResult.objects.all()
        polling=PollingResult.objects.get(state=state_title)  
        return render(request, 'pollingdetails.html', {'pollings':pollings, 'polling':polling, 'services':service})
    


# Elections Result View
class Elections(View):
    def get(self, request, elect):
        service = ServicePage.objects.all()
        state_title = elect.replace('-', ' ')
        elections = ElectionResult.objects.all()
        election = ElectionResult.objects.get(state=state_title)
        electionresultdetail = ElectionResultDetails.objects.all()
        electionseatsandparty = ElectionSeatsAndParty.objects.all()
        return render(request, 'electionresultdetails.html', {'elections':elections, 'election':election, 'electionresultdetail':electionresultdetail,'services':service, 'electionseatsandparty':electionseatsandparty})
    

# Contact Us Pages View
def contact(request):
    service = ServicePage.objects.all()
    member = CabinetMember.objects.all()
    if request.method == 'POST':

        username = 'Name: '
        useremail = 'Email: '
        userphone = 'Phone No.: '

        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        mobile = request.POST['mobile']
        message = request.POST['message']
        send_mail(
            subject,
            username+name +'\n'+'\n'+   useremail+email +'\n'+'\n'+  userphone+mobile +'\n'+'\n'+ message,
            settings.EMAIL_HOST_USER,
            ['devloperpritesh@gmail.com'],
            fail_silently=False,
        )
        messages.success(request,'Message send Successfull')
    return render(request, 'contact.html', {'services':service, 'member':member})