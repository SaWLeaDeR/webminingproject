
library("rvest")
library("httr")
library(rstudioapi)
options(encoding = "UTF-8")

# the following line is for getting the path of your current open file
current_path <- getActiveDocumentContext()$path 
# The next line set the working directory to the relevant one:
setwd(dirname(current_path ))
# you can make sure you are in the right directory
print( getwd() )


websites <- c("https://news.google.com/news/?ned=tr_tr&gl=TR&hl=tr",
              "https://news.google.com/news/headlines/section/topic/WORLD.tr_tr/D%C3%BCnya?ned=tr_tr&hl=tr&gl=TR",
              "https://news.google.com/news/headlines/section/topic/NATION.tr_tr/T%C3%BCrkiye?ned=tr_tr&hl=tr&gl=TR",
              "https://news.google.com/news/headlines/section/topic/BUSINESS.tr_tr/Ekonomi?ned=tr_tr&hl=tr&gl=TR",
              "https://news.google.com/news/headlines/section/topic/SCITECH.tr_tr/Bilim%2FTeknoloji?ned=tr_tr&hl=tr&gl=TR",
              "https://news.google.com/news/headlines/section/topic/ENTERTAINMENT.tr_tr/Magazin?ned=tr_tr&hl=tr&gl=TR",
              "https://news.google.com/news/headlines/section/topic/SPORTS.tr_tr/Spor?ned=tr_tr&hl=tr&gl=TR",
              "https://news.google.com/news/headlines/section/topic/HEALTH.tr_tr/Sa%C4%9Fl%C4%B1k?ned=tr_tr&hl=tr&gl=TR")
              


getData <- function(website) {
  data <- data.frame()
  webpage <- read_html(website)
  data <- html_nodes(webpage,".Cc0Z5d .VDXfz")
  data_2 <- html_nodes(webpage,".Cc0Z5d  , .dIH98c")
  data2_title <- html_text(data_2)
  data2_title[data2_title == ""] <- NA
  data2_img <- html_attr(data_2,"src")
  data2_img <- c(NA,data2_img) 
  data2_img <- data2_img[1:(length(data2_img)-1)]
  
  
  for (i in 1:length(data2_title)) {
    if (is.na(data2_title[i])) {
      data2_title <- data2_title[-c(i)]
      data2_img <- data2_img[-c(i)]
    }
  }
  
  data2_link <-  html_attr(data,"href")
  
  data2_link <- gsub("^./","" , data2_link)
  data2_link <- paste("https://news.google.com/", data2_link , sep="" )
  data2.df <- data.frame(data2_title,data2_link,data2_img)
  names(data2.df) <- c("title","link","img")
  data3.df <- data2.df[(data2.df$title != ""),]
  data3.df[,3] <- as.character(data3.df[,3])
  sayi <- nrow(data3.df)
  for (i in 1:sayi) {
    if (is.na(data3.df[i,3])) {
      print('here')
      data3.df[i,3] <- 'https://drive.google.com/file/d/1o_a7qyvWlg2c8zJ9S1SMSADxnWlJ2B0T/view?usp=sharing'
      
    }
    else {
      print('end')
    }
    
  }
  return (data3.df)
  
}
  





i <- 1
data.names <- c("headlines","world","turkey","economy","scienceandtech","mag","sport","health")

for (website in websites){
  temp <- getData(website)
  assign(paste("data",data.names[i],sep="."),temp)

  print(data.names[i])
  write.csv(temp,paste(file = paste("data",data.names[i],"csv",sep=".")),row.names = FALSE,fileEncoding = "UTF-8")
  
  
  i <- i +1
  }
  


  
