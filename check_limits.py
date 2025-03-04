# Daniel Meza
# Jr Embedded Software Developer
# check_limits.py


#Function check_range: This function checks if a value is 
# within a specific range and returns a status (True/False) and a gap ('low', 'high', 'normal').
def check_range(value, min_value, max_value, value_name):
    if value < min_value:
        print(f'{value_name} is below the minimum limit!')
        return False, 'low'
    elif value > max_value:
        print(f'{value_name} is above the maximum limit!')
        return False, 'high'
    return True, 'normal'


#Reduce cyclomatic complexity: 
# The battery_is_ok function can be split into smaller functions that check each condition separately.
#battery_is_ok function: Now uses check_range to check each parameter and, 
# if a notifier is provided, sends notification messages.
def battery_is_ok(temperature, soc, charge_rate, notifier=None):
  temp_status, temp_gap = check_range(temperature, 0, 45, 'Temperature')
  soc_status, soc_gap = check_range(soc, 20, 80, 'State of Charge')
  charge_rate_status, charge_rate_gap = check_range(charge_rate, 0, 0.8, 'Charge rate')

#The functions were modified to return information on whether the value is above or below the allowed range.
  if notifier:
    if not temp_status:
        notifier(f'Temperature is out of range! Gap: {temp_gap}')
    if not soc_status:
        notifier(f'State of Charge is out of range! Gap: {soc_gap}')
    if not charge_rate_status:
        notifier(f'Charge rate is out of range! Gap: {charge_rate_gap}')

    return temp_status and soc_status and charge_rate_status

#Notifier: A basic notifier (console_notifier) has been added that prints messages on the console.
def console_notifier(message):
    print(message)



#Additional tests: More test cases have been added to cover all possible conditions, 
# including cases where the values are below or above the limits.
if __name__ == '__main__':
    # Test cases
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
    assert(battery_is_ok(-1, 70, 0.7) is False)
    assert(battery_is_ok(25, 10, 0.7) is False)
    assert(battery_is_ok(25, 70, 0.9) is False)
    assert(battery_is_ok(25, 70, 0.9, console_notifier) is False)



# This code is more modular, easy to maintain and extensible,
# and covers all the conditions necessary to check the battery status. 
