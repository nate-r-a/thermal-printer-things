from datetime import datetime
import collections

try:
  from Adafruit_Thermal import *
  printer = Adafruit_Thermal("/dev/ttyUSB0", 19200, timeout = 5)
  # Set default settings for printer and print 
  # some test lines to get it warmed up
  printer.setDefault()
  printer.println("")
  printer.println("================================")
  printer.println("")
except Exception:
  pass

#######
# On loaded schedule page:
# Spring 2018
# Bladerunners:
# http://starcenter.hockeyshift.com/stats#/30/schedule?team_id=32106&all
# Direwolves:
# http://starcenter.hockeyshift.com/stats#/30/schedule?team_id=31967&all
# $("tbody").attr("ng-init")
#######

# Can probably figure out a way to get these from BeautifulSoup one of these days
# Bladerunners
br_sch = '''
[{"type":"game","id":"g-167130","league_id":30,"season_id":1132,"tournament_id":null,"game_id":167130,"number":null,"datetime":"2018-04-14T20:00:00+00:00","datetime_tz":"2018-04-15 01:00:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":"2018-04-15 02:24:04 +0000","created_at":"2018-04-06 11:49:20 +0000","home_team_id":32106,"home_team":"RC Bladerunners","home_team_short":"RC - Blad","home_team_logo_url":null,"away_team_id":32108,"away_team":"RC Wolves","away_team_short":"RC - Wolv","away_team_logo_url":null,"home_division_id":4657,"home_division":"RC - C League","away_division_id":4657,"away_division":"RC - C League","home_score":5,"away_score":4,"facility_id":146,"facility":"Richardson","facility_address":"522%20Centennial%20Blvd%2C%20Richardson%2C%20Usa%2C%2075081","rink_id":18,"rink":"RC - Red Rink","game_type":"Regular Season","notes":null,"status":"Final","overtime":true,"shootout":true,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-04-14"},{"type":"game","id":"g-167135","league_id":30,"season_id":1132,"tournament_id":null,"game_id":167135,"number":null,"datetime":"2018-04-21T21:15:00+00:00","datetime_tz":"2018-04-22 02:15:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-04-06 11:49:21 +0000","home_team_id":32103,"home_team":"RC Hitmen","home_team_short":"Hitmen","home_team_logo_url":null,"away_team_id":32106,"away_team":"RC Bladerunners","away_team_short":"RC - Blad","away_team_logo_url":null,"home_division_id":4657,"home_division":"RC - C League","away_division_id":4657,"away_division":"RC - C League","home_score":0,"away_score":0,"facility_id":146,"facility":"Richardson","facility_address":"522%20Centennial%20Blvd%2C%20Richardson%2C%20Usa%2C%2075081","rink_id":18,"rink":"RC - Red Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-04-21"},{"type":"game","id":"g-167139","league_id":30,"season_id":1132,"tournament_id":null,"game_id":167139,"number":null,"datetime":"2018-04-28T21:15:00+00:00","datetime_tz":"2018-04-29 02:15:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-04-06 11:49:21 +0000","home_team_id":32106,"home_team":"RC Bladerunners","home_team_short":"RC - Blad","home_team_logo_url":null,"away_team_id":32109,"away_team":"Team Hanson","away_team_short":"Team Hans","away_team_logo_url":null,"home_division_id":4657,"home_division":"RC - C League","away_division_id":4657,"away_division":"RC - C League","home_score":0,"away_score":0,"facility_id":146,"facility":"Richardson","facility_address":"522%20Centennial%20Blvd%2C%20Richardson%2C%20Usa%2C%2075081","rink_id":18,"rink":"RC - Red Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-04-28"},{"type":"game","id":"g-167140","league_id":30,"season_id":1132,"tournament_id":null,"game_id":167140,"number":null,"datetime":"2018-05-02T21:00:00+00:00","datetime_tz":"2018-05-03 02:00:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-04-06 11:49:21 +0000","home_team_id":32106,"home_team":"RC Bladerunners","home_team_short":"RC - Blad","home_team_logo_url":null,"away_team_id":32108,"away_team":"RC Wolves","away_team_short":"RC - Wolv","away_team_logo_url":null,"home_division_id":4657,"home_division":"RC - C League","away_division_id":4657,"away_division":"RC - C League","home_score":0,"away_score":0,"facility_id":146,"facility":"Richardson","facility_address":"522%20Centennial%20Blvd%2C%20Richardson%2C%20Usa%2C%2075081","rink_id":18,"rink":"RC - Red Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-05-02"},{"type":"game","id":"g-167146","league_id":30,"season_id":1132,"tournament_id":null,"game_id":167146,"number":null,"datetime":"2018-05-12T20:00:00+00:00","datetime_tz":"2018-05-13 01:00:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-04-06 11:49:21 +0000","home_team_id":32105,"home_team":"Lemmings","home_team_short":"Lemmings","home_team_logo_url":null,"away_team_id":32106,"away_team":"RC Bladerunners","away_team_short":"RC - Blad","away_team_logo_url":null,"home_division_id":4657,"home_division":"RC - C League","away_division_id":4657,"away_division":"RC - C League","home_score":0,"away_score":0,"facility_id":146,"facility":"Richardson","facility_address":"522%20Centennial%20Blvd%2C%20Richardson%2C%20Usa%2C%2075081","rink_id":18,"rink":"RC - Red Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-05-12"},{"type":"game","id":"g-167151","league_id":30,"season_id":1132,"tournament_id":null,"game_id":167151,"number":null,"datetime":"2018-05-19T21:15:00+00:00","datetime_tz":"2018-05-20 02:15:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-04-06 11:49:22 +0000","home_team_id":32107,"home_team":"RC Hangovers","home_team_short":"Hangovers","home_team_logo_url":null,"away_team_id":32106,"away_team":"RC Bladerunners","away_team_short":"RC - Blad","away_team_logo_url":null,"home_division_id":4657,"home_division":"RC - C League","away_division_id":4657,"away_division":"RC - C League","home_score":0,"away_score":0,"facility_id":146,"facility":"Richardson","facility_address":"522%20Centennial%20Blvd%2C%20Richardson%2C%20Usa%2C%2075081","rink_id":18,"rink":"RC - Red Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-05-19"},{"type":"game","id":"g-167155","league_id":30,"season_id":1132,"tournament_id":null,"game_id":167155,"number":null,"datetime":"2018-05-26T21:15:00+00:00","datetime_tz":"2018-05-27 02:15:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-04-06 11:49:22 +0000","home_team_id":32106,"home_team":"RC Bladerunners","home_team_short":"RC - Blad","home_team_logo_url":null,"away_team_id":32110,"away_team":"Top Corns","away_team_short":"Top Corns","away_team_logo_url":null,"home_division_id":4657,"home_division":"RC - C League","away_division_id":4657,"away_division":"RC - C League","home_score":0,"away_score":0,"facility_id":146,"facility":"Richardson","facility_address":"522%20Centennial%20Blvd%2C%20Richardson%2C%20Usa%2C%2075081","rink_id":18,"rink":"RC - Red Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-05-26"},{"type":"game","id":"g-167158","league_id":30,"season_id":1132,"tournament_id":null,"game_id":167158,"number":null,"datetime":"2018-06-02T20:00:00+00:00","datetime_tz":"2018-06-03 01:00:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-04-06 11:49:23 +0000","home_team_id":32109,"home_team":"Team Hanson","home_team_short":"Team Hans","home_team_logo_url":null,"away_team_id":32106,"away_team":"RC Bladerunners","away_team_short":"RC - Blad","away_team_logo_url":null,"home_division_id":4657,"home_division":"RC - C League","away_division_id":4657,"away_division":"RC - C League","home_score":0,"away_score":0,"facility_id":146,"facility":"Richardson","facility_address":"522%20Centennial%20Blvd%2C%20Richardson%2C%20Usa%2C%2075081","rink_id":18,"rink":"RC - Red Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-06-02"},{"type":"game","id":"g-167161","league_id":30,"season_id":1132,"tournament_id":null,"game_id":167161,"number":null,"datetime":"2018-06-06T22:15:00+00:00","datetime_tz":"2018-06-07 03:15:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-04-06 11:49:23 +0000","home_team_id":32106,"home_team":"RC Bladerunners","home_team_short":"RC - Blad","home_team_logo_url":null,"away_team_id":32104,"away_team":"Ice Cats","away_team_short":"Ice Cats","away_team_logo_url":null,"home_division_id":4657,"home_division":"RC - C League","away_division_id":4657,"away_division":"RC - C League","home_score":0,"away_score":0,"facility_id":146,"facility":"Richardson","facility_address":"522%20Centennial%20Blvd%2C%20Richardson%2C%20Usa%2C%2075081","rink_id":18,"rink":"RC - Red Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-06-06"},{"type":"game","id":"g-167164","league_id":30,"season_id":1132,"tournament_id":null,"game_id":167164,"number":null,"datetime":"2018-06-13T20:00:00+00:00","datetime_tz":"2018-06-14 01:00:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-04-06 11:49:23 +0000","home_team_id":32110,"home_team":"Top Corns","home_team_short":"Top Corns","home_team_logo_url":null,"away_team_id":32106,"away_team":"RC Bladerunners","away_team_short":"RC - Blad","away_team_logo_url":null,"home_division_id":4657,"home_division":"RC - C League","away_division_id":4657,"away_division":"RC - C League","home_score":0,"away_score":0,"facility_id":146,"facility":"Richardson","facility_address":"522%20Centennial%20Blvd%2C%20Richardson%2C%20Usa%2C%2075081","rink_id":19,"rink":"RC - Blue Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-06-13"}]
'''
# Direwolves
dw_sch = '''
[{"type":"game","id":"g-166186","league_id":30,"season_id":1132,"tournament_id":null,"game_id":166186,"number":null,"datetime":"2018-04-08T19:15:00+00:00","datetime_tz":"2018-04-09 00:15:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":"2018-04-09 16:14:01 +0000","created_at":"2018-04-03 16:07:53 +0000","home_team_id":31967,"home_team":"Direwolves","home_team_short":"Direwolve","home_team_logo_url":null,"away_team_id":31968,"away_team":"Blasters","away_team_short":"Blasters","away_team_logo_url":null,"home_division_id":4696,"home_division":"PL - D League","away_division_id":4696,"away_division":"PL - D League","home_score":5,"away_score":2,"facility_id":149,"facility":"Plano","facility_address":"4020%20W.%20Plano%20Parkway%2C%20Plano%2C%20TX%2C%20US%2C%2075093","rink_id":24,"rink":"PL - US Rink","game_type":"Regular Season","notes":"DIREW","status":"Final","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-04-08"},{"type":"game","id":"g-166195","league_id":30,"season_id":1132,"tournament_id":null,"game_id":166195,"number":null,"datetime":"2018-04-15T19:30:00+00:00","datetime_tz":"2018-04-16 00:30:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":"2018-04-16 01:38:14 +0000","created_at":"2018-04-03 16:07:54 +0000","home_team_id":31967,"home_team":"Direwolves","home_team_short":"Direwolve","home_team_logo_url":null,"away_team_id":31964,"away_team":"Hellfish","away_team_short":"Hellfish","away_team_logo_url":null,"home_division_id":4696,"home_division":"PL - D League","away_division_id":4696,"away_division":"PL - D League","home_score":6,"away_score":1,"facility_id":149,"facility":"Plano","facility_address":"4020%20W.%20Plano%20Parkway%2C%20Plano%2C%20TX%2C%20US%2C%2075093","rink_id":25,"rink":"PL - World Rink","game_type":"Regular Season","notes":null,"status":"Final","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-04-15"},{"type":"game","id":"g-166200","league_id":30,"season_id":1132,"tournament_id":null,"game_id":166200,"number":null,"datetime":"2018-04-22T18:00:00+00:00","datetime_tz":"2018-04-22 23:00:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-04-03 16:07:54 +0000","home_team_id":31974,"home_team":"Hangovers","home_team_short":"Hangovers","home_team_logo_url":null,"away_team_id":31967,"away_team":"Direwolves","away_team_short":"Direwolve","away_team_logo_url":null,"home_division_id":4696,"home_division":"PL - D League","away_division_id":4696,"away_division":"PL - D League","home_score":0,"away_score":0,"facility_id":149,"facility":"Plano","facility_address":"4020%20W.%20Plano%20Parkway%2C%20Plano%2C%20TX%2C%20US%2C%2075093","rink_id":24,"rink":"PL - US Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-04-22"},{"type":"game","id":"g-166207","league_id":30,"season_id":1132,"tournament_id":null,"game_id":166207,"number":null,"datetime":"2018-04-23T21:00:00+00:00","datetime_tz":"2018-04-24 02:00:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-04-03 16:07:55 +0000","home_team_id":31970,"home_team":"Frigid Beavers","home_team_short":"Frigid Be","home_team_logo_url":null,"away_team_id":31967,"away_team":"Direwolves","away_team_short":"Direwolve","away_team_logo_url":null,"home_division_id":4696,"home_division":"PL - D League","away_division_id":4696,"away_division":"PL - D League","home_score":0,"away_score":0,"facility_id":149,"facility":"Plano","facility_address":"4020%20W.%20Plano%20Parkway%2C%20Plano%2C%20TX%2C%20US%2C%2075093","rink_id":25,"rink":"PL - World Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-04-23"},{"type":"game","id":"g-166211","league_id":30,"season_id":1132,"tournament_id":null,"game_id":166211,"number":null,"datetime":"2018-04-29T21:45:00+00:00","datetime_tz":"2018-04-30 02:45:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-04-03 16:07:55 +0000","home_team_id":31967,"home_team":"Direwolves","home_team_short":"Direwolve","home_team_logo_url":null,"away_team_id":31966,"away_team":"Icejets","away_team_short":"Icejets","away_team_logo_url":null,"home_division_id":4696,"home_division":"PL - D League","away_division_id":4696,"away_division":"PL - D League","home_score":0,"away_score":0,"facility_id":149,"facility":"Plano","facility_address":"4020%20W.%20Plano%20Parkway%2C%20Plano%2C%20TX%2C%20US%2C%2075093","rink_id":25,"rink":"PL - World Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-04-29"},{"type":"game","id":"g-166220","league_id":30,"season_id":1132,"tournament_id":null,"game_id":166220,"number":null,"datetime":"2018-05-06T22:00:00+00:00","datetime_tz":"2018-05-07 03:00:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-04-03 16:07:56 +0000","home_team_id":31971,"home_team":"Blueliners","home_team_short":"Blueliner","home_team_logo_url":null,"away_team_id":31967,"away_team":"Direwolves","away_team_short":"Direwolve","away_team_logo_url":null,"home_division_id":4696,"home_division":"PL - D League","away_division_id":4696,"away_division":"PL - D League","home_score":0,"away_score":0,"facility_id":149,"facility":"Plano","facility_address":"4020%20W.%20Plano%20Parkway%2C%20Plano%2C%20TX%2C%20US%2C%2075093","rink_id":24,"rink":"PL - US Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-05-06"},{"type":"game","id":"g-166222","league_id":30,"season_id":1132,"tournament_id":null,"game_id":166222,"number":null,"datetime":"2018-05-07T20:30:00+00:00","datetime_tz":"2018-05-08 01:30:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-04-03 16:07:56 +0000","home_team_id":31967,"home_team":"Direwolves","home_team_short":"Direwolve","home_team_logo_url":null,"away_team_id":31969,"away_team":"Red Stags","away_team_short":"Red Stags","away_team_logo_url":null,"home_division_id":4696,"home_division":"PL - D League","away_division_id":4696,"away_division":"PL - D League","home_score":0,"away_score":0,"facility_id":149,"facility":"Plano","facility_address":"4020%20W.%20Plano%20Parkway%2C%20Plano%2C%20TX%2C%20US%2C%2075093","rink_id":24,"rink":"PL - US Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-05-07"},{"type":"game","id":"g-166229","league_id":30,"season_id":1132,"tournament_id":null,"game_id":166229,"number":null,"datetime":"2018-05-13T21:00:00+00:00","datetime_tz":"2018-05-14 02:00:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-04-03 16:07:57 +0000","home_team_id":31973,"home_team":"Snow Monkeys","home_team_short":"Snow Monk","home_team_logo_url":null,"away_team_id":31967,"away_team":"Direwolves","away_team_short":"Direwolve","away_team_logo_url":null,"home_division_id":4696,"home_division":"PL - D League","away_division_id":4696,"away_division":"PL - D League","home_score":0,"away_score":0,"facility_id":149,"facility":"Plano","facility_address":"4020%20W.%20Plano%20Parkway%2C%20Plano%2C%20TX%2C%20US%2C%2075093","rink_id":25,"rink":"PL - World Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-05-13"},{"type":"game","id":"g-166233","league_id":30,"season_id":1132,"tournament_id":null,"game_id":166233,"number":null,"datetime":"2018-05-20T19:45:00+00:00","datetime_tz":"2018-05-21 00:45:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-04-03 16:07:57 +0000","home_team_id":31967,"home_team":"Direwolves","home_team_short":"Direwolve","home_team_logo_url":null,"away_team_id":31972,"away_team":"krakens","away_team_short":"krakens","away_team_logo_url":null,"home_division_id":4696,"home_division":"PL - D League","away_division_id":4696,"away_division":"PL - D League","home_score":0,"away_score":0,"facility_id":149,"facility":"Plano","facility_address":"4020%20W.%20Plano%20Parkway%2C%20Plano%2C%20TX%2C%20US%2C%2075093","rink_id":25,"rink":"PL - World Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-05-20"},{"type":"game","id":"g-166238","league_id":30,"season_id":1132,"tournament_id":null,"game_id":166238,"number":null,"datetime":"2018-05-21T21:30:00+00:00","datetime_tz":"2018-05-22 02:30:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-04-03 16:07:58 +0000","home_team_id":31967,"home_team":"Direwolves","home_team_short":"Direwolve","home_team_logo_url":null,"away_team_id":31963,"away_team":"Buzzed Litebeers","away_team_short":"Buzzed Li","away_team_logo_url":null,"home_division_id":4696,"home_division":"PL - D League","away_division_id":4696,"away_division":"PL - D League","home_score":0,"away_score":0,"facility_id":149,"facility":"Plano","facility_address":"4020%20W.%20Plano%20Parkway%2C%20Plano%2C%20TX%2C%20US%2C%2075093","rink_id":25,"rink":"PL - World Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-05-21"}]
'''

