
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
# http://starcenter.hockeyshift.com/stats#/30/schedule?team_id=18103&all
# $("tbody").attr("ng-init")
#######

# Can probably figure out a way to get these from BeautifulSoup one of these days
# Bladerunners
br_sch = '''
[{"type":"game","id":"g-151656","league_id":30,"season_id":975,"tournament_id":null,"game_id":151656,"number":null,"datetime":"2018-01-13T20:15:00+00:00","datetime_tz":"2018-01-14 02:15:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-01-04 21:13:09 +0000","home_team_id":27518,"home_team":"Hangovers","home_team_short":"Hangovers","home_team_logo_url":null,"away_team_id":27521,"away_team":"RC Bladerunners","away_team_short":"RC - Blad","away_team_logo_url":null,"home_division_id":4175,"home_division":"RC - C League","away_division_id":4175,"away_division":"RC - C League","home_score":0,"away_score":0,"facility_id":146,"facility":"Richardson","facility_address":"522%20Centennial%20Blvd%2C%20Richardson%2C%20Usa%2C%2075081","rink_id":18,"rink":"RC - Red Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-01-13"},{"type":"game","id":"g-151659","league_id":30,"season_id":975,"tournament_id":null,"game_id":151659,"number":null,"datetime":"2018-01-17T22:45:00+00:00","datetime_tz":"2018-01-18 04:45:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-01-04 21:13:09 +0000","home_team_id":27521,"home_team":"RC Bladerunners","home_team_short":"RC - Blad","home_team_logo_url":null,"away_team_id":27519,"away_team":"Ice Cats","away_team_short":"Ice Cats","away_team_logo_url":null,"home_division_id":4175,"home_division":"RC - C League","away_division_id":4175,"away_division":"RC - C League","home_score":0,"away_score":0,"facility_id":146,"facility":"Richardson","facility_address":"522%20Centennial%20Blvd%2C%20Richardson%2C%20Usa%2C%2075081","rink_id":18,"rink":"RC - Red Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-01-17"},{"type":"game","id":"g-151663","league_id":30,"season_id":975,"tournament_id":null,"game_id":151663,"number":null,"datetime":"2018-01-24T22:45:00+00:00","datetime_tz":"2018-01-25 04:45:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-01-04 21:13:09 +0000","home_team_id":27524,"home_team":"Top Corns","home_team_short":"Top Corns","home_team_logo_url":null,"away_team_id":27521,"away_team":"RC Bladerunners","away_team_short":"RC - Blad","away_team_logo_url":null,"home_division_id":4175,"home_division":"RC - C League","away_division_id":4175,"away_division":"RC - C League","home_score":0,"away_score":0,"facility_id":146,"facility":"Richardson","facility_address":"522%20Centennial%20Blvd%2C%20Richardson%2C%20Usa%2C%2075081","rink_id":18,"rink":"RC - Red Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-01-24"},{"type":"game","id":"g-151669","league_id":30,"season_id":975,"tournament_id":null,"game_id":151669,"number":null,"datetime":"2018-02-03T21:30:00+00:00","datetime_tz":"2018-02-04 03:30:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-01-04 21:13:10 +0000","home_team_id":27521,"home_team":"RC Bladerunners","home_team_short":"RC - Blad","home_team_logo_url":null,"away_team_id":27522,"away_team":"RC Wolves","away_team_short":"RC - Wolv","away_team_logo_url":null,"home_division_id":4175,"home_division":"RC - C League","away_division_id":4175,"away_division":"RC - C League","home_score":0,"away_score":0,"facility_id":146,"facility":"Richardson","facility_address":"522%20Centennial%20Blvd%2C%20Richardson%2C%20Usa%2C%2075081","rink_id":18,"rink":"RC - Red Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-02-03"},{"type":"game","id":"g-151671","league_id":30,"season_id":975,"tournament_id":null,"game_id":151671,"number":null,"datetime":"2018-02-07T22:45:00+00:00","datetime_tz":"2018-02-08 04:45:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-01-04 21:13:10 +0000","home_team_id":27521,"home_team":"RC Bladerunners","home_team_short":"RC - Blad","home_team_logo_url":null,"away_team_id":27517,"away_team":"Hitmen","away_team_short":"Hitmen","away_team_logo_url":null,"home_division_id":4175,"home_division":"RC - C League","away_division_id":4175,"away_division":"RC - C League","home_score":0,"away_score":0,"facility_id":146,"facility":"Richardson","facility_address":"522%20Centennial%20Blvd%2C%20Richardson%2C%20Usa%2C%2075081","rink_id":18,"rink":"RC - Red Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-02-07"},{"type":"game","id":"g-151676","league_id":30,"season_id":975,"tournament_id":null,"game_id":151676,"number":null,"datetime":"2018-02-17T20:15:00+00:00","datetime_tz":"2018-02-18 02:15:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-01-04 21:13:10 +0000","home_team_id":27521,"home_team":"RC Bladerunners","home_team_short":"RC - Blad","home_team_logo_url":null,"away_team_id":27520,"away_team":"Lemmings","away_team_short":"Lemmings","away_team_logo_url":null,"home_division_id":4175,"home_division":"RC - C League","away_division_id":4175,"away_division":"RC - C League","home_score":0,"away_score":0,"facility_id":146,"facility":"Richardson","facility_address":"522%20Centennial%20Blvd%2C%20Richardson%2C%20Usa%2C%2075081","rink_id":18,"rink":"RC - Red Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-02-17"},{"type":"game","id":"g-151678","league_id":30,"season_id":975,"tournament_id":null,"game_id":151678,"number":null,"datetime":"2018-02-21T22:30:00+00:00","datetime_tz":"2018-02-22 04:30:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-01-04 21:13:10 +0000","home_team_id":27523,"home_team":"Team Hanson","home_team_short":"Team Hans","home_team_logo_url":null,"away_team_id":27521,"away_team":"RC Bladerunners","away_team_short":"RC - Blad","away_team_logo_url":null,"home_division_id":4175,"home_division":"RC - C League","away_division_id":4175,"away_division":"RC - C League","home_score":0,"away_score":0,"facility_id":146,"facility":"Richardson","facility_address":"522%20Centennial%20Blvd%2C%20Richardson%2C%20Usa%2C%2075081","rink_id":19,"rink":"RC - Blue Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-02-21"},{"type":"game","id":"g-151683","league_id":30,"season_id":975,"tournament_id":null,"game_id":151683,"number":null,"datetime":"2018-02-28T22:45:00+00:00","datetime_tz":"2018-03-01 04:45:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-01-04 21:13:11 +0000","home_team_id":27521,"home_team":"RC Bladerunners","home_team_short":"RC - Blad","home_team_logo_url":null,"away_team_id":27518,"away_team":"Hangovers","away_team_short":"Hangovers","away_team_logo_url":null,"home_division_id":4175,"home_division":"RC - C League","away_division_id":4175,"away_division":"RC - C League","home_score":0,"away_score":0,"facility_id":146,"facility":"Richardson","facility_address":"522%20Centennial%20Blvd%2C%20Richardson%2C%20Usa%2C%2075081","rink_id":18,"rink":"RC - Red Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-02-28"},{"type":"game","id":"g-151686","league_id":30,"season_id":975,"tournament_id":null,"game_id":151686,"number":null,"datetime":"2018-03-07T22:30:00+00:00","datetime_tz":"2018-03-08 04:30:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-01-04 21:13:11 +0000","home_team_id":27519,"home_team":"Ice Cats","home_team_short":"Ice Cats","home_team_logo_url":null,"away_team_id":27521,"away_team":"RC Bladerunners","away_team_short":"RC - Blad","away_team_logo_url":null,"home_division_id":4175,"home_division":"RC - C League","away_division_id":4175,"away_division":"RC - C League","home_score":0,"away_score":0,"facility_id":146,"facility":"Richardson","facility_address":"522%20Centennial%20Blvd%2C%20Richardson%2C%20Usa%2C%2075081","rink_id":18,"rink":"RC - Red Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-03-07"},{"type":"game","id":"g-151692","league_id":30,"season_id":975,"tournament_id":null,"game_id":151692,"number":null,"datetime":"2018-03-17T20:15:00+00:00","datetime_tz":"2018-03-18 01:15:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-01-04 21:13:11 +0000","home_team_id":27524,"home_team":"Top Corns","home_team_short":"Top Corns","home_team_logo_url":null,"away_team_id":27521,"away_team":"RC Bladerunners","away_team_short":"RC - Blad","away_team_logo_url":null,"home_division_id":4175,"home_division":"RC - C League","away_division_id":4175,"away_division":"RC - C League","home_score":0,"away_score":0,"facility_id":146,"facility":"Richardson","facility_address":"522%20Centennial%20Blvd%2C%20Richardson%2C%20Usa%2C%2075081","rink_id":18,"rink":"RC - Red Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-03-17"}]
'''

