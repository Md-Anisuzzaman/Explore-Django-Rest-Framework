
# funtion based api view url
# from django.contrib import admin
# from django.urls import path
# from quiz_category import views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('category/api/all',views.quiz_allcat_view),
#     path('category/api/<int:id>',views.quiz_singlecat_view),
#     path('category/api/create/',views.quiz_create_category_view),
#     path('category/api/test/',views.test),
#     path('category/api/edit/<int:id>',views.update)
# ]

# class based APIView

# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from django.contrib import admin
# from quiz_category import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/category/<int:pk>', views.CategoryView.as_view()),
#     path('api/allcategory/', views.AllCategoryView.as_view()),
#     path('api/createcategory/', views.CreateCategoryView.as_view()),
#     path('api/edit/<int:pk>', views.UpdateCategoryView.as_view()),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)


from django.urls import path
from django.contrib import admin
from quiz_category import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/category/<int:pk>/', views.RetrieveCategory.as_view()),
    path('api/allcategory/', views.ShowAllcategory.as_view()),
    path('api/createcategory/', views.CreatCategory.as_view()),
    path('api/showcreate/', views.ShowAndCategoryCreate.as_view()),
    path('api/reupdelete/<int:pk>/',
         views.Retrieve_UpdateAndCategory_Delete.as_view()),
    path('api/edit/<int:pk>/', views.UpdateCategory.as_view()),
    path('api/delete/<int:pk>/', views.DeleteCategory.as_view()),
]