br_sch = br_sch.replace("null", "None")
br_sch = br_sch.replace("false", "False")
br_sch = br_sch.replace("true", "True")
dw_sch = dw_sch.replace("null", "None")
dw_sch = dw_sch.replace("false", "False")
dw_sch = dw_sch.replace("true", "True")

def datestring(dt):
  dt = datetime.strptime(dt, "%Y-%m-%dT%H:%M")
  dt = datetime.strftime(dt, "%A, %B %d").lstrip("0").replace(" 0", " ") + suffix(int(datetime.strftime(dt, "%d")))
  return dt

def daystring(dt):
  dt = datetime.strptime(dt, "%Y-%m-%dT%H:%M")
  dt = datetime.strftime(dt, "%A")
  return dt

def monthdaystring(dt):
  dt = datetime.strptime(dt, "%Y-%m-%dT%H:%M")
  dt = datetime.strftime(dt, "%B %d")
  return dt

def timestring(dt):
  dt = datetime.strptime(dt[11:16], "%H:%M")
  dt = datetime.strftime(dt, "%-I:%M")
  return dt

def suffix(d):
  return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

### Organizing
teams = ["RC Bladerunners", "Direwolves"]
games_in_season = 10
combined_schedule = {}
ordered_schedule = {}
for sch in [dw_sch, br_sch]:# , dw_sch]:
  schedule = eval(sch)
  schedule = schedule[:games_in_season]

  for game in range(len(schedule)):
    #print(game) # `game` is the game's index a given schedule
    date = datetime.strptime(schedule[game]["datetime"][:16], "%Y-%m-%dT%H:%M")
    combined_schedule[date] = {}
    combined_schedule[date]["datestring"] = datestring(schedule[game]["datetime"][:16])
    combined_schedule[date]["daystring"] = daystring(schedule[game]["datetime"][:16])
    combined_schedule[date]["monthdaystring"] = monthdaystring(schedule[game]["datetime"][:16])
    combined_schedule[date]["timestring"] = timestring(schedule[game]["datetime"]) + "pm"
    combined_schedule[date]["team"] = "Bladerunners" if "RC Bladerunners" in [schedule[game]["home_team"], schedule[game]["away_team"]] else "Direwolves"
    combined_schedule[date]["home_team"] = schedule[game]["home_team"]
    combined_schedule[date]["away_team"] = schedule[game]["away_team"]
    combined_schedule[date]["location"] = schedule[game]["facility"]

