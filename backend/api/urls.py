from api.views import TaskView
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tasks', TaskView, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
]
