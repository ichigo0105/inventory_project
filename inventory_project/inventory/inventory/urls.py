from django.contrib import admin # type: ignore
from django.urls import path, include  # type: ignore # include を追加
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stock/', include('stock.urls')),  # stock のURLを登録
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)