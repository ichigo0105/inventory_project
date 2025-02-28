from django.shortcuts import render, redirect, get_object_or_404 # type: ignore
from .models import Item
from .forms import ItemForm

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # 商品一覧ページへリダイレクト
    else:
        form = ItemForm()
    return render(request, 'stock/item_form.html', {'form': form})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'stock/item_confirm_delete.html', {'item': item})

def item_list(request):
    items = Item.objects.all()  # データベースから全てのアイテムを取得
    return render(request, "stock/item_list.html", {'items': items})  # アイテムをテンプレートに渡す

def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'stock/item_form.html', {'form': form})

def item_edit_confirm(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        return redirect('item_update', pk=pk)  # 確認後に編集ページへ移動

    return render(request, 'stock/item_edit_confirm.html', {'item': item})