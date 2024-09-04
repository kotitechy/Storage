m=matrix(c(1,2,3,4,5,6,7,8,9),nrow=3,ncol=3,byrow=2)
m
m[1] # first element at row 1 
m[3,] # returns full row
m[,3] # returns column at index 3
m[c(1,2)] # returns first elements in 1st 2 rows
m[,c(1,2)] # returns columns of specified
m[-c(1),] # returns except 1st row
m[-c(2),] # except 2nd row
m[,-c(1)] # column wise returns 2nd and 3rd column
m[-c(1)] # except 1st element in 1st row prints all by vertical wise