ordered_schedule = collections.OrderedDict(sorted(combined_schedule.items()))
# print("***********************")
# print(ordered_schedule)
# print("***********************")
game_number = 1
console_game_number = 1
for game in ordered_schedule:
  osg = ordered_schedule[game]
  # Consoling
  print("Game #" + str(game_number))
  console_game_number += 1
  print(osg["location"])
  print(osg["team"])
  print(datetime.strftime(game, "%A, %B %d").lstrip("0")).replace("0", "")
  print(datetime.strftime(game, "%-I:%Mpm"))
  loc = "vs " if osg["home_team"] in teams else "@ "
  opp = osg["away_team"] if osg["home_team"] in teams else osg["home_team"]
  print(loc + opp)
  print("=========================")

  # Actual printing
  try:
    printer.setSize("M")
    printer.justify("C")
    printer.doubleWidthOn()
    printer.println("Game #" + str(game_number))
    game_number += 1
    printer.setSize("L")
    printer.println(osg["location"])
    printer.doubleWidthOff()
    printer.println(osg["team"])
    printer.setSize("M")
    printer.boldOn()
    printer.println(osg["datestring"])
    printer.doubleWidthOn()
    printer.println(osg["timestring"])
    printer.boldOff()
    printer.doubleWidthOff()
    loc = "vs " if osg["home_team"] in teams else "@ "
    opp = osg["away_team"] if osg["home_team"] in teams else osg["home_team"]
    printer.println(loc + opp)
    printer.setSize("S")
    printer.boldOn()
    printer.println("================================")
  except Exception:
    pass
