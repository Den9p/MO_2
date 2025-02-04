import pandas as pd

df = pd.read_csv('stackoverflow_full.csv')

pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', None)


df.drop(columns=['Unnamed: 0'], inplace=True)

df['Age'] = df['Age'].apply(lambda x: 1 if x == '<35' else 0)
df.rename(columns={'Age': '<35 Years'}, inplace=True)

df['Accessibility'] = df['Accessibility'].apply(lambda x: 1 if x == 'Yes' else 0)

#Зависимость от уровня образования ???? - Обсудить
education_mapping = {
    'NoHigherEd': 0,
    'Undergraduate': 1,
    'Master': 2,
    'PhD': 3,
    'Other': 4
}
df['EdLevel'] = df['EdLevel'].map(education_mapping)

#Может категорию NonBinary удалить? - Обсудить
df = pd.get_dummies(df, columns=['Gender'], prefix='Gender')

df['MentalHealth'] = df['MentalHealth'].apply(lambda x: 1 if x == 'Yes' else 0)

df['MainBranch'] = df['MainBranch'].apply(lambda x: 1 if x == 'Dev' else 0)

threshold = 500 # Определяем порог для "редких" стран - Обсудить
country_counts = df['Country'].value_counts()
rare_countries = country_counts[country_counts < threshold].index
df['Country'] = df['Country'].apply(lambda x: 'Other' if x in rare_countries else x)
df = pd.get_dummies(df, columns=['Country'], prefix='Country')

technologies = set()
for tech_list in df['HaveWorkedWith'].dropna():
    technologies.update(tech_list.split(';'))
tech_data = {f'Tech_{tech}': df['HaveWorkedWith'].apply(lambda x: 1 if tech in str(x) else 0) for tech in technologies}
tech_df = pd.DataFrame(tech_data)
df = pd.concat([df, tech_df], axis=1)
df.drop(columns=['HaveWorkedWith'], inplace=True)


df.info()
print(df.head())


