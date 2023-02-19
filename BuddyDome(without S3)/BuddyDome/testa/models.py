
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
import os
from django.conf.urls.static import static
from django.utils import timezone



class guide(models.Model):
    Practical='Practical'
    RampUp='RampUp'
    type=[
        (Practical,'Practical'),
        (RampUp,'RampUp')
    ]
    nameb=models.CharField(max_length=150)
    type=models.CharField(max_length=15, choices=type,default=RampUp)
    Link=models.TextField(max_length=500, blank=False)
    description = models.TextField(max_length=500, blank=True)


    def __str__(self):
        return self.nameb


class Course(models.Model):
     n = models.CharField(max_length=250,verbose_name="Name",blank=True, null=True)
     contributor = 'yes'
     nocontri = 'no'
     existing_contributor = [
        (contributor , 'yes'),
        (nocontri , 'no')
    ]
     existing_contributor= models.CharField(max_length=15, choices= existing_contributor, default=contributor)
    
     e = models.EmailField(max_length=250, verbose_name="Email",blank=True, null=True)
     t=models.CharField(max_length=250,verbose_name="Course Title",blank=True, null=True)
     a=models.CharField(max_length=250,verbose_name="Field(e.g AWS, cloud)",blank=True, null=True)
     l=models.CharField(max_length=250,verbose_name="Level(e.g Level-1, Level-2)",blank=True, null=True)
     cr = models.TextField(max_length=250 ,verbose_name="Discription",blank=True, null=True)
     re=models.CharField(max_length=250 ,verbose_name="Reference links",blank=True, null=True)
     slug = models.SlugField(null=True, blank=True)
     resume = models.FileField(verbose_name="Resume", blank=True, null=True)
     
     

     class Meta:
        ordering = ['cr']

     def __str__(self):
        return self.n

     def save(self, *args, **kwargs):
        self.slug = slugify(self.n)
        super().save(*args, **kwargs)

     def get_absolute_url(self):
        return reverse('testa:createcourse')
   
      



class Requestcourse(models.Model):
     name = models.CharField(max_length=250,blank=True, null=True)
     
     email = models.EmailField(max_length=250)
     title=models.CharField(max_length=250,verbose_name="Course Title",blank=True, null=True)
     area=models.CharField(max_length=250,verbose_name="Field(e.g AWS, cloud)",blank=True, null=True)
     level=models.CharField(max_length=250,verbose_name="Level(e.g Level-1, Level-2)",blank=True, null=True)
     create = models.TextField(max_length=250 ,verbose_name="Discription",blank=True, null=True)
     reference=models.CharField(max_length=250 ,verbose_name="Reference links",blank=True, null=True)
     impact=models.TextField(max_length=250 ,verbose_name="What would be the impact of this course?",blank=True, null=True)
     slug = models.SlugField(null=True, blank=True)
     

     

     class Meta:
        ordering = ['create']

     def __str__(self):
        return self.name

     def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

     def get_absolute_url(self):
        return reverse('testa:requestcourse')
   
   

      
class Blog(models.Model):
     nam = models.CharField(max_length=250,verbose_name="Name",blank=True, null=True)
     contributor = 'contributor'
     student='student'
     employee='employee'
     designation = [
        (contributor , 'contributor'),
        (student,'student'),
        (employee,'employee'), 
    ]
     designation= models.CharField(max_length=15, choices= designation, default=contributor)   
     ema = models.EmailField(max_length=250, verbose_name="Email",blank=True, null=True)
     tit=models.CharField(max_length=250,verbose_name="Blog Title",blank=True, null=True)
     af=models.CharField(max_length=250,verbose_name="Field",blank=True, null=True)
     
     crp = models.TextField(max_length=250 ,verbose_name="Discription",blank=True, null=True)
     rel=models.CharField(max_length=250 ,verbose_name="Bloglink",blank=True, null=True)
     slug = models.SlugField(null=True, blank=True)
     class Meta:
        ordering = ['crp']
     def __str__(self):
        return self.tit
     def save(self, *args, **kwargs):
        self.slug = slugify(self.nam)
        super().save(*args, **kwargs)
     def get_absolute_url(self):
        return reverse('testa:createblog')
   
class event(models.Model):
    name=models.CharField(max_length=150)
    Link=models.TextField(max_length=500, blank=False)
    description = models.TextField(max_length=500, blank=True)
    im=models.ImageField(upload_to="Images/Events/",default='eventp.png')
    def __str__(self):
        return self.name

      