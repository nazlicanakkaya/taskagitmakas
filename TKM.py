import random as r

user=0,  
botsayac=0
usersayac=0

for i in range(1,4):
    user1=input("tas,kagit ya da makas yaziniz: ")
    if user1=="tas":
        user=1
    if user1=="kagit":
        user=2
    if user1=="makas":
        user=3
    a=r.random()
    if a<0.33:
        bot=1 #taş
        kod="tas"
    elif a<=0.66:
        bot=2 #kağıt
        kod="kagit"
    else:
        bot=3 #makas
        kod="makas"
    
    
    print("kullanıcı: ", user1)
    print("bot: ", kod)

if bot==3 and user==2 or bot==2 and user==1 or bot==1 and user==3:
    print("bot kazandi")
    botsayac=botsayac+1
if bot==3 and user==1 or bot==1 and user==2 or bot==2 and user==3: 
    print("kullanıcı kazandi")
    usersayac=usersayac+1
if bot==user:
    print("berabere")
    

if usersayac>botsayac:
    print("KULLANICI KAZANDI")
if usersayac<botsayac:
    print("KULLANICI KAYBETTİ")
if usersayac==botsayac:
    print("BERABERLİK")
