import pandas as pd
import glob
import sqlite3

print(glob.glob("data/*.csv"))
# create dataframe to write to
all_data = pd.DataFrame()
# columns I want to keep
columns = ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC','AC','HY','AY','HR','AR',
            'B365H', 'B365D', 'B365A']

#loop through all CSVs and combine
for file in glob.glob("data/*.csv"):
    df = pd.read_csv(file)
    df = df[columns]
    all_data = all_data.append(df, ignore_index=True)

#Write to an Excel file (automatically overwrites)
# with pd.ExcelWriter("output.xlsx") as writer:
#     all_data.to_excel(writer, index=False)

# Write combined dataframe to SQL Database
conn = sqlite3.connect('EPL.db')
all_data.to_sql('PremTable', conn, if_exists='replace', index=False)
