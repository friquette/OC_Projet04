import models.m_player as m_player
import utility as utl

last_name = utl.ask_pattern("Nom: ")
first_name = utl.ask_pattern("Prenom: ")
birthdate = utl.ask_date("Date de naissance: ")
rank = utl.ask_int("Classement: ")

player = m_player.ModelPlayer(last_name, first_name, birthdate, rank)

print("Joueur: {} {}, né le {}. Classement: {}".format(player.last_name,
                                                       player.first_name,
                                                       player.birthdate,
                                                       player.rank))
