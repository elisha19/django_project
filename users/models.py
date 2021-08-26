from django.db import models
from django.contrib.auth.models import User

# cascade is to delete data of 'x' when 'y' is deleted

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    # to specify how the data needs to be displayed
    def __str__(self):
        return f'{self.user.username} Profile'