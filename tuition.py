# Initialize variables
current_tuition = 8000  # Starting tuition
increase_rate = 0.03    # 3% annual increase
years = 5               # Number of years to project

# Loop through each year
for year in range(1, years + 1):
    # Calculate the new tuition
    current_tuition *= (1 + increase_rate)
    # Display the projected tuition for the current year
    print(f"Year {year}: ${current_tuition:.2f}")

    