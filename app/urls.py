from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views


urlpatterns = [
     path('', views.HomePage.as_view(template_name='index.html'), name='home'),
     path('faq', views.HomePage.as_view(template_name='faq.html'), name='faq'),
     path('carrier', views.HomePage.as_view(template_name='carrier.html'), name='carrier'),
     path('survey', views.HomePage.as_view(template_name='survey.html'), name='survey'),
     path('openionpoll', views.HomePage.as_view(template_name='openionpoll.html'), name='openionpoll'),

     path('upcommingelectionresult', views.HomePage.as_view(template_name='upcommingelectionresult.html'), name='upcommingelectionresult'),

     path('electionresult', views.HomePage.as_view(template_name='electionresult.html'), name='electionresult'),
     path('electionresultdetails/<elect>', views.Elections.as_view(), name='electionresultdetails'),

     path('exitpoll', views.HomePage.as_view(template_name='exitpoll.html'), name='exitpoll'),
     path('pollingdetails/<stat>', views.Poling.as_view(), name='pollingdetails'),


     path('blog', views.HomePage.as_view(template_name='blog.html'), name='blog'),
     
     path('profile', views.HomePage.as_view(template_name='profile.html'), name='profile'),
     path('profiledetails/<prof>', views.Profile.as_view(), name='profiledetails'),

     path('services/<servd>', views.Services.as_view(), name='services'),

     path('news', views.HomePage.as_view(template_name='news.html'), name='news'),
     path('newsdetails/<new>', views.News.as_view(), name='newsdetails'),

     path('contact', views.contact, name='contact'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)