from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
# Model collect medical report from users
class MailList(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True, null=True)

    def __str__(self):
        return self.email











# class MedicalCondition(models.Model):
#     doctor_id = models.ForeignKey(
#         User, on_delete=models.CASCADE)
#     medical_condition = models.CharField(max_length=150, blank=True)
#     date_added = models.DateTimeField(default=datetime.now, blank=True)
#     date_updated = models.DateTimeField(default=datetime.now, blank=True)
