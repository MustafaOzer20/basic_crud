from django.urls import path
from .views import apiOverView, dataCreate, dataDelete, dataList, dataUpdate


urlpatterns = [
    # books
    path('', apiOverView),
    path('data-list/', dataList),
    path('data-create/', dataCreate),
    path('data-update/<str:id>/', dataUpdate),
    path('data-delete/<str:id>/', dataDelete)
]