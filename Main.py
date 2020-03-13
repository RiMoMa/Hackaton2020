## organizar datos en pandas
import os
import numpy as np
import ast
from unidecode import unidecode
from sklearn.feature_extraction.text import CountVectorizer
from stop_words import get_stop_words
stop_words = get_stop_words('spanish')
import pandas as pd
import plot_commun_words
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# Load the regular expression library
import re# Remove punctuation
import num2words
from sklearn.feature_extraction.text import CountVectorizer
from GenderIdentify import GenderIdentify
from gender_features import gender_features
import math

##### PREPROCESAMIENTO #############
######### PARA: CANDIDATES.CSV ##########


Candidates_cols = ['id',
                   'email',
                   'first_name',
                   'last_name',
                   'phone',
                   'birthdate',
                   'gender',
                   'identification_type',
                   'identification_number',
         'country_birth',
         'city',
         'education_level',
         'salary',
         'profile_description',
         'without_experience',  #binaria
         'without_studies',  #binaria
         'title_or_profession',  #Caracteres
         'available_to_move',  # binaria
         'civil_status',  #multiclase
         'has_video',  # Imágenes
         'studies',  # Caracteres
         'experiences',
                   # arreglo tipo "company":"Fabrica 1","position":"Nombre posicion en 1","start_date":"time_stamp","end_date":"2010-10-01", "at_present":binaria True False,"description":"","Job_functions":,end_date,"withdrawal_reason":null,"other_withdrawal_reason":null}

         'psy_tests',
                   ]

if not(os.path.exists('DataHackaton/Candidates2.csv')):

    text = open("DataHackaton/Candidates.csv", "r")
    text = ''.join([i for i in text]) \
        .replace("false", "False")\
        .replace("null","0")
    x = open("DataHackaton/Candidates2.csv","w")
    x.writelines(text)
    x.close()

DF_Candidates = pd.read_csv('DataHackaton/Candidates2.csv',
                 names=Candidates_cols)


Remover_innecesarios = ['email',
                        #'first_name',
                        'last_name',
                        'phone',
                        'identification_number',
                        'identification_type',
                        ]


DF_Candidates = DF_Candidates.drop(Remover_innecesarios,axis=1)
DF_Candidates['salary'] = DF_Candidates['salary'].astype(str)

########### poner edad y reemplazar bird date por numero de dias ############

time_min = pd.Timestamp.min.year
time_max = pd.Timestamp.max.year
print(time_max)
print(time_min)
Gd = GenderIdentify()
for n in range(DF_Candidates.index.stop):
   # print(DF_Candidates['birthdate'][n])
    ## Calcular Edad
    if DF_Candidates['birthdate'][n] is float(np.nan):
        edad = 'NoEdad'
    elif float(DF_Candidates['birthdate'][n][0:4])>time_min and float(DF_Candidates['birthdate'][n][0:4])<time_max:
        edad = pd.Timestamp.now() - pd.Timestamp(DF_Candidates['birthdate'][n])
        edad = num2words.num2words( np.round( edad.days/365 ),lang = 'es')

    else:
        #print(n)
        edad = 'NoEdad'
    DF_Candidates.at[n, 'birthdate'] = edad

      ## completar Genero
    if DF_Candidates['gender'][n] is float(np.nan):
        genderClassify = Gd.classify(gender_features(DF_Candidates['first_name'][n]))
        DF_Candidates.at[n, 'gender'] = genderClassify


  ##completar salario
    if math.isnan(float(DF_Candidates['salary'][n])):
        SalaryToWord = 'NoSalary'
    else:
        SalaryToWord = num2words.num2words(DF_Candidates['salary'][n],lang = 'es')

    DF_Candidates.at[n, 'salary'] = SalaryToWord

DF_Candidates2 = DF_Candidates.rename(columns={'birthdate':'edad'})
DF_Candidates2 = DF_Candidates2.set_index(['id'])

### para organizar los datos por candidato
#data =DF_Candidates2['studies'][6]
#res = ast.literal_eval(data[1:-1])
#StudiosC = pd.DataFrame(res)








######### PARA: VACANTS.CSV ##########


Vacants_cols = [
         'id',
         'title',
         'description',
         'salary_type',
         'min_salary',
         'max_salary',
         'status',
         'created_at',
         'company',
         'education_level',
         'agree',
         'requeriments',
         'publish_date',
         'confidential',
         'expiration_date',
         'experience_and_positions',
         'knowlede_and_skills',
         'titles_and_studies',
         'number_of_quotas'
         ]

if not(os.path.exists("DataHackaton/Vacants2.csv")):

    text = open("DataHackaton/Vacants.csv", "r")
    text = ''.join([i for i in text]) \
        .replace("false", "False")\
        .replace("null","None")
    x = open("DataHackaton/Vacants2.csv","w")
    x.writelines(text)
    x.close()

DF_Vacants = pd.read_csv('DataHackaton/Vacants2.csv',
                 names=Vacants_cols)


Remover_innecesarios = ['salary_type',
                        'created_at',
                        'publish_date',
                        'expiration_date',
                        'number_of_quotas'
                        ]


DF_Vacants2 = DF_Vacants.drop(Remover_innecesarios,axis=1)
DF_Vacants2 = DF_Vacants2.set_index(['id'])





######### PARA: STAGES.CSV ##########


Stages_cols = [
    'id',
    'title',
    'send_sms',
    'send_email',
    'send_call',
    'stage_type',
    'vacant_id',
    'stage_order'

         ]

