import math
import argparse
import sys
import Helper


# Store information about the command line arguments
def command_line_parameters():
    parser = argparse.ArgumentParser(description="This program simulates a real loan calculator.")

    # Loan calculator program parameters and acceptable arguments
    parser.add_argument("--type", choices=["diff", "annuity"], help="Type of payment the user wants to calculate.")
    parser.add_argument("--principal", help="The loan principal.")
    parser.add_argument("--periods", help="The number of monthly payments.")
    parser.add_argument("--interest", help="The interest rate on the loan.")
    parser.add_argument("--payment", help="The monthly payment amount.")


# Calculates the required parameter of a loan according to the user's inputs
def calculator(parameters):
    overpayment = 0
    if parameters.get("payment") is None:
        principal = float(parameters.get("principal"))
        periods = int(parameters.get("periods"))
        interest = float(parameters.get("interest"))
        n_interest = (interest / 100) / 12      # nominal interest = interest rate per month

        # --type=annuity --principal=1000000 --periods=60 --interest=10
        # Your annuity payment = 21248!
        # Overpayment = 274880
        if parameters.get("type") == "annuity":
            annuity = principal * ((n_interest * (1 + n_interest) ** periods) / ((1 + n_interest) ** periods - 1))
            overpayment = math.ceil(annuity) * periods - principal

            print(f"Your annuity payment = {math.ceil(annuity)}!")
        else:

            # --type=diff --principal=500000 --periods=8 --interest=7.8
            # Month 1: payment is 65750
            # Month 2: payment is 65344
            # Month 3: payment is 64938
            # Month 4: payment is 64532
            # Month 5: payment is 64125
            # Month 6: payment is 63719
            # Month 7: payment is 63313
            # Month 8: payment is 62907
            #
            # Overpayment = 14628
            for month in range(1, periods + 1):
                annuity = (principal / periods) + n_interest * (principal - ((principal * (month - 1)) / periods))
                overpayment += math.ceil(annuity)
                print(f"Month {month}: payment is {math.ceil(annuity)}")
            overpayment -= principal

    elif parameters.get("principal") is None:

        # --type=annuity --payment=8722 --periods=120 --interest=5.6
        # Your loan principal = 800018!
        # Overpayment = 246622
        annuity = float(parameters.get("payment"))
        periods = int(parameters.get("periods"))
        interest = float(parameters.get("interest"))

        n_interest = (interest / 100) / 12
        principal = annuity / ((n_interest * (1 + n_interest) ** periods) / ((1 + n_interest) ** periods - 1))
        overpayment = math.ceil(annuity) * periods - principal

        print(f"Your loan principal = {math.floor(principal)}!")

    elif parameters.get("periods") is None:

        # --type=annuity --principal=500000 --payment=23000 --interest=7.8
        # It will take 2 years to repay this loan!
        # Overpayment = 52000
        principal = float(parameters.get("principal"))
        annuity = float(parameters.get("payment"))
        interest = float(parameters.get("interest"))

        n_interest = (interest / 100) / 12
        periods = math.ceil(math.log((annuity / (annuity - n_interest * principal)), (1 + n_interest)))
        years = periods // 12
        months = periods % 12
        overpayment = periods * math.ceil(annuity) - principal

        if months == 0:
            if years > 1:
                print(f"It will take {years} years to repay this loan!")
            else:
                print("It will take 1 year to repay this loan!")
        else:
            if years == 0:
                if months > 1:
                    print(f"It will take {months} months to repay this loan!")
                else:
                    print("It will take 1 month to repay this loan!")
            else:
                print(f"It will take {years} years and {months} months to repay this loan!")

    print(f"Overpayment = {math.ceil(overpayment)}")


# Retrieves command line arguments and validates them
def get_parameters():
    arguments = helper.extract_arguments(sys.argv)

    # If --type is specified neither as "annuity" nor as "diff" or not specified at all, show the error message.
    if arguments.get("type") not in ["diff", "annuity"]:
        print("Incorrect parameters")

    # Fewer than four parameters cannot be provided.
    elif len(arguments) < 4:
        print("Incorrect parameters")

    # For --type=diff, a combination with --payment is invalid as payments are different every month.
    elif arguments.get("type") == "diff" and arguments.get("payment") is not None:
        print("Incorrect parameters")

    # The loan calculator cannot calculate the interest, so it must always be provided.
    elif arguments.get("interest") is None:
        print("Incorrect parameters")

    # Negative values cannot be entered for any parameter.
    elif helper.check_values(arguments):
        print("Incorrect parameters")
    else:
        calculator(arguments)


command_line_parameters()
get_parameters()



