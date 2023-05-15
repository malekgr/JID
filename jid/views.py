from django.shortcuts import render , redirect
from jid.models import Projets , Formations ,TeamBuilding , Institue , Event
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.urls import reverse 
import sesame.utils 
from jid.forms import EmailLoginForm 


# def jidadmin(request) :
#     return render(request , 'jidadmin.html')


def  secret(request) :
    if request.method == 'POST' :
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email = email).first()

            if user is None :
                # form.add_error('email','Not found')
                return render(request ,'secret.html',{'form' : form})
            link = request.build_absolute_uri(reverse('sesame-login'))
            print(link)

            link += sesame.utils.get_query_string(user)
    
            user.email_user(
                subject="Your Magic login link",
                message =f"""Dear {user.username} - login with this link {link}"""
            )
    
    
    context ={'form' : EmailLoginForm()}
    return render(request , 'secret.html',context)


@login_required
def jidadmin(request) :
    context ={}
    return render(request ,'jidadmin.html',context)


def affiche_project(request):
    items = Projets.objects.all()
    return render(request ,'projets.html',context = {'cle': items })


def affiche_formation(request):
    items = Formations.objects.all()
    return render(request ,'nos_formations.html',context = {'cle': items })

def affiche_teambuilding(request):
    items = TeamBuilding.objects.all()
    return render(request ,'nos_activites.html',context = {'cle': items })


def affiche_institue(request):
    items = Institue.objects.all()
    return render(request ,'nos_institues.html',context = {'cle': items })

def affiche_event(request):
    items = Event.objects.all()
    return render(request ,'events.html',context = {'cle': items })

def affiche_event2(request):
    items = Event.objects.all()
    return render(request ,'index.html',context = {'cle': items })



# Create your views here.
@login_required
@csrf_protect
def add_project(request) :
    if request.method == 'POST' :
        print(request.POST)
        projectname = request.POST["Projectname"]
        description = request.POST["Description"]
        photo =  request.POST["Photo"]
        Projets.objects.create(Nameproject = projectname ,Description = description , Photo = photo )
        return redirect("/Nos_projets/")
    return render (request,'add_project.html')

@login_required
@csrf_protect
def add_formation(request) :
    if request.method == 'POST' :
        print(request.POST)
        formationname = request.POST["f_name"]
        f_date = request.POST["f_date"]
        f_photo =  request.POST["f_photo"]
        f_description = request.POST["f_description"]
        Formations.objects.create(NameFormation = formationname ,F_Date = f_date , F_photo = f_photo  , F_Description = f_description)
        return redirect('/JID_activités/Nos_formations/')
    return render (request,'add_formation.html')


@login_required
@csrf_protect
def add_teambuilding(request) :
    if request.method == 'POST' :
        print(request.POST)
        t_name = request.POST["t_name"]
        t_date = request.POST["t_date"]
        t_photo =  request.POST["t_photo"]
        t_description = request.POST["t_description"]
        TeamBuilding.objects.create(T_Name = t_name ,T_Date = t_date , T_photo = t_photo  , T_Description = t_description)
        return redirect('/JID_activités/Nos_activites/')
    return render (request,'add_teambuilding.html')


@login_required
@csrf_protect
def add_institue(request) :
    if request.method == 'POST' :
        print(request.POST)
        i_name = request.POST["i_name"]
        i_date = request.POST["i_date"]
        i_photo =  request.POST["i_photo"]
        i_description = request.POST["i_description"]
        Institue.objects.create(I_Name = i_name ,I_Date = i_date , I_photo = i_photo  , I_Description = i_description)
        return redirect('/JID_activités/Nos_visites/')
    return render (request,'add_institue.html')


@login_required
@csrf_protect
def add_event(request) :
    if request.method == 'POST' :
        print(request.POST)
        e_name = request.POST["e_name"]
        e_date = request.POST["e_date"]
        e_day = request.POST["e_day"]
        e_month = request.POST["e_month"]
        e_year= request.POST["e_year"]
        e_photo =  request.POST["e_photo"]
        e_description = request.POST["e_description"]
        Event.objects.create(E_Name = e_name ,E_Date = e_date ,E_Day = e_day ,E_Month= e_month ,E_Year = e_year , E_photo = e_photo  , E_Description = e_description)
        return redirect('/Nos_événements/')
    return render (request,'add_event.html')





def homepage(request):
    items = Event.objects.all()
    return render(request ,'index.html',context = {'cle': items })



def about(request):
    return render(request,'index.html')

def projets(request):

    return render(request,'projets.html')
def BEX(request):

    return render(request,'BEX.html')
def events(request):

    return render(request,'events.html')
def test(request):

    return render(request,'test.html')

def visites(request):

    return render(request,'visites.html')
def teambuilding(request):

    return render(request,'team_building.html')
def events2(request):

    return render(request,'events2.html')
def JID_activités(request):

    return render(request,'JID_activités.html')
def formations(request):

    return render(request,'formations.html')
def Nos_formations(request):

    return render(request,'nos_formations.html')
def Nos_visites(request):

    return render(request,'nos_visites.html')
def Nos_activités(request):

    return render(request,'nos_activites.html')
def Adhesion(request):

    return render(request,'adhesion.html') #GET
    
# def add_project(request):
#     return render(request,'add_project.html')


#HTTP Requests
#POST
#UPDATE