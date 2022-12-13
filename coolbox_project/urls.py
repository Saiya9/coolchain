"""coolbox_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from coolboxapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('driver_login',views.driver_login,name='driver_login'),
    path('driver_monitor_detail',views.driver_monitor_detail,name='driver_monitor_detail'),
    path("moni1", views.moni1, name="moni1"),
    path("driver_monitor", views.driver_monitor, name="driver_monitor"),
    path('driver_shipping/<str:pk>',views.driver_shipping,name='driver_shipping'),
    path('driver_tracking',views.driver_tracking,name='driver_tracking'),
    path('driver_track',views.driver_track,name='driver_track'),
    path("driver_shipping_confrim/<str:pk>",views.driver_shipping_confrim,name='driver_shipping_confrim'),
    

    path('',views.login_request,name='login'),
    path("homepage_monitor", views.homepage_monitor, name="homepage_monitor"),
    path("monitor", views.monitor_detail, name="monitor"),
    path("moni1", views.moni1, name="moni1"),
    path("logout",views.logout,name='logout'),

    
    path("tracking",views.tracking,name='tracking'), 
    path("track",views.track,name='track'),
    path("profile_setting",views.profile_setting,name='profile_setting'),
    path("user_detail",views.user_detail,name='user_detail'),


    path("add_user",views.add_user,name='add_user'),
    path("add_driver",views.add_driver,name='add_driver'),
    path("add_car",views.add_car,name='add_car'),
    path("add_type",views.add_type,name='add_type'),
    path("add_coolbox",views.add_coolbox,name='add_coolbox'),
    path("add_medicine",views.add_medicine,name='add_medicine'),
    path("add_ship",views.add_ship,name='add_ship'),


    path("table_create",views.table_create,name='table_create'), 
    path("table_car",views.table_car,name='table_car'), 
    path("table_type",views.table_type,name='table_type'), 
    path("table_driver",views.table_driver,name='table_driver'), 
    path("table_shipping",views.table_shipping,name='table_shipping'), 
    path("table_coolbox",views.table_coolbox,name='table_coolbox'), 
    path("table_medicine",views.table_medicine,name='table_medicine'), 


    path("view_user/<str:pk>",views.view_user,name='view_user'),
    path("view_car/<str:pk>",views.view_car,name='view_car'),
    path("view_coolbox/<str:pk>",views.view_coolbox,name='view_coolbox'),
    path("view_driver/<str:pk>",views.view_driver,name='view_driver'),
    path("view_medicine/<str:pk>",views.view_medicine,name='view_medicine'),
    path("view_shipping/<str:pk>",views.view_shipping,name='view_shipping'),
    path("view_type/<str:pk>",views.view_type,name='view_type'),


    path("edit_user/<str:pk>",views.edit_user,name='edit_user'),
    path("edit_driver/<str:pk>",views.edit_driver,name='edit_driver'),
    path("edit_car/<str:pk>",views.edit_car,name='edit_car'),
    path("edit_type/<str:pk>",views.edit_type,name='edit_type'),
    path("edit_medicine/<str:pk>",views.edit_medicine,name='edit_medicine'),
    path("edit_coolbox/<str:pk>",views.edit_coolbox,name='edit_coolbox'),
    path("edit_shipping/<str:pk>",views.edit_shipping,name='edit_shipping'),

    # path("delete_driver/<str:pk>",views.delete_driver,name='delete_driver'),
    path("delete_type/<str:pk>",views.delete_type,name='delete_type'),
    path("delete_driver/<str:pk>",views.delete_driver,name='delete_driver'),
    path("delete_car/<str:pk>",views.delete_car,name='delete_car'),
    path("delete_medicine/<str:pk>",views.delete_medicine,name='delete_medicine'),
    path("delete_coolbox/<str:pk>",views.delete_coolbox,name='delete_coolbox'),
    path("delete_shipping/<str:pk>",views.delete_shipping,name='delete_shipping'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
