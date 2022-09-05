# \n -> New Line
suppose = "This string has been \nsplit over \nseveral \nlines"
print(suppose)
"""output : This string has been
split over
several 
lines"""

# \t -> tab space
tab_space = "1\t2\t3\t4\t5"
print(tab_space)
#output : 1 2 3 4 5

#\ -> the blackslash is used to escape special characters such as quotes and double quotes
print("The customer asked, \"Why don\'t you sell books\"?")
#output : The customer asked, "Why don't you sell books"?
split_string = "This string has been \
split over \
several \
lines"
#output : This string has been split over several lines

# using 'r' -> raw string
print("c:\\users\\dhruva\\notes.txt")
print(r"c:\users\dhruva\notes.txt")
"""output : c:\users\dhruva\notes.txt
c:\users\dhruva\notes.txt"""

