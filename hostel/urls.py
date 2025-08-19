from django.urls import path
from hostel.views import *
urlpatterns = [
    path('',base_view,name="base"),
    path('home/',home_view,name="home"),
    path('booking/',booking_view,name="booking"),
    path('login/',login_view,name="login"),
    path('register/',register_view,name="register"),
    path('shering/',shering_view,name="shering"),
    path('facilitys/',facilitys_view,name="facilitys"),
    path('schedules/',schedules_view,name="schedules"),
    path('contacts/',contact_view,name="contacts"),
    path('main/',main_view,name="main"),
    # Rooms Sherings Views path
    path('twoshering/',twoshering_view,name="twoshering"),
    path('threeshering/',threeshering_view,name="threeshering"),
    path('fourshering/',fourshering_view,name="fourshering"),
    path('fiveshering/',fiveshering_view,name="fiveshering"),
    path('sixshering/',sixshering_view,name="sixshering"),
]