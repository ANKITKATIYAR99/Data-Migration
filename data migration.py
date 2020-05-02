import pymysql

f=open(r"C:\Users\PrinceAnkit\Desktop\Book1.csv","r")
fstring = f.read()
flist=[]
for line in fstring.split("\n"):
    flist.append(line.split(","))
print(flist)

# open connection to database
db= pymysql.connect("localhost","tstuser","test123","TESTDB")
# prepare a cursor object using cursor() method
cursor=db.cursor()

# drop table if it is already exits using execute method
cursor.execute(" DROP TABLE IF EXISTS STUDENTS")

# create column names from first libe in flist
first_name=flist[0][0]
last_name=flist[0][1]
roll_no=flist[0][2]
code=flist[0][3]
year=flist[0][4]
college=flist[0][5]

len_firstrow=len(firstrow)
# crate student table
querycreatestudenttable = """CREATE TABLE STUDENTS({} varchar(255) not null,{} varchar(255) not null,{} varchar(255) not null ,{} varchar(255) ,{} varchar(255) not null,{} varchar(255) not null)""".format(first_name,last_name,roll_no,code,year,college)

cursor.execute(querycreatestudenttable)
del flist[0]
# print(flist)
rows= ""
for i in range(len(flist)-1):
    rows += "{'{}','{}','{}','{}','{}','{}'".format(flist[i][0],flist[i][1],flist[i][2],flist[i][3],flist[i][4],flist[i][5])
    if i != (len(flist)- 2):
        rows += ","

queryInsert="Insert INTO Student table" + rows

try:
    cursor.execute(queryInsert)
    db.commit()
except:
    db.rollback()

db.close()
