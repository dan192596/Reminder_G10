from django.shortcuts import render
from .forms import NotasForm
from .models import Notas
from django.views.decorators.csrf import csrf_exempt                                          

# Create your views here.
@csrf_exempt
def NotasCreateView(request):
    if request.method == "POST":
        form = NotasForm(request.POST)
        if form.is_valid():
            misnotas = form.save(commit=False)
            misnotas.save()
    form = NotasForm()    
    return render(request, 'misnotas_create.html', {'form': form})

@csrf_exempt
def NotasListView(request):
    queryset = Notas.objects.all()
    return render(request, 'misnotas_list.html', {'object_list':queryset})