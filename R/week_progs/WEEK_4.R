#1. (a) r prog on a. if-STATEMENT
age<-34
if(age>=18){
  print("U can vote")
}
# (b) if-else
age<-18
if(age<18){
  print("u are an minor u can't vote'")
}else if(age>=18){
  print("U can vote")
}else{
  print("invalid age")
}

# 2. for loop
nums<-list(1:10)
print(nums[1])
sum<-0
for (i in nums[[1]]){
  sum<-sum+i
}
print(paste("sum of 10 natural numbers : ",sum))
# (b) while loop
n<-5
if(n==1 || n==0){
  print("factorial is 1")
}else{
  i<-n
  fact<-1
  while(i>=1){
    fact<-fact*i
    i<- i - 1
  }
}
print(paste("Factorial is : ",fact))


# 3. w.a.r..program on repeat,break,next,return
sum_of_evens<-function(x){
  sum<-0
  repeat{
    if(x==20){
      return (sum)
      break
    }
    if(x%%2==0){
      print(paste(x," is even"))
      sum<-sum+x
      }else{
      next
    }
    x<-x+2
  }
}
sum_of_evens(0)