from textblob import TextBlob
from googletrans import Translator


def traduzir_texto(texto, lingua_destino='en'):
    tradutor = Translator()
    traducao = tradutor.translate(texto, dest=lingua_destino)
    return traducao.text


def analisar_sentimento(texto):

    texto_traduzido = traduzir_texto(texto)
    
  
    blob = TextBlob(texto_traduzido)
    
  
    sentimento = blob.sentiment
    

    return sentimento.polarity, sentimento.subjectivity

def main():
   
    texto = input("Digite o texto a ser analisado: ")
    
  
    polaridade, subjetividade = analisar_sentimento(texto)
    
  
    print(f"Texto original: {texto}")
    print(f"Texto traduzido: {traduzir_texto(texto)}")
    print(f"Polaridade: {polaridade}")
    print(f"Subjetividade: {subjetividade}")

if __name__ == "__main__":
    main()