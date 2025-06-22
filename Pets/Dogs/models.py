from django.db import models

# Create your models here.

class Lifespan(models.Model):
    id = models.IntegerField(primary_key=True)
    lifespan = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} {self.lifespan}"

class Temperament(models.Model):
    id = models.IntegerField(primary_key=True)
    temperament = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id} {self.temperament}"

class Trainability(models.Model):
    id = models.IntegerField(primary_key=True)
    trainability = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id} {self.trainability}"

class Size(models.Model):
    id = models.IntegerField(primary_key=True)
    size = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id} {self.size}"

class Hair(models.Model):
    id = models.IntegerField(primary_key=True)
    hair = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} {self.hair}"

class Color(models.Model):
    id = models.IntegerField(primary_key=True)
    color = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} {self.color}"


class Dog(models.Model):
    id = models.IntegerField(primary_key=True)
    breed = models.CharField(max_length=200) 
    lifespan = models.ForeignKey(Lifespan,on_delete=models.CASCADE)
    temperament = models.ForeignKey(Temperament,on_delete=models.CASCADE)
    trainability = models.ForeignKey(Trainability,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    hair = models.ForeignKey(Hair,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} {self.breed} {self.lifespan} {self.temperament} {self.trainability} {self.hair} {self.size} {self.color}"