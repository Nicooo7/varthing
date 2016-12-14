from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User




 

class Theme(models.Model):

    intitule = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.intitule


    
class Proposition(models.Model):

    ennonce = models.CharField(max_length=200, null=True)
    date_creation = models.DateField (default= timezone.now, null=True)
    categorie =  models.ForeignKey(Theme, null=True, blank = True)
    supporter = models.ManyToManyField(User, through= "Soutien", null =True)
    champ_lexical = models.CharField (max_length = 100000, default = "vide", null = True)

    def __str__(self):
        return self.ennonce

class Soutien(models.Model):

    CHOIX_LIEN= (
                ('CR' , 'createur'),
                ('SO', 'soutien')
    )
    propositions = models.ForeignKey(Proposition)
    user = models.ForeignKey(User, null=True)
    lien = models.CharField(max_length =2, choices= CHOIX_LIEN)

    def __str__(self):
        return "{0} soutenu par {1}".format(self.propositions, self.user)


class Lieu (models.Model):
    pays = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    
    def __str__(self):
        return self.ville

class Autre_utilisateur (models.Model):
    user = models.ForeignKey(User, null =True)

    def __str__(self):
        return "utilisateur {0} ".format (self.user)   


class Profile (models.Model):
    utilisateur = models.ForeignKey(User, null=True)
    lieu = models.ForeignKey (Lieu, null=True)
    theme_favoris = models.CharField(max_length = 200, null = True)
    utilisateurs_proches = models.ManyToManyField (Autre_utilisateur, through ="Proximite")

    def __str__(self):
        return "profile de {0}".format(self.utilisateur)



class Proximite(models.Model):
    profile = models.ForeignKey(Profile, null =True)
    Autre_utilisateur = models.ForeignKey (Autre_utilisateur)
    proba = models.DecimalField( max_digits=5, decimal_places=3)

    def __str__(self):
        return "proximite entre {0} et {1} ".format(self.profile , self.Autre_utilisateur)







