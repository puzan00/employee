from django.urls import path
from emp_app import views
urlpatterns = [
    path('', views.home,name='home'),
    path('view-all/',views.view_all,name='view-all'),
    path('add/',views.add,name='add'),
    path('edit/<int:id>',views.edit,name='edit'),
  
]
