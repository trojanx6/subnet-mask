
ip = str(input("ana ip giriniz: ")).split(".")
mask = input("mask(delfaut:255): ")
if len(str(mask)) == 0:
    mask = 256
for i in range(0, int(mask)):
    new_ip = bin(int(ip[0]))+"." + bin(int(ip[1])) + "." + bin(int(ip[2])) + "." + bin(i)
    bin_ip = new_ip.replace("0b", "")
    ip_STR = ip[0] + "."+ip[1] + "."+ip[2]+"."+str(i)
    print(bin_ip)
