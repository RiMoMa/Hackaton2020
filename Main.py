## organizar datos en pandas
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
names = ['id','email','first_name',
                        'last_name','phone','birthdate',
                        'gender','identification_type',
                        'identification_number','country_birth',
                        'city','education_level','salary',
                        'profile_description','without_experience',
                        'without_studies','title_or_profession',
                        'available_to_move','civil_status',
                        'has_video','studies','experiences',
                        'psy_tests']

df = pd.read_csv('DataHackaton/Candidates.csv',
                 names=names)
