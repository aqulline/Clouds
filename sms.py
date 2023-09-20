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

# URL of the page you want to monitor
url = 'https://sims.nit.ac.tz/index.php/view_result'

# Credentials
username = 'Nit/bcict/2020/458'
password = 'MBUYa'

# Create a session
session = requests.Session()

# Authenticate
login_data = {
    'identity': username,
    'password': password
}
response = session.post(login_url, data=login_data)

responses = session.get(url)
html = responses.content

# print(html)

# getting raw data
soup = BeautifulSoup(html, 'html.parser')

name = soup.find_all('table', attrs={'class': 'table table-responsive table-bordered'})

if response.status_code==200:
    print("Logged in successfully!")
else:
    print("Not ")
    breakpoint()

# Monitor changes
previous_html = ''

while True:
    try:
        response = session.get(url)
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

    # print(html)

    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')

    name = soup.find_all('table', attrs={'class': 'table table-responsive table-bordered'})

    names = [elem.text.strip() for elem in name]

    # print(names)

    list_dat = []

    temp_data = []

    for i in names:
        for x in i.strip().split("\n"):
            if x != "":
                list_dat.append(x.strip())
    course_headers = ['Course Code', 'Course Name', 'Unit', 'CA', 'SE', 'Total', 'Grade', 'Point', 'Remark']
    field_headers = ['Course Code', 'Course Name', 'Unit', 'CA', 'Total', 'Grade', 'Point', 'Remark']
    gpa_remarl = ["Semester GPA", 'Remark']
    course_data = []

    filtered_list_one = [item for item in list_dat if item not in course_headers]
    count = 0
    data = {}
    for i in range(len(filtered_list_one) - 1):

        if count <= 8:
            temp_data.append(filtered_list_one[i])
            count += 1

            if filtered_list_one[i] == "PASS" and count == 8:
                course = {
                    field_headers[j]: temp_data[j]
                    for j in range(8)
                }
                course_data.append(course)
                count = 10
        elif count == 9:
            course = {
                course_headers[j]: temp_data[j]
                for j in range(9)
            }
            course_data.append(course)
            count = 0
            temp_data = []
            temp_data.append(filtered_list_one[i])
            count += 1
        elif count == 10:
            temp_data = []
            temp_data.append(filtered_list_one[len(filtered_list_one) - 2])
            temp_data.append(filtered_list_one[len(filtered_list_one) - 1])
            course = {
                gpa_remarl[j]: temp_data[j]
                for j in range(2)
            }
            count = 0

            course_data.append(course)

    # print(course_data)

    table = soup.find("table", class_="table table-responsive table-bordered")
    bs = soup.find("div", id="cont")

    b = bs.find_all("b")[0]
    print(b.text)

    # Find the row that you want to update
    row = table.find_all("tr")

    lend = len(table.find_all("tr")) - 1

    list_gpa = []
    list_cos = []
    remark_gpa = []

    for bl in bs.find_all("b"):
        list_cos.append(bl.text)

    for i in range(len(row[lend].find_all("td"))):
        rw = row[lend].find_all("td")[i]
        for j in rw:
            print(j.text)
            if i == 1:
                list_gpa.append(j.text)
            else:
                remark_gpa.append(j.text)
    print(list_gpa)
    print(list_cos)
    x = "Ordinary Diploma in  Information Technology - [ DIT ] THIRD YEAR :: 2022/2023 - SEMESTER I"
