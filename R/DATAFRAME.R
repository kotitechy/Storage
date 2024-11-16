# create a df
df=data.frame(
roll=c(17,16,20),
names=c('karthik','shiva','satish'),
distance=c('1km','20km','30km')
)
# display the df
df
# summarize the df finds mean median min max for the inetger values
summary(df)
# access df by index names
df['names']
# or
df$roll
# add new column and row
df=cbind(df,food=c('apple','watermelon','banana'))
df=rbind(df,c(21,'manish','78km','water'))
df         
# remove row 
d=df[-c(2),]
# remove column
d=df[,-c(2)]
# rows x columns of rows
dim(df)
# ncol, n row
ncol(df)
nrow(df)
# length
length(df)
#combining 2 df's
df1=data.frame(rolls=c(17,16,20,21),marks=c(10,11,12,14))
df2=data.frame(food=c('apple','watermelon','banana','water'),distance = c('1km','20km','30km',"43km"))
df3=cbind(df1,df2)
df3

