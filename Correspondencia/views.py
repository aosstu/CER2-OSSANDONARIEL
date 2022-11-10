from django.shortcuts import render
from Correspondencia.models import Correspondencia

# Create your views here.

def home(request):
    correspondeciasListadas=Correspondencia.objects.all()
    search_query = request.GET.get('buscar')
    if search_query !="" and search_query is not None:
        print(search_query)
        correspondeciasListadas=correspondeciasListadas.filter(nResidencia__nResidencia__iexact=search_query)
    
    
    return render(request,"Correspondencia/correspondencia_list.html",{"correspondencia":correspondeciasListadas})

# class home(ListView):
#     model: Correspondencia
#     template_name: 'home.html'
    
#     def get_queryset(self):
#         search_query = request.GET.get('search')
#         if search_query != '' and search_query is not None:
#             return Correspondencia.objects.filter(nResidencia__icontains=search_query)
#         else:
#             return Correspondencia.objects.all()
    
#     def get_context_data(self, **kwargs):
#         return super().get_context_data(**kwargs)
#         context['titulo'] = ['Home: Correspondencias']
#         return context
