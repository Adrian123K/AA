from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.generic import RedirectView
from django.shortcuts import get_object_or_404
# Create your views here.

from subscribeapp.models import Subscription
from projectapp.models import Project


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk':self.request.GET.get('project_pk')})
    
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk')) # 'project_pk'를 가지고 있는 project 검색, 없으면 404 error
        user = self.request.user
        
        subscription = Subscription.objects.filter(user=user, project=project)
        
        if subscription.exists(): # 존재하면 삭제
            subscription.delete()
        else: # 없으면 추가 후 저장
            Subscription(user=user, project=project).save()
        
        return super(SubscriptionView, self).get(request, *args, **kwargs)
    
    