# OVERRIDE EXPLICITLY - Actions on the child override the action on the parent.

class Parent(object):

	def override(self):
		print "PARENT override()"

class Child(Parent):

	def override(self):
		print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()