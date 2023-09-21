Animal = {}

reptile = ["เต่าบึงหัวเหลือง", "คอร์นสเนค", "งูกะปะ", "งูจงอาง", "งูปล้องทอง", "งูปี่แก้วลายแต้ม", "งูหลามทอง", 
           "งูหลาม", "งูหลามบอล", "งูเห่าพ่นพิษสยาม", "ตุ๊ดตู่", "ปาดยักษ์ออสเตรเลีย", "ตะโขง", "เต่าดำ", "เต่าท้องแดงฟลอริดา",
           "เต่าตีนแดง", "เต่าลายตีนเป็ด", "งูเขียวปากจิ้งจก", "เคย์แมน", "เต่าอัลลิเกเตอร์", "เหี้ย", "เห่าช้าง"]

mammal = ["ฮิปโปโปเตมัส","เนื้อทราย","ชะนีมงกุฎ","ไนอาลา","ช้างเอเชีย","นากเล็กเล็บสั้น","ชะนีแก้มขาวเหนือ","ค่างแว่นถิ่นใต้",
          "ยีราฟ","กวางป่า","ค่างห้าสี","จิงโจ้แดง","กวางดาว","กวางป่า","กวางผา","กูดู","ควายป่าแอฟริกัน","ค่างดำ","ค่างห้าสี",
          "คาปิบารา","จิงโจ้แดง","ชะมดเช็ด","ช้างแอฟริกา","ตัวกินมดยักษ์","พังพอน","ม้าลาย","ละมั่ง","ลา","ลามา","ลิง",
          "สมเสร็จ","สกั้ง","สิงโต","สล็อต","สล็อตสองนิ้ว","หมาใน","หมี"]


def writeDict(data,filename) :
    data_str = ""
    for name in data :
        data_str += "{'"+name+"':''}"+","

    with open(filename+'.txt', 'w', encoding="UTF-8") as dt:
        dt.write(data_str)

# Animal.update({name:food})
writeDict(mammal, "Mammal")