import pandas as pd

df = pd.read_csv('E:/Musaddiq/Python//Mini_Projects/project_scores.csv')

python_scores = df['Python_Score']

mean_python = python_scores.mean()
print("Mean Python Score:", mean_python)

print("\nFirst 3 rows of the DataFrame:")
print(df.head(3))

print("\nName and ML_Score columns:")
print(df[['Name', 'ML_Score']])

df['Total_Score'] = df[['Python_Score', 'ML_Score', 'AI_Score']].fillna(0).sum(axis=1)

df.fillna(0, inplace=True)

df['Result'] = df['Total_Score'].apply(lambda x: 'Pass' if x >= 240 else 'Fail')

passed_cs_students = df[(df['Department'] == 'CS') & (df['Result'] == 'Pass')]
print("\nPassed CS Students:")
print(passed_cs_students)

df_sorted = df.sort_values(by='Total_Score', ascending=False)

df_sorted.to_csv('final_results.csv', index=False)

print("\nFinal cleaned DataFrame saved as 'final_results.csv'")
