from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html',
        context={'title': 'Home'
        }
    )

def presupuesto(request):
    return render(request, 'presupuesto.html',
        context={'title': 'Presupuesto'
        }
    )

def contacto(request):
    return render(request, 'contacto.html',
        context={'title': 'Contacto'
        }
    )
