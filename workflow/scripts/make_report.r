library(rmarkdown)



plot <- normalizePath(snakemake@input[["plot"]])
classes <- normalizePath(snakemake@input[["classes"]])
prediction <- normalizePath(snakemake@input[["prediction"]])
Train_test_distribution <- normalizePath(snakemake@input[["Train_test_distribution"]])
history <- normalizePath(snakemake@input[["history"]])
Train_test_distribution <- normalizePath(snakemake@input[["Train_test_distribution"]])
eval <- normalizePath(snakemake@input[["eval"]])
loss <- normalizePath(snakemake@input[["loss"]])

render("scripts/Report.Rmd", 
       output_format = "pdf_document", 
       output_dir=dirname(normalizePath(snakemake@output[[1]])),
       output_file=basename(normalizePath(snakemake@output[[1]]))
       )
