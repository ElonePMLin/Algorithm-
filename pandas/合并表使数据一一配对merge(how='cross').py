import pandas as pd


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df = students.merge(subjects, how="cross")
    exam = examinations.groupby(by=["student_id", "subject_name"])["subject_name"].size().reset_index(name="attended_exams")
    return exam.merge(df, on=["student_id", "subject_name"], how="right").fillna({"attended_exams": 0}).sort_values(by=["student_id", "subject_name"], ascending=True)[["student_id", "student_name", "subject_name", "attended_exams"]]

    # pd.DataFrame(students.values, subjects.values)
    # print(students.info)


data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]
students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype({'student_id':'Int64', 'student_name':'object'})
data = [['Math'], ['Physics'], ['Programming']]
subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name':'object'})
data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'], [13, 'Math'], [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype({'student_id':'Int64', 'subject_name':'object'})


students_and_examinations(students, subjects, examinations)


