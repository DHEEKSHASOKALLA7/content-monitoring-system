from django.urls import path
from .views import (
    ApiRootView,
    KeywordCreateView,
    ScanView,
    FlagListView,
    FlagUpdateView
)

urlpatterns = [
    path('', ApiRootView.as_view()),   # 🔥 important
    path('keywords/', KeywordCreateView.as_view()),
    path('scan/', ScanView.as_view()),
    path('flags/', FlagListView.as_view()),
    path('flags/<int:id>/', FlagUpdateView.as_view()),
]