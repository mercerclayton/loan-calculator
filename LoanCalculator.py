import math
import argparse


# Function used to parse command line arguments
def parse_arguments() -> list[float | int]:
    """Parse and return the specified command line arguments as a list."""

    parser = argparse.ArgumentParser()

    # Arguments the user can specify
    parser.add_argument("--type", type=str)
    parser.add_argument("--payment", type=float)
    parser.add_argument("--principal", type=float)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)

    args = parser.parse_args()

    return [args.type, args.payment, args.principal, args.periods, args.interest]


def calculate_principal(payment: float, periods: int, interest: float) -> None:
    """
    Print the principal amount of the loan.
    
    param payment: Payment to be made in each period.
    param periods: Number of periods payment is to be made. Period is assumed to be monthly.
    param interest: Annualized interest rate. E.g., 10 means 10%
    """

    check = negative_check(payment, periods, interest)
    if check:
        print("Incorrect parameters")
        return

    monthly_interest = (interest * 0.01) / 12
    numerator = monthly_interest * (1 + monthly_interest) ** periods
    denominator = (1 + monthly_interest) ** periods - 1
    principal = payment / (numerator / denominator)

    overpayment = math.ceil((payment * periods) - principal)
    print(f"Your loan principal = {math.ceil(principal)}!\nOverpayment = {overpayment}")


def calculate_number_of_payments(principal: float, payment: float, interest: float) -> None:
    """
    Print the number of yearly and/or monthly payments required to pay off the principal.

    param principal: Principal amount of the loan.
    param payment: Payment to be made in each period. Period is assumed to be monthly.
    param interest: Annualized interest rate. E.g., 10 means 10%
    """

    check = negative_check(principal, payment, interest)
    if check:
        print("Incorrect parameters")
        return

    monthly_interest = (interest * 0.01) / 12
    x = payment / (payment - monthly_interest * principal)
    number_of_months = math.ceil(math.log(x, 1 + monthly_interest))

    years = number_of_months // 12
    remaining_months = number_of_months % 12
    cond1 = "years" if years > 1 else "year"
    cond2 = "months" if remaining_months > 1 else "month"
    if years:
        if remaining_months:
            print(f"It will take {years} {cond1} and {remaining_months} {cond2} to repay this loan!")
        else:
            print(f"It will take {years} {cond1} to repay this loan!")
    else:
        print(f"It will take {remaining_months} {cond2} to repay the loan!")

    overpayment = math.ceil((payment * number_of_months) - principal)
    print(f"Overpayment = {overpayment}")


def calculate_monthly_payment(principal: float, periods: int, interest: float, diff=True) -> None:
    """
    Calculate the monthly payment required to pay off the principal.

    param principal: Principal amount of the loan.
    param periods: Number of periods payment is to be made. Period is assumed to be monthly.
    param interest: Annualized interest rate. E.g., 10 means 10%
    """

    check = negative_check(principal, periods, interest)
    if check:
        print("Incorrect parameters")
        return

    monthly_interest = (interest * 0.01) / 12
    if diff:
        total = 0
        for month in range(1, periods + 1):
            payment = math.ceil(
                principal / periods + monthly_interest * (principal - (principal * (month - 1)) / periods))
            total += payment
            print(f"Month {month}: payment is {payment}")

        overpayment = round(total - principal)
        print(f"\nOverpayment = {overpayment}")
    else:
        numerator = monthly_interest * (1 + monthly_interest) ** periods
        denominator = (1 + monthly_interest) ** periods - 1
        annuity_payment = math.ceil(principal * (numerator / denominator))

        overpayment = round(annuity_payment * periods - principal)
        print(f"Your monthly payment = {annuity_payment}!\nOverpayment = {overpayment}")


# Function used to check if any value in a list is negative.
def negative_check(*args: float | int) -> bool:
    for arg in args:
        if arg < 0:
            return True
    return False


def main():

    calculation_types = ["diff", "annuity"]

    arguments = parse_arguments()
    calculation_type, payment, principal, periods, interest = arguments
    bool_arguments = [True if x is not None else False for x in arguments]

    # Input parameter validation under the following criteria:
    # - Calculation type must be either annuity or diff;
    # - Interest rate must be provided;
    # - Number of input parameters must not be less than 4.
    # - Calculation type can only be diff if calculating payment amount.
    if calculation_type not in calculation_types or not interest or sum(bool_arguments) < 4:
        print("Incorrect parameters")
    elif not principal and not calculation_type == "diff":
        calculate_principal(payment, periods, interest)
    elif not periods and not calculation_type == "diff":
        calculate_number_of_payments(principal, payment, interest)
    elif not payment:
        if calculation_type == "diff":
            calculate_monthly_payment(principal, periods, interest)
        else:
            calculate_monthly_payment(principal, periods, interest, diff=False)
    else:
        print("Incorrect parameters")


if __name__ == "__main__":
    main()
