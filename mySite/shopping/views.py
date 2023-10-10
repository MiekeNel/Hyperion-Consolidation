from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Products, Choice
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    latest_question_list = Products.objects.order_by('-price')[::]
    context = {'latest_question_list': latest_question_list}
    return render(request, "shopping/shop_page.html", context)

@login_required
def detail(request, question_id):
    question = get_object_or_404(Products, pk=question_id)
    return render(request, 'shopping/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Products, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
            pk=request.POST['choice']
        )
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'shopping/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        
        return HttpResponseRedirect(
            reverse('shopping:results', args=(question_id,))
        )
    
def results(request, question_id):
    question = get_object_or_404(Products, pk=question_id)
    return render(request, 'shopping/results.html', {'question': question})
