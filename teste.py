import requests
import feedparser
import re
import nltk
import tkinter as tk
from tkinter import scrolledtext
from collections import Counter
from nltk.corpus import stopwords
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from deep_translator import GoogleTranslator

# Baixa as stopwords se ainda não estiverem disponíveis
nltk.download('stopwords')

# Configurar stopwords em português e inglês
stop_words = set(stopwords.words('english') + stopwords.words('portuguese'))

# Fontes de dados (Feeds RSS de tecnologia e programação)
rss_feeds = [
    "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
    "https://feeds.feedburner.com/TechCrunch/",
    "https://hnrss.org/newest",
    "https://www.reddit.com/r/programming/.rss"
]

# Coleta e limpeza dos dados
def fetch_and_clean_articles(feeds):
    all_text = []

    for feed_url in feeds:
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:10]:  # Pega até 10 artigos por fonte
                content = entry.get("title", "") + " " + entry.get("summary", "")
                content = re.sub(r'&[a-zA-Z0-9#]+;', ' ', content)  # Remove entidades HTML (&nbsp;)
                content = re.sub(r'<[^>]+>', ' ', content)  # Remove tags HTML
                content = re.sub(r'[^A-Za-zÀ-ÿ\s]', ' ', content)  # Remove caracteres especiais
                content = content.lower()  # Converte para minúsculas
                words = content.split()
                words = [word for word in words if word not in stop_words and len(word) > 2]  # Remove stopwords
                all_text.extend(words)
        except Exception as e:
            print(f"Erro ao processar {feed_url}: {e}")

    return all_text

# Processa os artigos para encontrar tendências
words = fetch_and_clean_articles(rss_feeds)

# Identifica os tópicos mais frequentes
word_freq = Counter(words).most_common(10)
top_words = [word for word, freq in word_freq]

# Define o assunto principal para o artigo
assunto_principal = top_words[0] if top_words else "tecnologia"

# Carrega o modelo de IA GPT-2
device = "cuda" if torch.cuda.is_available() else "cpu"  # Usa GPU se disponível
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2").to(device)

# Gera um artigo para o LinkedIn
input_text = f"Escreva um artigo para o LinkedIn sobre '{assunto_principal}' no contexto de tecnologia e programação."
inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=100).to(device)

output = model.generate(
    **inputs,
    max_length=250,  # Limita o tamanho do texto
    temperature=0.7,  # Controla a criatividade
    top_p=0.9,  # Mantém a coerência do texto
    repetition_penalty=1.2,  # Reduz repetições
    pad_token_id=tokenizer.eos_token_id  # Evita warnings
)

texto_gerado = tokenizer.decode(output[0], skip_special_tokens=True)

# Função para traduzir o texto
def traduzir_texto():
    texto_atual = text_area.get("1.0", tk.END)  # Obtém o texto da caixa
    texto_traduzido = GoogleTranslator(source="auto", target="pt").translate(texto_atual)
    text_area.delete("1.0", tk.END)  # Limpa o texto antigo
    text_area.insert(tk.END, texto_traduzido)  # Insere a tradução

# Criar a interface gráfica com Tkinter
root = tk.Tk()
root.title("Artigo do LinkedIn - Tendências Tech")
root.geometry("800x600")

# Título
title_label = tk.Label(root, text="📢 Assunto em Alta:", font=("Arial", 14, "bold"))
title_label.pack(pady=5)

# Assunto principal
topic_label = tk.Label(root, text=assunto_principal.upper(), font=("Arial", 12), fg="blue")
topic_label.pack(pady=5)

# Palavras mais frequentes
word_label = tk.Label(root, text=f"🔍 Palavras mais frequentes: {', '.join(top_words)}", font=("Arial", 10))
word_label.pack(pady=5)

# Caixa de texto para exibir o artigo
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=20, font=("Arial", 11))
text_area.insert(tk.END, texto_gerado)
text_area.pack(pady=10)

# Botão para traduzir o texto
translate_button = tk.Button(root, text="Traduzir para Português", command=traduzir_texto, font=("Arial", 12), bg="green", fg="white")
translate_button.pack(pady=5)

# Botão para fechar
close_button = tk.Button(root, text="Fechar", command=root.quit, font=("Arial", 12), bg="red", fg="white")
close_button.pack(pady=10)

# Iniciar o loop da interface gráfica
root.mainloop()
