x = int(input())

anos = int(x/365)
mes = int((x%365)/30)
dia = int(((x%365)%30))
print(anos,'ano(s)')
print(mes,'mes(es)')
print(dia,'dia(s)')