library(tidyverse)
setwd("C:\\Users\\belokurowsr\\OneDrive - Kantar\\Desktop\\baseball-ods")

files = list.files(pattern = "baseballgames") %>% file.info() %>% rownames()

df = data.frame()
for (file in files){
  aux=read.csv(file) %>% mutate(filename = file)
  df = bind_rows(df,aux)
}
teams = readRDS("C:\\Users\\belokurowsr\\OneDrive - Kantar\\Desktop\\R pessoal\\mlb-winners\\data\\work\\teams.rds")

df= df  %>% #head(100) %>%
  filter(grepl(paste(teams$club_name, collapse = "|"), name_x) & !str_detect(name_x,"KIA|LG|Lotte|KT|Hiroshima|Tokyo|Yokohama|Chunichi|Yomiuri|Hanshin")) %>%
  mutate(day = as.Date(str_extract(filename, "\\d{8}"), format = "%Y%m%d"),
         hour = sub(".*([0-9]{4})\\.csv$", "\\1", filename),
         date2=as.Date(date))

res = readRDS("C:\\Users\\belokurowsr\\OneDrive - Kantar\\Desktop\\R pessoal\\mlb-winners\\data\\work\\df2.rds")

dftotal = data.frame()
totalgames= data.frame()
#dates = c("2023-04-16","2023-04-17","2023-04-18","2023-04-25","2023-05-02","2023-05-03","2023-05-09")
dates = unique(res$officialDate)[unique(res$officialDate)<Sys.Date()]
for (i in dates){
  print(i)
  #i = "2023-04-14"
  res2 = res %>% #filter(officialDate %in% c("2023-04-14", "2023-04-16", "2023-04-17")) %>%
    select(game_pk,gameDate,officialDate,teams.home.team.name,teams.away.team.name,teams.home.score,teams.away.score,teams.home.isWinner,
           teams.home.leagueRecord.pct,teams.away.leagueRecord.pct) %>%
    filter(officialDate == i) %>%
    left_join(teams %>% select(team_full_name,home = club_name),by=c("teams.home.team.name"="team_full_name")) %>%
    left_join(teams %>% select(team_full_name,away = club_name),by=c("teams.away.team.name"="team_full_name")) %>%
    group_by(game_pk) %>% slice(1) %>% ungroup %>%
  group_by(teams.home.team.name,teams.away.team.name)%>% slice(1) %>% ungroup

# df %>% filter(day == date_check & isLive_x=="False") %>% #count(id_y,name_x)%>%
#   separate(name_x, c("home", "away"), " - ")  %>%
#   mutate( away = gsub("Cleveland ","",away),
#           home = gsub("Cleveland ","",home)) %>%
#   inner_join(res2) %>% arrange(game_pk)
#i="2023-05-03"
# df %>%
#   filter(date2 == i & isLive_x=="False") %>%
#   #filter(name_x =="Tigers - Mets") %>%
#   group_by(id_y,name_x) %>%
#   separate(name_x, c("home", "away"), " - ") %>%
#   mutate( away = gsub("Cleveland ","",away),
#           home = gsub("Cleveland ","",home),
#           name = gsub("Cleveland ","",name))%>%
#   group_by(id_y,lx) %>% slice_max(hour) %>%
#   group_by(home,away,date) %>% slice_max(day)

games = df %>%
  filter(date2 == i & isLive_x=="False") %>%
  #filter(name_x =="Tigers - Mets") %>%
  group_by(id_y,name_x) %>%
  separate(name_x, c("home", "away"), " - ") %>%
  mutate( away = gsub("Cleveland ","",away),
          home = gsub("Cleveland ","",home),
          name = gsub("Cleveland ","",name)) %>%
  #group_by(id_y,lx) %>% slice_max(hour) %>%
  group_by(home,away) %>% slice_max(date) %>% slice_max(day)%>%
  mutate(type = if_else(home==name,"home_odds","away_odds"))%>%slice_max(day) %>%
  slice_max(hour) %>%
  group_by(home,away) %>%
  pivot_wider(names_from=type,values_from=odds,id_cols=c(home,away))%>%
  inner_join(res2) %>% arrange(game_pk) %>%


  # group_by(id_y,lx,home,away)%>%
  # arrange(date ) %>%
  # filter(date == min(date)) %>%
  # select(home,away,name,odds) %>%
  # group_by(home,away) %>%
  # mutate(type = if_else(home==name,"home_odds","away_odds")) %>% View()
  #
  # slice_max(day) %>%
  # mutate(date3=as.POSIXct(date))%>%
  # as.data.frame() %>%
  # left_join(res2  %>%
  #   select(game_pk,gameDate,officialDate,teams.home.team.name,teams.away.team.name,home,away),
  #   by=c("date"="gameDate","home","away")) %>%
  # arrange(date) %>%
  # group_by(id_y,lx,home,away)%>%
  # filter(date == min(date)) %>% select(home,away,name,odds) %>%
  # group_by(home,away) %>%
  # mutate(type = if_else(home==name,"home_odds","away_odds")) %>%
  # pivot_wider(names_from=type,values_from=odds,id_cols=c(home,away))
  #
  #   arrange(date) %>%
  #   group_by(id_y,lx,home,away)%>%
  #   filter(date == min(date)) %>% select(home,away,name,odds) %>%
  #   group_by(home,away) %>%
  #   mutate(type = if_else(home==name,"home_odds","away_odds")) %>%

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

print(paste0("Games: ",nrow(games)))
  openxlsx::write.xlsx(games,paste0(format(as.Date(i), "%Y%m%d"),"_games.xlsx"))
  totalgames = bind_rows(totalgames,games)
  means = games %>%
    ungroup %>%
    summarize(mean_home_odds = mean(home_odds),
              mean_away_odds = mean(away_odds),
              mean_winner_odds = mean(winner_odds),
              mean_winner_margin = mean(winner_margin),
              mean_favorite_winpct = mean(favorite_won),
              mean_bestrecord_winpct = mean(best_record_won),
              mean_home_winpct = mean(teams.home.isWinner),
              mean_diff_record = mean(diff_record)) %>%
    pivot_longer(everything())



  multiples = games %>%
    ungroup %>%
    mutate(units = n(),
           units_triple = units/ceiling(units / 3),
           units_double = units/ceiling(units / 2),
           double = ceiling(row_number() / 2),
           triple = ceiling(row_number() / 3))
  paid = unique(multiples$units)

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


  results = games %>%
    ungroup %>% summarize(
      units = n(),
      units_triple = units/ceiling(units / 3),
      units_double = units/ceiling(units / 2),
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
        mutate(value = value-paid) %>%
        mutate(name="total triple")
    ) %>%
    bind_rows(doubles)%>%
    bind_rows(
      doubles %>%
        summarize(value=sum(value)) %>%
        mutate(value = value-paid) %>%
        mutate(name="total double")
    ) %>%
    bind_rows(means) %>%
    mutate(date=i)

  openxlsx::write.xlsx(results,paste0(format(as.Date(i), "%Y%m%d"),"_results.xlsx"))

  dftotal = bind_rows(dftotal,results)
}
totalgames %>%
  group_by(officialDate) %>%
  summarize(bw=mean(best_record_won))

