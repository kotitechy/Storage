x<-1:5
x
n<-6:10
n
y<-c(x,n)
z=append(x,n)
print(y)
print(z)
#--------------------
#create vector
x<-1:5
n<-letters[1:5]
y<-c(x,n)
print(y)
typeof(y)
print(x)
typeof(n)
#------------
x<-1:5
x<-append(x,6:10)
print(x)
#------------
v1<-c(1,2,3,4)
v1[5]<-5
v1[6]<-6
v1
#write a r program to crete and name the vector
x<-c(1,5,4,9,0)
typeof(x)
class(x)
length(x)
y<-c(1,5.4,TRUE,"hello")
y
typeof(y)
class(y)
length(y)
#creating a character vector
fruits<-c("apple","banana","cherry")
names(fruits)<-c("fruit1","fruit2","fruit3")
print("named character vector:")
print(names)
#-----------------------------------

#week1 b)write a program inplement vector 
x<-1:15
cat("original vector: ",x, "\n")
#subsetting vector
cat("first 5 values of vector:", x[1:5],"\n")
cat("without values present at index 1,2 and 3:")
x[-c(1,2,3)],"\n"
