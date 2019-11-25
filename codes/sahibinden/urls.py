from django.urls import path
from . import views
from sahibinden.views import SahibindenListView, SahibindenDetailView, SahibindenCreateView, SahibindenUpdateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('post/<int:pk>/edit/', SahibindenUpdateView.as_view(),
         name='post_edit'),
    path('post/new/', SahibindenCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', SahibindenDetailView.as_view()),
    path('post-detail/<int:post_id>/', views.post, name ='post_detail'),
    path('', SahibindenListView.as_view(), name='home')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


