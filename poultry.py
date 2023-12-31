import csv

def PoultryClass(animalType,animal,questions,answers) :
    with open(animalType+'.csv', 'w', newline='',encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow([animalType, "Question", "Answer"])
        for name in animal :
            for question in questions :
                for answer in answers :
                    writer.writerow([animalType, f"{name}{question}", f"{answer}"])



poultry_question = ["อยู่ไหน","มีไหม","หาได้ที่ไหน"]
poultry_answer = ["อยู่ในโซนสัตว์สัตว์ปึกของสวนสัตว์"]

poultry = ["นกกระตั้วดำ","นกกระแตแต้แว๊ด","นกกุลา","นกขมิ้นท้ายทอยดำ","นกค๊อกคาเทล","นกตะกราม","นกตีทอง","นกปรอดสวน","นกปรอดหัวสีเขม่า","นกปรอดหัวโขน","นกปรอดเหลืองหัวจุก",
           "นกปรอดแม่ทะ","นกพิราบหงอนวิคตอเรีย","นกลุมพูเขียว","นกหกเล็กปากดำ","นกเขาเขียว","นกเขาเปล้าธรรมดา","นกเขาใหญ่","นกเขียวก้านตองปีกสีฟ้า","นกเขียวก้านตองใหญ่",
           "นกเขียวคราม","นกเงือกกรามช้าง","นกเงือกหัวแรด","นกเงือกหัวหงอก","นกเพนกวินฮัมโบลด์","นกเอี้ยงหงอน","นกแก้วเอคเลคตัส","นกแต้วแล้วธรรมดา",
           "หงส์ดำ","เป็ดวู๊ด","เป็ดหงส์","เหยี่ยวแดง","นกกระจอกเทศ"]

PoultryClass("Poultry", poultry, poultry_question, poultry_answer)

answers = ["Poultry"]*99
questions = ['นกกระตั้วดำอยู่ไหน','นกกระตั้วดำมีไหม','นกกระตั้วดำหาได้ที่ไหน','นกกระแตแต้แว๊ดอยู่ไหน','นกกระแตแต้แว๊ดมีไหม','นกกระแตแต้แว๊ดหาได้ที่ไหน','นกกุลาอยู่ไหน','นกกุลามีไหม','นกกุลาหาได้ที่ไหน','นกขมิ้นท้ายทอยดำอยู่ไหน','นกขมิ้นท้ายทอยดำมีไหม','นกขมิ้นท้ายทอยดำหาได้ที่ไหน','นกค๊อกคาเทลอยู่ไหน','นกค๊อกคาเทลมีไหม','นกค๊อกคาเทลหาได้ที่ไหน','นกตะกรามอยู่ไหน','นกตะกรามมีไหม','นกตะกรามหาได้ที่ไหน','นกตีทองอยู่ไหน','นกตีทองมีไหม','นกตีทองหาได้ที่ไหน','นกปรอดสวนอยู่ไหน','นกปรอดสวนมีไหม','นกปรอดสวนหาได้ที่ไหน','นกปรอดหัวสีเขม่าอยู่ไหน','นกปรอดหัวสีเขม่ามีไหม','นกปรอดหัวสีเขม่าหาได้ที่ไหน','นกปรอดหัวโขนอยู่ไหน','นกปรอดหัวโขนมีไหม','นกปรอดหัวโขนหาได้ที่ไหน','นกปรอดเหลืองหัวจุกอยู่ไหน','นกปรอดเหลืองหัวจุกมีไหม','นกปรอดเหลืองหัวจุกหาได้ที่ไหน','นกปรอดแม่ทะอยู่ไหน','นกปรอดแม่ทะมีไหม','นกปรอดแม่ทะหาได้ที่ไหน','นกพิราบหงอนวิคตอเรียอยู่ไหน','นกพิราบหงอนวิคตอเรียมีไหม','นกพิราบหงอนวิคตอเรียหาได้ที่ไหน','นกลุมพูเขียวอยู่ไหน','นกลุมพูเขียวมีไหม','นกลุมพูเขียวหาได้ที่ไหน','นกหกเล็กปากดำอยู่ไหน','นกหกเล็กปากดำมีไหม','นกหกเล็กปากดำหาได้ที่ไหน','นกเขาเขียวอยู่ไหน','นกเขาเขียวมีไหม','นกเขาเขียวหาได้ที่ไหน','นกเขาเปล้าธรรมดาอยู่ไหน','นกเขาเปล้าธรรมดามีไหม','นกเขาเปล้าธรรมดาหาได้ที่ไหน','นกเขาใหญ่อยู่ไหน','นกเขาใหญ่มีไหม','นกเขาใหญ่หาได้ที่ไหน','นกเขียวก้านตองปีกสีฟ้าอยู่ไหน','นกเขียวก้านตองปีกสีฟ้ามีไหม','นกเขียวก้านตองปีกสีฟ้าหาได้ที่ไหน','นกเขียวก้านตองใหญ่อยู่ไหน','นกเขียวก้านตองใหญ่มีไหม','นกเขียวก้านตองใหญ่หาได้ที่ไหน','นกเขียวครามอยู่ไหน','นกเขียวครามมีไหม','นกเขียวครามหาได้ที่ไหน','นกเงือกกรามช้างอยู่ไหน','นกเงือกกรามช้างมีไหม','นกเงือกกรามช้างหาได้ที่ไหน','นกเงือกหัวแรดอยู่ไหน','นกเงือกหัวแรดมีไหม','นกเงือกหัวแรดหาได้ที่ไหน','นกเงือกหัวหงอกอยู่ไหน','นกเงือกหัวหงอกมีไหม','นกเงือกหัวหงอกหาได้ที่ไหน','นกเพนกวินฮัมโบลด์อยู่ไหน','นกเพนกวินฮัมโบลด์มีไหม','นกเพนกวินฮัมโบลด์หาได้ที่ไหน','นกเอี้ยงหงอนอยู่ไหน','นกเอี้ยงหงอนมีไหม','นกเอี้ยงหงอนหาได้ที่ไหน','นกแก้วเอคเลคตัสอยู่ไหน','นกแก้วเอคเลคตัสมีไหม','นกแก้วเอคเลคตัสหาได้ที่ไหน','นกแต้วแล้วธรรมดาอยู่ไหน','นกแต้วแล้วธรรมดามีไหม','นกแต้วแล้วธรรมดาหาได้ที่ไหน','หงส์ดำอยู่ไหน','หงส์ดำมีไหม','หงส์ดำหาได้ที่ไหน','เป็ดวู๊ดอยู่ไหน','เป็ดวู๊ดมีไหม','เป็ดวู๊ดหาได้ที่ไหน','เป็ดหงส์อยู่ไหน','เป็ดหงส์มีไหม','เป็ดหงส์หาได้ที่ไหน','เหยี่ยวแดงอยู่ไหน','เหยี่ยวแดงมีไหม','เหยี่ยวแดงหาได้ที่ไหน','นกกระจอกเทศอยู่ไหน','นกกระจอกเทศมีไหม','นกกระจอกเทศหาได้ที่ไหน']

answers = ["อยู่ในโซนสัตว์สัตว์ปึกของสวนสัตว์"]*99
