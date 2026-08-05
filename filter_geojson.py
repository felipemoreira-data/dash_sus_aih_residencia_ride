import json
import pandas as pd
from sqlalchemy import text
from db_connect import obter_conexao

engine = obter_conexao()
with engine.connect() as conn:
    df = pd.read_sql(text('SELECT DISTINCT codigo_municipio FROM sus_ride_df_aih_residencial'), conn)

codigos = set(df['codigo_municipio'].astype(str).str.zfill(6))
print(f'Encontrados {len(codigos)} códigos no banco.')

with open('municipios_br.json', encoding='utf-8') as f:
    geo = json.load(f)

print(f"Total features originais: {len(geo['features'])}")

geo['features'] = [f for f in geo['features'] if str(f['properties'].get('codarea'))[:6] in codigos]

print(f"Total features filtradas: {len(geo['features'])}")

with open('municipios_ride.json', 'w', encoding='utf-8') as f:
    json.dump(geo, f)

print('Arquivo municipios_ride.json criado com sucesso.')
