from address import Adress
from mail import Mailing

to_adress = Adress("789456", "Voronez", "Mira", "45", "14")
from_adress = Adress("415344", "Kirov", "Lenina", "2", "78")

Mail = Mailing(to_adress, from_adress, "4.99", "78945613")



print (f"Отправление ", Mail.track, "из ", {Mail.to_addres}, "в ", {Mail.from_adress}, "Стоимость ", Mail.cost, "рублей")