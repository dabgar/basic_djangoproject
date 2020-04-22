from django.http import Http404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from .models import Questions, Answers
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

class IndexView(generic.ListView):
    template_name='legal/index.html'
    context_object_name ='all_questions'

    def get_queryset(self):
        return Questions.objects.all()
    
 

def detail(request,question_id):
    allanswers=Answers.objects.all()
    #Answers.objects.get(pk=question_id)
    answer=get_object_or_404(Answers,pk=question_id)
    print(allanswers)
    return render(request,'legal/detail.html',{'answer':answer})
   
class QuestionCreate(CreateView):
    model = Questions
    fields = ['question','category']

class UserFormView(View):
    form_class=UserForm
    template_name='legal/registration_form.html'

#blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})
#process form data
    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user=authenticate(username=username, password=password)
            
            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect('legal:index')

        return render(request,self.template_name,{'form':form})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                questions = Questions.objects.filter(user=request.user)
                return render(request, 'legal/index.html', {'questions': questions})
            else:
                return render(request, 'legal/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'legal/login.html', {'error_message': 'Invalid login'})
    return render(request, 'legal/login.html')



       

    