if not(os.path.exists("DataHackaton/Stages2.csv")):

    text = open("DataHackaton/Stages.csv", "r")
    text = ''.join([i for i in text]) \
        .replace("false", "False")\
        .replace("null","None")
    x = open("DataHackaton/Stages2.csv","w")
    x.writelines(text)
    x.close()

DF_Stages = pd.read_csv('DataHackaton/Stages2.csv',
                 names=Stages_cols)


Remover_innecesarios = [
                        'send_sms',
                        'send_email',
                        'send_call'

                        ]


DF_Stages2 = DF_Stages.drop(Remover_innecesarios,axis=1)
DF_Stages2 = DF_Stages2.set_index(['vacant_id'])## ojo, vacant_id






######### PARA: Applications.CSV ##########


Applications_cols = [
    'id',
    'vacant_id',
    'candidate_id',
    'created_at',
    'status',
    'discard_type'
]


if not(os.path.exists("DataHackaton/Applications2.csv")):
    text = open("DataHackaton/Applications.csv", "r")
    text = ''.join([i for i in text]) \
        .replace("false", "False")\
        .replace("null","None")
    x = open("DataHackaton/Applications2.csv","w")
    x.writelines(text)
    x.close()

DF_Applications = pd.read_csv('DataHackaton/Applications2.csv',
                 names=Applications_cols)


Remover_innecesarios = [#'id',
                        #'vacant_id',
                      #  'candidate_id',
                        'created_at'
                      #  'status',
                      #  'discard_type'
                        ]


DF_Applications2 = DF_Applications.drop(Remover_innecesarios,axis=1)
DF_Applications2 = DF_Applications2.set_index(['id'])


########


######### PARA: ApplicationStages.CSV ##########


Stages_cols = ['id',
               'stage_id',
               'application_id',
               'created_at',
               'status'

               ]

if not(os.path.exists("DataHackaton/ApplicationStages2.csv")):

    text = open("DataHackaton/ApplicationStages.csv", "r")
    text = ''.join([i for i in text]) \
        .replace("false", "False") \
        .replace("null", "None")
    x = open("DataHackaton/ApplicationStages2.csv", "w")
    x.writelines(text)
    x.close()

DF_ApplicationStages = pd.read_csv('DataHackaton/ApplicationStages2.csv',
                              names=Stages_cols)

Remover_innecesarios = [#'id',
            #   'stage_id',
            #   'application_id',
               'created_at',
             #  'status'
               ]
DF_ApplicationStages2 = DF_ApplicationStages.drop(Remover_innecesarios, axis=1)
DF_ApplicationStages2 = DF_ApplicationStages2.set_index(['application_id'])
DF_ApplicationStages2 = DF_ApplicationStages2.sort_index(axis = 0)
########








### Generar relaciones entre los datos -- Stage con id Vacant--


####### AQUI VA LA APLICACION DE LA BOLSA DE PALABRAS #######

DF_Vacants2['paper_text_processed'] = DF_Candidates2['studies'].map(lambda x: re.sub('[,\.!?·:#()]',' ', str(x)))# Convert the titles to lowercase
DF_Vacants2['paper_text_processed'] = DF_Vacants2['paper_text_processed'].map(lambda x: re.sub('[&]','', str(x)))# eliminar &
DF_Vacants2['paper_text_processed'] = DF_Vacants2['paper_text_processed'].map(lambda x: re.sub('[;]','', str(x)))#eliminar ;
DF_Vacants2['paper_text_processed'] = DF_Vacants2['paper_text_processed'].map(lambda x: re.sub('<[^<]+?>',' ', str(x)))#eliminar HTML
DF_Vacants2['paper_text_processed'] = DF_Vacants2['paper_text_processed'].apply(unidecode)
DF_Vacants2['paper_text_processed'] = DF_Vacants2['paper_text_processed'].map(lambda x: re.sub('{|acute|}','', str(x)))
DF_Vacants2['paper_text_processed'] = DF_Vacants2['paper_text_processed'].map(lambda x: re.sub('{|tilde|}','', str(x)))
DF_Vacants2['paper_text_processed'] = DF_Vacants2['paper_text_processed'].map(lambda x: re.sub('{|nbsp|}','', str(x)))
DF_Vacants2['paper_text_processed'] = DF_Vacants2['paper_text_processed'].map(lambda x: re.sub('{|iquest|}','', str(x)))
DF_Vacants2['paper_text_processed'] = DF_Vacants2['paper_text_processed'].map(lambda x: re.sub('{|13|}','', str(x)))


#DF_Vacants2['paper_text_processed'] = DF_Vacants2['paper_text_processed'].map(lambda x: re.sub('[?P=ntilde]',' ', str(x)))
DF_Vacants2['paper_text_processed'] = DF_Vacants2['paper_text_processed'].map(lambda x: x.lower())# Print out the first rows of papers
DF_Vacants2['paper_text_processed'].head()

# Import the wordcloud library

from wordcloud import WordCloud# Join the different processed titles together.
long_string = ','.join(list(DF_Vacants2['paper_text_processed'].values))# Create a WordCloud object
wordcloud = WordCloud(background_color="white", max_words=5000, contour_width=3, contour_color='steelblue')# Generate a word cloud
wordcloud.generate(long_string)# Visualize the word cloud
wordcloud.to_image()

count_vectorizer = CountVectorizer(stop_words=stop_words)
count_data = count_vectorizer.fit_transform(DF_Vacants2['paper_text_processed'])
plot_common_words(count_data, count_vectorizer,80,160)

print('Fin')
