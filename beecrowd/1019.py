x = int(input())

anos = int(x/3600)
mes = int((x%3600)/60)
dia = int(((x%3600)%60))
print(str(anos)+':'+str(mes)+':'+str(dia))
