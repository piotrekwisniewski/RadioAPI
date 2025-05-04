from django.urls import path
from .views import HitListCreateAPIView, HitDetailAPIView

urlpatterns = [
    path('hits', HitListCreateAPIView.as_view(), name='hit-list-create'),
    path('hits/<slug:title_url>', HitDetailAPIView.as_view(), name='hit-detail'),
]

