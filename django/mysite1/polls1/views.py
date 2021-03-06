from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponseRedirect
from .models import Choice, Question
from django.views import generic
from django.urls import reverse

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls1/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls1/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls1/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls1/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls1:results', args=(question.id,)))