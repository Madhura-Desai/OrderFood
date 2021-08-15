def order_food(s_dog,m_dog,l_dog,r_food):
    #Check the number of dogs is 0<= Size of dogs <= 30
    if(s_dog >= 0 and s_dog <= 30 and m_dog >= 0 and m_dog <=30 and l_dog >=0 and l_dog <= 30 and r_food >= 0 ):
        #Check if the total number of dogs is less than or equal to 30
        if(s_dog + m_dog + l_dog) <=30:
            #Calculate order quantity
            min_food_reqd = (s_dog *10) + (m_dog * 20) + (l_dog * 30)
            difference_food = min_food_reqd - r_food
            if(difference_food >= 0):
                order_qty = difference_food *1.2
                order_qty = round(order_qty,1)
                print("Please order "+ str(order_qty)+"lbs of food")
            else:
                #Error check
                order_qty =0
                print("Sufficient food in stock " + str(order_qty ))
                return order_qty
        else:
            #Error check
            order_qty = -999
            print("Total number of dogs cannot exceed 30 "+str(order_qty))
            return order_qty
    else:
        #Error check
        order_qty = -999
        print("Invalid input!! Number of dogs has to be between 0 and 30, and remaining food cannot be negative "+str(order_qty))
    return order_qty