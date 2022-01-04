
cost_per_hour=1.02
cost_per_day=1.02*24
cost_per_month=cost_per_day*30
cost_twentyservers_day=20*cost_per_day
cost_twentyservers_month=cost_twentyservers_day*30
oneserver_days_1836_dollars=1836/cost_per_day
print('The cost per day is ${}'.format(cost_per_day))
print('The cost per month is ${}'.format(cost_per_month))
print('The cost per day of twenty servers is {}'.format(cost_twentyservers_day))
print('The cost per month of twenty servers is {}'.format(cost_twentyservers_month))
print('The amount of days you operate with $1,836 is {}'.format(oneserver_days_1836_dollars))
