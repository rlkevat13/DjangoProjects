from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import School, Student


# Create your views here.
class indexView(TemplateView):
    template_name = 'index.html'


class schoolListView(ListView):
    context_object_name = 'schools'
    model = School
    template_name = 'school_list.html'


class schoolDetailView(DetailView):
    template_name = 'school_detail.html'
    model = School
    context_object_name = 'school_detail'


class schoolCreateView(CreateView):
    model = School
    fields = ('sch_name', 'sch_principal', 'sch_location')
    template_name = 'school_form.html'


class studentCreateView(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'student_form.html'
    success_url = '/schools'

    def form_valid(self, form):
        student = form.save(commit=False)
        print("\n\nschool_id-------->", form.data)
        school_id = form.data['school']
        school = get_object_or_404(School, id=school_id)
        student.school = school
        return super(studentCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(studentCreateView, self).get_context_data(**kwargs)
        print("\n\ncontext------------->", context)
        print("\n\nself.kwargs", self.kwargs)
        context['a_id'] = self.kwargs['pk']
        return context

    def get_success_url(self, **kwargs):
        return reverse("my_app:school_detail", kwargs={'pk': self.object.school.pk})



class schoolUpdateView(UpdateView):
    model = School
    fields = ['sch_name', 'sch_principal']
    template_name = 'school_update.html'
    context_object_name = 'school_edit'
    success_url = '/schools'


class studentUpdateView(UpdateView):
    model = Student
    fields = "__all__"
    template_name = 'student_update.html'
    success_url = '/schools'

    def get_success_url(self, **kwargs):
        return reverse("my_app:school_detail", kwargs={'pk': self.object.school.pk})


class schoolDeleteView(DeleteView):
    model = School
    template_name = 'school_confirm_delete.html'
    success_url = reverse_lazy("my_app:schools")


class studentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'

    def get_success_url(self, **kwargs):
        return reverse("my_app:school_detail", kwargs={'pk': self.object.school.pk})


def school_delete_all(request):
    schools = School.objects.all()
    print("\n\n schools", schools)
    for school in schools:
        school.delete()
    return redirect('/schools')


def student_delete_all(request):
    students = Student.objects.all()
    print("\n\n schools", students)
    for student in students:
        student.delete()
    return redirect('/schools')
