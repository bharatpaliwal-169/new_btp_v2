from django.db import models

#database
class Main(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  mobile = models.CharField(max_length=10,unique=True)
  
  def __str__(self):
    return self.name

class Contact(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  comment = models.TextField(max_length=500)

  def __str__(self):
    return self.name