import mysql.connector
import re
from bs4 import BeautifulSoup

def processtext(data):
    if 'mlang' in data:
        data = re.findall('\{mlang\sfr\}(.*?)\{mlang\}', data)
        data = " ".join(data)
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
cursor2 = db2.cursor()

query = "SELECT * FROM `mdl_course`"
cursor.execute(query)
results = cursor.fetchall()

for result in results:

    query = "SELECT id, intro FROM mdl_label where course = " + str(result[0])
    cursor.execute(query)
    results2 = cursor.fetchall()
    content = ""

    for result2 in results2:
        tmp = BeautifulSoup(result2[1], features="html.parser").getText()
        tmp = tmp.replace('\r', '').replace('\n', ' ').strip()
        content += " " + processtext(tmp)

    id = result[0]
    name = processtext(result[3])
    tags = ""
    category = ""

    query = "INSERT INTO courses (id, name, tags, category, content) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE content = %s"
    val = (id, name, tags, category, content, content)
    cursor2.execute(query, val)
    db2.commit()


