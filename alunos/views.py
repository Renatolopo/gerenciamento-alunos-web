from django.shortcuts import render
from .forms import ProdutoModelForm
from django.contrib import messages
from.models import Produto
from django.shortcuts import redirect

# Create your views here.
def index(request):
    context = {

    'produtos': Produto.objects.all()

    }
    return render(request,'index.html',context)

def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST,request.FILES)

            if form.is_valid():
                form.save()
                messages.success(request, 'Produtosalvo comsucesso')
                form = ProdutoModelForm()

            else:
                messages.error(request, 'Erro ao salvar produto')

        else:
            form = ProdutoModelForm()

        context = {

        'form': form

        }
        return render(request,'produto.html', context)
    else:

        return redirect('index')