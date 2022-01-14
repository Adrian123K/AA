from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accountapp.views import AccountCreateView, hello_world, AccountDetailView


app_name = 'accountapp'


urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    
    # Login, logout 구현
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # 계정 생성 구현
    path('create/', AccountCreateView.as_view(), name='create'), #as_view 함수형으로 작동하는 view 전달
    
    # 사용자 my page 구현
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'), # userid값을 입력해야 원하는 상세페이지가 출력
]
