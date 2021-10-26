"""
|-------------------------------------------------------------------------------
| cookie_clicker.py
|-------------------------------------------------------------------------------
|
| Author:   Alwin Tareen
| Created:  Sep 27, 2021
|
| Venv setup:       python3 -m venv venv
| Venv activation:  source venv/bin/activate
| Requirements:     pip install -r requirements.txt
| Run:              python cookie_clicker.py
| Conclusion:       deactivate
|
| Description:
| This program implements the cookie clicker simulator.
|
"""

#import simpleplot

# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)

import math
import matplotlib.pyplot as plt
import poc_clicker_provided as provided
import random

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total_cookies_produced = 0.0
        self._current_cookies = 0.0
        self._current_time = 0.0
        self._current_cps = 1.0
        self._history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        result = "\n"
        result += "Current time: " + str(self._current_time) + "\n"
        result += "Current cookie balance: " + str(self._current_cookies) + "\n"
        result += "Current cookies per second(CPS): " + str(self._current_cps) + "\n"
        result += "Total cookies produced: " + str(self._total_cookies_produced)
        #result += f"History: {self._history}"
        return result
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return self._history[:]

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if self._current_cookies >= cookies:
            return 0.0
        return math.ceil((cookies-self._current_cookies) / self._current_cps)
        
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time <= 0.0:
            return
        self._current_time += time
        self._current_cookies += time*self._current_cps
        self._total_cookies_produced += time*self._current_cps
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if cost > self._current_cookies:
            return
        self._current_cookies -= cost
        self._current_cps += additional_cps
        self._history.append((self._current_time, item_name, cost, self._total_cookies_produced))


def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    # Replace with your code
    build_clone = build_info.clone()
    clicker = ClickerState()
    
    while clicker.get_time() <= duration:
        time_remaining = duration - clicker.get_time()
        item_name = strategy(clicker.get_cookies(), clicker.get_cps(), clicker.get_history(), time_remaining, build_clone)
        if item_name is None:
            break

        item_cost = build_clone.get_cost(item_name)
        time_quantity = clicker.time_until(item_cost)
        if time_quantity > time_remaining:
            break

        clicker.wait(time_quantity)
        clicker.buy_item(item_name, item_cost, build_clone.get_cps(item_name))
        build_clone.update_item(item_name)
    
    # Allow cookies to accumulate for any remaining time
    clicker.wait(duration - clicker.get_time())
    
    # Allow for the purchase of items at final duration time
    item_name = strategy(clicker.get_cookies(), clicker.get_cps(), clicker.get_history(), 0, build_clone)
    if item_name is None:
        return clicker
    item_cost = build_clone.get_cost(item_name)
    clicker.buy_item(item_name, item_cost, build_clone.get_cps(item_name))
    build_clone.update_item(item_name)

    return clicker


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    inventory = {}
    cookie_balance = cookies + time_left*cps
    for item in build_info.build_items():
        inventory[item] = build_info.get_cost(item)
    lowest = float('inf')
    product = None
    for item in inventory:
        if inventory[item] < lowest and inventory[item] <= cookie_balance:
            lowest = inventory[item]
            product = item 
    return product

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    inventory = {}
    cookie_balance = cookies + time_left*cps
    for item in build_info.build_items():
        inventory[item] = build_info.get_cost(item)
    highest = float('-inf')
    product = None
    for item in inventory:
        if inventory[item] > highest and inventory[item] <= cookie_balance:
            highest = inventory[item]
            product = item 
    return product

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    Always buy the item with the lowest cost/cps ratio.
    """
    inventory = {}
    cookie_balance = cookies + time_left*cps
    for item in build_info.build_items():
        inventory[item] = 1.0*build_info.get_cost(item)/build_info.get_cps(item)
    lowest = float('inf')
    product = None
    for item in inventory:
        if inventory[item] < lowest and inventory[item] <= cookie_balance:
            lowest = inventory[item]
            product = item 
    return product
    
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print(strategy_name, ":", state)

    # Plot total cookies over time
    #-----------------------------
    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)


    # The following is the custom built code for plotting all strategies on the same graph
    #-------------------------------------------------------------------------------------
#    state = simulate_clicker(provided.BuildInfo(), time, strategy_cheap)
#    history = state.get_history()
#    plt.plot([x[0] for x in history], [x[3] for x in history], 'r-', label=f"Strategy = Cheap")

#    state = simulate_clicker(provided.BuildInfo(), time, strategy_expensive)
#    history = state.get_history()
#    plt.plot([x[0] for x in history], [x[3] for x in history], 'b-', label=f"Strategy = Expensive")
#    
#    state = simulate_clicker(provided.BuildInfo(), time, strategy_best)
#    history = state.get_history()
#    plt.plot([x[0] for x in history], [x[3] for x in history], 'g-', label=f"Strategy = Best")

#    plt.title("Cookie Clicker")
#    plt.xlabel("Time")
#    plt.ylabel("Total Cookies")
#    plt.legend()
#    plt.show()
    
    # The following statement is for testing purposes
    #------------------------------------------------
    # return state
    
def run():
    """
    Run the simulator.
    """
    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)
    
run()

