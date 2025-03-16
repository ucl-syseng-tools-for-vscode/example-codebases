def apply_discount(amount, discount):
    """Applies a discount but has an untested edge case."""
    if discount > 100:
        return "Invalid discount"
    if discount < 0:
        return "Negative discounts not allowed"
    
    final_amount = amount - (amount * discount / 100)

    if final_amount < 0:  
        return "Negative total (untested case)"

    return final_amount

def calculate_tax(amount, tax_rate=0.05):
    """Calculates tax on an amount but isn't fully tested."""
    if tax_rate < 0: 
        return "Invalid tax rate"
    
    return amount * tax_rate

def split_bill(amount, people):
    """Splits an amount among people but contains unreachable logic."""
    if people <= 0:  
        return "Invalid number of people"

    if amount == 0:
        return "No bill to split"  

    return amount / people
