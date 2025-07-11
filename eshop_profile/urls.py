from django.urls import path
from eshop_profile.views import profile_main_page, profile_user_order, profile_setting

app_name = 'eshop_profile'
urlpatterns = [
    path('profile', profile_main_page),
    path('profile/orders', profile_user_order, name='orders'),
    path('profile/setting', profile_setting, name='setting')
]