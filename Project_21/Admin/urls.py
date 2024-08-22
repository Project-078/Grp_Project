from Admin import views
from django.urls import path

app_name='Admin'
urlpatterns = [
     path('',views.home,name='home'),
    path('<int:item_id>/',views.details,name='details'),
    path('add/',views.add_item,name='additem'),
    path('update/<int:id>/',views.update_item,name='update'),
    path('delete/<int:id>/',views.delete_item,name='delete'),
]

