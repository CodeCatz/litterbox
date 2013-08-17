from kalkulator import calculate_score

print "Koliko si star/a?"
age = raw_input(">>> ")
while not age.isdigit():
    age = raw_input("ne se hecat, vnesi starost: ")

pogoj = True
print "si moski (0), ali zenska(1)?"
gender = raw_input(">>> ")
while pogoj:
    if not gender.isdigit():
        print "vpisi samo stevilke!"
    elif int(gender) < 0 or int(gender) > 1:
        print "samo prikazane vrednosti, prosim"
    else:
        pogoj = False
    if pogoj:
        gender = raw_input("0 (moski) ali 1 (zenska): ")

# spremenimo gender iz stevilke v enak input, kot za web
if gender == 0:
    gender = "male"
else:
    gender = "female"

complexity = calculate_score(gender, int(age))

print "Zapletenost tvojega zivljnja je ", complexity
