from django.db import models


# Create your models here.
class Contact(models.Model):

    user_name = models.CharField(max_length=40)
    user_email = models.EmailField(max_length=40)
    user_message = models.CharField(max_length=200)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user_name
