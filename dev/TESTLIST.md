# File list

This is a master reference for all files used by tf2 huds.

## scripts/

File | Description
---- | -----------
hudlayout.res | Controls the positioning of the majority of elements
hudanimations_tf.txt | Controls the majority of animations
hudanimations_manifest.txt | Controls which animations files are used
mod_textures.txt | Controls many miscellanious icons and textures (such as killfeed icons)
chapterbackgrounds.txt | Controls the random backgrounds and characters that appear on the mainmenu

## resource/

File | Description
---- | -----------
clientscheme.res | Controls definitions for font declarations, font sizes, colors, borders
chatscheme.res | Like clientscheme, but for the chat box
sourcescheme.res | Like clientscheme, but for old-style windows like the console
gamemenu.res | Controls tooltips, visibility ingame/inmenu, etc. of some main menu elements
closecaption_english.dat | Controls captions
closecaption_english.txt | Source file to compile into closecaption_english.dat. Does not do anything itself.

Of note, you can create custom closecaption files that can be named whatever you want (as long as they start with closecaption_). That said, they must have both the .dat and .txt file, though the .txt can be completely blank.

As well, custom localization can be added to chat_english.txt, or other languages. The full list of valid languages is:
```
brazilian
bulgarian
czech
danish
dutch
english
finnish
french
german
greek
hungarian
italian
japanese
korean
koreana
norwegian
polish
portuguese
romanian
russian
schinese
spanish
swedish
tchinese
thai
turkish
pirate
```

## resource/ui/

