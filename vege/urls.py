from django.urls import path
from . import views
urlpatterns = [
    path('', views.recipes, name='recipes' ),
    path('delete/<id>/', views.delete, name='delete' ),
    path('update/<id>', views.update, name='udpate')

]
