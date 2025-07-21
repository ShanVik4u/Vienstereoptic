from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    job_type = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    salary_range = models.CharField(max_length=100)
    job_description = models.TextField()
    responsibilities = models.TextField()
    qualifications = models.TextField()
    benefits = models.TextField()
    application_method = models.CharField(max_length=50)
    application_email = models.EmailField(blank=True, null=True)
    application_url = models.URLField(blank=True, null=True)
    deadline = models.DateField()
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
