from django.urls import path, include
from django.contrib import admin
from core import views as project_views
from .views import ExamListView, ExamCreateView, StudentExamListView, ExamUpdateView, ExamDelete, ActiveExam
from taker import urls as taker_url

app_name = 'exams'

urlpatterns = [
    path('<int:pk>/delete/', ExamDelete.as_view(), name='exam_delete_url'),
    path('<int:pk>/active/', ActiveExam.as_view(), name='exam_active_url'),
    path('list', ExamListView.as_view(), name='examlist'),
    path('student_exam', StudentExamListView.as_view(), name='studentExamList'),
    path('exam_submit/', ExamCreateView.as_view(), name='createQuestion'),
    # TODO
    path('<int:pk>/update/', ExamUpdateView.as_view(), name='exam_update'),

]
