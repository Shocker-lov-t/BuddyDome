from django.contrib import admin

from .models import Course
from .models import Requestcourse
from .models import Blog
from .models import guide
from .models import event

admin.site.register(event)
admin.site.register(guide)
admin.site.register(Course)
admin.site.register(Blog)
admin.site.register(Requestcourse)

# Register your models here.
