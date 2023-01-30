import pandas as pd


def main(paths):
    """to call other function 

    Args:
        paths (list): this list contains 10 csv file path
    """  
    
    index = 1
    for path  in paths:
        data = read_csv(path)
        updated = update(data)
        save_csv(data,index)
        index = index +1 

def read_csv(csv_path):
  
  """to read the contain of csv file to keyword read data

  Args:
      csv_path (str): this string (path name)
  Returns:
      Pandas DataFrame : Pandas DataFrame consists of three principal components, the data, rows, and columns. 
  """  
  read_data = pd.read_csv(csv_path) 
  return read_data

def update(update_data):
    """to change the column data value

    Args:
        update_data (Pandas DataFrame): Two dimensional data structure 

    Returns:
       Pandas DataFrame : Pandas DataFrame consists of three principal components, the data, rows, and columns. 
    """    
    update_data['college'] = update_data['college'].replace({"dlihe" :"Dlihe"})
    return update_data

def save_csv(data,index):
  """write udate DataFrame to new csv file

  Args:
      data (Pandas DataFrame): Two Dimensional data stucture 
      index (int): number of range 1-10
  """  
  data.to_csv(f"updated_new_csv/updated{index}_csv.csv")


if __name__ == "__main__":
    paths =[
      "./csv_data/csv_file1.csv",
      "./csv_data/csv_file2.csv",
      "./csv_data/csv_file3.csv",
      "./csv_data/csv_file4.csv",
      "./csv_data/csv_file5.csv",
      "./csv_data/csv_file6.csv",
      "./csv_data/csv_file7.csv",
      "./csv_data/csv_file8.csv",
      "./csv_data/csv_file9.csv",
      "./csv_data/csv_file10.csv",
    ]
    main(paths)

