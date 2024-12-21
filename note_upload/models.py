# models.py
from django.db import models
from django.contrib.auth.models import User  # Import the default User model

class Note(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    file = models.FileField(upload_to='notes/')
    upload_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes'
    )
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-upload_date']
