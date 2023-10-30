'''
12. Ne imaginam o echipa de fotbal pt teren sintetic.
3 Schimbari maxime admise:

?	Declara o Lista cu 5 jucatori
?	Schimbari_efectuate = te joci tu cu valori diferite
?	Schimbari_max = 3

Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
-	Efectueaza schimbarea
-	Sterge jucatorul scos din lista
-	Adauga jucatorul intrat
-	Afisaza a intrat x, a iesit y, mai ai z schimbari

Daca jucatorul nu e in teren:
-	Afisaza nu se poate efectua schimbarea deoarece jucatorul x nu e in teren
-	Afisaza mai ai z schimbari

Testeaza codul cu diferite valori
'''

def substitute(player_in, player_out,players_off_field:list, players_on_field:list, no_of_substituted_players, max_substitutions):
    if no_of_substituted_players < max_substitutions:
        if player_out in players_on_field and player_in in players_off_field:
            players_off_field.remove(player_in)
            players_on_field.remove(player_out)
            players_on_field.append(player_in)
            players_off_field.append(player_out)
            no_of_substituted_players += 1
            print(f'A intrat {player_in} si a iesit {player_out}')
            print(f'Mai ai {max_substitutions - no_of_substituted_players} schimbari')
        else:
            print('Nu se poate efectua schimbarea')
    else:
        print('Nu mai ai schimbari disponibile')

    return players_on_field, players_off_field, no_of_substituted_players


max_substitutions = 3
players_team_1 = ['player 1', 'player 2', 'player 3', 'player 4', 'player 5']
players_on_field_team_1 = ['player 1', 'player 2', 'player 3']
players_off_field_team_1 = list(set(players_team_1) - set(players_on_field_team_1))
no_substituted_players_team_1 = 0

players_on_field_team_1, players_off_field_team_1, no_substituted_players_team_1 = substitute ('player 4',
           'player 1',
           players_off_field_team_1,
           players_on_field_team_1,
           no_substituted_players_team_1,
           max_substitutions)

print(players_on_field_team_1)
print(players_off_field_team_1)

print('Aceasta este o schimbare')
