from django.db import models
from embed_video.fields import EmbedVideoField


# Main Slider models.
class MainSlider(models.Model):
    image = models.ImageField(upload_to="sliderimg", blank=True)        

# News Page models.
class NewsPage(models.Model):
    image = models.ImageField(upload_to="newsimg", blank=True)
    date = models.DateField(blank=True)
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    sub_Content = models.TextField(max_length=300, blank=True)
    video = EmbedVideoField(blank=True)

    def title_to_url(self):
        return self.title.replace(' ', '-')

# Clint Profile models.
class ClintProfile(models.Model):
    image = models.ImageField(upload_to="clintprofile", blank=True)
    date = models.DateField(blank=True)
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    Sub_Content = models.TextField(max_length=300, blank=True)
    video = EmbedVideoField(blank=True)

    def title_to_url(self):
        return self.title.replace(' ', '-')
    
# Service Page models.
class ServicePage(models.Model):
    Service_Title =models.CharField(max_length=50, blank=True)
    First_Service_Image = models.ImageField(upload_to="servimg", blank=True)
    First_Service_Content = models.TextField( max_length=2000, blank=True)
    video = EmbedVideoField(blank=True)

    def title_to_url(self):
        return self.Service_Title.replace(' ', '-')
    
# Gallery on Home Page models.
class Gallery(models.Model):
    image = models.ImageField(upload_to='galleryimg', blank=True)

# Testomonials on Home Page models.
class Testomonials(models.Model):
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='CabinetMembers', blank=True)
    name = models.CharField(max_length=100, blank=True)
    memberpost = models.CharField(max_length=100, blank=True)
    video = EmbedVideoField(blank=True)

# Blog Page models.
class BlogPost(models.Model):
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='blogimg', blank=True)
    content = models.TextField(blank=True)
    Sub_Content = models.TextField(max_length=300, blank=True)

    def title_to_url(self):
        return self.title.replace(' ', '-')



class PollingResult(models.Model):
    state = models.CharField(max_length=100, blank=True)
    opening_Poll = models.IntegerField(max_length=150, blank=True)
    Exit_Poll = models.IntegerField(max_length=200, blank=True)
    Result = models.IntegerField(max_length=200, blank=True)
    image = models.ImageField(upload_to='pollings', blank=True)
    content = models.TextField(blank=True)
    video = EmbedVideoField(blank=True)
    date = models.DateField(blank=True)

    def state_to_url(self):
        return self.state.replace(' ', '-')
    


class ElectionResult(models.Model):
    state = models.CharField(max_length=100, blank=True)
    date = models.DateField(blank=True)
    Ruling_Party = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='pollings', blank=True)
    content = models.TextField(blank=True)
    video = EmbedVideoField(blank=True)

    def state_to_url(self):
        return self.state.replace(' ', '-')
    



class ElectionResultDetails(models.Model):
    Constituency_Name = models.CharField(max_length=200, blank=True)
    Candidate_Name = models.CharField(max_length=200, blank=True)
    Party = models.CharField(max_length=200, blank=True)
    Level = models.CharField(max_length=200, blank=True)
    Votes = models.IntegerField(blank=True)
    Margin = models.IntegerField(blank=True)


class ElectionSeatsAndParty(models.Model):    
    seats = models.IntegerField(blank=True)
    partylogo = models.ImageField(upload_to='partylogo',blank=True)
    partyname = models.CharField(max_length=50, blank=True)



class UpcommingElectionResult(models.Model):
    state = models.CharField(max_length=100, blank=True)
    date = models.DateField(blank=True)
    Ruling_Party = models.CharField(max_length=200, blank=True)



class CabinetMember(models.Model):
    image = models.ImageField(upload_to='cabinet_member', blank=True)
    name = models.CharField(max_length=200, blank=True)
    desination = models.CharField(max_length=50, blank=True)