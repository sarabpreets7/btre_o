from django.urls import path,include
from . import views
app_name='listings'

urlpatterns = [

    path('',views.index,name='listings'),
    path('search/',views.search,name='search'),
    path('<int:listing_id>',views.listing,name='listing'),
]