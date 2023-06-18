library(tidyverse)
setwd("C:\\Users\\belokurowsr\\OneDrive - Kantar\\Desktop\\baseball-ods")

files = list.files() %>% file.info() %>% rownames()

df = data.frame()
for (file in files[20:25]){
  aux=read.csv(file) %>% mutate(filename = file)
  df = bind_rows(df,aux)
}
df
teams = readRDS("C:\\Users\\belokurowsr\\OneDrive - Kantar\\Desktop\\R pessoal\\mlb-winners\\data\\work\\teams.rds")

df %>% head() %>% filter( grepl(name_x,teams$club_name))

df= df  %>% #head(100) %>%
  filter(grepl(paste(teams$club_name, collapse = "|"), name_x) & !str_detect(name_x,"KIA|LG|Lotte|KT|Hiroshima|Tokyo|Yokohama|Chunichi|Yomiuri|Hanshin")) %>%
  mutate(day = as.Date(str_extract(filename, "\\d{8}"), format = "%Y%m%d"),
         hour = sub(".*([0-9]{4})\\.csv$", "\\1", filename))

res = readRDS("C:\\Users\\belokurowsr\\OneDrive - Kantar\\Desktop\\R pessoal\\mlb-winners\\data\\work\\df2.rds")
res %>% View()
res2 = res %>% filter(officialDate %in% c("2023-04-14", "2023-04-16", "2023-04-17")) %>%
  select(game_pk,officialDate,teams.home.team.name,teams.away.team.name,teams.home.score,teams.away.score,teams.home.isWinner,
         teams.home.leagueRecord.pct,teams.away.leagueRecord.pct) %>% filter(officialDate == "2023-04-17") %>%
  left_join(teams %>% select(team_full_name,home = club_name),by=c("teams.home.team.name"="team_full_name")) %>%
  left_join(teams %>% select(team_full_name,away = club_name),by=c("teams.away.team.name"="team_full_name"))


df %>% filter(day == "2023-04-16" & isLive_x=="False") %>% #count(id_y,name_x)%>%
  separate(name_x, c("home", "away"), " - ")  %>%
  mutate( away = gsub("Cleveland ","",away),
          home = gsub("Cleveland ","",home)) %>%
  inner_join(res2) %>% arrange(game_pk)

df %>% filter(day == "2023-04-17" & isLive_x=="False") %>%
  group_by(id_y,name_x) %>%
  #filter(name_x =="Red Sox - Angels") %>% #count(id_y,name_x)%>%
  separate(name_x, c("home", "away"), " - ") %>%
  group_by(lx) %>% slice_max(hour) %>% as.data.frame() %>% select(home,away,name,odds) %>%
  group_by(home,away) %>%
  mutate(type = if_else(home==name,"home_odds","away_odds")) %>%
  pivot_wider(names_from=type,values_from=odds,id_cols=c(home,away))%>%
  inner_join(res2) %>% arrange(game_pk)%>%
  mutate(favorite = case_when(
    home_odds <= (away_odds - 0.1) ~ "home",
    away_odds <= (home_odds - 0.1) ~ "away",
    TRUE ~ "tie"
  ),
    winner_odds = if_else(teams.home.isWinner==TRUE,home_odds,away_odds),
         winner_margin = if_else(teams.home.isWinner==TRUE,teams.home.score-teams.away.score,teams.away.score-teams.home.score),
  favorite_won = if_else(home_odds == winner_odds & favorite == "home"|
                          away_odds == winner_odds & favorite == "away",TRUE,FALSE),
  best_record = case_when(teams.home.leagueRecord.pct>teams.away.leagueRecord.pct~"home",
                          teams.home.leagueRecord.pct<teams.away.leagueRecord.pct~"away",
                          TRUE~"tie"),
  best_record_won = if_else(best_record=="home"& teams.home.isWinner |
                              best_record == "away"& !teams.home.isWinner,TRUE,FALSE)) %>% openxlsx::write.xlsx("teste.xlsx")
  clipr::write_clip()




res %>% filter(officialDate == "2023-04-16")
