from uuid import uuid4
from random import randint
import pandas as pd
num_people = 10
names = [
    'Olivia',
    'Emma',
    'Charlotte',
    'Amelia',
    'Ava',
    'Sophia',
    'Isabella',
    'Mia',
    'Evelyn',
    'Harper']
ids = [uuid4() for i in range(num_people)]
roles =  [
    'painter',
    'cook',
    'police officer',
    'programmer',
    'it help desk',
    'doctor',
    'scientist',
    'sales',
    'technician',
    'ceo'
]
ages = [randint(20,59) for i in range(10)]
all_companies = ['Google', 'Yahoo', 'Bing']
companies = [all_companies[randint(0,len(all_companies)-1)] for i in range(num_people)]

d1 = dict(names=names,ids=ids,roles=roles,ages=ages,companies=companies)
df = pd.DataFrame(d1)
# print(df)
print(df.melt(id_vars=df.columns[1:3], var_name='Position', value_name='Value'))
# print(df.melt(id_vars='names'))
