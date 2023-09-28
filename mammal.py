import csv

def MammalClass(animalType,animal,questions,answers) :
    with open(animalType+'.csv', 'w', newline='',encoding="UTF-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Mammal", "Question", "Answer"])
        for name in animal :
            for question in questions :
                for answer in answers :
                    writer.writerow([animalType, f"{name}{question}", f"{answer}"])


mammal = ["ฮิปโปโปเตมัส","เนื้อทราย","ชะนีมงกุฎ","ไนอาลา","ช้างเอเชีย","นากเล็กเล็บสั้น","ชะนีแก้มขาวเหนือ","ค่างแว่นถิ่นใต้",
          "ยีราฟ","กระจงหนู","กระทิง","กวางดาว","กวางป่า","ค่างห้าสี","จิงโจ้แดง","ตัวกินมดยักษ์","ม้าลายเบอร์เชล",
          "ละมั่งพันธุ์พม่า","ลิงชิมแพนซี","สมเสร็จ","สิงโต","สล็อตสองนิ้ว","หมีหมา"]

mammal_question = ["อยู่ไหน","มีไหม","หาได้ที่ไหน"]
mammal_answer = ["อยู่ในโซนสัตว์สัตว์เลี้ยงลูกด้วยนมของสวนสัตว์"]

# MammalClass("Mammal",mammal,mammal_question,mammal_answer)


answers = ["Mammal"]*69
questions = ['ฮิปโปโปเตมัสอยู่ไหน','ฮิปโปโปเตมัสมีไหม','ฮิปโปโปเตมัสหาได้ที่ไหน','เนื้อทรายอยู่ไหน','เนื้อทรายมีไหม','เนื้อทรายหาได้ที่ไหน','ชะนีมงกุฎอยู่ไหน','ชะนีมงกุฎมีไหม','ชะนีมงกุฎหาได้ที่ไหน','ไนอาลาอยู่ไหน','ไนอาลามีไหม','ไนอาลาหาได้ที่ไหน','ช้างเอเชียอยู่ไหน','ช้างเอเชียมีไหม','ช้างเอเชียหาได้ที่ไหน','นากเล็กเล็บสั้นอยู่ไหน','นากเล็กเล็บสั้นมีไหม','นากเล็กเล็บสั้นหาได้ที่ไหน','ชะนีแก้มขาวเหนืออยู่ไหน','ชะนีแก้มขาวเหนือมีไหม','ชะนีแก้มขาวเหนือหาได้ที่ไหน','ค่างแว่นถิ่นใต้อยู่ไหน','ค่างแว่นถิ่นใต้มีไหม','ค่างแว่นถิ่นใต้หาได้ที่ไหน','ยีราฟอยู่ไหน','ยีราฟมีไหม','ยีราฟหาได้ที่ไหน','กระจงหนูอยู่ไหน','กระจงหนูมีไหม','กระจงหนูหาได้ที่ไหน','กระทิงอยู่ไหน','กระทิงมีไหม','กระทิงหาได้ที่ไหน','กวางดาวอยู่ไหน','กวางดาวมีไหม','กวางดาวหาได้ที่ไหน','กวางป่าอยู่ไหน','กวางป่ามีไหม','กวางป่าหาได้ที่ไหน','ค่างห้าสีอยู่ไหน','ค่างห้าสีมีไหม','ค่างห้าสีหาได้ที่ไหน','จิงโจ้แดงอยู่ไหน','จิงโจ้แดงมีไหม','จิงโจ้แดงหาได้ที่ไหน','ตัวกินมดยักษ์อยู่ไหน','ตัวกินมดยักษ์มีไหม','ตัวกินมดยักษ์หาได้ที่ไหน','ม้าลายเบอร์เชลอยู่ไหน','ม้าลายเบอร์เชลมีไหม','ม้าลายเบอร์เชลหาได้ที่ไหน','ละมั่งพันธุ์พม่าอยู่ไหน','ละมั่งพันธุ์พม่ามีไหม','ละมั่งพันธุ์พม่าหาได้ที่ไหน','ลิงชิมแพนซีอยู่ไหน','ลิงชิมแพนซีมีไหม','ลิงชิมแพนซีหาได้ที่ไหน','สมเสร็จอยู่ไหน','สมเสร็จมีไหม','สมเสร็จหาได้ที่ไหน','สิงโตอยู่ไหน','สิงโตมีไหม','สิงโตหาได้ที่ไหน','สล็อตสองนิ้วอยู่ไหน','สล็อตสองนิ้วมีไหม','สล็อตสองนิ้วหาได้ที่ไหน','หมีหมาอยู่ไหน','หมีหมามีไหม','หมีหมาหาได้ที่ไหน']
answers = ["อยู่ในโซนสัตว์สัตว์เลี้ยงลูกด้วยนมของสวนสัตว์"]*69