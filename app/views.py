from django.shortcuts import render
from .models import *
from django.db import transaction
import random
from django.http import HttpResponse

def home(request):
    """
        home
    """
    return render(request, 'home/home.html')

def participation(request):
    """
        participation
    """
    context = {}
    visitor_count = Visitor.objects.count()
    # context['visitor_count'] = visitor_count
    context['visitor_count'] = request.visitor_count
    if 'voeux' in request.POST:
        prenom = request.POST.get('prenom').upper()
        nom = request.POST.get('nom').upper()
        souhait = request.POST.get('souhait').upper()
        MessagSuccess =""
        MessagError= ""

        user = R_user.objects.filter(r_user_prenom=prenom, r_user_nom=nom).first()
        if not user : 
            with transaction.atomic():
                record_user = R_user(   
                    r_user_nom = nom,
                    r_user_prenom =prenom,
                    r_user_voeux = souhait,
                )
                record_user.save()

                record_user_secret = R_user_secret(   
                    r_user_secret_nom = nom,
                    r_user_secret_prenom =prenom,
                )
                record_user_secret.save()

                MessagSuccess =  " Un immense merci " + prenom  +" pour avoir partagé ton précieux vœu avec nous."

        else:
            MessagError = "l'utilisateur existe déja"

        context = {'MessagError': MessagError, 'MessagSuccess': MessagSuccess }

    return render(request, 'home/participation.html', context)


def secrets(request):
    Data_R_user = R_user.objects.all()
    context = {'Data_R_user': Data_R_user}
    available_names=[]

    if 'decouvrir' in request.POST:
        prenom = request.POST.get('prenom').upper()
        nom = request.POST.get('nom').upper()

        user = R_user.objects.filter(r_user_prenom=prenom, r_user_nom=nom, r_user_jouer=False).first()
        print(user)
        if user:
            users_secrets = R_user_secret.objects.all()

            for us in users_secrets:
                if us.r_user_secret_prenom != prenom and us.r_user_secret_nom != nom and us.r_user_secret_choisie == False : 
                    name = us.r_user_secret_nom +"_"+ us.r_user_secret_prenom
                    available_names.append(name)

            print(available_names)

            if available_names:
                nom_choisi = random.choice(available_names)
                chosen_last_name, chosen_first_name = nom_choisi.split('_')
                user.r_user_jouer = True
                print(user.r_user_jouer)
                user.save()

                users_secret = R_user_secret.objects.filter(r_user_secret_prenom=chosen_first_name, r_user_secret_nom=chosen_last_name).first()
                user_voeu = R_user.objects.filter(r_user_prenom=chosen_first_name, r_user_nom=chosen_last_name).first()

                users_secret.r_user_secret_choisie = True
                users_secret.save()

                with transaction.atomic():
                    record_Tj_user_preson_secret = Tj_user_preson_secret(
                        r_user_id=user,
                        r_user_secret_id=users_secret,
                    )
                    record_Tj_user_preson_secret.save()

                context['nom_choisi'] = f"{users_secret.r_user_secret_nom} {users_secret.r_user_secret_prenom}"
                context['Voeu'] = user_voeu.r_user_voeux

                return render(request, 'home/secret_person.html', context)
            else:
                context['MessagError'] = "Aucun utilisateur secret disponible."
        else:
            print('error')
            context['MessagError'] = "L'utilisateur n'existe pas ou a déjà joué."

    return render(request, 'home/secrets.html', context)






    # Data_R_user = R_user.objects.all()
    # context = { 'Data_R_user':Data_R_user}

    # if 'decouvrir' in request.POST:
    #     liste_name= []
    #     prenom = request.POST.get('prenom').upper()
    #     nom = request.POST.get('nom').upper()

    #     user = R_user.objects.filter(r_user_prenom=prenom, r_user_nom=nom).first()
    #     print(user)
        
    #     if user and user.r_user_jouer == False : 
            
    #         user.r_user_jouer == True
    #         user.save() 
    #         users_secrets = R_user_secret.objects.exclude(r_user_secret_prenom=prenom, r_user_secret_nom=nom)

    #         for user_s in users_secrets :
    #             if user_s.r_user_secret_choisie == False:
    #                 name = user_s.r_user_secret_nom +"_"+ user_s.r_user_secret_prenom
    #                 liste_name.append(name)
    #         print(liste_name)
    #         nom_choisi = random.choice(liste_name)
    #         chaine = nom_choisi.split('_')
    #         users_secret = R_user_secret.objects.filter(r_user_secret_prenom=chaine[1], r_user_secret_nom=chaine[0]).first()
    #         user_voeu = R_user.objects.filter(r_user_prenom=chaine[1], r_user_nom=chaine[0]).first()

    #         users_secret.r_user_secret_choisie == True

    #         with transaction.atomic():
    #             record_Tj_user_preson_secret = Tj_user_preson_secret(   
    #                 r_user_id = user,
    #                 r_user_secret_id = users_secret,
    #             )
    #             record_Tj_user_preson_secret.save()

    #         context['nom_choisi'] = user_voeu.r_user_nom + " " + user_voeu.r_user_prenom
    #         context['Voeu'] = user_voeu.r_user_voeux

    #         return render(request, 'home/secret_person.html', context)

    #     else: 
    #         print('error')
    #         context['MessagError'] = "L'utilisateur n'existe déja"

        

    # return render(request, 'home/secrets.html', context)
