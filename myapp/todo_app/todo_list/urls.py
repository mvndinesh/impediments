from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('',views.home,name = 'home'),
    # path('alldefects/',views.alldefects,name ='alldefects'),
    path('about/',views.about,name = 'about'),
    path('delete/<list_id>',views.delete,name = 'delete'),
    path('cross_off/<list_id>',views.cross_off,name = 'cross_off'),
    path('uncross/<list_id>',views.uncross,name = 'uncross'),
    path('edit/<list_id>',views.edit,name = 'edit'),
    path('alldefects/',views.alldefects,name='alldefects'),
    path('enterdefect/',views.enterdefect,name = 'enterdefect'),
    path('editdefect/<list_id>',views.editdefect,name='editdefect'),
    path('selection/',views.selection,name='selection'),
    path('',views.login,name='login'),
    path('sendmail/',views.sendmail,name='sendmail'),
    path('sendmaillid/<list_id>',views.sendmaillid,name='sendmaillid'),
    path('logout/',views.logout_view,name='logout'),
    # path('loggedout/',views.loggedout,name='loggedout'),
    
]
