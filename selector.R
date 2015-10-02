args<-commandArgs(trailingOnly = TRUE)      #to pass the selector.sh arguments to R
input_file_path<-args[1]
output_file_path<-args[2]

# Read the input file

dat<-read.delim(input_file_path,sep="|",header=TRUE)
outdat <- dat[dat$feature_name == "onset_delta"  | 
            dat$feature_name == "onset_site"   |
            dat$feature_name == "Q1_Speech"    |
            dat$feature_name == "Q3_Swallowing"|
            dat$feature_name == "Q5_Cutting"   |
            dat$feature_name == "fvc_percent1" ,]
ind_cl <- 1
outdat <- rbind(c(paste("cluster: ",ind_cl,sep=""),rep("",dim(outdat)[2]-1)),as.matrix(outdat))
write.table(outdat, 
          file = output_file_path,
          sep = "|", 
          row.names = FALSE,
          col.names = FALSE,
          quote = FALSE)

