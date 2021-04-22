# by kevin alvaro adianto

def balik(data):
    tuker=dict()
    for x,y in data.items():
        tuker[y]=x
    return(tuker)
def urutkan(data):
    lis=[]
    for x in data:
        lis.append(x)
    lis.sort()
    return(lis)
def dicturut (data,lis):
    urut=dict()
    for z in lis:
        y=data.get(z,0)
        urut[z]=y
    return(urut)

data=dict()
pilihan = "y"
while pilihan != "t" :
    nama=input("masukkan nama: ")
    nilai=int(input("masukkan nilai: "))
    data[nama]=nilai
    print("data setelah di tambahkan: ",data)
    pilihan=input("lagi? (y/t): ").lower()

balik=balik(data)
lis=urutkan(balik)
urut=dicturut(balik,lis)
print("data urut: ",urut)
