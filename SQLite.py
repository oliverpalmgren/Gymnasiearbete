import sqlite3
import time

# TA BORT ALLA HASHTAGS FÖR DEN DELEN AV KODEN DU VILL ANVÄNDA

### Startar en tidtagare så man kan se hur lång tid det tar för koden att köras igenom ###
start = time.time()

### Kopplar ihop databasen ###
dbase = sqlite3.connect('students.db')

mycursor = dbase.cursor()

print('Database opened')

################################################
### Skapar databasen om det inte finns någon ###
################################################
dbase.execute(''' CREATE TABLE IF NOT EXISTS student_records(
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INT NOT NULL,
    gender TEXT NOT NULL,
    class TEXT NOT NULL,
    program TEXT NOT NULL) ''')
################################################





#####################################################
### Skapar värden och lägger till dem i databasen ###
#####################################################

#sqlFormula = 'INSERT INTO student_records (first_name, last_name, age, gender, class, program) VALUES (?, ?, ?, ?, ?, ?)'

#studentall = [
#              ]

#mycursor.executemany(sqlFormula, studentall)

#dbase.commit()




####################################################
### Söker efter de olika produkterna som skapats ###
####################################################
def read_Data():
    data = dbase.execute(''' SELECT * FROM student_records ORDER BY last_name''')
    for record in data:                                            # Byt ut * mot något av dessa värden
        print('first_name : ' +str(record[0]))                     # first_name, last_name, age, gender, class, program
        print('last_name : ' +str(record[1]))                      # Om det är något specifikt du vill söka efter.
        print('age : ' +str(record[2]))
        print('gender : ' +str(record[3]))
        print('class : ' +str(record[4]))
        print('program : ' +str(record[5]) + '\n\n')

#read_Data()
###################################################




#######################################
### Uppdaterar de olika produkterna ###
#######################################
#def update_record():
#    dbase.execute(''' UPDATE student_records set class = '17TEa' ''')     # För specifik uppdatering skriv efter set ? = *
                                                                   # WHERE ? = *
#    dbase.commit()                                                 # ? är olika rader i databasen t.ex first_name
                                                                   # och * är ett värde för produkten i raden (?)
#update_record()                                                    # t.ex Adam
#read_Data()
######################################




#########################
### Raderar produkter ###
#########################
#def delete_record():
#    dbase.execute(''' DELETE FROM student_records ''')          # Raderar alla produkter från databasen.
#    dbase.commit()                                              # Skriv ( WHERE ? = * ) om du vill radera en/flera
                                                                # rader från databasen.
#delete_record()
#read_Data()
#########################



dbase.close()
print('Database closed')

#################################################
### Stannar tidtagaren när koden körts igenom ###
################################################
stop = time.time()

### Skriver ut tiden ###
print("Finished in", stop - start, "sec.")