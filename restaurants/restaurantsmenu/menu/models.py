from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Item(models.Model):
    section = models.ForeignKey(Section,on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.name



class Modifiers(models.Model):
    item = models.ManyToManyField(Item,related_name='modifiers')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.name


