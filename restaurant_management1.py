from restaurant_management import consumer
def ask():
    ask1=input("Are you admin or consumer?\n")
    if ask1=='Consumer':
        consumer()
    else:
        ask2=input("\nDo you want to see the customer data?\n")
        if ask2=='Yes':
                with open("customer-data.txt") as f:
                    data=f.read()
                    print("\n")
                    print(data)
                    f.close()
        else:
            print(exit(0))
ask()