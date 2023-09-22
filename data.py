import csv
import glob
import pandas as pd
from mammal import *
from reptile import *
from poultry import *
    
def writeDict(data,filename) :
    data_str = ""
    for name in data :
        data_str += "'"+name+"':''"+","

    with open(filename+'.txt', 'w', encoding="UTF-8") as dt:
        dt.write(data_str)

def animal_question(animalType,data,data_food) :
    with open(animalType+'.csv', 'w', newline='',encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Class", "Question", "Answer"])
        for name in data :
            writer.writerow(["Animal", f"{name}", f"ที่นี่มี{name}ค่ะ"])
            writer.writerow(["Animal", f"มี{name}ไหม", f"ที่นี่มี{name}ค่ะ"])
            writer.writerow(["Animal", f"มี{name}ไหมอ่ะ", f"ที่นี่มี{name}ค่ะ"])
            writer.writerow(["Animal", f"มี{name}ไหมหรือเปล่า", f"ที่นี่มี{name}ค่ะ"])
            writer.writerow(["Animal", f"มี{name}ป้ะ", f"ที่นี่มี{name}ค่ะ"])
            
            writer.writerow(["Animal", f"{name}กินอะไร", f"{data_food[name]}"])
            writer.writerow(["Animal", f"{name}กินไรอ่ะ", f"{data_food[name]}"])
            writer.writerow(["Animal", f"{name}กินราย", f"{data_food[name]}"])
            writer.writerow(["Animal", f"{name}กินไอไหร", f"{data_food[name]}"])
            writer.writerow(["Animal", f"{name}กินไร", f"{data_food[name]}"])


def schedule_question(scheduleType,data) :
    with open(scheduleType+'.csv', 'w', newline='',encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Class", "Question", "Answer"])
        for time in data :
            writer.writerow(["Schedule", f"{time}เปิดกี่โมง", f"ที่นี่เปิดทุกวันเวลา 08:00 ค่ะ"])
            writer.writerow(["Schedule", f"{time}ปิดกี่โมง", f"ที่นี่ปิดเวลา 17:00 ค่ะ"])
        writer.writerow(["Schedule", f"เปิดกี่โมง", f"ที่นี่เปิดทุกวัน 08:00 ค่ะ"])
        writer.writerow(["Schedule", f"ปิดกี่โมง", f"ที่นี่ปิดเวลา 17:00 ค่ะ"])
        writer.writerow(["Schedule", f"เปิดปิดกี่โมง", f"ที่นี่เปิดเวลา 08:00-17:00 ค่ะ"])
        writer.writerow(["Schedule", f"เปิด-ปิดกี่โมง", f"ที่นี่เปิดเวลา 08:00-17:00 ค่ะ"])


def price_question(priceType,data,data_price,price) :
    with open(priceType+'.csv', 'w', newline='',encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Class", "Question", "Answer"])
        for age in data :
            writer.writerow(["Price", f"บัตร{age}", f"{data_price[age]}ค่ะ"])
            writer.writerow(["Price", f"{age}กี่บาท", f"{data_price[age]}ค่ะ"])
            writer.writerow(["Price", f"ราคาเข้า{age}", f"{data_price[age]}ค่ะ"])
            writer.writerow(["Price", f"บัตร{age}เท่าไร", f"{data_price[age]}ค่ะ"])
            writer.writerow(["Price", f"ค่าเข้า{age}เท่าไร", f"{data_price[age]}ค่ะ"])
        writer.writerow(["Price", f"ค่าเข้า", f"{price}"])
        writer.writerow(["Price", f"ค่าเข้ากี่บาท", f"{price}"])
        writer.writerow(["Price", f"ราคาบัตร", f"{price}"])
        writer.writerow(["Price", f"บัตรเข้ากี่บาท", f"{price}"])
        writer.writerow(["Price", f"บัตรเข้าสวนสัตว์กี่บาท", f"{price}"])
        writer.writerow(["Price", f"ราคาเข้า", f"{price}"])
        writer.writerow(["Price", f"บัตรเข้าราคา", f"{price}"])


def activities_question(priceType,data,data_activities) :
    with open(priceType+'.csv', 'w', newline='',encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Class", "Question", "Answer"])
        for activities in data :
            writer.writerow(["Activities", f"", f""])

def merge(output_filename="merged_data.csv"):
    csv_files = glob.glob('*.csv')
    
    dfs = []

    for file in csv_files:
        df = pd.read_csv(file, encoding="UTF-8")
        dfs.append(df)
    
    all_data = pd.concat(dfs, ignore_index=True)
    all_data.to_csv(output_filename, index=False, encoding="UTF-8")


# animal_question("reptile",reptile,reptile_food)
# animal_question("mammal",mammal,mammal_food)
# animal_question("poultry",poultry,poultry_food)
# merge("all_animal.csv")

