import pandas as pd
import re
#s = "This cost $350 but i can sell it for 300"
random_data = pd.read_fwf('random_para.txt')
random_data  = re.sub("[$,0-9]", "", str(random_data ))
print (random_data )
#random_data.to_fwf('data/new_randon_para.txt')
random_data.to_fwf(r'data/new_random.txt', str(df.values))