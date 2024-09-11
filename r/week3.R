# r program on access and manipulate list

l=list(c(1:10),list(20:30),c('omg','india'))
l
names(l) <- c('numbers','num','words')
l[['num']] # 
l[['num']][[1]][1]
