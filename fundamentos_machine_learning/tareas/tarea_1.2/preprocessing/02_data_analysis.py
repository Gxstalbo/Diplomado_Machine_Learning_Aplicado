import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
import numpy as np

os.chdir(r"C:\Users\gpvel\OneDrive\Escritorio\Diplomado_Machine_Learning_Aplicado\fundamentos_machine_learning\tareas\tarea_1.2")

df_fifa=pd.read_csv(r"datasets\files\output\fifa_dataset_clean.csv", sep=",", index_col="sofifa_id", encoding="utf8", usecols=['sofifa_id','overall','potential','value_eur','wage_eur',
'age','height_cm','weight_kg','club_team_id','league_level','nationality_id','weak_foot','skill_moves',
'international_reputation','pace','shooting','passing','dribbling','defending','attacking_crossing','attacking_finishing','attacking_heading_accuracy','attacking_short_passing','attacking_volleys','skill_dribbling','skill_curve','skill_fk_accuracy','skill_long_passing','skill_ball_control','movement_acceleration',
'movement_sprint_speed','movement_agility','movement_reactions','movement_balance','power_shot_power','power_jumping','power_stamina','power_strength','power_long_shots','mentality_aggression','mentality_interceptions','mentality_positioning','mentality_vision','mentality_penalties','defending_marking_awareness','defending_standing_tackle','defending_sliding_tackle','goalkeeping_diving',
'goalkeeping_handling','goalkeeping_kicking','goalkeeping_positioning','goalkeeping_reflexes','goalkeeping_speed','FIFA_YEAR','fl_national_selected'])

#club_name,league_name,club_position,preferred_foot,work_rate,'body_type'

X=df_fifa.drop('fl_national_selected',axis=1)
y=df_fifa['fl_national_selected']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3, random_state=0)

hyperparameters = [{'max_depth': [1, 2, 5, 10, 20,25,30], 'criterion': ['gini', 'entropy']}]
tree = GridSearchCV(DecisionTreeClassifier(), hyperparameters)
tree.fit(X_train, y_train)
predicted = tree.predict(X_test)
print(f' Matríz de confusión: \n {metrics.confusion_matrix(y_test, predicted)}')
print(f' Accuracy:  {metrics.balanced_accuracy_score(y_test, predicted)}')

