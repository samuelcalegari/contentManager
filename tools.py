import mysql.connector
import re
from bs4 import BeautifulSoup

def processtext(data):
    if 'mlang' in data:
        data = re.findall('\{mlang\sfr\}(.*?)\{mlang\}', data)
    return data

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="forco"
)

db2 = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mirobot"
)

cursor = db.cursor()

query = "SELECT * FROM `mdl_course`"
cursor.execute(query)
results = cursor.fetchall()

for result in results:
    print(result[3])
    query = "SELECT id, intro FROM mdl_label where course = " + str(result[0])
    cursor.execute(query)
    results2 = cursor.fetchall()
    content = ""
    ## Showing the data
    for result2 in results2:
        tmp = BeautifulSoup(result2[1], features="html.parser").getText()
        tmp = tmp.replace('\r', '').replace('\n', '')
        content += " ".join(processtext(tmp))

    print(content)