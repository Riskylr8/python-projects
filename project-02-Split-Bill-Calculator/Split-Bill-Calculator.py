def split_bill():
  print("Welcome to the Split Bill Calculator!")

  total_bill = float(input("What was the total bill? Rp"))
  num_people = int(input("How many people will split the bill? "))

  # Ask if the user wants to add a tip
  give_tip = input("Do you want to add a tip? (yes/no): ")

  if give_tip.lower() == "yes":
      tip_percentage = float(input("What percentage tip would you like to give? ")) / 100 #if you wanna give tip remember this code using percentage from total bill
      tip_amount = total_bill * tip_percentage  # Calculate tip amount separately
      total_bill += tip_amount  # Add tip amount to the total bill

  # Calculate the amount each person should pay
  amount_per_person = total_bill / num_people

  # Format the amount into Indonesian Rupiah format
  formatted_amount = f"Rp{amount_per_person:,.2f}"

  print(f"Each person should pay: {formatted_amount}")

  # Ask if the user wants to do another calculation
  another_calculation = input("Do you want to do another calculation? (yes/no): ")
  if another_calculation.lower() == "yes":
      return True
  else:
      return False

# Call the function to start the calculation
while split_bill():
  pass
