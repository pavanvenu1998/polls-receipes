# from django.shortcuts import HttpResponse
# from django.shortcuts import render
#
# def show_details(request):
#     return HttpResponse("Name: {},<br>Email: {}<br>phone: {}".format("pavan kumar reddy","pavan@gmail.com","9949165435"))
#
# # Create your views here.
# def college_details(request):
#     return HttpResponse("Name: {},<br>department:{},<br>hodsir: {}".format("ssn","mechanical","suresh"))
#
# def bank_details(request):
#     return HttpResponse("accountdetails: {},<br>phonenumber:{},<br>atm_pin: {}".format("9876544321","987653432","8765"))
#
# def family_details(request):
#     return HttpResponse("father: {},<br>mother: {},<br>son1:{},<br>son2:{}".format("srekanth","pramila","venu","pavan"))
#
# def index(request):
#     context={"name":"pavan","marks":22,
#              "schools":["sri vani high school","sai sree convent"],
#              "working":[{"company":"hcl","exp":2},{"company":"wipro","exp":1}]}
#     return render(request,'polls/index.html',context)
#
# def home(request):
#     details={"family":[{"name":"father name is srekanth","occupation":"farmer"},{"name":"my brother name is venu", "occupation":"employee"}]}
#     return render(request,"polls/index.html",details)
#
# def capitals(request):
#     computer={"india":[{"state":"andhra","language":"telugu"},{"state":"tamilnadu","language":"tamil"}]}
#     return render(request,"polls/index.html",computer)
#
# def colleges(request):
#     list ={"popular":[{"name":"ssn","location":"ongole"},{"name":"klu","location":"vijaywada"}]}
#     return render(request,"polls/index.html",list)
#
# def company(request):
#     office={"details":[{"name":"ramesh","company":"wipro","salary":34567},{"name":"anusha","company":"hcl","salary":43256},
#                        {"name":"ganesh","company":"capgemini","salary":98767}]}
#     return render(request,"polls/index.html",office)
#
# def institute(request):
#     bangalore={"storage":[{"name":"pavan","course":"python","location":"anathapur"},{"name":"ramesh","course":"django",
#                             "location":"kadapa"}]}
#     return render(request,"polls/index.html",bangalore)


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))







