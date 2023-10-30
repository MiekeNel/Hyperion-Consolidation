from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Products, Choice
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    """
    View function for the index or shop page.

    This view retrieves a list of the latest products, sorts them by price, and renders them on the shop page.
    
    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered HTML page displaying the latest products.
    """

    latest_question_list = Products.objects.order_by('-price')[::]
    context = {'latest_question_list': latest_question_list}
    return render(request, "shopping/shop_page.html", context)


@login_required
def detail(request, question_id):
    """
    View function for the product detail page.

    This view displays details about a specific product when accessed.

    Args:
        request (HttpRequest): The HTTP request object.
        question_id (int): The ID of the product to display.

    Returns:
        HttpResponse: A rendered HTML page displaying product details.
    """


def vote(request, question_id):
    """
    View function for handling user votes on a product.

    This view processes user votes for a specific product and redirects to the results page.

    Args:
        request (HttpRequest): The HTTP request object.
        question_id (int): The ID of the product to vote for.

    Returns:
        HttpResponseRedirect: Redirects to the results page after processing the vote.
    """
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
    """
    View function for displaying voting results for a product.

    This view displays the results of votes for a specific product, including vote counts, percentages, etc.

    Args:
        request (HttpRequest): The HTTP request object.
        question_id (int): The ID of the product to display results for.

    Returns:
        HttpResponse: A rendered HTML page displaying voting results.
    """
    question = get_object_or_404(Products, pk=question_id)
    return render(request, 'shopping/results.html', {'question': question})
