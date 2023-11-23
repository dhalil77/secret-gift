from django.db import models

# Create your models here.
class R_user(models.Model):
    """
        Create a user table
    """
    r_user_id = models.AutoField(primary_key=True, auto_created = True)         
    r_user_nom = models.CharField(max_length=255)  
    r_user_prenom = models.CharField(max_length=255) 
    r_user_voeux = models.CharField(max_length=500)
    r_user_jouer = models.BooleanField(default=False) 
    r_user_created_at = models.DateTimeField(auto_now_add=True) 
    r_user_updated_at  = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.r_user_nom


class R_user_secret(models.Model):
    """
        Create a secret
    """
    r_user_secret_id = models.AutoField(primary_key=True, auto_created = True)         
    r_user_secret_nom = models.CharField(max_length=255)  
    r_user_secret_prenom = models.CharField(max_length=255) 
    r_user_secret_choisie = models.BooleanField(default=False) 
    r_user_secret_created_at = models.DateTimeField(auto_now_add=True) 
    r_user_secret_updated_at  = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.r_user_secret_nom


class Tj_user_preson_secret(models.Model):
    """
        Jonction entre user and user secret
    """
    tj_user_preson_secret_id = models.AutoField(primary_key=True, auto_created = True)         
    r_user_id = models.ForeignKey(R_user, on_delete=models.CASCADE)
    r_user_secret_id = models.ForeignKey(R_user_secret, on_delete=models.CASCADE)
 
    

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)