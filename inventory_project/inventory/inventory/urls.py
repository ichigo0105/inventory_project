from django.contrib import admin
from django.urls import path, include  # include を追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stock/', include('stock.urls')),  # stock のURLを登録
]
