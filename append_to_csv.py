import pandas as pd
from pathlib import Path
from csv import writer
def append_csv(csv1):
    list= pd.read_csv(csv1)

    with open('./csv_data/event.csv', 'a') as f_object:
        writer_object = writer(fs_object)
        writer_object.writerow(list[])
        #f_object.close()
        return

csv1 = Path("./csv_data/csv_file3.csv")
append_csv(csv1)