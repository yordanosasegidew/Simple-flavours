"""
    Future improvement ideas for this project
    - User categorization logic (Residential/Commercial)
    - Export to 'Digital receipt' using File I/O to save the output to a text/image file
    - Interactive menu using a while loop
    - Config settings into JSON
"""

def calculate_bill():
    FIXED_FEE = 10.0
    VAT = 0.15

    TIERS = [(50,0.50),(100,0.75),(None,1.20)]

    print("===== Electricity bill calculator =====")

    try:
        prev = int(input("Enter previous reading: "))
        curr = int(input("Enter current reading: "))

        if curr < prev:
            prev("Error: Current reading can't be less than the previous")
            return

    except ValueError:
        print("Error: Please enter valid whole numbers.")
        return

    total_units = curr - prev
    remaining_units = total_units
    energy_charge = 0
    previous_limit = 0

    for limit,rate in TIERS:
        if remaining_units <= 0:
            break

        if limit is None:
            energy_charge += remaining_units * rate 
            remaining_units = 0
        else:
            tier_capacity = limit - previous_limit
            units_in_this_tier = min(remaining_units,tier_capacity)

            energy_charge += units_in_this_tier * rate
            remaining_units -= units_in_this_tier
            previous_limit = limit 

    subtotal = energy_charge + FIXED_FEE
    tax_amount = subtotal * VAT
    grand_total = subtotal + tax_amount

    print('\n'+'='*30)
    print(f"Total consumption: {total_units} units")
    print(f"Energy charge: ${energy_charge:.2f}")
    print(f"Fixed service fee: ${FIXED_FEE:.2f}")
    print(f"VAT (15%): {tax_amount:.2f}")
    print("-"*30)
    print(f"TOTAL BILL: ${grand_total:.2f}")
    print('='*30)

if __name__ == "__main__":
    calculate_bill()

calculate_bill()