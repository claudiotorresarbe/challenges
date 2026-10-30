n = input()
 
if n == '{}':
    print(0)
else:
    n = n.replace('{','').replace('}','').replace(' ','').replace("'",'').split(',')
    rst = set(n)
    print(len(rst))