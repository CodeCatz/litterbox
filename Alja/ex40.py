class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# my stuff

another_song = Song(["Summertime sadness..."])

another_song.sing_me_a_song()

lyrics = ["Bla bla bla"]

yet_another_song = Song(lyrics)

yet_another_song.sing_me_a_song()

print '-' * 10

# a much better example of classes and objects
# source: http://www.tutorialspoint.com/python/python_classes_objects.htm

class Employee:
   'Common base class for all employees'
   empCount = 0

   # this is stuff that gets initialized every time you add a new object
   # that's why you can increase the count with each new employee
   # in this case, every employee has a name and salary as argument
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   # .variable to call variable, .function() to call functions
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

# adding new objects, employees with two arguments
"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp3 = Employee("Boss", 10000)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()

emp3.displayCount()

print "Total Employee %d" % Employee.empCount

