plot(1,3)
plot(c(10,20),c(1,2))
# multiple points
x=seq(1,100,by=5)
y=seq(1,1000,by=50)
plot(x,y)
# line graph
plot(1:10,type='l')
#sequence
plot(1:20)

#labelling
plot(x,y,main="Diabetic graph",xlab='people',ylab='level')
# add color
plot(x,y,main="Diabetic graph",xlab='people',ylab='level',col='RED')
# size
plot(x,y,main="Diabetic graph",xlab='people',ylab='level',col='RED',cex=1)
# shape of pointer
plot(x,y,main="Diabetic graph",xlab='people',ylab='level',col='RED',cex=1,pch=20)
