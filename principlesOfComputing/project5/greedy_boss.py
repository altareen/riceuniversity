"""
|-------------------------------------------------------------------------------
| greedy_boss.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Sep 24, 2021
|
| Venv setup:       python3 -m venv venv
| Venv activation:  source venv/bin/activate
| Requirements:     pip install -r requirements.txt
| Run:              python greedy_boss.py
| Conclusion:       deactivate
|
| Description:
| This program implements the greedy boss simulator.
|
"""

#import simpleplot
import math
import matplotlib.pyplot as plt
#import codeskulptor
#codeskulptor.set_timeout(20)

STANDARD = True
LOGLOG = False

# constants for simulation
INITIAL_SALARY = 100
SALARY_INCREMENT = 100
INITIAL_BRIBE_COST = 1000


def greedy_boss(days_in_simulation, bribe_cost_increment, plot_type = STANDARD):
    """
    Simulation of greedy boss
    """
    
    # initialize necessary local variables
    current_day = 0
    current_salary = 100
    savings_balance = 0
    total_salary_earned = 0
    bribe_cost = 1000
    
    # define list consisting of days vs. total salary earned for analysis
    days_vs_earnings = []

    # Each iteration of this while loop simulates one bribe
    while current_day <= days_in_simulation:
        # update list with days vs total salary earned
        # use plot_type to control whether regular or log/log plot
        if plot_type == STANDARD:
            days_vs_earnings.append((current_day, total_salary_earned))
        else:
            if current_day != 0:
                days_vs_earnings.append([math.log(current_day), math.log(total_salary_earned)])
        
        # check whether we have enough money to bribe without waiting
        if savings_balance+current_salary >= bribe_cost:
            current_day += 1
            savings_balance += current_salary
            total_salary_earned += current_salary

        # advance current_day to day of next bribe (DO NOT INCREMENT BY ONE DAY)
        else:
            duration = math.ceil((bribe_cost-savings_balance)/current_salary)
            current_day += duration
            savings_balance += duration*current_salary
            total_salary_earned += duration*current_salary

        # update state of simulation to reflect bribe
        qty = math.floor(savings_balance/bribe_cost)
        savings_balance -= qty*bribe_cost
        current_salary += qty*100
        bribe_cost += qty*bribe_cost_increment
           
    return days_vs_earnings


def run_simulations():
    """
    Run simulations for several possible bribe increments
    """
    plot_type = STANDARD
    days = 70
    inc_0 = greedy_boss(days, 0, plot_type)
    inc_500 = greedy_boss(days, 500, plot_type)
    inc_1000 = greedy_boss(days, 1000, plot_type)
    inc_2000 = greedy_boss(days, 2000, plot_type)
    
    plt.plot([x[0] for x in inc_0], [x[1] for x in inc_0], 'y-', label="Bribe Increment = 0")
    plt.plot([x[0] for x in inc_500], [x[1] for x in inc_500], 'b-', label="Bribe Increment = 500")
    plt.plot([x[0] for x in inc_1000], [x[1] for x in inc_1000], 'r-', label="Bribe Increment = 1000")
    plt.plot([x[0] for x in inc_2000], [x[1] for x in inc_2000], 'g-', label="Bribe Increment = 2000")
    
    plt.title("Greedy Boss")
    plt.xlabel("Days")
    plt.ylabel("Total Earnings")
    plt.legend()
    plt.show()
    
#    simpleplot.plot_lines("Greedy boss", 600, 600, "days", "total earnings", 
#                          [inc_0, inc_500, inc_1000, inc_2000], False,
#                         ["Bribe increment = 0", "Bribe increment = 500",
#                          "Bribe increment = 1000", "Bribe increment = 2000"])

run_simulations()

print(greedy_boss(35, 100))
# should print [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), (29, 7900), (31, 9300), (33, 10900), (35, 12700)]

print(greedy_boss(35, 0))
# should print [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900)]
            
    
