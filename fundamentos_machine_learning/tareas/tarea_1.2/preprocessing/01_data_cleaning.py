import pandas as pd
import os

os.chdir(r"C:\Users\gpvel\OneDrive\Escritorio\Diplomado_Machine_Learning_Aplicado\fundamentos_machine_learning\tareas\tarea_1.2")
df_fifa= pd.read_csv(r"datasets\files\intermedia\fifa_dataset.csv", sep=",",index_col="sofifa_id")

df_fifa.shape
df_fifa.head()

#Eliminaremos filas que sean una URL
for column in df_fifa:
    if column.endswith("_url"):
        del(df_fifa[column])

# Check NaN values
df_fifa.columns[df_fifa.isnull().sum()>0]

# Debemos hacernos cargo de los NaN que sí tienen sentido
#Jugador no fue transferido
df_fifa['club_loaned_from'].fillna("None", inplace=True)
df_fifa['club_joined'].fillna("None", inplace=True)
df_fifa['league_level'].fillna(df_fifa['league_level'].median(), inplace=True)

#Jugador no tiene numero porque no fue convocado a la selección
df_fifa['player_tags'].fillna("None", inplace=True)
df_fifa['player_traits'].fillna("None", inplace=True)

df_release=df_fifa[df_fifa['release_clause_eur'].notnull()]

factor_release=df_release['release_clause_eur'].median()/df_release['value_eur'].median()

df_fifa['release_clause_eur']=df_fifa.apply(lambda row: factor_release*row['value_eur'] if pd.isnull(row['release_clause_eur']) else row['release_clause_eur'], axis=1)
df_fifa['fl_national_selected']= df_fifa['nation_jersey_number'].apply(lambda x: 1 if pd.notnull(x) else 0)

df_fifa['fl_national_selected'].value_counts()

del df_fifa['nation_position']
del df_fifa['nation_team_id']
del df_fifa['nation_jersey_number']

df_fifa['passing'] = df_fifa.apply(lambda row: 0 if (row['player_positions']=='GK') & pd.isnull(row['passing']) else row['passing'] , axis=1)
df_fifa['dribbling'] = df_fifa.apply(lambda row: 0 if (row['player_positions']=='GK') & pd.isnull(row['dribbling']) else row['dribbling'] , axis=1)
df_fifa['defending'] = df_fifa.apply(lambda row: 0 if (row['player_positions']=='GK') & pd.isnull(row['defending']) else row['defending'] , axis=1)
df_fifa['shooting'] = df_fifa.apply(lambda row: 0 if (row['player_positions']=='GK') & pd.isnull(row['shooting']) else row['shooting'] , axis=1)
df_fifa['pace'] = df_fifa.apply(lambda row: 0 if (row['player_positions']=='GK') & pd.isnull(row['pace']) else row['pace'] , axis=1)
df_fifa['goalkeeping_speed'].fillna(0, inplace=True)

del df_fifa['physic']
del df_fifa['mentality_composure']

#Se pierden aprox 2000 datos
df_fifa.dropna(inplace=True)

df_fifa.to_csv(r"datasets\files\output\fifa_dataset_clean.csv", sep=",", index=True)
