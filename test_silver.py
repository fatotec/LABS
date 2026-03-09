import pandas as pd
import os

def test_silver_file_exists():
    assert os.path.exists('data/silver/dados_limpos.parquet')

def test_no_duplicates_in_silver():
    df = pd.read_parquet('data/silver/dados_limpos.parquet')
    assert df['id'].is_unique