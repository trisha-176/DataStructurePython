import sqlite3
conn=sqlite3.connect("student.db")
cur=conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS student(
  regno INTEGER PRIMARY KEY,
  name TEXT,
  sub1 INTEGER,
  sub2 INTEGER,
  sub3 INTEGER
)
""")
n=int(input("Enter number of students:"))
for i in range(n):
  regno=int(input("Enter registration number:"))
  name=input("Enter student name:")
  sub1=int(input("Enter marks in subject 1:"))
  sub2=int(input("Enter marks in subject 2:"))
  sub3=int(input("Enter marks in subject 3:"))
  cur.execute("INSERT INTO student VALUES(?,?,?,?,?)",(regno,name,sub1,sub2,sub3))
  conn.commit()
  print("\nStudent record inserted successfully")
  print("\nStudent Details")
  print("Regno\tName\tSub1\tSub2\tSub3")
  cur.execute("SELECT * FROM student")
  rows=cur.fetchall()
  for r in rows:
    print(r[0],"\t",r[1],"\t",r[2],"\t",r[3],"\t",r[4])
    conn.close()

