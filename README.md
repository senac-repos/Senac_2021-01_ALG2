# Algoritmos e Programação II
###### Aluno: Thiago Martins Proença

---

Este repositório é exclusivo para atividades e trabalhos da cadeira de ALG2.

---

### É importante saber:
No arquivo `MetodosAuxiliares.py` localizado em `~/Atividades/` existem duas classes, uma delas é utilizada para auxiliar
todos os exercícios e trabalhos do semestre. A outra classe é utilizada para formatar a fonte das mensagens no console.

Na classe `Auxiliares` existe um método chamado `limpa_tela_menu`, este método tem a função de limpar a tela do console 
e exibir como cabeçalho o nome do menu conforme definido pelo 
programa, mas para que este método funcione corretamente em distribuições Unix (Lunix e MacOs), é necessário realizar
a seguinte configuração:

Acessar a tela "Run/Debug Configurations", acessar a sessão "Execution" e marcar a opção "Emulate terminal in output 
console" conforme imagem abaixo:

![img.png](img.png)

Caso esta confirmação não seja realizada, será exibida uma mensagem de erro: _TERM environment variable not set._, o 
programa irá executar normalmente, porém o método não irá funcionar.

---

### Diretórios:

Todas as atividades estarão hospedadas em `~/Atividades`. Trabalhos estarão hospedados em `~/Trabalhos`.

---

### Documentações

Os métodos das classes localizadas no arquivo `MetodosAuxiliares.py` estão todas documentadas para auxiliar o usuário 
que ler o código. Esta abordagem foi utilizada para que outras pessoas fossam analisar o código e entender o que está 
sendo realizado a cada
método.