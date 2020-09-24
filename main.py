signo = ["capricornio", "acuario", "piscis", "aries", "tauro", "geminis",
        "cancer","leo", "virgo", "libra", "escorpio", "sagitario"]
fechas = [20, 19, 20, 20, 21, 20, 21, 23, 21, 21, 21, 21]

dia = int(input())
mes = int(input())

mes = mes - 1
if dia > fechas[mes]:
    mes += 1
if mes == 12:
     mes = 0
print(signo[mes])