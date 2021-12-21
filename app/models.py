from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=65,null=False)
    def __str__(self) -> str:
        return self.name

class RandomList(models.Model):
    name=models.CharField(max_length=65,null=False)
    description=models.TextField(null=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='random_list')
    def __str__(self)->str:
        return self.name