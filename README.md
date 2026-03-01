\# Alpha Language



Alpha é uma linguagem brasileira que transforma arquivos .alf em aplicações web completas.


Tudo estará disponível em releases!!
---

\## Como executar

Faça o comando pela primeira vez necessário uma vez só.
````
py -m pip install requests .
````
Clique duas vezes no arquivo tradutor.py. Ele vai perguntar qual é o nome do arquivo (.alf) . Escreva o nome do arquivo ex: "arquivo.alf" (sem aspas) e é NECESSÁRIO usar .alf no final.
Logo depois, ele perguntará qual vai ser o nome do arquivo (.html) . Escreva SEM .html . Depois está pronto!

---

Se precisar de ajuda, consulte o dicionario.md disponível em releases.


\## Estrutura básica de exemplo



```


<janela> #B0C4DE {login}
<meio>
*usuario "Usuário"
*senha "Senha"

@entrar 

@google -> https://google.com

&mensagem "Bem-vindo ao Alpha"
&mensagem "Esse é um arquivo de teste. Os botões são uma demonstração. Não funcionam."

<meio>
<imagem>
+src $online +src "https://raw.githubusercontent.com/alphalanguage/alf/refs/heads/main/Alpha-logo.png"
</imagem>
</meio>

<som>
+src $online +src "https://github.com/alphalanguage/alf/raw/refs/heads/main/test-audio.mp3"
</som>

+js "alert('Alpha funcionando')"
<meio>
</janela>


```



---



\## Regras



\- Tudo em minúsculo no código

\- Sem acentos fora de aspas

\- Aspas aceitam qualquer caractere

\- +src obrigatório antes de qualquer "link"

\- < > sempre minúsculo

\- # indica cor hexadecimal


