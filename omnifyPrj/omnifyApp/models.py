from django.db import models
CHOICE=(
    ('YOGA','Yoga'),
    ('ZUMBA','Zumba'),
    ('HIIT','Hiit')
)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Fitness(BaseModel):
    name= models.CharField(max_length=300, null=True)
    type= models.CharField(choices=CHOICE,max_length=200, null=True)
    date=models.DateTimeField(blank=True, null=True)
    instructor= models.CharField(max_length=300, null=True)
    slot= models.CharField(max_length=100, null=True)
    
class Book(BaseModel):
    fitness = models.ForeignKey(Fitness, on_delete=models.CASCADE,null=True,related_name='fitness')
    client_name= models.CharField(max_length=300, null=True)
    client_email= models.EmailField(max_length=200, null=True)