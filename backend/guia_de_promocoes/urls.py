from django.contrib import admin
from django.urls import path, include
from core.urls import router
from core.views import RegisterView, me, MeDetailsView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # rotas de autenticação
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path("api/auth/me/", me, name="me"),
    path("api/auth/me/details/", MeDetailsView.as_view(), name="me-details"),
]
