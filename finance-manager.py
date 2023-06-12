import csv
import gspread
import time

## Change month/year
MONTH = '01'
YEAR = '2023'

## First, you have to convert PDF - CSV
file = f'./bankStatements/nu/csv/{YEAR}/Nu_{YEAR}-{MONTH}.csv'

transactions = []

def nuFin(file):
  with open(file, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
      date = row[0][0:2] + f"/{MONTH}/{YEAR}"
      name = row[3]
      amount = float(row[4])
      category = row[2]
      if "Restaurante" in category:
        category = "Consumo"
      if "Bodega Altamirano" in name:
        category = "Despensa"
      if "Gaso" in name:
        category = "Combustible"
      if "Spotify" in name:
        category = "Entretenimiento"
      if "Undostres" in name:
        category = "Teléfono"
      if "Telmex" in name:
        category = "Teléfono"
      if "Pago a tu tarjeta de crédito" in name:
        category = "Pago"
      if "Merpago*Conpeccati" in name:
        category = "Consumo"
      if "Cfe" in name:
        category = "Hogar"
      if "Devolución" in name:
        category = "Devolución"
      if "Digitalocea" in name:
        category = "Hosting"
      if "Alegra" in name:
        category = "Negocio"
      if "Platzi" in name:
        category = "Educación"
      transaction = ((date, name, amount, category))
      # print(transaction)
      transactions.append(transaction)
    return transactions

sa = gspread.service_account()
## Here goes the file name (google spreadsheet)
sh = sa.open(f"Nu-{YEAR}")
## Here goes the worksheet name
wks = sh.worksheet(f"{MONTH}-{YEAR}")
rows = nuFin(file)

for row in rows:
  wks.insert_row([row[0], row[1], row[2], row[3]], 2)
  time.sleep(2)