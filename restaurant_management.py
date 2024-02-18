def consumer():
    import time 

    print("\nWelcome to the our restaurant!")
    consumer_name=input("\nEnter the your good name, sir?\n")

    menu_card={
        "Tomato soup":80,
        "Manchurian":120,
        "Veg fried rice":150,
        "Veg hakka noodles":150
    }

    # time.sleep(3)
    print("\nDishes\t\t\tPrice\nTomato Soup\t\t80\nManchurian\t\t120\nVeg Fried Rice\t\t150\nVeg Hakka Noodles\t150")
    # time.sleep(5)

    bill1=0
    your_choice=input("\nWhat would you like to order, sir?\n")
    if your_choice=='Manchurian':
        bill1=menu_card["Manchurian"]
    elif your_choice=='Tomato soup':
        bill1=menu_card['Tomato soup']
    elif your_choice=='Veg fried rice':
        bill1=menu_card["Veg fried rice"]
    elif your_choice=='Veg hakka noodles':
        bill1=menu_card['Veg hakka noodles']
    else:
        print("\nSorry sir, this entered dish is not currently available in our restaurant!")

    bill2=0
    while True:
        again_order=input("\nDo you want to give another order, sir?\n")
        if again_order=='Yes':
            dish=input("\nWhat would you like to order, sir?\n")
            if dish=='Manchurian':
                bill2=bill2+menu_card["Manchurian"]
            elif dish=='Tomato soup':
                bill2=bill2+menu_card["Tomato soup"]
            elif dish=='Veg fried rice':
                bill2=bill2+menu_card["Veg fried rice"]
            elif dish=='Veg hakka noodles':
                bill2=bill2+menu_card["Veg hakka noodles"]
            else:
                print("Sorry sir, this entered dish is not currently available in our restaurant!\n")
        elif again_order=='No':
            break
        else:
            print("You entered the wrong keyword!\n")

    final_bill=bill1+bill2
    if final_bill!=0:
        with open("customer-data.txt",'a') as f:
            f.write(f"\n{consumer_name}\t\t{final_bill}")

    # time.sleep(5)
    print(f"\nSir, this is your final bill {final_bill}")
    print("Thank you, visit again!")