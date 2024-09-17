# list -> collection of data
# list also called second type of vector 
# in vector we store only similiar dtypes and here we store different dtypes
# Create a list 
l1<-list("apple",'banana','cherry')
l1 
# check if it is a list
class(l1) # list
typeof(l1)
# nested list
l2<-list(c("nan",'fab','mat'),matrix(c(1,2,3,4,5,6),nrow=3,ncol=2,byrow=2),list("green",12,23))
l2
# naming the list
names(l2)
names(l2)='s'
names(l2)<-c('quarter','a_matrix','a list')
names(l2)
l2
l2['quarter']
# accessing list elements
l2[[1]][1]
l2[1]  
l2
# add element in a list 
l2[4]=1314
l2
# delete an element from the list
l2[4]<-NULL
l2
# update 
l2[3]='updated'
l2
# merging list
l3=list(c(l1,l2))
class(l3)
typeof(l3)
l3
l3[1]
l3[2]
l3[3]
l3[[2]][3] # last element of list 2
# converting list to vector
l=list(1:10) # list
typeof(l)    # list
class(l)    # list
l=unlist(l)  # conversion
typeof(l)   # vector of integers
class(l)    # integer
# vector of integers
l1=c(1:10)
l1
typeof(l1)
class(l1)
# adding 2 vectors gives addition of each element in the vector1 with each element of vector2
l3<-(l1+l)
l3
typeof(l3)
class(l3)

# list length
l=list(1:10)
l
length(l)
append(l,34,index=9)
l
