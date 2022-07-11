from django.urls import path
from .views import AllUsersParameterView, ParameterView, UserView

app_name = "test_case"
urlpatterns = [
    path('parameters/<user_name>/', AllUsersParameterView.as_view()),
    path('parameters/<user_name>/<parameter_name>/', ParameterView.as_view()),
    path('users/', UserView.as_view()),
]