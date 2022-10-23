import json

listofnames = ['Vasya', 'Nikolay', 'Dmitriy']
listofadreses = ['192.168.8.1', '201.255.11.1', '186.109.1.1']
listoflogins = ['v@sy@1337', 'K0lya_666', 'Dima_Dima']
listofusers = [{'name':listofnames[i], 'ip':listofadreses[i], 'login':listoflogins[i]} for i in range(3)]
print(listofusers)

json.dump(listofusers, open('listofusers.json', 'w'))
