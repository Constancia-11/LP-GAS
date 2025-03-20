from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Route to your main application (Modify if needed)
    path('', include('gas_requests.urls')),  

    path('api/', include('users.urls')), 
]
