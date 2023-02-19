from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (CreateView)
from .forms import CourseForm,BlogForm
from .forms import RequestForm
from .models import Course,Blog,guide,event
from .models import Requestcourse
from django.urls import reverse_lazy
from django.views.generic import ( CreateView)
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

def com(request):
    return render(request,'testa.html')

class test1(TemplateView):
    template_name = 'quiz.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        guides = guide.objects.all()
        context['guides'] = guides
        return context

class Event(TemplateView):
    template_name = 'event.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = event.objects.all()
        context['events'] = events
        return context

class test2(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Blogs = Blog.objects.all()
        context['Blogs'] = Blogs
        return context

def test3(request):
    return render(request,"course.html")

class CourseCreateView(CreateView):
    # fields = ('existing_contributor','name','email','title', 'area', 'level' , 'create','reference'  ,'resume')
    form_class = CourseForm
    context_object_name = 'course'
    model= Course
    template_name = 'create_course.html'

    def getsuccessurl(self):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('testa:createcourse',kwargs={'standard':standard.slug,
                                                             'slug':self.object.slug})

    def formvalid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.Standard = self.object.standard
        fm.sub = self.object
        fm.save()
        return HttpResponseRedirect(self.getsuccessurl())

    def form2valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.user = self.request.user
        fm.Standard = self.object.standard
        fm.sub = self.object.sub
        fm.save()
        return HttpResponseRedirect(self.getsuccessurl())
                                                        


class RequestCourseView(CreateView):
    # fields = ('name','email','title', 'area', 'level' , 'create','reference','impact')
    form_class = RequestForm
    context_object_name = 'course'
    model=  Requestcourse
    template_name = 'request_course.html'

    def getsuccessurl(self):
        self.object = self.get_slug_field()
        standard = self.object.standard
        return reverse_lazy('testa:requestcourse',kwargs={'standard':standard.slug,
                                                             'slug':self.object.slug})


    def formvalid(self, form, *args, **kwargs):
        self.object = self.get_slug_field()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.Standard = self.object.standard
        fm.course = self.object
        fm.save()
        return HttpResponseRedirect(self.getsuccessurl())

    def form2valid(self, form, *args, **kwargs):
        self.object = self.get_slug_field()
        fm = form.save(commit=False)
        fm.user = self.request.user
        fm.Standard = self.object.standard
        fm.course = self.object.course
        fm.save()
        return HttpResponseRedirect(self.getsuccessurl())
                                                        
                                                        
                                                        
                                                        
class BlogCreateView(CreateView):
        # fields = ('existing_contributor','name','email','title', 'area', 'level' , 'create','reference'  ,'resume')
    form_class = BlogForm
    context_object_name = 'blog'
    model= Blog
    template_name = 'create_blog.html'

    def getsuccessurl(self):
        self.object = self.get_object()
        standard = self.object.standard
        return reverse_lazy('testa:createblog',kwargs={'standard':standard.slug,
                                                             'slug':self.object.slug})


    def formvalid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.Standard = self.object.standard
        fm.sub = self.object
        fm.save()
        return HttpResponseRedirect(self.getsuccessurl())

    def form2valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.user = self.request.user
        fm.Standard = self.object.standard
        fm.sub = self.object.sub
        fm.save()
        return HttpResponseRedirect(self.getsuccessurl())
                                                        
                                                   
                                                        