from django.db import models

class Tasks(models.Model):

    username = models.CharField(max_length=20)
    task  = models.CharField(max_length=200)
    description = models.CharField(max_length=1000,blank=True,null=True)
    status = models.CharField(max_length=20,default="Pending")
    file = models.FileField(upload_to="taskfiles/",max_length=150,null=True,default=None)

    def __str__(self):
        return f'{self.task}'