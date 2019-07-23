from django.conf.urls import url
from django.contrib.auth import views as auth_views
from core import views as core_views
from core.views import Signup,Index,Show,Delete,Music,Dance,Birthday,SkinBurn,Ai,Index2,Formset
from django.urls import path

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^Signup/$', Signup.as_view(), name='Signup'),
    path('emp', Index.as_view()),

        path('Music', Music.as_view()),
        path('Dance', Dance.as_view()),
        path('Birthday', Birthday.as_view()),
        path('SkinBurn', SkinBurn.as_view()),
        path('show', Show.as_view()),
        path('Ai', Ai.as_view()),
        path('formset', Formset.as_view()),

    path('reg_form', Index2.as_view()),



    path('delete/<int:id>/', Delete.as_view(), name='show'),
]
