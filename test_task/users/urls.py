from django.urls import path, include

from . import views

from .routers import MyRouter

router = MyRouter()
router.register(r'user', views.UserView)
router.register(r'user-list', views.UserListView, basename='users')
print(router.urls)

urlpatterns = [
    path('', include(router.urls))
]

