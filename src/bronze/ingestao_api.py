import pandas as pd
import requests
import os

def ingest_raw_data(api_url):
    """Simula a captura de dados brutos e salva na camada Bronze"""
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        
        # Simulando o salvamento em um 'Data Lake' local
        os.makedirs('data/bronze', exist_ok=True)
        df.to_parquet('data/bronze/dados_brutos.parquet')
        print("Dados ingeridos com sucesso na camada Bronze!")
    else:
        print(f"Erro na requisição: {response.status_code}")

if __name__ == "__main__":
    # Exemplo com uma API pública de teste
    ingest_raw_data("https://jsonplaceholder.typicode.com/users")