rate = input("Оцените работу оператора от 1 до 5: ")
rate_us_number = int(rate)

if (rate_us_number < 1):
    rate_us_number = 1

if (rate_us_number > 5):
    rate_us_number = 5

print (rate_us_number)


feedback = ''
if rate_us_number == 1:
    feedback = input("Расскажите как исправиться: ")
else:
    if rate_us_number == 2:
        feedback = input("Что вас смутило? ")
    else:
        if rate_us_number == 3:
            feedback = input("Что вам не понравилось? ") 
        else:
            if rate_us_number == 4:
                feedback = input("Как нам добиться 5? ")
            else:
                if rate_us_number == 5:
                    feedback = input("Спасибо за вашу оценку! ")

print(feedback)