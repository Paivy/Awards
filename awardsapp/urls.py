from django.urls import path,include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
     path('',views.home, name="home"),
     path('new_project',views.new_project, name="new_project"),
     path('profile',views.profile,name='profile'),
     path('new_profile',views.new_profile,name = 'new_profile'),
     path('edit/profile',views.profile_edit,name = 'edit_profile'),
     path('search',views.search_project, name='search_results'),
     path('project/review/<project_id>',views.project_review,name='project_review'),
     path('api/profile/', views.ProfileList.as_view()),
     path('api/projects/', views.ProjectList.as_view()),
    #  '<int:project_id>/'
    path('logout/',views.log_out),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
