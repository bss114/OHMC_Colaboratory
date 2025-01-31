library(tidyverse)
library(readxl)

dat<-clipr::read_clip_tbl()
dat %>%
  pivot_longer(!Row) %>%
  mutate(name=gsub("X","", name)) %>%
  filter(!is.na(value)) %>%
  mutate(wells=paste0(Row, name)) %>%
  pull(wells) %>%
  paste(collapse = "','") %>%
  clipr::write_clip()
