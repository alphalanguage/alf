import os
import re
import json
import requests

def carregar_banco(origem, caminho):
    if origem == "$local":
        if os.path.exists(caminho):
            with open(caminho, "r", encoding="utf-8") as f:
                return json.load(f)
        return []
    elif origem in ["$online", "$github"]:
        r = requests.get(caminho)
        if r.status_code == 200:
            return r.json()
        return []

def gerar_saida(nome_saida, html, css, js):
    with open(f"{nome_saida}.html", "w", encoding="utf-8") as f:
        f.write(f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Alpha App</title>
<style>
body {{
    font-family: Arial;
}}

.janela {{
    padding: 20px;
}}

.esquerda {{
    text-align: left;
}}

.meio {{
    text-align: center;
}}

.direita {{
    text-align: right;
}}

button {{
    padding: 10px 15px;
    cursor: pointer;
}}
{css}
</style>
</head>
<body>
{html}
<script>
{js}
</script>
</body>
</html>
""")

def traduzir(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    html = ""
    css = ""
    js = ""
    alinhamento_atual = "esquerda"

    for linha in linhas:
        linha = linha.strip()

        # janela
        if linha.startswith("<janela>"):
            match_cor = re.search(r"#([0-9a-fA-F]{6})", linha)
            if match_cor:
                css += f"body {{ background-color: {match_cor.group(0)}; }}\n"
            html += f"<div class='janela {alinhamento_atual}'>\n"

        elif linha.startswith("</janela>"):
            html += "</div>\n"

        # alinhamento
        elif linha == "<esquerda>":
            alinhamento_atual = "esquerda"
        elif linha == "<meio>":
            alinhamento_atual = "meio"
        elif linha == "<direita>":
            alinhamento_atual = "direita"

        # campo
        elif linha.startswith("*"):
            partes = linha.split('"')
            nome = linha.split()[0][1:]
            texto = partes[1] if len(partes) > 1 else nome.capitalize()
            html += f"<div class='{alinhamento_atual}'>"
            html += f"<label>{texto}</label><br>"
            html += f"<input name='{nome}'><br><br></div>\n"

        # botão com link
        elif linha.startswith("@"):
            partes = linha.split()
            nome_botao = partes[0][1:]
            link = None
            acao_js = None

            if "->" in linha:
                link = linha.split("->")[1].strip()

            if "+acao" in linha:
                acao_js = linha.split('"')[1]

            html += f"<div class='{alinhamento_atual}'>"
            if link:
                html += f"<button onclick=\"window.location.href='{link}'\">{nome_botao.capitalize()}</button>"
            elif acao_js:
                js += acao_js + "\n"
                html += f"<button onclick=\"{acao_js}\">{nome_botao.capitalize()}</button>"
            else:
                html += f"<button>{nome_botao.capitalize()}</button>"
            html += "</div><br>\n"

        # mensagem
        elif linha.startswith("&mensagem"):
            msg = linha.split('"')[1]
            html += f"<div class='{alinhamento_atual}'><p>{msg}</p></div>\n"

        # mídia
        elif linha.startswith("+src"):
            partes = linha.split('"')
            link = partes[1]
            html += f"<div class='{alinhamento_atual}'>"
            if link.endswith((".png", ".jpg", ".jpeg")):
                html += f"<img src='{link}' width='300'>"
            elif link.endswith(".mp3"):
                html += f"<audio controls src='{link}'></audio>"
            elif link.endswith(".mp4"):
                html += f"<video controls width='400' src='{link}'></video>"
            html += "</div><br>\n"

        # js direto
        elif linha.startswith("+js"):
            codigo = linha.split('"')[1]
            js += codigo + "\n"

    nome_saida = input("Como gostaria de salvar o arquivo? (sem .html): ")
    gerar_saida(nome_saida, html, css, js)
    print(f"Arquivo {nome_saida}.html gerado com sucesso.")

if __name__ == "__main__":
    arquivo = input("Digite o nome do arquivo .alf: ")
    traduzir(arquivo)
