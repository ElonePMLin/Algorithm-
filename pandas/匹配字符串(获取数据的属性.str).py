import pandas as pd
import re


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # DIAB1
    print(patients[patients['conditions'].str.contains("^DIAB1.*|.* DIAB1.*")])


data = [[1, 'Daniel', 'YFEV COUGH'], [2, 'Alice', ''], [3, 'Bob', 'DIAB100 MYOP'], [4, 'George', 'ACNE DIAB100'], [5, 'Alain', 'DIAB201']]
patients = pd.DataFrame(data, columns=['patient_id', 'patient_name', 'conditions']).astype({'patient_id':'int64', 'patient_name':'object', 'conditions':'object'})
find_patients(patients)
