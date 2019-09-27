#-*-coding:utf8;-*-
#qpy:3
#qpy:console



def primes(num):
    counter = 2
    while counter < num:

        if num%counter == 0:
            print(counter,"f")
                
            break
        counter +=1
        
    if counter == num:
        print("is prime")
        
while 1==1:
    primes(int(input("enter prime")))
