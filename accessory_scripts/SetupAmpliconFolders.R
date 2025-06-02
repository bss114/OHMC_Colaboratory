#!/usr/bin/env Rscript

message("#################################################################################################################")
message("#Amplicon processing setup v0.01")
message("#J Bisanz 2 June 2025")
message("#Parses projects for an amplicon run and creates a per-project run folder")
message("#################################################################################################################")
message(" ")


suppressMessages(library(optparse))
option_list = list(
  make_option(c("-t", "--tracking"),    type="character",                        help="Index Tracking Excel File",                              metavar="character"),
  make_option(c("-r", "--reads"),       type="character",                        help="Absolute File Path to Read Directory",                   metavar="character"),
  make_option(c("-n", "--threads"),     type="numeric",     default="48",        help="Total number of threads to be used across all projects", metavar="character"),
  make_option(c("-o", "--outdir"),      type="character",   default="processed", help="Output folder",                                          metavar="character")
)

opt_parser = OptionParser(option_list=option_list)
opt = parse_args(opt_parser)

if (is.null(opt$tracking) | is.null(opt$reads)){
  print_help(opt_parser)
  stop("Specify the ampification results (--csv), tracking sheet (--tracking), instrument (--instrument), and plate ID (--plateid)")
}



library(tidyverse)
library(readxl)

#setwd("/data/SequencingRuns/2025May05_Amplicon10/")
#samplesheet<-"/data/SequencingRuns/2025May05_Amplicon10/jbmod_Amplicon10_IndexTrackingSheet_22May2025.xlsx"
#dat<-read_excel(samplesheet, "SampleSheet.csv", skip=19)
#reads<-"/data/SequencingRuns/2025May05_Amplicon10/reads"

samplesheet<-opt$tracking
dat<-read_excel(samplesheet, "SampleSheet.csv", skip=19)
reads<-opt$reads

projectsums<-dat %>% mutate(Project=gsub("_..+","", Sample_ID)) %>% group_by(Project) %>% summarize(SampleN=n()) %>% filter(Project!="Controls")
threadspersample<-opt$threads/sum(projectsums$SampleN) #threads per sample


dir.create(opt$outdir)
download.file("https://github.com/BisanzLab/OHMC_Colaboratory/raw/refs/heads/main/analysis_scripts/AmpliconSeq_q2.Rmd", paste0(opt$outdir, "/AmpliconSeq_q2_template.Rmd"))

for (p in projectsums$Project){
  dir.create(paste0(opt$outdir, "/", p))
  q2  <- readLines(paste0(opt$outdir, "/AmpliconSeq_q2_template.Rmd"))
  q2  <- gsub(pattern = "PROJECTPREFIXHERE", replace = p, x = q2)
  q2  <- gsub(pattern = "\\/data\\/SequencingRuns\\/PATHTOTRACKINGSHEET", replace = samplesheet, x = q2)
  q2  <- gsub(pattern = "\\/data\\/SequencingRuns\\/PATHTOSEQS", replace = reads, x = q2)
  
  ncores<-round(projectsums %>% filter(Project==p) %>% .$SampleN * threadspersample)
  if(ncores>18){ncores=18}
  if(ncores<4){ncores=4}
  q2  <- gsub(pattern = "NSLOTS=32", replace = paste0("NSLOTS=",ncores), x = q2)
  message(paste("Running", p, "with", ncores, "cores in", paste0(opt$outdir,"/",p)))
  writeLines(q2, paste0(opt$outdir, "/", p,"/AmpliconSeq_q2.Rmd"))
  }
