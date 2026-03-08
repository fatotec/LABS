import pandas as pd
import os

def process_silver_layer():
    # Caminhos (simulando o Data Lake)
    input_path = 'data/bronze/dados_brutos.parquet'
    output_path = 'data/silver/dados_limpos.parquet'
    
    # 1. Leitura dos dados da Bronze
    if not os.path.exists(input_path):
        print("Erro: Arquivo Bronze não encontrado!")
        return

    df = pd.read_parquet(input_path)
    print(f"Iniciando processamento de {len(df)} registros...")

    # 2. Limpeza e Transformação
    # Exemplo: Padronizar nomes de colunas para minúsculo
    df.columns = [col.lower() for col in df.columns]

    # Exemplo: Remover duplicados baseado no ID
    df = df.drop_duplicates(subset=['id'])

    # Exemplo: Tratar valores nulos (Preencher nomes vazios com 'N/A')
    if 'name' in df.columns:
        df['name'] = df['name'].fillna('Sem Nome')

    # 3. Salvando na Silver (Particionado ou simples)
    os.makedirs('data/silver', exist_ok=True)
    df.to_parquet(output_path, index=False)
    
    print(f"Camada Silver processada com sucesso em: {output_path}")

if __name__ == "__main__":
    process_silver_layer()