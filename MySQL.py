import mysql.connector
import time

# TA BORT ALLA HASHTAGS FÖR DEN DELEN AV KODEN DU VILL ANVÄNDA

start = time.time()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123password",
    database ="testdb"
)

mycursor = mydb.cursor()




########################
### Skapar en tabell ###
########################

mycursor.execute("CREATE TABLE IF NOT EXISTS students (first_name VARCHAR(100), last_name VARCHAR(100)," +
                 "age INTEGER(10), gender VARCHAR(100), class VARCHAR(100), program VARCHAR(100))")








########################
### Skapar produkter ###
########################

#sqlFormula = "INSERT INTO students (first_name, last_name, age, gender, class, program) VALUES (%s, %s, %s, %s, %s, %s)"

#studentall = [
#              ]

#mycursor.executemany(sqlFormula, studentall)

#mydb.commit()




##################################
### Söker efter alla produkter ###
##################################

#mycursor.execute("SELECT * FROM students")

#myresult = mycursor.fetchall()

#for row in myresult:
#    print(row)








########################
### Specifik sökning ###
########################

#sql = "SELECT * FROM students WHERE first_name = %s"

#mycursor.execute(sql, ("Amanda", ))

#myresult = mycursor.fetchall()

#for result in myresult:
#    print(result)









#################################
### Lägger värderna i ordning ###
#################################

#sql = "SELECT * FROM students ORDER BY age DESC" #DESC, flippar ordningen. T.ex age börjar med äldsta istället för yngst

#mycursor.execute(sql)

#myresult = mycursor.fetchall()

#for r in myresult:
#    print(r)








##############################
### Uppdaterar produkterna ###
##############################

#sql = "UPDATE students SET class = '17TEa' "

#mycursor.execute(sql)

#mydb.commit()










############################################
### Raderar värderna eller hela tabellen ###
############################################

#sql = "DROP TABLE IF EXISTS students" # Raderar hela tabellen

#sql = "DELETE FROM students " # Raderar alla rader som stämmer överräns med input värdet

#mycursor.execute(sql)

#mydb.commit()


stop = time.time()

print("Finished in", stop - start, "sec")
