from django.urls import path, include

from travelapp import views

urlpatterns = [
    path('',views.fun,name='fun'),

    # path('add',views.addition,name='add')
]
# urlpatterns = [
# path('funn/',views.funn,name='funn'),
#     ]