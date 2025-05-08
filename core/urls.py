from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('', home_view),
    path('talabalar/', talabalar_view),
    path('talabalar/<int:talaba_id>/', talaba_view),
    path('kitoblar/', kitoblar_view),

    path('kitobli-talabalar/', kitobli_talabalar_view),
]
