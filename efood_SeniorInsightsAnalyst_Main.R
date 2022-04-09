########################################
#EFOOD
########################################

#library 
LibrariesPath = "C:/Users/emakrand"
.libPaths(LibrariesPath)
#packages
install.packages("dplyr")
library(dplyr)
loadpackages = c("DBI", "RMySQL","readxl","data.table","xlsx","RODBC","RSQLite","sqldf","openxlsx","stringr")
lapply(loadpackages,FUN = require,character.only = TRUE)
#library(RMariaDB,lib.loc = LibrariesPath)

#set working directory
setwd("C:/Users/emakrand/work/Efood")
#list files
list.files()

#change locale settings to read greek
Sys.setlocale(category = "LC_ALL", locale = "Greek")

#import file 
#data=read.csv("ordersfinal.txt", header=TRUE, sep = ",",encoding="UTF-8")
Orders = as.data.table(read.csv("orders.csv",encoding="UTF-8"))

### check Orders dataset - data quality inspection
head(Orders)
dim(Orders)
str(Orders)
Orders[,.N] # 534270 rows
Orders[is.na(order_id)] # no blank orders
Orders[is.na(user_id)] # no blank users
Orders[is.na(city)] # no blank city
Orders[is.na(amount)] # no blank amount
Orders[is.na(paid_cash)] # no blank date
Orders[is.na(cuisine)] # no blank cuisine
# no blanks 

### data exploration
Orders[,max(amount)] # max: 204.8
Orders[,.SD[which.max(amount)]] #in Lamia, online payment, meat
Orders[,min(amount)] # min: 0.4 euros !!!!!
Orders[,mean(amount)] # avg: 8.5 euros
hist(Orders$amount) # most orders between 1-10 amount 
Orders[amount>50] # 466 orders with more than 50 euros

#convert date from char to date in case we need any calculation 
Orders=Orders[,order_timestamp:=as.Date(order_timestamp)]
Orders[,range(order_timestamp)]




#calculate some metrics per user_id following rfm approach
analysis_date <- max(Orders$order_timestamp)
rfm_df <- Orders %>% group_by(user_id) %>% summarise(Recency_efood = as.numeric(analysis_date- max(order_timestamp)), Frequency_efood = n(), Monetary_efood = sum(amount), AVGspent_efood = mean(amount))
nrow(rfm_df)

#focus on breakfast cuisine metrics
Orders[,Breakfast:=0]
Orders[cuisine=="Breakfast", Breakfast:=1]
Orders_breakfast <- Orders[(Orders$Breakfast!="0"), ]
# create a similar data with the above rfm logic for breakfast pickers 
analysis_date2 <- max(Orders_breakfast$order_timestamp)
rfm_df2 <- Orders_breakfast %>% group_by(user_id) %>% summarise(Recency_breakfast = as.numeric(analysis_date2 - max(order_timestamp)), Frequency_breakfast = n(), Monetary_breakfast = sum(amount), AVGspent_breakfast = mean(amount))
nrow(rfm_df2)

#calculate the last cuisine pick for each user 
LastInteractionIDLevel = Orders[,.SD[which.max(order_timestamp)], by=.(user_id)][,.( user_id,LastInteractionDate = order_timestamp,  LastCuisine = cuisine )]

#merge the datasets
OrdersJanuary = merge(x=rfm_df,y=rfm_df2,by="user_id",all.x=TRUE)
OrdersJanuary2 = merge(x=OrdersJanuary,y=LastInteractionIDLevel,by="user_id",all.x=TRUE)


#export and save data 
write.csv(OrdersJanuary2,"C:/Users/emakrand/work/Efood/OrdersJanuary.csv", row.names = FALSE, sep = "|", quote=FALSE)
#save rdata
save(list = ls(.GlobalEnv), file = "C:/Users/emakrand/work/Efood/OrdersJanuary.rdata" )

