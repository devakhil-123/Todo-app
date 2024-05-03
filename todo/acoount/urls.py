from django.urls import path
from .views import *


urlpatterns=[
    path('add',WorkView.as_view(),name='add'),
    path('list',TodolistView.as_view(),name="list"),
    path('tdelt/<int:id>',TododeleteView.as_view(),name='tdelt'),
    path('tedit/<int:id>',TodoeditView.as_view(),name='tedit')
]