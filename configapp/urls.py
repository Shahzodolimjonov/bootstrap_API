from django.urls import path
from .views import index,detail,n_del,add_new,new_update,add_category,HomeCategory,search
# index,category

urlpatterns = [
    # path('index/', HomeNews.as_view(),name='home'),
    path('category/<int:pk>/', HomeCategory.as_view(),name='category'),
    path('index/', index,name='home'),
    # path('category/<int:pk>/', category,name='category'),
    path('detail/<int:pk>/', detail,name='detail'),
    path('n_del/<int:pk>/', n_del, name='n_del'),
    path('add_new/', add_new, name='add_new'),
    path('new_update/<int:pk>/', new_update, name='new_update'),
    path('add_category/', add_category, name='add_category'),
    # path('Search/', search.as_view(), name='Search'),
    path('Search/', search, name='Search'),

]
