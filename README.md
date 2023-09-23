# Loan Calculator

This Loan Calculator is a Python command-line tool that allows you to calculate various aspects of loans, including monthly payments (annuity payment), principal amounts, and the number of monthly payments. Additionally, it can also calculate differentiated monthly payments. This tool is designed to help you make informed financial decisions when dealing with loans.

## Features:

* (Annuity) Monthly Payments: You can calculate the fixed monthly payment required to repay a loan with a given principal amount, annual interest rate (automatically converted to a monthly interest rate), and the number of periods (in months).

* (Differentiated) Monthly Payments: If you want to calculate the monthly payments for a loan with differentiated payments, you can provide the principal amount, annual interest rate (automatically converted to a monthly interest rate), and the number of periods (in months). The calculator will show the monthly payments.

* Principal Amount: If you know the desired monthly payment, the annual interest rate, and the number of periods, you can calculate the principal amount that can be borrowed while meeting these criteria.

* Number of Monthly Payments: You can determine the number of months required to repay a loan, given the principal amount, annual interest rate (automatically converted to a monthly interest rate), and the desired monthly payment.

* The calculator also provides the overpayment amount i.e., amount paid over the principal due to the interest, with every calculation.

## The program allows users to:

* Calculate (Annuity) Monthly Payment: `python loan_calculator.py --type=annuity --principal=1000000 --periods=60 --interest=10`
* Calculate (Differentiated) Monthly Payment: `python loan_calculator.py --type=diff --principal=500000  --periods=8 --interest=7.8`
* Calculate Principal Amount: `python loan_calculator.py --type=annuity --payment=8722  --periods=120 --interest=5.6`
* Calculate Number of Monthly Payments: `python loan_calculator.py --type=annuity --principal=500000 --payment=23000 --interest=7.8`

## How to Use:

* Clone this repository to your local machine: `git clone https://github.com/mercerclayton/loan-calculator.git`
* Navigate to the project directory: `cd loan-calculator`
* Command-Line Arguments
    * `--type`: Specifies the type of calculation to perform (monthly payments (annuity), differentiated).
    * `--principal`: The principal loan amount (initial loan amount).
    * `--interest`: The annual interest rate as a percentage.
    * `--payment`: The desired monthly payment amount.
    * `--periods`: The number of periods (in months).

## Disclaimer

This Loan Calculator is for educational and informational purposes only. It should not be considered financial advice. Always consult with a qualified financial advisor or professional before making any financial decisions.