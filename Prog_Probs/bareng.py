"""
It was 1985 when the President decreed that the rebel Bareng be evicted from the Philippines for his crimes.  
The President’s order is that Bareng be taken to sea and left to wander in a small boat possibly to find the 
nearest civilization ( 200 miles away from the Philippines).  Bareng is also given 5 days ration of food and water.
Displaying his compassion, the President had Bareng taken 50 miles in the correct direction. 
Bareng then begins sailing.  Initially, he is able to sail 20 miles/day.
However, after each day, he becomes weaker and weaker so his rate decreases by 1 mile/day.
Also, he loses 2 miles of those he gained each day to wind and sea storm that blows him backward.  
Although Bareng can stretch his ration of food and water, he will collapse and die on the 13th day of wandering. 
 
Create a program that will calculate: 
a.	 The day, rate and miles he has to travel each day. 
b.	The day when Bareng collapses or reaches civilization. 
 
Output layout: 
DAY			RATE			MILES 
 
  1			  20			   68 
  2			  19			   85 
 
…			  …			  ... 
 
         Bareng reaches civilization on day _ or Bareng dies on day _
"""


sail_move_rate = 20
miles_to_travel = 200
external_deducs = -2
net_deduc = sail_move_rate + external_deducs
miles_traveled = 50
day = 0

print("DAY\tRATE\tMILES")
while day <= 13:
    day += 1
    if day == 13:
        print(f"Bareng dies on day {day}")
        break
    elif miles_traveled < miles_to_travel:

        miles_traveled += net_deduc
        print(f"{day}\t{sail_move_rate}\t{miles_traveled}")

        
        sail_move_rate -= 1
        net_deduc = sail_move_rate + external_deducs
    else:
        print(f"Bareng reaches civilization on day {day}")
        break
    




    

