
from django.contrib import admin
from django.urls import path, include
from mpesa.urls import mpesa_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('APP.urls')),
    path('mpesa/', include(mpesa_urls)),

]
