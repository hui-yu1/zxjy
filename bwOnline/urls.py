from django.urls import path,include,re_path
from django.views.generic.base import TemplateView
from apps.users.views import LoginView,RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView
import xadmin
from organization.views import OrgView
from django.views.static import serve
from bwOnline.settings import MEDIA_ROOT

urlpatterns = [
    path('captcha/',include('captcha.urls')),
    path('xadmin/',xadmin.site.urls),
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'),
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path("org/", include('organization.urls', namespace="org")),
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
]
