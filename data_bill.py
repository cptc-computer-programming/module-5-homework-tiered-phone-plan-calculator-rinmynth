# constant values are set here:
TIER_2_DATA_LIMIT_GB = 10
TIER_3_DATA_LIMIT_GB = 20
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

# processing

# how many gb they are over tier 2
overage_gb_tier_2 = data_used - TIER_2_DATA_LIMIT_GB
# how many gb they are over tier 3
overage_gb_tier_3 = data_used - TIER_3_DATA_LIMIT_GB

'''regular user over cost'''
# cost per gb tier 2
Tier_2_over_cost = REGULAR_USER_OVERAGE_RATE_TIER_2 * overage_gb_tier_2
 # cost per gb tier 3
Tier_3_over_cost = REGULAR_USER_OVERAGE_RATE_TIER_3 * overage_gb_tier_3

'''premium user over cost'''
# cost per gb tier 2
Tier_2_premium_over_cost = PREMIUM_USER_OVERAGE_RATE_TIER_2 * overage_gb_tier_2
 # cost per gb tier 3
Tier_3_premium_over_cost = PREMIUM_USER_OVERAGE_RATE_TIER_3 * overage_gb_tier_3


'''total bill'''
total_cost_over_tier_2 = monthly_plan_cost + Tier_2_over_cost
total_cost_over_tier_3 = monthly_plan_cost + Tier_3_over_cost

total_premium_cost_over_tier_2 = monthly_plan_cost + Tier_2_premium_over_cost
total_premium_cost_over_tier_3 = monthly_plan_cost + Tier_3_premium_over_cost

# regular tier 2
if data_used >= TIER_2_DATA_LIMIT_GB:
    print("you are within your data limit")
    print("GB over limit: " + str(overage_gb_tier_2))
    print("total bill: " + str(total_cost_over_tier_2))