from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('userlogin/<int:id>',views.voting,name='userlogin'),
    path('managedb',views.dbl,name='managedb'),
    path('olddata/<int:userid>',views.olddata,name='olddata'),
    
    # path('demo',views.demo,name='demo'),
     path('upvotedata1/<int:userid>/<int:postid>',views.upvotedata1,name='upvotedata1'),
   
]
 