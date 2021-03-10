from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('test/', testview.as_view(), name='test'),
    path('activate/<uid>/<token>/', acc_active_email.as_view(), name='activate')
]
