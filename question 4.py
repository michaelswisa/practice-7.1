# כתוב תוכנית המקבלת שני קלטים: מחרוזת str_my, וכן מספר שלם אי-שלילי num.
# בתחילת המחרוזת str_my ישנו רצף של ספרות. רצף זה מסתיים בתו הראשון שאינו ספרה או עד ארבע ספרות.
# רצף הספרות שבתחילת המחרוזת מייצג מספר שלם. על הפונקציה ליצור ולהחזיר מחרוזת חדשה בשם result
# כאשר result מכילה את תוצאת החיבור בין רצף הספרות שבתחילת str ובין num
# לדוגמא עבור:
# ”my_str = “1241abca!3
# num = 214
# הפונקציה תחזיר:
# ”result = “1455


new_s = 0
my_str = input("הכנס אותיות ומספרים\n")
num = int(input("הכנס מספרים בלבד\n"))
new_necklace = my_str[:4]
if new_necklace[0].isdigit():
    new_s = + 1
    if new_necklace[1].isdigit():
        new_s = new_s + 1
        if new_necklace[2].isdigit():
            new_s = new_s + 1
            if new_necklace[3].isdigit():
                new_s = new_s + 1
result = int(my_str[:new_s]) + num
print(result)

# צריך לבדוק איך לסדר את זה שמתי שהמחרוזת מתחילה באות זה לא יעשה שגיאה
