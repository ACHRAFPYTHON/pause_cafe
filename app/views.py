from datetime import datetime
from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import render
from matplotlib.pyplot import step
from .models import boissonschaudes, boissonsfraiches, carte, crepes, glaces, jus, lignecommande, serveur,comande
import time
import json
def demo(request):
    context={
        'serveur':serveur.objects.all()
    }

    print("demarer")
    return render(request,'pages/index.html',context)

def user_login(request):
    print("login h")
    login=serveur.objects.all()
    if request.method=="POST":
        username=request.POST.get("email")
        password=request.POST.get("pass")
        for i in login:
            if username==i.email and password==i.password:
                print(i.matricule)
                
                
               
                return render(request,'pages/{}.html'.format(i.name),{'hassan':serveur.objects.get(matricule=i.matricule)})
        else:
            return render(request,'pages/index.html')
                
                
def hassanmenu(request):
    print("hhhh")
    
    
    print("jjj")
    return render(request,'pages/hassanmenu.html',{'boissonchaudes':boissonschaudes.objects.all(),'boissonsfraiches':boissonsfraiches.objects.all(),'crepe':crepes.objects.all(),'carte':carte.objects.all(),'jus':jus.objects.all(),'glaces':glaces.objects.all()})

def commande(request):
      
      fname=request.POST.getlist('fname')
      quantite=request.POST.getlist('quantite')
      remarque=request.POST.getlist('rema')

      print("______________________________________________________________________________________________________________________")
      print(fname)
      print(quantite)
      print(remarque)
      
      print("______________________________________________________________________________________________________________________")
      t=[]
      bc=boissonschaudes.objects.all()
      bf=boissonsfraiches.objects.all()
      
     
      
      

      
      
      
      for l in range(len(fname)):
          for i in bc:
              if i.name==fname[l]:
                  prix1=int(i.prix)
          for i in bf:
              if i.name==fname[l]:
                  prix1=int(i.prix)
          e=int(quantite[l])
          print(e)
          print(type(e))
          k=lignecommande()
          k.produits=fname[l]
          k.price=prix1*e
          k.quantite=quantite[l]
          k.remarque=remarque[l]
          k.save()
      m=comande()
      text="["
      prix2=0
      lg=lignecommande.objects.all()
      for i in range(len(lg)):
          text+="produit : {} ( {} quantite: {} )".format(i+1,str(lg[i].produits),str(lg[i].quantite))
          prix2+=int(lg[i].price)
      text+="]"
      

      x = datetime.now()   
      m.time=datetime.time(x)
      m.date=datetime.date(x)
      m.listitem=text
      m.price=prix2
      m.save()
      
                  
      response = {
        '': ''
         }
     
      return JsonResponse(response)



def listh(request):
    print(datetime.date(datetime.now()))
    
    a=comande.objects.values()
    
    list_result = [entry for entry in a]
    a=str(list_result[-1]["time"])
    
    return render(request,'pages/listh.html',{'commandes':list_result,'sin':a})