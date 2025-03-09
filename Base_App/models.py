from django.db import models

# Create your models here.

class Glina(models.Model):
    kolicina = models.IntegerField(default=0)

    def __str__(self):
        return f"Glina: {self.kolicina} kg"
    
class Grumen(models.Model):
    kolicina_g = models.IntegerField(default=0)

    def __str__(self):
        return f"Grumen zemlje: {self.kolicina_g} kg"
    
class NeoblikovanCrep(models.Model):
    brojN = models.IntegerField(default=0)

    def __str__(self):
        return f"Broj neoblikovanih crepa: {self.brojN}"
    
class OblikovanCrep(models.Model):
    brojO = models.IntegerField(default=0)

    def __str__(self):
        return f"Broj oblikovanih crepa: {self.brojO}"
    
class VagonSusenje(models.Model):
    brojVS = models.IntegerField(default=0)

    def __str__(self):
        return f"Broj vagona za susenje: {self.brojVS}"
    
class OsusenCrep(models.Model):
    brojOS = models.IntegerField(default=0)

    def __str__(self):
        return f"Broj osusenih crepa: {self.brojOS}"
    
class VagonPecenje(models.Model):
    brojVP = models.IntegerField(default=0)

    def __str__(self):
        return f"Broj vagona za pecenje: {self.brojVP}"
    
    
class IspecenCrep(models.Model):
    brojIC = models.IntegerField(default=0)

    def __str__(self):
        return f"Broj ispecenih crepa: {self.brojIC}"
    
class PaketCrepa(models.Model):
    brojPC = models.IntegerField(default=0)

    def __str__(self):
        return f"Broj paketa crepa: {self.brojPC}"