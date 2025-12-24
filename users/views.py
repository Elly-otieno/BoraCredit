from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.contrib.auth import login



# Create your views here.
class RegisterView(FormView):
    '''
    Register a user
    '''
    template_name = ''
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user) # do auto login onregistration
        return redirect(self.get_success_url())
    
    def dispatch(self, request, *args, **kwargs):
        '''
        prevent logged in users from registering again
        '''
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
