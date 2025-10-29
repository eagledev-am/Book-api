
from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns   
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView


router = DefaultRouter()
router.register(r'authors' , views.AuthorViewSet)

urlpatterns = [
    path('books/', views.BookList.as_view() , name='book_list_class' ),
    path('books/<int:id>/', views.BookDetail.as_view() , name='book_detail_class'),
    path('' , include(router.urls)),
    path('token/' , TokenObtainPairView.as_view() , name='token_obtain_pair'),
    path('token/refresh/' , TokenRefreshView.as_view() , name='token_refresh'),
]
