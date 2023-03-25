import pandas as pd
from sqlalchemy import create_engine

rawData = pd.read_csv('P:\\OEE_Dashboard\\stencil\\StencilBulkUpload.csv')


df = pd.DataFrame(rawData)
print(df)


#SQL Connection Windows Authentication#

# Server = 'UKC-VM-SQL01'
# Database = 'ToolBank'
# Driver = 'ODBC Driver 17 for SQL Server'
# Database_con = f'mssql://@{Server}/{Database}?driver={Driver}'

# engine = create_engine(Database_con)
# con = engine.connect()

# df.to_sql('Stencil_Bank', con, if_exists='append', index = False)

#Fin#
print('Program Complete')


