from django.db import models

# Create your models here.
class UserInfo(models.Model):
    usercred = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.usercred
