#Programme  qui affiche les diviseurs d’un entier positif n non nul.
n=int(input("Entrer un entier n : "))
while(n<=0):
   n=int(input("Veuillez entrer un entier n ! : "))
d=0
for i in range(1,n+1):
   if(n % i == 0):
      d=i
      print(d)

