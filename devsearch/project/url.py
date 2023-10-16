from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.registerUser,name="register"),
    path('',views.viewproject,name="home"),
    path('add_project/',views.addproject,name="add-project"),
    path('view_project/<str:pk>',views.viewSingleProject,name="view-project"),
    path('edit_project/<str:pk>',views.editProject,name="edit-project"),
    path('delete_project/<str:pk>',views.deleteProject,name="delete-project")
    
]