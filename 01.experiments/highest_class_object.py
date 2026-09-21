class First:
	pass

class Second(First):
	pass

print(Second.mro())
