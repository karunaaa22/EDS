print("ONLINE SHOPPING APP")
def dilevery_charges():
    cart=int(input("Enter Total Price in Cart: "))
    dist=float(input("Enter Total Distance: "))
    age=int(input("Enter Age: "))
    if cart>5000 and dist<10 and age>18:
        print("FREE DILEVERY")
    elif cart>2000 and dist<15 and age>18:
        print("Rs. 10 charges for DILEVERY")
    elif cart>500 and dist<20 and age>18:
        print("Rs. 30 charges for DILEVERY")
    elif age<18:
        print("10% DISCOUNT")
    else:
        print("Rs. 50 charges for DILEVERY")

dilevery_charges()
