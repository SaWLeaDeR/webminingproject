library(rvest)
library("XML")
library("httr")
setwd("/app/")

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
  data <- html_nodes(webpage,".kWyHVd .ME7ew")
  data2 <- html_nodes(webpage,".lmFAjc , .kWyHVd .ME7ew")
  img_data <- html_nodes(webpage,".lmFAjc")
  img_data <- html_attr(img_data,"src")
  data2_img <- html_attr(data2,"src")
  data2_img <- c(NA,data2_img) 
  data2_img <- data2_img[1:(length(data2_img)-1)]
  #data2_img <- na.omit(data2_img)
  data2_title <- html_text(data2)
  #data2_title <- data2_title[data2_title != ""]
  data2_link <-  html_attr(data2,"href")
  #data2_link <- na.omit(data2_link)
  data2.df <- data.frame(data2_title,data2_link,data2_img)
  names(data2.df) <- c("title","link","img")
  data3.df <- data2.df[(data2.df$title != ""),]
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
  


  
