from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),                     # Homepage with list of entries
    path("wiki/<str:title>", views.entry, name="entry"),     # Entry page for each encyclopedia entry
    path("search", views.search, name="search"),             # Search results page
]
