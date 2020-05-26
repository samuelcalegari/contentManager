import mysql.connector
import re
from bs4 import BeautifulSoup

def processtext(data):
    if data is not None:
        if 'mlang' in data:
            data = re.findall('\{mlang\sfr\}(.*?)\{mlang\}', data)
            data = " ".join(data)
    else:
         data = ""
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

query = "SELECT mdl_course.id, mdl_course.fullname, mdl_course_categories.name FROM `mdl_course` LEFT JOIN `mdl_course_categories` ON mdl_course.category=mdl_course_categories.id"
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
    name = processtext(result[1])
    tags = ""
    category = processtext(result[2])

    query = "INSERT INTO courses (id, name, tags, category, content) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE name = %s, category = %s, content = %s"
    val = (id, name, tags, category, content, name, category, content)
    cursor2.execute(query, val)
    db2.commit()