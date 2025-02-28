from django.urls import path # type: ignore
from .views import item_edit_confirm, item_list, item_create, item_update, item_delete  # ビューをインポート

urlpatterns = [
    path('', item_list, name='item_list'),  # 商品一覧
    path('add/', item_create, name='item_create'),  # 商品追加
    path('<int:pk>/edit/', item_update, name='item_update'),  # 商品編集
    path('<int:pk>/delete/', item_delete, name='item_delete'),  # 商品削除
    path('<int:pk>/edit-confirm/', item_edit_confirm, name='item_edit_confirm'),

]
