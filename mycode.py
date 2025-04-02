import pandas as pd
import os

data = {'Name': ['Avinash Gawai','Vishal Bahadure','Roshan Yadav','Vikas Pawar','Mayur Sangale','Anurag Fengade'],
        'Age' : [21,23,22,23,22,21],
        'City': ['Chikhali','Nanded','Uttar Pradesh','Lasur','Vidarbha','Lonar']}
df= pd.DataFrame(data=data)
print(df)
    
data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir,'simple_data.csv')

df.to_csv(file_path,index=False)

print(f"CSV file Saved to {file_path}")