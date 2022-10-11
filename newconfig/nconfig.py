from faker import Faker
import pandas as pd
from files import user, employee, company, customer, contact
import os

f = Faker()


def generate_data(records, provider):
    data = []
    for i in range(records):
        if provider == 'id':
            data.append(i)
        else:
            func = getattr(f, provider)
            data.append(func())
    return data


def save_file(data, filename):
    df = pd.DataFrame(data)
    print(df)
    df.to_csv(filename+'.csv', index=False)


folder_path = r'C:\Users\Rehana\PycharmProjects\pythonProject1\newconfig\files'
list_of_files = os.listdir(folder_path)

for lst in list_of_files:
    if lst == '__pycache__':
        continue
    nm = lst.split('.')[0]
    x = eval(nm)

    rec = x.User["Records"]
    # print(rec)
    nm = x.User["Name"]
    x.User.pop("Records")
    x.User.pop("Name")
    new_data = {}
    for key, val in x.User.items():
        column = key.split(".")[-1]
        column_data = generate_data(rec, column)
        new_data[val] = column_data

    save_file(new_data, nm)
