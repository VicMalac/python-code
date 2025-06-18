from bs4 import BeautifulSoup

# Lê o conteúdo HTML salvo
with open("pagina.html", "r", encoding="utf-8") as f:
    conteudo = f.read()

# Analisa o HTML com BeautifulSoup
soup = BeautifulSoup(conteudo, "html.parser")

# Busca todas as tags de imagem (img)
imagens = soup.find_all("img")

# Filtro extra opcional: ignorar ícones pequenos, como logo do Google
imagens_validas = [img for img in imagens if img.get("src") and "googleusercontent" in img.get("src")]

# Salva backup
with open("backup.txt", "w", encoding="utf-8") as bkp:
    bkp.write(f"Total de imagens: {len(imagens_validas)}\n")
    for img in imagens_validas:
        bkp.write(img.get("src") + "\n")

print(f"✅ Total de imagens encontradas: {len(imagens_validas)}")
