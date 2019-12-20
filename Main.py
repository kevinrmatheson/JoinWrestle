import pandas as pd
data1 = pd.read_csv(r"C:\Users\Kevin\PycharmProjects\JoinWrestle\venv\Wrestle_Comm_Scores_Dec.xlsx.csv")
data2 = pd.read_csv(r"C:\Users\Kevin\PycharmProjects\JoinWrestle\venv\WE WANT LIST PULL 12-3-2019 - RAW PULL-KM EDIT.csv")


d2names = data2['First Name :: General'] + " " + data2['Last Name :: General']
data2['Name'] = d2names

result = pd.merge(data2, data1, on = 'Name', how = 'left')

result.to_csv('MergedWrestlerComms.csv')

