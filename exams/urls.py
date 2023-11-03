from django.urls import path
from .views import ExamListView, ExamCreateView, StudentExamListView, ExamUpdateView, ExamDelete, ActiveExam

app_name = 'exams'

urlpatterns = [
    path('<int:pk>/delete/', ExamDelete.as_view(), name='exam_delete_url'),
    path('<int:pk>/active/', ActiveExam.as_view(), name='exam_active_url'),
    path('<int:id>/list', ExamListView.as_view(), name='examlist'),
    path('student_exam', StudentExamListView.as_view(), name='studentExamList'),
    path('<int:id>/exam_submit/', ExamCreateView.as_view(), name='createQuestion'),
    path('<int:course_id>/update/<int:pk>/', ExamUpdateView.as_view(), name='exam_update'),

]
