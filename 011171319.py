import numpy as np
np.random.seed(10)

import matplotlib.pyplot as plt

# Take input m & n
m = int(input("Maximum Inventory: "))
n = int(input("Review Period: "))

beginning_inventory = 3
demand = 0
ending_inventory = 0
shortage_quantity = 0
order_quantity = 8
days_until_next_arrival = 2
total_ending_inventory = []
average_ending_inventory = []
shortage_days = 0

for cycle in range(1, 11):

    print("Cycle No: ", cycle)

    for day in range(1, n + 1):

        print("Day No: ", day)

        if days_until_next_arrival == 0:

            beginning_inventory = beginning_inventory + order_quantity

        demand = np.random.choice(a=[0, 1, 2, 3, 4], p=[0.10, 0.25, 0.35, 0.21, 0.09])
        total_demand = demand + shortage_quantity

        if total_demand <= beginning_inventory:

            ending_inventory = beginning_inventory - total_demand
            shortage_quantity = 0

        else:
            extra_demand = total_demand - beginning_inventory
            shortage_quantity = extra_demand
            ending_inventory = 0
            shortage_days = shortage_days + 1

        total_ending_inventory.append(ending_inventory)

        print("Beginning Inventory: ", beginning_inventory)
        print("Daily Demand: ", demand)
        print("Ending Inventory: ", ending_inventory)
        print("Shortage Quantity: ", shortage_quantity)

        if day == n:

            day = 0
            order_quantity = m - ending_inventory
            print("Next Order: ", order_quantity)
            days_until_next_arrival = np.random.choice(a=[1, 2, 3], p=[0.60, 0.30, 0.10])
            print('Days Until Next Arrival', days_until_next_arrival)
            days_until_next_arrival += 1

        beginning_inventory = ending_inventory

        days_until_next_arrival -= 1


average_ending_inventory = sum(total_ending_inventory) / (n*10)
print("Average Ending Inventory: ", average_ending_inventory)
print("Total Number of Days Shortage Occurs: ", shortage_days)

plt.figure(figsize=(8, 8))
plt.plot(total_ending_inventory, marker='*')
plt.title("Inventory Level vs Day")
plt.xlabel("Day Number")
plt.ylabel("Ending Inventory of Each Day")
plt.show()
