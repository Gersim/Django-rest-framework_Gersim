from django.urls import path
from . import views

urlpatterns = [
    path('',views.endpoints),
    path('advocates/', views.advocate_list, name="advocates"),
    path('advocates/<str:username>/', views.AdvocateDetail.as_view()),


    # company model
    path('companies/', views.CompanyList.as_view(), name="companies"),
    path('companies/<str:name>', views.CompanyDetails.as_view()),
]