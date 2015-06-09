#Format strings and embedding variables in them.

my_name = 'Rito'
my_age = 20.564
my_age = round(my_age)
print "Hi, I am %s and I am %d years old.\n" % (my_name, my_age)

jokeValue = False
# Remember : capitalize False and not false.

x = "Print the jokevalue %r"

print x % jokeValue 