from django.urls import path

from bookmark import views
from bookmark.views import BookmarkLV

app_name = 'bookmark'
urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'),
    path('bookmark/<int:pk>/', views.BookmarkDV.as_view(), name='detail'),

    path('add/', views.BookmarkCreateView.as_view(), name='add'),
    path('change/', views.BookmarkChangeLV.as_view(), name='change'),
    path('<int:pk>/update/', views.BookmarkUpdateView.as_view(), name='update'),
    path('<intLpk>/delete/', views.BookmarkDeleteView.as_view(), name='delete'),
]