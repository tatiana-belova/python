time = int(input("Введите время в секундах "))
hr = time // 3600
mn = (time - hr * 3600) // 60
sec = time - (hr * 3600 + mn * 60)
if hr < 10:
    hr = "0" + str(hr)
    if mn < 10:
        mn = "0" + str(mn)
        if sec < 10:
            sec = "0" + str(sec)
if time >= 86400:
    print("Введите число меньше 86400")
else:
    print(f"Время в формате чч:мм:сс  {hr} : {mn} : {sec}")
