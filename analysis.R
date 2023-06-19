library(tidyverse)
setwd("C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\baseball-odds\\data")


files = list.files(pattern = "baseballgames") %>% file.info() %>% rownames()

df = data.frame()
for (file in files[20:25]){
  aux=read.csv(file) %>% mutate(filename = file)
  df = bind_rows(df,aux)
}
df

#teams = readRDS("C:\\Users\\belokurowsr\\OneDrive - Kantar\\Desktop\\R pessoal\\mlb-winners\\data\\work\\teams.rds")
teams = readRDS("C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\baseball-odds\\data\\work\\teams.rds")

df= df  %>% #head(100) %>%
  filter(grepl(paste(teams$club_name, collapse = "|"), name_x) & !str_detect(name_x,"KIA|LG|Lotte|KT|Hiroshima|Tokyo|Yokohama|Chunichi|Yomiuri|Hanshin")) %>%
  mutate(day = as.Date(str_extract(filename, "\\d{8}"), format = "%Y%m%d"),
         hour = sub(".*([0-9]{4})\\.csv$", "\\1", filename))

res = readRDS("C:\\Users\\rafae\\OneDrive\\Área de Trabalho\\baseball-odds\\data\\work\\df2.rds")

res2 = res %>% #filter(officialDate %in% c("2023-04-14", "2023-04-16", "2023-04-17")) %>%
  select(game_pk,officialDate,teams.home.team.name,teams.away.team.name,teams.home.score,teams.away.score,teams.home.isWinner,
         teams.home.leagueRecord.pct,teams.away.leagueRecord.pct) %>% 
  filter(officialDate == "2023-04-17") %>%
  left_join(teams %>% select(team_full_name,home = club_name),by=c("teams.home.team.name"="team_full_name")) %>%
  left_join(teams %>% select(team_full_name,away = club_name),by=c("teams.away.team.name"="team_full_name"))


df %>% filter(day == "2023-04-17" & isLive_x=="False") %>% #count(id_y,name_x)%>%
  separate(name_x, c("home", "away"), " - ")  %>%
  mutate( away = gsub("Cleveland ","",away),
          home = gsub("Cleveland ","",home)) %>%
  inner_join(res2) %>% arrange(game_pk)

games = df %>% 
  filter(day == "2023-04-17" & isLive_x=="False") %>%
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
                              best_record == "away"& !teams.home.isWinner,TRUE,FALSE)) %>% 
  mutate(diff_record = if_else(teams.home.leagueRecord.pct>teams.away.leagueRecord.pct,
                               teams.home.leagueRecord.pct-teams.away.leagueRecord.pct,teams.away.leagueRecord.pct-teams.home.leagueRecord.pct))
games %>%
  ungroup %>% 
  summarize(mean(home_odds),
            mean(away_odds),
            mean(winner_odds),
            mean(winner_margin),
            mean(favorite_won),
            mean(best_record_won),
            mean(teams.home.isWinner),
            mean(diff_record))

games %>% group_by() %>% 
  
  
# %>% 
#   openxlsx::write.xlsx("teste3.xlsx")

multiples = games %>% 
  ungroup %>% 
  mutate(units = n(),
         units_triple = units/ 4,
         units_double = units/6,
         double = ceiling(row_number() / 2),
         triple = ceiling(row_number() / 3)) 

triples = multiples %>%
  group_by(triple) %>% 
  mutate(games=n(),won=sum(best_record_won)) %>%
  mutate(hit_not = if_else(won==games,"hit","not")) %>% 
  group_by(triple) %>% 
  mutate(total_winner=prod(winner_odds)) %>% 
  mutate(total_winner = ifelse(hit_not=="hit",total_winner*units_triple,0)) %>% 
  select(winner_odds,tail(colnames(.))) %>% 
  summarize(total_money=sum(unique(total_winner)))  %>% 
  mutate(triple = paste0("triple ",triple)) %>% 
  rename(name=triple,value=total_money)


doubles = multiples %>%
  group_by(double) %>% 
  mutate(games=n(),won=sum(best_record_won)) %>%
  mutate(hit_not = if_else(won==games,"hit","not")) %>% 
  group_by(double) %>% 
  mutate(total_winner=prod(winner_odds)) %>% 
  mutate(total_winner = ifelse(hit_not=="hit",total_winner*units_double,0)) %>% 
  select(winner_odds,tail(colnames(.))) %>% 
  summarize(total_money=sum(unique(total_winner))) %>% 
  mutate(double = paste0("double ",double)) %>% 
  rename(name=double,value=total_money)


games %>% 
  ungroup %>% summarize(
    units = n(),
    units_triple = ceiling(units/ 3),
    units_double = ceiling(units/2),
    bet_home = sum(home_odds[games$teams.home.isWinner==T])-units,
    bet_away = sum(away_odds[games$teams.home.isWinner==F])-units,
    bet_favorite = sum(winner_odds[games$favorite_won==T])-units,
    bet_underdog = sum(winner_odds[games$favorite_won==F])-units,
    bet_underdog = sum(winner_odds[games$best_record_won==T])-units
  ) %>% pivot_longer(everything()) %>% 
  bind_rows(triples) %>% 
  bind_rows(
    triples %>% 
      summarize(value=sum(value)) %>% 
      mutate(name="total triple")
  ) %>% 
  bind_rows(doubles)%>% 
  bind_rows(
    doubles %>% 
      summarize(value=sum(value)) %>% 
      mutate(name="total double")
  ) %>%
  mutate(date="2023-04-16") 
