from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # rest-auth
    path('rest-auth/', include('rest_auth.urls')),    # 로그인, 로그아웃
    path('rest-auth/registration/', include('rest_auth.registration.urls')),    # 회원가입
    # my app
    path('', include('investment.urls'))
]
