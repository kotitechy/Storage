v<-2:10  # new vector
print(v) 
v[3] # index 3 element
v[c(3,5)] # new sub vector with values at index 3,5
v[-c(3,5)] # vector with eliminating particular indexes
v[c(-3,-5)] # similar to above
v[c(3,5)] # similar to above but adds index 5
# create 
data<-c(1,2,3,4,5,6)
thismatrix <- matrix(data,nrow=3,ncol=2,byrow=TRUE)
thismatrix
thismatrix[3]
# matrix of strings
data=c('1','2','3','4','5','6')
strmat = matrix(data,nrow=2,ncol=3,byrow=TRUE)
strmat[3] # row priority
# matrix access specific value
data<-c(1,2,3,4,5,6,7,8,9)
thismatrix <- matrix(data,nrow=3,ncol=3)# as if we do not mention by row it will take as column wise
thismatrix
thismatrix[1,3] # get value3
thismatrix[1,]# matrix print row
thismatrix[,2]# matrix print 
# ex-
data=c('apple','banana','cherry','orange')
m=matrix(data,nrow=2,ncol=2)
m
m[1,2]
m[2,]
m[,1]
# ex-
m<-matrix(c('apple','banana','cherry','orange','grape','pineapple','pear','melon','fig'),nrow=3,ncol=3)
m
m[c(1,2),]# only that rows
m[,c(1,2)]
# adding columns to matrix
m1=cbind(m,c('strawberry','blueberry','rasberry'))
m1
# adding rows to matrix
m2=rbind(m1,c("mango","","",""))
m2
# chaned here
