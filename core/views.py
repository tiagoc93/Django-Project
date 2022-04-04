from django.views.generic import FormView
# Class Based Views == necessita importar o padrão do django a cima.
from django.urls import reverse_lazy
from django.contrib import messages

# Importando os models
from .models import Servico, Funcionario, Recurso
from .forms import ContatoForm

# TemplateView só pede o template_name e recebe o caminho html
class IndexView(FormView):               # página web que possue formulário
    template_name = 'index.html'         # nome do template
    form_class = ContatoForm             # Classe do formulárop
    success_url = reverse_lazy('index')  # Redireciona para index se sucesso.

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all() # Ordenar por um caractere aleatorio, poderia ser por id ou qualquer outro.
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['recursos'] = Recurso.objects.order_by('?').all()
        return context

    def form_valid(self, form, *args, **kwargs):                         # Se formulário valido
        form.send_mail()                                                 # Envia e-mail
        messages.success(self.request, 'E-mail enviado com sucesso!')    # Retorna mensagem de sucesso
        return super(IndexView, self).form_valid(form, *args, **kwargs)  # Retorna o formulário

    def form_invalid(self, form, *args, **kwargs):                       # Se inválido
        messages.error(self.request, 'Erro ao enviar e-mail.')           # Mensagem de erro
        return super(IndexView, self).form_invalid(form, *args, **kwargs)# Retorna ao formulário

