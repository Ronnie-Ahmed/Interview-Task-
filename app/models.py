from django.db import models
from django.utils import timezone

# Create your models here.

class UserDetails(models.Model):
    username=models.CharField(max_length=20,null=False,blank=False)
    userpic=models.ImageField(upload_to='photos')
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table='UserDetails'
        verbose_name='User Details'
        verbose_name_plural='User Details'
        
    

class TaskDetails(models.Model):
    Phases={
        ('Backlog','Backlog'),
        ('ToDo','ToDo'),
        ('Doing','Doing'),
        ('Completion','Completion')
        
        
    }
    user=models.ForeignKey(UserDetails,on_delete=models.CASCADE)
    taskname=models.CharField(max_length=10000,null=False,blank=False)
    phases=models.CharField(max_length=15,choices=Phases)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    def changeDate(self):
        if self.phases=='Completion' and self.completed_at is None:
            self.completed_at= timezone.now()  + timezone.timedelta(hours=6)
        else:
            pass
        
    def save(self, *args, **kwargs):
        self.changeDate()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.taskname
    
    class Meta:
        db_table='Task Details'
        verbose_name = 'Task Details'
        verbose_name_plural = 'Task Details'