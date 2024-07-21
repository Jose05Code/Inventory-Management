from django.urls import path
from .views import ItemView

urlpatterns = [
    path('items/', ItemView.as_view(), name='items-list-create'),
    path('items/<int:item_id>/', ItemView.as_view(), name='items-detail-update'),
]