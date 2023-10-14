from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from .models import Exam
from .forms import ExamForm
import json
# TODO
# from django.http import JsonResponse
# from django.core import serializers
from decimal import Decimal
from django.urls import reverse_lazy



# Create your views here.

class ExamListView(ListView):
    model = Exam
    template_name = 'home/exams.html'
    context_object_name = 'exams'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exams = self.get_queryset()

        exams_data = [{
            'id': exam.id,
            'label': exam.label,
            'score_type': exam.score_type,
            'unanswered_penalty': exam.unanswered_penalty,
            'shuffle_answer': exam.shuffle_answer,
            'incorrect_penalty': exam.incorrect_penalty,
            'percent_passing_score': exam.percent_passing_score,
            'point_passing_score': exam.point_passing_score,
            'duration': exam.duration,
            'deadline': exam.deadline
        } for exam in exams]

        exams_json = json.dumps(exams_data, cls=DecimalEncoder, indent=4, sort_keys=True, default=str)
        context['exams_json'] = exams_json

        return context

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super(DecimalEncoder, self).default(obj)


class StudentExamListView(ListView):
    model = Exam
    template_name = 'home/student-exams.html'
    context_object_name = 'exams'

    def get_queryset(self):
        # Return only exams where action is True
        print('salam')
        return Exam.objects.filter(action=True)


class ExamCreateView(CreateView):
    model = Exam
    form_class = ExamForm
    template_name = 'home/exams.html'
    success_url = '/success/'

# TODO
class ExamUpdateView(UpdateView):
    model = Exam
    form_class = ExamForm
    template_name = 'home/exams.html'
    success_url = reverse_lazy('exams:exam_update')

    def form_valid(self, form):
        print("Form is valid!")
        # Here you can add custom logic before saving the form
        # For example, you can perform some additional processing or validation
        print('sasam')

        # Call the parent class's form_valid method to save the form
        response = super().form_valid(form)

        # Add any additional custom logic after saving the form

        return response

#
#TODO

# class ExamDelete(View):
#     def delete(self, request, id):
#         try:
#             data = json.loads(request.body.decode('utf-8'))
#             name = data.get('name')
#
#             if name == 'question':
#                 question = get_object_or_404(Question, id=id)
#                 question.delete()
#             elif name == 'question_group':
#                 question_group = get_object_or_404(QuestionGroup, id=id)
#                 question_group.delete()
#             else:
#                 return JsonResponse({'error': 'Invalid name'}, status=400)
#
#             return JsonResponse({'result': 'ok'}, status=200)
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON data'}, status=400)