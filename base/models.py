from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    '''Task model for each task on the todo list
    :param user:<int>pk of remote model for Many to one relation to User model, set to cascade delete 
        tasks when user is deleted.
    :param title:<str> title of task  
    :param complete:<Bool> If task completed or not, default=False
    :param create:<DateTime> datetime of task creation, autofill=True
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, 
                             null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) 
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta: 
        '''To order model by task completion status
        '''
        ordering = ['complete']
    