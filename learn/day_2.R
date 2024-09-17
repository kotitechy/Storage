#day-2 lab p1
fruits <- c("apple","pineapple","Orange")
fruits[1:1]
paste("length of vector: ", length(fruits))
numbers <- c(10,20,30)
# range of numbers
numbers <- 10:1
numbers
# sort a vector
sort(fruits)
sort(numbers)
# access the vector
fruits[3]
# changing vector value
fruits[3] <-"coconut"
fruits[3]
# repeat numbers in vector
numbers=1:3
repeatnums <- rep(numbers,each=3)
repeatnums
# repeat a vector for n times
repeatnums <- rep(numbers,times=3)
repeatnums
# repeat vector for elements of vector times
rn <- rep(c(1,2,3),times=c(2,2,4))
rn
# 
print(2 %in% rn)
# sequence of vectors
n <- seq(from=0,to=100,by=20)
n
n[1:4]