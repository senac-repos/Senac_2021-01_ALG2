# Algoritmos e Programação II
###### Aluno: Thiago Martins Proença

---

### É importante saber:
No diretório `~/MetodosAuxiliares/` existem três classes:
- Classe `Auxiliares`: é utilizada para auxiliar e reutilizar todos os métodos nos exercícios e trabalhos do semestre;
- Classe `Mensagens`: é utilizada para padronizar a forma de exibição das mensagens de Alerta, Erro e Sucesso;
- Classe `FormatarFontes`: é utilizada para formatar a fonte das mensagens no console.

Na classe `Auxiliares` existe um método chamado `limpa_tela_menu`, este método tem a função de limpar a tela do console 
e exibir como cabeçalho o nome do menu conforme definido pelo 
programa, mas para que este método funcione corretamente em distribuições Unix (Lunix e MacOs), é necessário realizar
a seguinte configuração:

Acessar a tela "Run/Debug Configurations", acessar a sessão "Execution" e marcar a opção "Emulate terminal in output 
console" conforme imagem abaixo:

![img.png](img.png)

Caso esta ação não seja realizada, será exibida uma mensagem de erro: _TERM environment variable not set._, o 
programa irá executar normalmente, porém o método não irá funcionar corretamente.

---

### Diretórios:
- Atividades estarão hospedadas em `~/Atividades`.
- Trabalhos estarão hospedados em `~/Trabalhos`.

---

### Documentações
Os métodos das classes localizadas no arquivo `Metodos.py` estão documentadas para auxiliar o usuário que ler o código.
Esta abordagem foi utilizada para que outras pessoas fossam analisar o código e entender o que está sendo realizado a 
cada chamada.