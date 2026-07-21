from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Job, Application
from .forms import JobForm

@login_required
def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            return redirect('dashboard')
    else:
        form = JobForm()
    return render(request, 'jobs/create_job.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    if user.role == 'employer':
        jobs = Job.objects.filter(posted_by=user)
        return render(request, 'jobs/employer_dashboard.html', {'jobs': jobs})
    elif user.role == 'seeker':
        applications = Application.objects.filter(applicant=user)
        return render(request, 'jobs/seeker_dashboard.html', {'applications': applications})
    else:
        return HttpResponseForbidden()

@login_required
def apply_for_job(request, job_id):
    if request.user.role != 'seeker':
        return HttpResponseForbidden()
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        resume = request.FILES.get('resume')
        cover_letter = request.POST.get('cover_letter', '')
        if not resume:
            messages.error(request, "Resume is required.")
        else:
            Application.objects.create(job=job, applicant=request.user, resume=resume, cover_letter=cover_letter)
            messages.success(request, "Application submitted successfully!")
            return redirect('dashboard')
    return render(request, 'jobs/apply_job.html', {'job': job})
