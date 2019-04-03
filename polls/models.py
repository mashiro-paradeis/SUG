from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class Ubicacion(models.Model):
 nombre =  models.CharField(max_length=200)
 lat = models.CharField(max_length=50)
 lng = models.CharField(max_length=50)
 fecha = models.DateTimeField(auto_now_add=True)
 user = models.ForeignKey(User, on_delete=models.PROTECT)
	 
def __unicode__(self): return self.nombre
	
class UbicacionForm(ModelForm): 
  class Meta: 
      model = Ubicacion
      fields = '__all__'  
	  
   
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self): return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
		
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self): 
	    return self.choice_text
    


	
	
	
	
	