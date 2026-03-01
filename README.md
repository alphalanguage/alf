\# Alpha Language



Alpha é uma linguagem brasileira que transforma arquivos .alf em aplicações web completas.



\## Como executar



Insira o comando no cmd mas no caminho. ex: cd C:\\Users\\User\\Documents\\ e logo depois execute o seguinte comando (troque o nome do arquivo.alf pelo nome do seu arquivo. Lembrando, NÃO mexa no arquivo tradutor.py, se não pode não funcionar mais.): 

python tradutor.py arquivo.alf

mas o arquivo só irá funcionar se você rodar o comando antes (só precisa uma vez):

py -m pip install requests .

```



Ele irá gerar:



```

arquivo.html

```



Abra no navegador.



---



\## Estrutura básica de exemplo



```

<janela> #ffffff {login}

\*usuario "Usuário"

\*senha "Senha"

@entrar

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

