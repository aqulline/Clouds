import requests
import time

from bs4 import BeautifulSoup


def change(content):
    soup = BeautifulSoup(content, 'html.parser')

    # print(table)
    import hashlib

    # Assume previous_html is the hash of the previous version of the HTML content

    # Get the current HTML content
    current_htm = str(soup)

    # print(current_htm)
    # Create an SHA-256 hash object for the current HTML content
    hash_object = hashlib.sha256()
    hash_object.update(current_htm.encode('utf-8'))
    current_hash = hash_object.hexdigest()

    print("Current Hash:", current_hash)

    return current_hash


# URL of the login page
login_url = 'https://sims.nit.ac.tz/index.php/login/?callback=https://sims.nit.ac.tz/index.php'

hd = ["S/No", "Pick", "nvoiceNo", "Control Number", "Description", "Payment Mode", "Currency", "Invoice", "Amount",
      "Paid", "Amount", "Balance", "Statement"]

# URL of the page you want to monitor
url = 'https://sims.nit.ac.tz/index.php/view_result'
inv = 'https://sims.nit.ac.tz/index.php/invoice_list'

# Credentials
username = 'Nit/bcict/2020/458'
password = 'MBUYA'

# Create a session
session = requests.Session()

# Authenticate
login_data = {
    'identity': username,
    'password': password
}
response = session.post(login_url, data=login_data)

responses = session.get(inv)
html = responses.content

# getting raw data
soup = BeautifulSoup(html, 'html.parser')

name = soup.find_all('table', attrs={'class': 'table table-responsive table-bordered'})

if response.status_code == 200:
    print("Logged in successfully!")
else:
    print("Not ")
    breakpoint()

# Monitor changes
previous_html = ''

while True:
    try:
        response = session.get(inv)
        current_html = response.text

        if previous_html != response.text:
            print("Website content has changed!")
            # Do something here, like sending a notification

        # Update the previous_html for the next iteration
        previous_html = current_html

    except requests.RequestException as e:
        print("Error:", e)

    # Adjust the time interval based on your needs
    time.sleep(6)  # Wait for 1 minute before checking again

    html = response.content

    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')

    name = soup.find('div', attrs={'class': 'ibox-content clearfix'})

    headd = soup.find_all('div', attrs={
        'style': 'font-weight: bold; color: brown; font-size: 15px; border-bottom: 1px solid brown; margin-bottom: 10px;'})

    tbl = name.find_all("table")

    # print(headd.__len__())

    # print(tbl.__len__())

    # print(tbl[0])
    data_main = {}
    data_tem = {}
    for i in range(tbl.__len__() - 1):
        tr = tbl[i].find_all("tr")
        print(headd[i].text)
        head = headd[i].text
        for j in range(tr.__len__()):
            td = tr[j].find_all("td")
            if td:
                for k in range(td.__len__() - 1):
                    #print(hd[k], td[k].text)
                    data = {f"{td[0].text}_{head}": {td[0].text: {
                        hd[p]:td[p].text
                        for p in range(td.__len__() - 1)}}}

                    data_main = {**data_main, **data}

                    print(data)
                    """data_temp = {headd[i].text: {td[0].text for o in range(): {
                        hd[o]: td[o].text
                        for o in range(td.__len__() - 1)}}}
                    data_main = {**data_temp, **data_main}"""
    print(data_main)
