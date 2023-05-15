"""jid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.http import HttpResponse 
from django.conf import settings
from sesame.views import LoginView
from django.conf.urls.static import static
from django.urls import path 
from jid.views import homepage,about,projets ,BEX,events,test,teambuilding,\
    visites,events2,formations,Nos_formations,Nos_visites,Nos_activités,\
        JID_activités,Adhesion ,affiche_project,add_project  ,affiche_formation ,\
            add_formation ,add_teambuilding ,affiche_teambuilding , add_institue , affiche_institue ,\
                add_event ,affiche_event , jidadmin,secret
                


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('about/', about),
    path('Nos_projets/', affiche_project),
    path('Notre_équipe/', BEX),
    path('Nos_événements/', affiche_event),
    path('test/', test),
    path('teambuilding/', teambuilding),
    path('visites/', visites),
    path('formations/', formations),
    path('Nos_événements//events_page_2/', events2),
    path('JID_activités/Nos_formations/', affiche_formation),
    path('JID_activités/Nos_activités/', affiche_teambuilding),
    path('JID_activités/Nos_visites/', affiche_institue),
    path('JID_activités/',JID_activités),
    path('Adhesion/', Adhesion),
    path('jidadmin/add_project/',add_project ),
    path('jidadmin/',jidadmin ),
    path('jidadmin/add_formation/',add_formation ),
    path('jidadmin/add_teambuilding/',add_teambuilding ),
    path('jidadmin/add_institue/',add_institue ),
    path('jidadmin/add_event/',add_event ),

    path('jidadmin/',jidadmin , name ="jidadmin" ),
    path('secret/',secret , name ="secret" ),


 path("sesame/login/", LoginView.as_view(), name="sesame-login"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
