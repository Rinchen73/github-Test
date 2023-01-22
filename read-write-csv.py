
import pandas as pd
  
student_list= pd.read_csv('data/stu-list.csv')
  # removing last line for data/stu-list.csv
student_list= student_list.iloc[:-1]
  # printing modified data/stu-list.csv 
print(student_list)
    #saving update info into new csv file
student_list.to_csv('data/new-stu-list.csv')