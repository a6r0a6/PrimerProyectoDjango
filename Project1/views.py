from django.http import HttpResponse
def saludo(request): 
    return HttpResponse ("Mi primer página con Django. Aida Ruiz Azotea, IRD-43")
def despedida(request):
    return HttpResponse ("¡Adiós! :D")
