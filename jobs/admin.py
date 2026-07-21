from django.contrib import admin
from .models import Job, Application

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'salary', 'posted_date', 'posted_by')
    list_filter = ('location',)
    search_fields = ('title', 'company', 'description')
    ordering = ('-posted_date',)

    
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'applicant', 'applied_date')
    list_filter = ('job__location', 'applied_date')
    search_fields = ('job__title', 'applicant__username')
    ordering = ('-applied_date',)


admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)

 


 