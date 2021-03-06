from django.contrib import admin
from django.urls import path, include
from hospital import views as HospView
from django.contrib.auth import views
from django.contrib.staticfiles.urls import static
from .import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	path('', HospView.homePage, name='homePage'),
	path('patient/add', HospView.addPatient, name='add_patient'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)