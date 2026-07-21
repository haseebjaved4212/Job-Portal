from django.db import models
from django.conf import settings
# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)




    class Meta:
        ordering = ['-posted_date']


    def __str__(self):
         return self.title


class application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    applied_date = models.DateTimeField(auto_now_add=True)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField(blank=True)

    class Meta:
        ordering = ['-applied_date']

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"





    


    
