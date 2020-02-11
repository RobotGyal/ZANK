from django.urls import path
from .views import (
    home,
    CodeList,
    CodeDetail,
    CodeCreate,
    CodeUpdate,
    CodeDelete,
)

app_name = 'codes'

urlpatterns = [
    path('', home, name='home_page'),
    # view for the results/reference page (the list view)
    path('codes/', CodeList.as_view(), name='reference'),
    path('codes/add-code/', CodeCreate.as_view(), name='add_code'),
    path('codes/<slug:slug>/edit/', CodeUpdate.as_view(), name='edit_code'),
    path('codes/<slug:slug>/delete/', CodeDelete.as_view(),
         name='remove_code'),
    path('codes/<slug:slug>/', CodeDetail.as_view(), name='details'),
]
