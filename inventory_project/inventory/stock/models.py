from django.db import models # type: ignore

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)  # 商品名
    description = models.TextField(blank=True, null=True)  # 説明
    quantity = models.PositiveIntegerField()  # 在庫数
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 価格
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # カテゴリ
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)  # 画像
    added_at = models.DateTimeField(auto_now_add=True)  # 登録日時

    def __str__(self):
        return self.name
