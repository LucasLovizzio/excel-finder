import pandas as pd
df = pd.read_csv("docs\\data.csv", delimiter=';', on_bad_lines='skip')

article_code = "17307" # Validar esto y verificar que existe, de lo contrario dar mensaje de error
result = df[df['Cód. Artículo'] == article_code]

if result.empty:
    print("El artículo no existe")
else:
    print(result)