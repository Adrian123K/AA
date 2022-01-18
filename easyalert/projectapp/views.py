from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView

from django.urls import reverse
from django.utils.decorators import method_decorator
from projectapp.decorators import project_ownership_required
from projectapp.forms import ProjectCreationForm
# Create your views here.

from projectapp.models import Project

@method_decorator(project_ownership_required, 'get')
@method_decorator(project_ownership_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk':self.object.pk})

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'target_project'
    template_name = 'project/detail.html'
    
    
    
class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'project/list.html'
    paginate_by = 25
    
    
    