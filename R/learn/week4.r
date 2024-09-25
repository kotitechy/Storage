# if 
a<-10
if(a>5){
  print("a is greater than 5")
}
# if-else
a<-10
if(a==10){
  print("a is 10")
}else{
  print("a != 10")
}
# nested-if
a<-10
b<-20
c<-30
if(a>b){
  if(a>c){
    print("a is big")
  }else{
    print("b>a")
  }
}

# for loop
for (i in 1:10){
  print(i)
}
# nested for loop
a<-list('red','yeloow','tasty')
f<-list('apple','banana','mango')
for (i in a){
  for(j in f){
    print(paste(i,j))
  }
}
# while loop
i<- 1
while(i<6){
  print(i)
  i<-i+1
}
# repeat loop
i<-1
repeat{
  print(i)
  i<-i+1
  if(i==10){
    break
  }
}
# break, next
for(i in 1:10){
  if(i<=5){
    next
  }
  if(i==8){
    break
  }
  print(i)
}
# return statement
check<-function(x){
  if(x>0){
  result<-"Positive"
  }else if(x<0){
    result<-"negative"
  }else{
    result<-"Zero"
  }
  return (result)
}
check(10)