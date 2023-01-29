import pandas as pd


file_path = "data/chat.txt"

with open(file_path, mode='r', encoding="utf8") as f:
    data = f.readlines()

dataset = data[1:]
data_nqya = []

#print(dataset)

for line in dataset:
    
    if '/' in line and ':' in line and ',' in line and '-' in line:

        date = line.split(",")[0]
        line2 = line[len(date):]
        time = line2.split("-")[0][2:]
        line3 = line2[len(time):]
        name = line3.split(":")[0][4:]
        line4 = line3[len(name):]
        message = line4[6:-1]
        data_nqya.append([date, time, name, message])

    else:
        new = data_nqya[-1][-1] + " " + line
        data_nqya[-1][-1] = new

#save to excel xlsx
df = pd.DataFrame(data_nqya, columns = ['Date', 'Time', 'Name', 'Message'])
df.to_excel('chat_history.xlsx', index=False)

