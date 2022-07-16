# amazon-top-30
 Analyzes the top 30 books on Amazon

This script was began on July 1st 2022 for a data science class,
and I only got acess to the code on the 5th, meaning I missed the
week of July 1st in this data. The data was collected by using the
wayback machine on archive.org. The title of the weeks are a bit
confusing, since 4/29/22 is marked as week ten, since it was the
last data point that I collected, and 7/5/22 is marked as week one,
since it was the first data point that I collected.

The multiple txt files are all the html code from the top books on
amazon.com, and were all gotten with the help from the wayback
machine. This code goes through every txt file, and looks for 
certain tags to help find certain attributes, specifically it looks
for the name of the book, the placement (1-30), and something that 
wasn't used in the code but was still searched for, was the price.
The program then puts the data into dictionaries, and plots two
graphs from the data.

The program outputs two plots, the first being titled "Weeks in
the top 30," which is a bar graph that shows how many books (y axis)
were in the top 30 for how many weeks (x axis). The second graph is
a line graph titled "Most occuring books on amazon top 30 through
the weeks," which shows the books which occured in the top 30 for
all ten weeks. There is then a line graph that shows the placement
of the book (y axis) throughout the weeks (x axis) for each book.

When the program runs, the first plot will show, and the second
plot will be shown after you close the first.