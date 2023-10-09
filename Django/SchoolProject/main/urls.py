from django.urls import path
from .views import index, view_director, view_zauch, view_student, view_curator, view_grade, view_lesson

urlpatterns = [
    path('', index, name='home_page'),
    path('director/', view_director, name='director_page'), 
    path('zauch/', view_zauch, name='zauch_page'),
    path('student/', view_student, name='student_page'),
    path('curator/', view_curator, name='curator_page'),
    path('grade/',  view_grade, name='grade_page'),
    path('lesson/', view_lesson, name='lesson_page'),

]
