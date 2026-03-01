import sys
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

def gerar_saida(nome_arquivo, html, css, js):
    base = os.path.splitext(nome_arquivo)[0]
    with open(f"{base}.html", "w", encoding="utf-8") as f:
        f.write(f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Alpha App</title>
<style>
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

    janela_cor = ""

    for linha in linhas:
        linha = linha.strip()

        # janela
        if linha.startswith("<janela>"):
            match_cor = re.search(r"#([0-9a-fA-F]{6})", linha)
            if match_cor:
                janela_cor = match_cor.group(0)
                css += f"body {{ background-color: {janela_cor}; }}\n"
            html += "<div class='janela'>\n"

        elif linha.startswith("</janela>"):
            html += "</div>\n"

        # campo
        elif linha.startswith("*"):
            partes = linha.split('"')
            nome = linha.split()[0][1:]
            texto = partes[1] if len(partes) > 1 else nome.capitalize()
            html += f"<label>{texto}</label><br>\n"
            html += f"<input name='{nome}'><br><br>\n"

        # botão
        elif linha.startswith("@"):
            botao = linha.split()[0][1:]
            html += f"<button>{botao.capitalize()}</button><br><br>\n"

        # imagem / som / video
        elif linha.startswith("+src"):
            partes = linha.split('"')
            link = partes[1]
            if link.endswith((".png", ".jpg", ".jpeg")):
                html += f"<img src='{link}' width='300'><br>\n"
            elif link.endswith(".mp3"):
                html += f"<audio controls src='{link}'></audio><br>\n"
            elif link.endswith(".mp4"):
                html += f"<video controls width='400' src='{link}'></video><br>\n"

        # mensagem
        elif linha.startswith("&mensagem"):
            msg = linha.split('"')[1]
            html += f"<p>{msg}</p>\n"

        # js inline
        elif linha.startswith("+js"):
            codigo = linha.split('"')[1]
            js += codigo + "\n"

    gerar_saida(arquivo, html, css, js)
    print("Arquivo gerado com sucesso.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python tradutor.py arquivo.alf")
    else:
        traduzir(sys.argv[1])
