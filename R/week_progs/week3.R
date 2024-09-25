# r program on access and manipulate list

l=list(c(1:10),list(20:30),c('omg','india')) # create
l # access

l1<-(1:10)
l1[1] # access
l1[2]<-500  # modify
l1[2]
l1[-2] # delete



# list-> vector
ls<-list(1:20)
typeof(ls)
print(ls)
ls1<-unlist(ls)
typeof(ls1)
print(ls1)
