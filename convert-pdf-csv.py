import tabula

MONTH = '04'
YEAR = '2023'
DIR_INPUT = 'bankStatements/nu/pdf'
DIR_OUTPUT = 'bankStatements/nu/csv'

tabula.convert_into(f"./{DIR_INPUT}/{YEAR}/Nu_{YEAR}-{MONTH}.pdf", f"./{DIR_OUTPUT}/{YEAR}/Nu_{YEAR}-{MONTH}.csv", output_format="csv", pages='all')

## Batch
# tabula.convert_into_by_batch(DIR_INPUT, output_format='csv', pages='all')