dftotal %>% filter(name %in% c("units","bet_home","bet_away","bet_favorite","bet_underdog","total triple","total double")) %>%
  group_by(name) %>% summarize(sum(value))

totalgames %>%
  filter(best_record=="home") %>%
  select(best_record_won,home_odds,teams.home.isWinner,diff_record) %>%
  arrange(home_odds) %>%
  mutate(bin=cut(diff_record,c(0,0.05,0.1,0.2,0.25,0.3,1))) %>% group_by(bin) %>%
  summarize(mean(best_record_won),mean(home_odds),n())

#times da casa estão 7 de 8 quando diferença de vitórias > .200 e odds > 1.75
#times da casa estão 54 de 67 quando diferença de vitórias > .200
totalgames %>%
  filter(best_record=="home"&home_odds > 1.75) %>%
  select(best_record_won,home_odds,teams.home.isWinner,diff_record) %>%
  arrange(home_odds)  %>% filter(best_record_won)

#times de fora estão 25 de 29 quando diferença de vitórias > .300 (qualquer odd)
totalgames %>%
  filter(best_record=="away") %>%
  select(best_record_won,away_odds,teams.home.isWinner,diff_record) %>%
  arrange(away_odds) %>%
  mutate(bin=cut(diff_record,c(0,0.05,0.1,0.2,0.3,1))) %>% group_by(bin) %>%
  summarize(mean(best_record_won),mean(away_odds),n())

#times no total estão 55 de 61 quando diferença de vitórias > .300
totalgames %>%
  #filter(best_record=="home") %>%
  select(best_record_won,home_odds,winner_odds,teams.home.isWinner,diff_record) %>%
  arrange(home_odds) %>%
  mutate(bin=cut(diff_record,c(0,0.05,0.1,0.2,0.25,0.3,1))) %>% group_by(bin) %>%
  summarize(mean(best_record_won),mean(winner_odds),n())


totalgames %>% #filter(officialDate == "2023-04-30") %>%
  filter(diff_record > 0.25) %>%
  group_by(officialDate) %>%
  summarize(n=n(),b=sum(best_record_won)) %>%
  filter(n==b)

  summarize(mean(best_record_won))
