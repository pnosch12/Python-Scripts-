#Shipping Cost Calculations
prem_gs = 125.00


def cost_gs(weight):
    if weight <= 2.0:
        return (1.50 * weight + 20.00) 
    elif weight > 2.0 and weight < 6.0:
        return (3.00 * weight + 20.00) 
    elif weight > 6.0 and weight < 10.0:
        return (4.00 * weight + 20.00) 
    elif weight > 10.0:
        return (4.75 * weight + 20.00) 
    else:
        return "Cost can't be calculated"
    

def cost_d(weight):
    if weight <= 2.0:
        return (4.50 * weight) 
    elif weight > 2.0 and weight < 6.0:
        return (9.00 * weight) 
    elif weight > 6.0 and weight < 10.0:
        return (12.00 * weight) 
    elif weight > 10.0:
        return (14.25 * weight) 
    else:
        return "Cost can't be calculated"





def best_cost(weight):
    ground = cost_gs(weight)
    prem = prem_gs
    drone = cost_d(weight)



    if ground < drone and ground < prem:
        method = "standard ground"
        cost = ground
    elif prem < ground and prem < drone:
        method = "preminum ground"
        cost = prem
    else:
        method = "drone"
        cost = drone



    print("The cheapest option availabe is $%.2f with %s shipping." % (cost, method)
    )

best_cost(41.5)