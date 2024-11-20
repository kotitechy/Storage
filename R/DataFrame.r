df = read.csv("D:/24915A0516/DATASET/CardioGoodFitness.csv",stringsAsFactors = F)
print(head(df))
mean(df$Fitness)
mean(df$Miles)
mean(df$Education)

mean(df$Age)
median(df$Age)


install.packages("data.table")
library(data.table)
df = fread("D:/24915A0516/DATASET/CardioGoodFitness.csv")
dt=data.table(df)
dt