File | Description
---- | -----------
abusereportsubmitdialog.res | 
achievementsdialog.res | 
annotationspanelcallout.res | 
badgepanel.res | 
casualrankpanel.res | 
casualwelcomedialog.res | 
charinfoarmorysubpanel.res | 
charinfoloadoutsubpanel.res | 
charinfopanel.res | 
chatpopup.res | 
cheatdetectiondialog.res | 
classloadoutpanel.res | 
classmenu.res | 
classselection.res | 
classselection_sc.res | 
classtipsitem.res | 
classtipslist.res | 
coachedbypanel.res | 
competitiveaccessinfo.res | 
competitivewelcomedialog.res | 
comprankpanel.res | 
comprankstooltip.res | 
compstats.res | 
confirmabandondialog.res | 
controlpointcountdown.res | 
controlpointicon.res | 
controlpointprogressbar.res | 
craftingpanel.res | 
craftingstatusdialog.res | 
dashboardpartymember.res | 
disguisestatuspanel.res | 
dynamicrecipepanel.res | 
enemycountpanel.res | 
explanationpopup.res | 
flagcalloutpanel.res | 
flagstatus.res | 
freezepanelcallout.res | 
freezepanelkillerhealth.res | 
freezepanel_basic.res | 
giveawayitempanel.res | 
globalchat.res | 
globalexplanations.res | 
healthiconpanel.res | 
hudaccountpanel.res | 
hudachievementfloatingnumber.res | 
hudachievementtrackeritem.res | 
hudalert.res | 
hudammoweapons.res | 
hudarenacappointcountdown.res | 
hudarenaclasslayout.res | 
hudarenanotification.res | 
hudarenaplayercount.res | 
hudarenateammenu.res | 
hudarenateammenu_sc.res | 
hudarenavspanel.res | 
hudarenawinpanel.res | 
hudbosshealth.res | 
hudbowcharge.res | 
hudcurrencyaccount.res | 
huddamageaccount.res | 
huddemomancharge.res | 
huddemomanpipes.res | 
hudhealthaccount.res | 
hudinspectpanel.res | 
huditemattributetracker.res | 
huditemeffectmeter.res | 
huditemeffectmeter_cleaver.res | 
huditemeffectmeter_demoman.res | 
huditemeffectmeter_engineer.res | 
huditemeffectmeter_halloweensouls.res | 
huditemeffectmeter_heavy.res | 
huditemeffectmeter_kartcharge.res | 
huditemeffectmeter_killstreak.res | 
huditemeffectmeter_organs.res | 
huditemeffectmeter_particlecannon.res | 
huditemeffectmeter_pomson.res | 
huditemeffectmeter_powerupbottle.res | 
huditemeffectmeter_pyro.res | 
huditemeffectmeter_raygun.res | 
huditemeffectmeter_sapper.res | 
huditemeffectmeter_scout.res | 
huditemeffectmeter_sniper.res | 
huditemeffectmeter_sniperfocus.res | 
huditemeffectmeter_sodapopper.res | 
huditemeffectmeter_spy.res | 
huditemeffectmeter_spyknife.res | 
hudkillstreaknotice.res | 
hudmannvsmachinestatus.res | 
hudmatchstatus.res | 
hudmatchsummary.res | 
hudmediccharge.res | 
hudmenutauntselection.res | 
hudmenutauntselection_sc.res | 
hudminigame_base.res | 
hudminigame_collection.res | 
hudminigame_platform.res | 
hudminigame_soccer.res | 
hudminigame_soccersuddendeath.res | 
hudobjectiveflagpanel.res | 
hudobjectivekothtimepanel.res | 
hudobjectiveplayerdestruction.res | 
hudobjectiverobotdestruction.res | 
hudobjectivestatus.res | 
hudobjectivetimepanel.res | 
hudpasstime.res | 
hudpasstimeballstatus.res | 
hudpasstimeoffscreenarrow.res | 
hudpasstimepassnotify.res | 
hudpasstimeteamscore.res | 
hudplayerclass.res | 
hudplayerhealth.res | 
hudpowerupeffectmeter.res | 
hudpvewinpanel.res | 
hudrocketpack.res | 
hudroundcounter.res | 
hudspellselection.res | 
hudstalemate.res | 
hudstopwatch.res | 
hudteamgoal.res | 
hudteamgoaltournament.res | 
hudteamswitch.res | 
hudtournament.res | 
hudtournamentsetup.res | 
hudtraining.res | 
hudtrainingmsg.res | 
hudupgradepanel.res | 
hudwarcount.res | 
hudweaponselection.res | 
hud_obj_dispenser.res | 
hud_obj_sapper.res | 
hud_obj_sentrygun.res | 
hud_obj_sentrygun_disp.res | 
hud_obj_tele.res | 
hud_obj_tele_entrance.res | 
hud_obj_tele_exit.res | 
importfiledialog.res | 
importfiletexteditdialog.res | 
importmaterialeditdialog.res | 
importpreviewitempanel.res | 
ingamequeuestatus.res | 
intromenu.res | 
intromenu_sc.res | 
invitenotification.res | 
itemoptionspanel.res | 
itemquickswitch.res | 
itemrenameconfirmationdialog.res | 
itemrenamedialog.res | 
itemrenameinvaliddialog.res | 
itemselectionpanel.res | 
itemslotpanel.res | 
layeredmappanel.res | 
layeredmappanelitem.res | 
layeredmappaneltooltip.res | 
leaderboardentry.res | 
leaderboardentryrank.res | 
leaderboardentryscore.res | 
leaderboardspreadentry.res | 
loadoutpresetpanel.res | 
lobbycontainerframe.res | 
lobbycontainerframe_casual.res | 
lobbycontainerframe_comp.res | 
lobbycontainerframe_mvm.res | 
lobbypanel.res | 
lobbypanel_casual.res | 
lobbypanel_comp.res | 
lobbypanel_mvm.res | 
mainmenueventplaylistentry.res | 
mainmenuoverride.res | 
mainmenuplaylistentry.res | 
mainmenu_saxxyawards.res | 
mapinfomenu.res | 
mapinfomenu_sc.res | 
matchhistoryentrypanel.res | 
matchmakingcasualcriteria.res | 
matchmakingcategorymappanel.res | 
matchmakingcategorypanel.res | 
matchmakingdashboard.res | 
matchmakingdashboardcasualcriteria.res | 
matchmakingdashboardcomp.res | 
matchmakingdashboardcompaccess.res | 
matchmakingdashboardeventmatch.res | 
matchmakingdashboardleftsidepanel.res | 
matchmakingdashboardmvmcriteria.res | 
matchmakingdashboardmvmmodeselect.res | 
matchmakingdashboardplaylist.res | 
matchmakingdashboardpopup.res | 
matchmakingdashboardpopup_mapvotepanel.res | 
matchmakingdashboardpopup_newmatch.res | 
matchmakingdashboardpopup_nextmapvoting.res | 
matchmakingdashboardpopup_nextmapwinner.res | 
matchmakingdashboardsidepanel.res | 
matchmakingdatacenterpopulationpanel.res | 
matchmakinggrouppanel.res | 
matchmakingpanel.res | 
matchmakingpingpanel.res | 
matchmakingplaylist.res | 
matchmakingtooltip.res | 
mediccallerpanel.res | 
mvmbombcarrierprogresspanel.res | 
mvmcreditspendpanel.res | 
mvmcreditsubpanel.res | 
mvmcriteria.res | 
mvmeconrequirementdialog.res | 
mvminworldcurrency.res | 
mvmscoreboard.res | 
mvmscoreboardenemyinfo.res | 
mvmstatentry.res | 
mvmvictorycontainer.res | 
mvmvictorymannupentry.res | 
mvmvictorymannuploot.res | 
mvmvictorymannuppanel.res | 
mvmvictorymannuptab.res | 
mvmvictorypanel.res | 
mvmvictorysplash.res | 
mvmwavelosspanel.res | 
navigationpaneltest.res | 
newrecipefounddialog.res | 
objectivestatusescort.res | 
objectivestatusmultipleescort.res | 
playerticketstatus.res | 
publishedfilebrowserdialog.res | 
publishfiledialog.res | 
pvpcasualrankpanel.res | 
pvpcomprankpanel.res | 
pvprankpanel.res | 
quickplaybusydialog.res | 
quickplaydialog.res | 
revivedialog.res | 
robotdestructionstatus.res | 
roundinfo.res | 
saxxyawards_submitform.res | 
scoreboard.res | 
selectmosthelpfulfrienddialog.res | 
selectplayerdialog.res | 
selectplayerdialog_coach.res | 
selectplayerdialog_duel.res | 
servernotconnectedtosteam.res | 
spectator.res | 
spectatorcoach.res | 
spectatorguihealth.res | 
spectatortournament.res | 
spectatortournamentguihealth.res | 
spectator_sc.res | 
stampdonationadd.res | 
staticbadgepanel.res | 
statpanel_base.res | 
statsummary.res | 
statsummary_embedded.res | 
steamfriendpanel.res | 
steamworkshopdialog.res | 
steamworkshopitem.res | 
streamlistpanel.res | 
streampanel.res | 
supportnotificationdialog.res | 
surveypanel_base.res | 
surveypanel_casualinquiry.res | 
surveypanel_compinquiry.res | 
surveypanel_mapquality.res | 
surveypanel_matchquality.res | 
surveypanel_randomcrit.res | 
tankprogressbar.res | 
tankstatuspanel.res | 
targetid.res | 
tauntcallerpanel.res | 
teammenu.res | 
teammenu_sc.res | 
testitembotcontrols.res | 
testitemdialog.res | 
testitemroot.res | 
textwindow.res | 
textwindowcustomserver.res | 
textwindowcustomserver_sc.res | 
textwindow_sc.res | 
tfadvancedoptionsdialog.res | 
tfhudrobotdestruction_activestate.res | 
tfhudrobotdestruction_deadstate.res | 
tfhudrobotdestruction_robotindicator.res | 
tfhudrobotdestruction_shieldedstate.res | 
trainingcomplete.res | 
trainingdialog.res | 
trainingdialog_old.res | 
trainingitempanel.res | 
upgradeboxdialog.res | 
upgradebuypanel.res | 
videopanel.res | 
viewrecipespanel.res | 
votehud.res | 
vrcalibration.res | 
waitingforplayerspanel.res | 
wavecompletesummarypanel.res | 
wavestatuspanel.res | 
winpanel.res | 
xboxdialogs.res | 
xpsourcepanel.res | 
