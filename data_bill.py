# constant values are set here:
TIER_1_DATA_LIMIT_GB = 10
TIER_2_DATA_LIMIT_GB = 20
PREMIUM_USER_OVERAGE_RATE_TIER_2 = 1
REGULAR_USER_OVERAGE_RATE_TIER_2 = 2
PREMIUM_USER_OVERAGE_RATE_TIER_3 = 2
REGULAR_USER_OVERAGE_RATE_TIER_3 = 3


# Your code goes here:
''' # example
Enter data used (GB): 8
Enter base monthly plan cost: 40
Do you have a premium plan? (yes or no): no

You are within your data limit.
GB over limit: 0
Overage cost: $0.00
Total bill: $40.00
'''
'''
You are 15.0 GB over your limit.
Overage rate: $3 per GB
Overage cost: $45.00
Total bill: $85.00
'''

# inputs
data_used = float(input("Enter your data usage (in GB): "))
monthly_plan_cost = float(input("Enter your monthly plan cost: "))
user_premium_plan = input("Do you have premium plan? (yes or no): ")

# bool
has_premium = user_premium_plan in ('yes', 'Yes')


if has_premium:
    print('ok')
else:
    print('nooo')