import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie','Max', 'Bobby', 'Chintu','Eva', 'Juilet', 'Pintu', 'Vaibhav'],

    'Subject':['Maths', 'Maths', 'Chem', 'Chem', 'Physics', 'Physics', 'CS', 'CS', 'Maths', 'Physics'],

    'Score': [50, 52, 75, 60, 99, 87, 67, 59, 69, 99],

}

df=pd.DataFrame(data)

grades = []
for score in df['Score']:
    if score >= 90:
        grades.append('A')
    elif score >= 80:
        grades.append('B')
    elif score >= 70:
        grades.append('C')
    elif score >= 60:
        grades.append('D')
    else:
        grades.append('F')

df['Grade'] = grades

sorted = df.sort_values(by='Score', ascending=False)
grouped = df.groupby('Subject')['Score'].mean()

print(sorted)
print(grouped)

def pandas_filter_pass(dataframe):
    names = []
    subjects = []
    scores = []
    grades = []

    for i in range(len(dataframe)):
        grade = dataframe.loc[i, 'Grade']
        if grade == 'A' or grade == 'B':
            names.append(dataframe.loc[i, 'Name'])
            subjects.append(dataframe.loc[i, 'Subject'])
            scores.append(dataframe.loc[i, 'Score'])
            grades.append(grade)

    new_df = pd.DataFrame({
        'Name': names,
        'Subject': subjects,
        'Score': scores,
        'Grade': grades
    }
)
    return new_df

pandas_filter_pass(df)

filtered_df = pandas_filter_pass(df)
print(filtered_df)