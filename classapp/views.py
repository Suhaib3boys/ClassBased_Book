from msilib.schema import Class
from pyexpat import model
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView

from classapp.models import Books

# Create your views here.
class ViewBook (ListView):
    model = Books
    template_name = 'index.html'
    context_object_name = 'book'

class AddBook (CreateView):
    model = Books
    fields = '__all__'
    success_url = reverse_lazy('add')
    template_name = 'add.html'

class DetailBook (DetailView):
    model = Books
    fields = '__all__'
    context_object_name = 'detail'
    template_name = 'detail.html'
class UpdateBook (UpdateView):
    model = Books
    fields = '__all__'
    context_object_name = 'edit'
    template_name = 'edit.html'
    success_url = reverse_lazy('index')
class DeleteBook (DeleteView):
    model = Books
    fields = '__all__'
    context_object_name = 'delete'
    template_name = 'delete.html'
    success_url = reverse_lazy('index')