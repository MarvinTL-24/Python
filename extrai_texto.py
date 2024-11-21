import requests
from bs4 import BeautifulSoup

# URL da página web a ser analisada
url = "https://www.wikipedia.org/"

# Fazendo a requisição para a página
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Parseando o conteúdo HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extraindo o texto principal
    texto = soup.get_text()
    
    # Exibindo as primeiras linhas do texto
    print("Texto extraído da página:")
    print(texto[:500])  # Exibe os primeiros 500 caracteres
else:
    print(f"Erro ao acessar a página. Status code: {response.status_code}")