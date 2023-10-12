from django.contrib import admin
from .models import ServicePage, MainSlider, ClintProfile, Gallery, Testomonials, BlogPost, NewsPage, PollingResult, ElectionResult, ElectionResultDetails, ElectionSeatsAndParty,UpcommingElectionResult, CabinetMember

# Register your models here.
admin.site.register(MainSlider)

@admin.register(ServicePage)
class ServicePageAdmin(admin.ModelAdmin):
    list_display = ('id', 'Service_Title', 'First_Service_Image')


@admin.register(ClintProfile)
class ClintProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'date', 'title', 'video')

@admin.register(NewsPage)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'date', 'title', 'video')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']


@admin.register(Testomonials)
class TestomonialsAdmin(admin.ModelAdmin):
    list_display = ['id','image', 'name', 'memberpost', 'video']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id','title','image']



@admin.register(PollingResult)
class PollingResultAdmin(admin.ModelAdmin):
    list_display = ['id','state','opening_Poll', 'Exit_Poll', 'Result', 'image', 'video', 'date']


@admin.register(ElectionResult)
class ElectionResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'video', 'state', 'date', 'Ruling_Party']



@admin.register(ElectionResultDetails)
class ElectionResultDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'Constituency_Name', 'Candidate_Name', 'Party', 'Level', 'Votes', 'Margin']



@admin.register(ElectionSeatsAndParty)
class ElectionSeatsAndPartyAdmin(admin.ModelAdmin):
    list_display = ['id', 'seats', 'partylogo', 'partyname']


@admin.register(UpcommingElectionResult)
class UpcommingElectionResultAdmin(admin.ModelAdmin):
    list_display = ['id','state', 'date', 'Ruling_Party']



@admin.register(CabinetMember)
class CabinetMember(admin.ModelAdmin):
    list_display = ['id','image', 'name', 'desination']