# Direwolves
dw_sch = '''
[{"type":"game","id":"g-152509","league_id":30,"season_id":975,"tournament_id":null,"game_id":152509,"number":null,"datetime":"2018-01-11T21:00:00+00:00","datetime_tz":"2018-01-12 03:00:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-01-08 21:54:20 +0000","home_team_id":27799,"home_team":"Direwolves","home_team_short":"Direwolve","home_team_logo_url":null,"away_team_id":27800,"away_team":"Ol' Rooks","away_team_short":"Ol' Rooks","away_team_logo_url":null,"home_division_id":4202,"home_division":"Plano D","away_division_id":4202,"away_division":"Plano D","home_score":0,"away_score":0,"facility_id":149,"facility":"Plano","facility_address":"4020%20W.%20Plano%20Parkway%2C%20Plano%2C%20TX%2C%20US%2C%2075093","rink_id":24,"rink":"PL - US Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-01-11"},{"type":"game","id":"g-152521","league_id":30,"season_id":975,"tournament_id":null,"game_id":152521,"number":null,"datetime":"2018-01-18T23:15:00+00:00","datetime_tz":"2018-01-19 05:15:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-01-08 21:59:19 +0000","home_team_id":27795,"home_team":"Icejets","home_team_short":"Icejets","home_team_logo_url":null,"away_team_id":27799,"away_team":"Direwolves","away_team_short":"Direwolve","away_team_logo_url":null,"home_division_id":4202,"home_division":"Plano D","away_division_id":4202,"away_division":"Plano D","home_score":0,"away_score":0,"facility_id":149,"facility":"Plano","facility_address":"4020%20W.%20Plano%20Parkway%2C%20Plano%2C%20TX%2C%20US%2C%2075093","rink_id":25,"rink":"PL - World Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-01-18"},{"type":"game","id":"g-152526","league_id":30,"season_id":975,"tournament_id":null,"game_id":152526,"number":null,"datetime":"2018-01-25T23:15:00+00:00","datetime_tz":"2018-01-26 05:15:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-01-08 21:59:19 +0000","home_team_id":27796,"home_team":"Blasters","home_team_short":"Blasters","home_team_logo_url":null,"away_team_id":27799,"away_team":"Direwolves","away_team_short":"Direwolve","away_team_logo_url":null,"home_division_id":4202,"home_division":"Plano D","away_division_id":4202,"away_division":"Plano D","home_score":0,"away_score":0,"facility_id":149,"facility":"Plano","facility_address":"4020%20W.%20Plano%20Parkway%2C%20Plano%2C%20TX%2C%20US%2C%2075093","rink_id":25,"rink":"PL - World Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-01-25"},{"type":"game","id":"g-152532","league_id":30,"season_id":975,"tournament_id":null,"game_id":152532,"number":null,"datetime":"2018-02-06T23:30:00+00:00","datetime_tz":"2018-02-07 05:30:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-01-08 22:04:55 +0000","home_team_id":27804,"home_team":"Frigid Beavers","home_team_short":"Frigid Be","home_team_logo_url":null,"away_team_id":27799,"away_team":"Direwolves","away_team_short":"Direwolve","away_team_logo_url":null,"home_division_id":4202,"home_division":"Plano D","away_division_id":4202,"away_division":"Plano D","home_score":0,"away_score":0,"facility_id":149,"facility":"Plano","facility_address":"4020%20W.%20Plano%20Parkway%2C%20Plano%2C%20TX%2C%20US%2C%2075093","rink_id":25,"rink":"PL - World Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-02-06"},{"type":"game","id":"g-152545","league_id":30,"season_id":975,"tournament_id":null,"game_id":152545,"number":null,"datetime":"2018-02-11T20:15:00+00:00","datetime_tz":"2018-02-12 02:15:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-01-08 22:10:59 +0000","home_team_id":27799,"home_team":"Direwolves","home_team_short":"Direwolve","home_team_logo_url":null,"away_team_id":27806,"away_team":"Hellfish","away_team_short":"Hellfish","away_team_logo_url":null,"home_division_id":4202,"home_division":"Plano D","away_division_id":4202,"away_division":"Plano D","home_score":0,"away_score":0,"facility_id":149,"facility":"Plano","facility_address":"4020%20W.%20Plano%20Parkway%2C%20Plano%2C%20TX%2C%20US%2C%2075093","rink_id":25,"rink":"PL - World Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-02-11"},{"type":"game","id":"g-152546","league_id":30,"season_id":975,"tournament_id":null,"game_id":152546,"number":null,"datetime":"2018-02-20T22:15:00+00:00","datetime_tz":"2018-02-21 04:15:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-01-08 22:11:02 +0000","home_team_id":27799,"home_team":"Direwolves","home_team_short":"Direwolve","home_team_logo_url":null,"away_team_id":27807,"away_team":"Snow Monkeys","away_team_short":"Snow Monk","away_team_logo_url":null,"home_division_id":4202,"home_division":"Plano D","away_division_id":4202,"away_division":"Plano D","home_score":0,"away_score":0,"facility_id":149,"facility":"Plano","facility_address":"4020%20W.%20Plano%20Parkway%2C%20Plano%2C%20TX%2C%20US%2C%2075093","rink_id":25,"rink":"PL - World Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-02-20"},{"type":"game","id":"g-152552","league_id":30,"season_id":975,"tournament_id":null,"game_id":152552,"number":null,"datetime":"2018-02-27T22:30:00+00:00","datetime_tz":"2018-02-28 04:30:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-01-08 22:16:52 +0000","home_team_id":27799,"home_team":"Direwolves","home_team_short":"Direwolve","home_team_logo_url":null,"away_team_id":27801,"away_team":"Phantoms","away_team_short":"Phantoms","away_team_logo_url":null,"home_division_id":4202,"home_division":"Plano D","away_division_id":4202,"away_division":"Plano D","home_score":0,"away_score":0,"facility_id":149,"facility":"Plano","facility_address":"4020%20W.%20Plano%20Parkway%2C%20Plano%2C%20TX%2C%20US%2C%2075093","rink_id":24,"rink":"PL - US Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-02-27"},{"type":"game","id":"g-152566","league_id":30,"season_id":975,"tournament_id":null,"game_id":152566,"number":null,"datetime":"2018-03-06T22:15:00+00:00","datetime_tz":"2018-03-07 04:15:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-01-08 22:23:09 +0000","home_team_id":27798,"home_team":"Mallards","home_team_short":"Mallards","home_team_logo_url":null,"away_team_id":27799,"away_team":"Direwolves","away_team_short":"Direwolve","away_team_logo_url":null,"home_division_id":4202,"home_division":"Plano D","away_division_id":4202,"away_division":"Plano D","home_score":0,"away_score":0,"facility_id":149,"facility":"Plano","facility_address":"4020%20W.%20Plano%20Parkway%2C%20Plano%2C%20TX%2C%20US%2C%2075093","rink_id":25,"rink":"PL - World Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-03-06"},{"type":"game","id":"g-152570","league_id":30,"season_id":975,"tournament_id":null,"game_id":152570,"number":null,"datetime":"2018-03-13T20:00:00+00:00","datetime_tz":"2018-03-14 01:00:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-01-08 22:28:04 +0000","home_team_id":27799,"home_team":"Direwolves","home_team_short":"Direwolve","home_team_logo_url":null,"away_team_id":27797,"away_team":"Blueliners","away_team_short":"Blueliner","away_team_logo_url":null,"home_division_id":4202,"home_division":"Plano D","away_division_id":4202,"away_division":"Plano D","home_score":0,"away_score":0,"facility_id":149,"facility":"Plano","facility_address":"4020%20W.%20Plano%20Parkway%2C%20Plano%2C%20TX%2C%20US%2C%2075093","rink_id":24,"rink":"PL - US Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-03-13"},{"type":"game","id":"g-152573","league_id":30,"season_id":975,"tournament_id":null,"game_id":152573,"number":null,"datetime":"2018-03-18T19:15:00+00:00","datetime_tz":"2018-03-19 00:15:00 +0000","time_zone":"US/Central","time_zone_abbr":"","updated_at":null,"created_at":"2018-01-08 22:28:04 +0000","home_team_id":27802,"home_team":"Flyers United","home_team_short":"Flyers Un","home_team_logo_url":null,"away_team_id":27799,"away_team":"Direwolves","away_team_short":"Direwolve","away_team_logo_url":null,"home_division_id":4202,"home_division":"Plano D","away_division_id":4202,"away_division":"Plano D","home_score":0,"away_score":0,"facility_id":149,"facility":"Plano","facility_address":"4020%20W.%20Plano%20Parkway%2C%20Plano%2C%20TX%2C%20US%2C%2075093","rink_id":24,"rink":"PL - US Rink","game_type":"Regular Season","notes":null,"status":"Not Started","overtime":false,"shootout":false,"allow_players":true,"tickets_url":null,"watch_live_url":null,"has_play_by_play":false,"date_group":"2018-03-18"}]
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
for game in ordered_schedule:
  osg = ordered_schedule[game]
  # Consoling
  print("Game #" + str(game_number))
  game_number += 1
  print(osg["location"])
  print(osg["team"])
  print(datetime.strftime(game, "%A, %B %d").lstrip("0").replace("0", ""))
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
