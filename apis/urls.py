from django.urls import path
from . import views as user_views


urlpatterns = [
        path('get/users/detail/<int:pk>', user_views.GetUsersDetailView.as_view()),
        path('cretae/contact/', user_views.ContactCreateView.as_view()),
        path('get/user/contact/list/<int:pk>', user_views.GetUsersContactListView.as_view()),
        path('contact/search/', user_views.ContactSearch.as_view())


]