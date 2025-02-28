from django.contrib import admin # type: ignore
from .models import Item, Category

admin.site.register(Item)  # 管理画面に登録
admin.site.register(Category)  # 管理画面に登録
