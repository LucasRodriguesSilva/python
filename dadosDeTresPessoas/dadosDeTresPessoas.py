cliente = [[1,2,3],[1,2,3],[1,2,3]]

x = 0
i = 0

for i in range(3):
    y = 0
    cliente[x][y] = str(input("Qual é o seu nome\n")).upper()
    y = y + 1
    cliente[x][y] = str(input("Onde você mora?\n")).upper()
    y = y + 1
    cliente[x][y] = str(input("Qual a sua idade?\n")).upper()
    x = x + 1

i = 0
x = 0
y = 0
print("")
for i in range(3):
    y = 0
    print("Nome: ".upper(),cliente[x][y]," ")
    y = y + 1
    print("Mora em: ".upper(),cliente[x][y]," ")
    y = y + 1
    print("Idade: ".upper(),cliente[x][y]," ")
    x = x + 1
    print("")