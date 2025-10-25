import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def ussd():
    session_id   = request.values.get("sessionId", None)
    serviceCode  = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text         = request.values.get("text", "default")

    if text == '':
        response = "CON Welcome Grace MFI:"
        response +="1. Borrow loan\n2. Repay Loan\n3. Buy Airtime\n4. Buy Bundles\n5. Check Balance"
    elif text == '1':
        response = "CON You've successfully Borrowed KES 10,000"
    elif text == "2":
        response = "CON You've successfully repayed KES 10,000 loan"
    elif text == "3":
        response = "CON You've successfully bought KES 10,000 airtime"
    elif text == "4":
        response = "CON You've successfully bought 500 MBs"
    elif text == "5":
        response = "CON Your balance is KES 10,000"
    else:
        response = "END Invalid Input"


    return response


if __name__ == '__main__':
    app.run(debug=True)



# Borrow loan
# Repay
# Check balance
# Buy Airtime
# Buy bundles