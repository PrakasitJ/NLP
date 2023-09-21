import csv

def datasource(Type):
    zone = {"สะวันนา":{"สิงโต":"1A","ม้าลาย":"5A"},
         "บึง":{"จระเข้":"7C","บูลฟร็อค":"10C","งู":"12C"},
         "สวนนก":{"นกแก้ว":"15B","นกอีก๋อย":"99B"},
         "ศูนย์อนุรักษ์ควายป่า":{"ไอเตอร์":"Z1","ไอมิ้นท์":"Z2"},
         "อาร์คติก":{"เพนกวิน":"AC1"}
         }
    place = "ห้องน้ำ|ศูนย์อาหาร|ร้านขายของที่ระลึก"
    animal = "สิงโต|ม้าลาย|จระเข้|บูลฟร็อค|นกแก้ว|นกอีก๋อย|ไอเตอร์|ไอมิ้นท์|งู|เพนกวิน"

    pictures = {"นกแก้ว":"https://www.pangpond.com/wp-content/uploads/%E0%B8%99%E0%B8%81%E0%B9%81%E0%B8%81%E0%B9%89%E0%B8%A7.jpg",
               "สิงโต":"https://pbs.twimg.com/media/DHZ21VKUwAAbk9q.jpg",
               "เพนกวิน":"https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/King_Penguins_at_St._Andrews_Bay%2C_South_Georgia_%285817245080%29.jpg/1200px-King_Penguins_at_St._Andrews_Bay%2C_South_Georgia_%285817245080%29.jpg"
               }
    locations = {"นกแก้ว":"https://www.google.com/maps/dir//%E0%B8%81%E0%B8%A3%E0%B8%87%E0%B8%99%E0%B8%81%E0%B9%83%E0%B8%AB%E0%B8%8D%E0%B9%88+6395%2B73Q+%E0%B8%95%E0%B8%B3%E0%B8%9A%E0%B8%A5+%E0%B8%9A%E0%B8%B2%E0%B8%87%E0%B8%9E%E0%B8%A3%E0%B8%B0+%E0%B8%AD%E0%B8%B3%E0%B9%80%E0%B8%A0%E0%B8%AD%E0%B8%A8%E0%B8%A3%E0%B8%B5%E0%B8%A3%E0%B8%B2%E0%B8%8A%E0%B8%B2+%E0%B8%8A%E0%B8%A5%E0%B8%9A%E0%B8%B8%E0%B8%A3%E0%B8%B5+20110/@13.217234,101.0554585,18z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3102cbe4ee78d1cd:0xfc546ebaad3109dc!2m2!1d101.0577268!2d13.2182249?entry=ttu",
               "สิงโต":"https://www.google.com/maps/dir//13.2189499,101.055545/@13.2174378,101.0546369,18z?entry=ttu",
               "เพนกวิน":"https://www.google.com/maps/dir//%E0%B8%AA%E0%B9%88%E0%B8%A7%E0%B8%99%E0%B9%81%E0%B8%AA%E0%B8%94%E0%B8%87%E0%B8%9E%E0%B8%B2%E0%B9%80%E0%B8%AB%E0%B8%A3%E0%B8%94+%E0%B9%80%E0%B8%9E%E0%B8%99%E0%B8%81%E0%B8%A7%E0%B8%B4%E0%B8%99+%E0%B9%80%E0%B8%A5%E0%B8%82%E0%B8%97%E0%B8%B5%E0%B9%88+235+%E0%B8%95%E0%B8%B3%E0%B8%9A%E0%B8%A5+%E0%B8%9A%E0%B8%B2%E0%B8%87%E0%B8%9E%E0%B8%A3%E0%B8%B0+%E0%B8%AD%E0%B8%B3%E0%B9%80%E0%B8%A0%E0%B8%AD%E0%B8%A8%E0%B8%A3%E0%B8%B5%E0%B8%A3%E0%B8%B2%E0%B8%8A%E0%B8%B2+%E0%B8%8A%E0%B8%A5%E0%B8%9A%E0%B8%B8%E0%B8%A3%E0%B8%B5+20110/@13.2161499,101.0562445,20.25z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3102cb10c75a311f:0xbf2e19a3e0f926bc!2m2!1d101.056434!2d13.2161468?entry=ttu"
               }

    if(Type == "Zone") : return zone
    if(Type == "Place") : return place
    if(Type == "Animal") : return animal
    if(Type == "Picture") : return pictures
    if(Type == "Location") : return locations


with open('data.csv', 'w', newline='',encoding="UTF-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Class", "Question", "Answer"])

    for animal in datasource("Animal").split("|"):
        zone = datasource("Zone")
        for locate in zone:
            if animal in zone[locate]:
                location = locate
                cage = zone[locate][animal]
        writer.writerow(["Animal", f"{animal}อยู่ไหน", f"{animal}อยู่ใน{location}"])
        writer.writerow(["Animal", f"{animal}กินอะไร", f"{animal}กินขี้"])