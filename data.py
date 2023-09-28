import csv
import glob
import pandas as pd
import os, sys
    
def writeDict(data,filename) :
    data_str = ""
    for name in data :
        data_str += "'"+name+"':''"+","

    with open(filename+'.txt', 'w', encoding="UTF-8") as dt:
        dt.write(data_str)


def big_class() :
    return "KEY"


def animal_question(animalType,data,data_food) :
    with open(animalType+'.csv', 'w', newline='',encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Animal", "Question", "Answer"])
        for name in data :
            writer.writerow([animalType, f"{name}", f"ที่นี่มี{name}ค่ะ"])
            writer.writerow([animalType, f"มี{name}ไหม", f"ที่นี่มี{name}ค่ะ"])
            writer.writerow([animalType, f"มี{name}ไหมอ่ะ", f"ที่นี่มี{name}ค่ะ"])
            writer.writerow([animalType, f"มี{name}ไหมหรือเปล่า", f"ที่นี่มี{name}ค่ะ"])
            writer.writerow([animalType, f"มี{name}ป้ะ", f"ที่นี่มี{name}ค่ะ"])
            
            writer.writerow([animalType, f"{name}กินอะไร", f"{data_food[name]}"])
            writer.writerow([animalType, f"{name}กินไรอ่ะ", f"{data_food[name]}"])
            writer.writerow([animalType, f"{name}กินราย", f"{data_food[name]}"])
            writer.writerow([animalType, f"{name}กินไอไหร", f"{data_food[name]}"])
            writer.writerow([animalType, f"{name}กินไร", f"{data_food[name]}"])


def schedule_question(scheduleType,data,ans) :
    with open(scheduleType+'.csv', 'w', newline='',encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Class", "Question", "Answer"])
        for time in data :
            writer.writerow(["Schedule", f"{time}เปิดกี่โมง", f"{ans[0]}"])
            writer.writerow(["Schedule", f"{time}ปิดกี่โมง", f"{ans[0]}"])
        writer.writerow(["Schedule", f"เปิดกี่โมง", f"{ans[0]}"])
        writer.writerow(["Schedule", f"ปิดกี่โมง", f"{ans[0]}"])
        writer.writerow(["Schedule", f"เปิดปิดกี่โมง", f"{ans[0]}"])
        writer.writerow(["Schedule", f"เปิด-ปิดกี่โมง", f"{ans[0]}"])


def price_question(priceType,data,price) :
    with open(priceType+'.csv', 'w', newline='',encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Class", "Question", "Answer"])
        for age in data :
            writer.writerow(["Price", f"บัตร{age}", f"{price}ค่ะ"])
            writer.writerow(["Price", f"{age}กี่บาท", f"{price}ค่ะ"])
            writer.writerow(["Price", f"ราคาเข้า{age}", f"{price}ค่ะ"])
            writer.writerow(["Price", f"บัตร{age}เท่าไร", f"{price}ค่ะ"])
            writer.writerow(["Price", f"ค่าเข้า{age}เท่าไร", f"{price}ค่ะ"])
        writer.writerow(["Price", f"ค่าเข้า", f"{price}"])
        writer.writerow(["Price", f"ค่าเข้ากี่บาท", f"{price}"])
        writer.writerow(["Price", f"ราคาบัตร", f"{price}"])
        writer.writerow(["Price", f"บัตรเข้ากี่บาท", f"{price}"])
        writer.writerow(["Price", f"บัตรเข้าสวนสัตว์กี่บาท", f"{price}"])
        writer.writerow(["Price", f"ราคาเข้า", f"{price}"])
        writer.writerow(["Price", f"บัตรเข้าราคา", f"{price}"])
        writer.writerow(["Price", f"เท่าไร", f"{price}"])


def activities_question(activitiesType,data,data_activities) :
    with open(activitiesType+'.csv', 'w', newline='',encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Class", "Question", "Answer"])
        for activities in data :
            writer.writerow(["Activities", f"{activities}", f"{data_activities}"])
            writer.writerow(["Activities", f"มี{activities}อะไรบ้าง", f"{data_activities}"])
        writer.writerow(["Activities", f"รอบการแสดง", f"{data_activities}"])
        writer.writerow(["Activities", f"ขอดูรอบการแสดงหน่อย", f"{data_activities}"])
            

def merge(output_filename="merged_data.csv"):
    csv_files = glob.glob('*.csv')
    
    dfs = []

    for file in csv_files:
        df = pd.read_csv(file, encoding="UTF-8")
        dfs.append(df)
    
    all_data = pd.concat(dfs, ignore_index=True)
    all_data.to_csv(output_filename, index=False, encoding="UTF-8")

def clear() :
    all_csv = glob.glob('*.csv')
    all_txt = glob.glob('*.txt')
    for data in all_csv :
        os.remove(data)

    for data in all_txt :
        os.remove(data)

def openfile() :
    readme = os.open("README.txt", os.O_RDWR|os.O_CREAT)  
    os.close(readme)

# clear()

# animal_question("reptile",reptile,reptile_food)
# animal_question("mammal",mammal,mammal_food)
# animal_question("poultry",poultry,poultry_food)
# merge("all_animal.csv")

