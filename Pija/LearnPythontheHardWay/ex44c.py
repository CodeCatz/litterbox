# ALTER BEFORE OR AFTER - Actions on the child alter the action on the parent.
# This is a special case of overriding where you want to alter the behavior before or after the Parent class's version runs.

class Parent(object):

	def altered(self):
		print "PARENT altered()"

class Child(Parent):

	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()