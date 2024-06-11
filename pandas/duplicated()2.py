import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby(by='class')['student'].nunique()  # nunique() 统计不相同元素的总个数
    print(df[df >= 5].reset_index()[['class']])
    return df[df >= 5]
    # print(courses[courses.groupby(by='class')['class'].transform('count') >= 5].drop_duplicates(subset='class')[['class']])


data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'], ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student':'object', 'class':'object'})

find_classes(courses)
