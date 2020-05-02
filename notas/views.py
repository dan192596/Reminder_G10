from django.shortcuts import render
from .forms import NotasForm
from .models import Notas

# Create your views here.
def NotasCreateView(request):
    if request.method == "POST":
        form = NotasForm(request.POST)
        if form.is_valid():
            misnotas = form.save(commit=False)
            misnotas.save()
    form = NotasForm()    
    return render(request, 'misnotas_list.html', {'form': form})

def NotasListView(request):
    queryset = Notas.objects.filter()
    return render(request, 'misnotas_create.html', {'object_list':queryset})