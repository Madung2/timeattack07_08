
from django.contrib import admin
from django.urls import path, include
from user import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('user/', include('user.urls')),

    path('post/', include('post.urls')),

    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/authonly/', views.OnlyAuthenticatedUserView.as_view()),

]
