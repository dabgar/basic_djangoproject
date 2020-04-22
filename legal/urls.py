from django.conf.urls import url
from .import views
app_name='legal'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    #/legal/712
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    #/legal/questions/add
    url(r'questions/add/$',views.QuestionCreate.as_view(),name='Question_add'),
    #/legal/questions/2/delete
    #url(r'questions/delete/$',views.QuestionDelete.as_view(),name='Question_delete')
    
    ]