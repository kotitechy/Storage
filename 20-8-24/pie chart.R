#create 2 vectors and draw a pie chart
books=c(210,450,250,100,50,90)
subjects=c("r","java","ds","c","c++","python")
#creating piechart
pie(books,labels=subjects,col = "green",main="subject library")