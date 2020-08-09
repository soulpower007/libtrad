from django.contrib import admin
from django.urls import path, include
from accounts import views
from django.contrib.auth import views as auth_views


from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
    path('create', views.BookCreateView.as_view(), name = 'bookcreate'),
    path('detail/<slug:slug>', views.BookDetailView.as_view(), name = 'bookview'),
    path('delete/<slug:slug>', views.BookDeleteView.as_view(), name = 'bookdelete'),
    path('list/', views.BookListView.as_view(), name = 'booklist'),
    path('tag/<slug:slug>', views.tagged, name  = 'booktaglist'),
    path('trade/<slug:slug>', views.TradeView, name='reqtrade'),
    path('tradedelete/<int:idd>', views.TradeDeleteView,name='tradedelete'),
    path('tradeapprove/<int:id>', views.TradeApproveView,name='tradeapprove'),
    path('tag/<slug:slug>', views.TagListView.as_view(), name='taglist'),

]
