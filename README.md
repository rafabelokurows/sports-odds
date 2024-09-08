# Scraping sports odds from sportsbook

Update 2024-09-08: I renamed the repository as I've just added a scraper for NFL game odds to go with the one for MLB games that was already in place. 

**Short-term Goal**: analyzing how the moneyline and odds move over time for a certain game  

**Long-term Goal**: seeing if we could make f*cking money with this 🤑

Using Python and Github Actions for now

- [x] Add fallback for when API call returns no rows
- [ ] Start analyzing results to see trends on odds for one side or another

# Next steps
* Carregar todos os arquivos com as odds
* Agrupar por dia e jogo
* Ver odd final e odd inicial
* Obter dados para os jogos pós 09/05
  
Calcular:
* odds médias vencedor
* odds médias favoritos
* margem média de vitória
  * total
  * favorito
  * dark horse
  * away
  * home
* diferença média entre favorito e underdog

Estratégias:
 * home_team
 * favorito
 * away_team
 * underdog
 * best_record
 * triplas
 * duplas
formas diferentes de agrupar duplas/triplas

Value bets:
favoritos grande margem com odd 1.8+
