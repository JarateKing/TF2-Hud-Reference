# File list

This is a master reference for all files used by tf2 huds.

## scripts/

File | Description
---- | -----------
chapterbackgrounds.txt | Controls the random backgrounds and characters that appear on the mainmenu
hudanimations.txt | Controls hl2 animations
hudanimations_manifest.txt | Controls which animations files are used
hudanimations_tf.txt | Controls the majority of animations
hudlayout.res | Controls the positioning of the majority of elements
mod_textures.txt | Controls many miscellaneous icons and textures (such as killfeed icons)

## resource/

File | Description
---- | -----------
chatscheme.res | Like clientscheme, but for the chat box
chat_english.txt | Controls some chat-related localization. Can add new localization to custom huds.
clientscheme.res | Controls definitions for font declarations, font sizes, colors, borders
closecaption_english.dat | Controls captions
closecaption_english.txt | Source file to compile into closecaption_english.dat. Does not do anything itself.
gamemenu.res | Controls tooltips, visibility ingame/inmenu, etc. of some main menu elements
sourcescheme.res | Like clientscheme, but for old-style windows like the console

Of note, you can create custom closecaption files that can be named whatever you want (as long as they start with closecaption_). That said, they must have both the .dat and .txt file, though the .txt doesn't matter and can be completely blank (closecaption_english.txt is unnecessary, since it exists in the vpk's). These files can be loaded with the console command:
```
cc_lang custom // will load "resource/closecaption_custom.dat", the rest is implied
```

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
abusereportsubmitdialog.res | Abuse report compilation menu
achievementsdialog.res |
annotationspanelcallout.res |
badgepanel.res |
basechat.res | Chatbox
casualrankpanel.res |
casualwelcomedialog.res | Might be no longer in use
charinfoarmorysubpanel.res | Mann co. Catalog
charinfoloadoutsubpanel.res | Loadouts, Backpack, Crating, Catalog, Trades, Warpaints selection menu
charinfopanel.res | Top sheet and bottom bar in the Loadout/Backpack/Crafting/Catalog menus
chatpopup.res | Party popup messages
cheatdetectiondialog.res |
classloadoutpanel.res | Class loadout/taunts menu
classmenu.res |
classselection.res | Class selection menu
classselection_sc.res | Class selection menu, but for steam controller
classtipsitem.res |
classtipslist.res |
coachedbypanel.res |
competitiveaccessinfo.res | Competitive mode acess requirements message
competitivewelcomedialog.res | Might be no longer in use
comprankpanel.res |
comprankstooltip.res |
compstats.res | Competitive games played statistics menu
confirmabandondialog.res |
controlpointcountdown.res | Point activation countdown
controlpointicon.res | Control point Icons used for CP, Koth, A/D
controlpointprogressbar.res | Point capture progress circle bar
craftingpanel.res | Crafting Panel
craftingstatusdialog.res |
dashboardpartymember.res | Party members displayed in the menu dashborad
disguisestatuspanel.res | Spy disguise status
dynamicrecipepanel.res |
enemycountpanel.res | Robot wave icons used for MvM
explanationpopup.res |
flagcalloutpanel.res |
flagstatus.res | Flag icon and arrow (part of hudobjectiveflagpanel.res)
freezepanelcallout.res | Indicates your body parts after death
freezepanelkillerhealth.res | Enemy health on kill cam
freezepanel_basic.res | Enemy kill cam
giveawayitempanel.res |
globalchat.res | Party chat
globalexplanations.res | Explanations for casual, competitive, tutorial, warpaints, loadout, store ...
healthiconpanel.res | Teammates health displayed above their head (only visible with tf_hud_target_id_disable_floating_health "0")
hudaccountpanel.res | Engineer metal count
hudachievementfloatingnumber.res |
hudachievementtrackeritem.res |
hudalert.res |
hudammoweapons.res | Ammo in clip and ammo in reserve
hudarenacappointcountdown.res |
hudarenaclasslayout.res | Arena team composition panel
hudarenanotification.res |
hudarenaplayercount.res | Alive players counter for arena mode
hudarenateammenu.res | Spectate/Fight arena selection menu
hudarenateammenu_sc.res | Spectate/Fight arena selection menu, but for steam controller
hudarenavspanel.res |
hudarenawinpanel.res | End round arena scoreboard
hudbosshealth.res | Healthbar for Halloween bosses
hudbowcharge.res | old charge meter for Huntsman
hudcurrencyaccount.res | currency in MvM
huddamageaccount.res | Damage numbers when hitting other players
huddemomancharge.res | charge meter for Stickybomb Launcher, demoman shields, and Huntsman
huddemomanpipes.res | count for stickies currently out
hudhealthaccount.res | floating numbers when picking up healthpacks
hudinspectpanel.res |
huditemattributetracker.res |
huditemeffectmeter.res | charge meter for Sandman, Wrap Assassin
huditemeffectmeter_cleaver.res | charge meter for Flying Guillotine
huditemeffectmeter_demoman.res | count for Eyelander heads
huditemeffectmeter_engineer.res | count for Frontier Justice and Manmelter
huditemeffectmeter_halloweensouls.res | count for Halloween souls collected
huditemeffectmeter_heavy.res | charge meter for Heavy in MvM
huditemeffectmeter_kartcharge.res | charge meter for Halloween Karts
huditemeffectmeter_killstreak.res | count for killstreak weapons
huditemeffectmeter_organs.res | count for Vita-Saw
huditemeffectmeter_particlecannon.res | charge meter for Cow Mangler
huditemeffectmeter_pomson.res | charge meter for Pomson
huditemeffectmeter_powerupbottle.res | count for PowerUp Canteen in MvM
huditemeffectmeter_pyro.res | charge meter for Phlogistinator
huditemeffectmeter_raygun.res | charge meter for Righteous Bison
huditemeffectmeter_sapper.res | charge meter for Sapper
huditemeffectmeter_scout.res | charge meter for Bonk! Atomic Punch and Crit-a-Cola
huditemeffectmeter_sniper.res | count for Bazaar Bargain
huditemeffectmeter_sniperfocus.res | charge meter for Hitman's Heatmaker
huditemeffectmeter_sodapopper.res | charge meter for Sodapopper
huditemeffectmeter_spy.res | count for Diamondback
huditemeffectmeter_spyknife.res | charge for Spy-cicle
hudkillstreaknotice.res |
hudmannvsmachinestatus.res |
hudmatchstatus.res |
hudmatchsummary.res | End game summary scoreboard used for Casuals and Competitive gamemodes
hudmediccharge.res | Ubercharge numbers and Vaccinatore charges
hudmenutauntselection.res | Taunt selection menu
hudmenutauntselection_sc.res | Taunt selection menu, but for steam controller
hudminigame_base.res | Halloween minigame for sd_doomsday_event (Main file)
hudminigame_collection.res | Halloween ducks collection race minigame
hudminigame_platform.res | Halloween platform elimination minigame
hudminigame_soccer.res | Halloween soccer minigame
hudminigame_soccersuddendeath.res | Halloween soccer minigame
hudobjectiveflagpanel.res | Capture the flag points counter
hudobjectivekothtimepanel.res | King of the hill timers
hudobjectiveplayerdestruction.res | Player destruction
hudobjectiverobotdestruction.res | Robot destruction counter for the robots destroyed.
hudobjectivestatus.res | No longer in use
hudobjectivetimepanel.res | Round timer background, clock icon and server timer
hudpasstime.res |
hudpasstimeballstatus.res |
hudpasstimeoffscreenarrow.res |
hudpasstimepassnotify.res |
hudpasstimeteamscore.res |
hudplayerclass.res | Class icon and 3d model depending on convars
hudplayerhealth.res | Health number
hudpowerupeffectmeter.res |
hudpvewinpanel.res |
hudrocketpack.res | Charge meter for Thermal Thruster
hudroundcounter.res |
hudspellselection.res | Owned spells selection for halloween modes
hudstalemate.res |
hudstopwatch.res | Payload, A/D cap time
hudteamgoal.res | Summary of the game mode goal at the start of the round
hudteamgoaltournament.res | Summary of the game mode goal for tounament game modes
hudteamswitch.res | Teams auto-balance message
hudtournament.res | Tournament Blue-Red teams status/names and game win conditions
hudtournamentsetup.res | Ready/Unready and team name change PopUp menu for tournament
hudtraining.res |
hudtrainingmsg.res |
hudupgradepanel.res |
hudwarcount.res |
hudweaponselection.res |
hud_obj_dispenser.res | Engineer dispenser build status and Health
hud_obj_sapper.res | Building sapped icon
hud_obj_sentrygun.res | Engineer sentrygun build status, health, ammo
hud_obj_sentrygun_disp.res | Optional MvM Minisentry build status, health, ammo
hud_obj_tele.res | Engineer Teleport build status, health
hud_obj_tele_entrance.res | Engineer Teleport entrance health
hud_obj_tele_exit.res | Engineer Teleport exit health
importfiledialog.res |
importfiletexteditdialog.res |
importmaterialeditdialog.res |
importpreviewitempanel.res |
ingamequeuestatus.res | Queued for Casual/Competitive/MvM ingame message
intromenu.res |
intromenu_sc.res |
invitenotification.res | Invite to party received message
itemoptionspanel.res |
itemquickswitch.res | Loadout and weapons quickswitch menu
itemrenameconfirmationdialog.res | Name Tag - Description Tag confirmation menu
itemrenamedialog.res | Name Tag - Description Tag appliaction menus
itemrenameinvaliddialog.res | Name Tag - Description Tag appliaction failed menu
itemselectionpanel.res | Loadout item/weapon selection menu
itemslotpanel.res |
layeredmappanel.res |
layeredmappanelitem.res |
layeredmappaneltooltip.res |
leaderboardentry.res |
leaderboardentryrank.res |
leaderboardentryscore.res |
leaderboardspreadentry.res |
loadoutpresetpanel.res |
lobbycontainerframe.res | No longer in use
lobbycontainerframe_casual.res | No longer in use
lobbycontainerframe_comp.res | No longer in use
lobbycontainerframe_mvm.res | No longer in use
lobbypanel.res | No longer in use
lobbypanel_casual.res | No longer in use
lobbypanel_comp.res | No longer in use
lobbypanel_mvm.res | No longer in use
mainmenueventplaylistentry.res |
mainmenuoverride.res | central file for the main menu
mainmenuplaylistentry.res | *Find a game* game modes buttons and description
mainmenu_saxxyawards.res |
mapinfomenu.res | Map informations menu
mapinfomenu_sc.res | Map information menu, but for steam controller
matchhistoryentrypanel.res | Comptitive matches history menu
matchmakingcasualcriteria.res | Main Casual mode file
matchmakingcategorymappanel.res | Casual popup map list for each gamemode
matchmakingcategorypanel.res | Casual game modes list panel
matchmakingdashboard.res | Main Dashboard file that includes the party members, chat button, find a game, quit button and the queue status panels
matchmakingdashboardcasualcriteria.res | Additional Casual file, controls the queue button and moves/resizes the gamemodes list
matchmakingdashboardcomp.res | Main Competitive mode file
matchmakingdashboardcompaccess.res | Competitive mode access requirements list
matchmakingdashboardeventmatch.res | Special events menu such as halloween etc...
matchmakingdashboardleftsidepanel.res | Contains the matchmaking panels backgrounds, shadows, close buttons used for the leftside panels (only ping panel currently)
matchmakingdashboardmvmcriteria.res | MvM Mode main file
matchmakingdashboardmvmmodeselect.res | MvM Practice/MannUp mode selection menu
matchmakingdashboardplaylist.res | Similiar to matchmakingdashboardsidepanel.res but affects only *find a game* main panel
matchmakingdashboardpopup.res |
matchmakingdashboardpopup_mapvotepanel.res |
matchmakingdashboardpopup_newmatch.res | Popup panel displayed when a new matchmaking game is found
matchmakingdashboardpopup_nextmapvoting.res |
matchmakingdashboardpopup_nextmapwinner.res |
matchmakingdashboardsidepanel.res | Contains the matchmaking panels backgrounds, shadows, close buttons used for the Casual,Comp,MvM... panels
matchmakingdatacenterpopulationpanel.res |
matchmakinggrouppanel.res | Controls the Casual enable/disable gamemode checkbutton bar
matchmakingpanel.res |
matchmakingpingpanel.res | Ping and Party settings panel
matchmakingplaylist.res | Contains the main *find a game* buttons (Casual,Comp,MvM,Training,Server,Create)
matchmakingtooltip.res | Matchmaking tips
mediccallerpanel.res |
mvmbombcarrierprogresspanel.res |
mvmcreditspendpanel.res | Part of the MvM Scoreboard, shows the wave credits
mvmcreditsubpanel.res | Part of the MvM Scoreboard, shows the full game credits
mvmcriteria.res | MvM matchmaking menu main panel
mvmeconrequirementdialog.res |
mvminworldcurrency.res | MvM wave gained/lost money
mvmscoreboard.res | MvM specific elements for the scoreboard
mvmscoreboardenemyinfo.res | MvM enemy in wave icons
mvmstatentry.res |
mvmvictorycontainer.res |
mvmvictorymannupentry.res |
mvmvictorymannuploot.res |
mvmvictorymannuppanel.res |
mvmvictorymannuptab.res |
mvmvictorypanel.res |
mvmvictorysplash.res | MvM course victory message
mvmwavelosspanel.res | MvM wave lost panel
navigationpaneltest.res |
newrecipefounddialog.res |
objectivestatusescort.res | Payload cart panel
objectivestatusmultipleescort.res | Payload race carts
playerticketstatus.res |
publishedfilebrowserdialog.res |
publishfiledialog.res |
pvpcasualrankpanel.res |
pvpcomprankpanel.res |
pvprankpanel.res | Name, Level, Experience bar used for MainMenu and end game scoreboard
quickplaybusydialog.res | No longer in use
quickplaydialog.res | No longer in use
revivedialog.res | MvM teammate revive panel
robotdestructionstatus.res |
roundinfo.res |
saxxyawards_submitform.res |
scoreboard.res | Scoreboard, including positioning for existing scoreboard elements in MvM
selectmosthelpfulfrienddialog.res |
selectplayerdialog.res | Generic player selection Panel
selectplayerdialog_coach.res | Select a player to be your coach Panel
selectplayerdialog_duel.res | Select a player to duel Menu
servernotconnectedtosteam.res |
spectator.res | Spectator panel, includes the respawn time and the spectated player carried items panel
spectatorcoach.res |
spectatorguihealth.res | Teammate Health, part of TargetUI.res
spectatortournament.res | Spectator panel for tournament modes, includes Health,Name,Uber,Respawntimes for each teammate as well as the personal respawntime
spectatortournamentguihealth.res | Teammates Health, part of spectatortournament.res
spectator_sc.res | Spectator panel, but for steam controller
stampdonationadd.res |
staticbadgepanel.res |
statpanel_base.res | After death stats
statsummary.res | Connecting to server screen, includes the Map name/Category as well as all your personal stats
statsummary_embedded.res | Personal stats for each class displayed on the loadout menu tab
steamfriendpanel.res |
steamworkshopdialog.res |
steamworkshopitem.res |
streamlistpanel.res | Main menu Twitch streams list, displays each streamer name/title/viewers
streampanel.res | Main menu Twitch streams panel
supportnotificationdialog.res |
surveypanel_base.res |
surveypanel_casualinquiry.res |
surveypanel_compinquiry.res |
surveypanel_mapquality.res |
surveypanel_matchquality.res |
surveypanel_randomcrit.res |
tankprogressbar.res | MvM Tank Health bar
tankstatuspanel.res | MvM Tank Health bar background
targetid.res | Teammates Name/Health/Ammo/Ubercharge displayed when looking at them or beign healed
tauntcallerpanel.res |
teammenu.res | Team selection Menu
teammenu_sc.res | Team selection Menu, but for steam controller
testitembotcontrols.res |
testitemdialog.res |
testitemroot.res |
textwindow.res | Server intro message
textwindowcustomserver.res | Server intro message
textwindowcustomserver_sc.res | Server intro message, but for steam controller
textwindow_sc.res | Server intro message, but for steam controller
tfadvancedoptionsdialog.res | Advance Options Menu
tfhudrobotdestruction_activestate.res |
tfhudrobotdestruction_deadstate.res |
tfhudrobotdestruction_robotindicator.res |
tfhudrobotdestruction_shieldedstate.res |
trainingcomplete.res |
trainingdialog.res |
trainingdialog_old.res |
trainingitempanel.res |
upgradeboxdialog.res |
upgradebuypanel.res | MvM buy upgrades menu
videopanel.res |
viewrecipespanel.res |
votehud.res | Controls both vote menu and ingame vote popup
vrcalibration.res |
waitingforplayerspanel.res |
wavecompletesummarypanel.res | Wave complete message for MvM
wavestatuspanel.res | Wave progress bar for MvM
winpanel.res | End round scoreboard that shows the best winning team players and game score
xboxdialogs.res |
xpsourcepanel.res |

## resource/ui/build_menu/

There are several different folders that all contain the same folder structure. They may not contain all files, however. They are:
```
ui\build_menu\
ui\build_menu\pipboy\
ui\build_menu_360\
ui\build_menu_sc\
```
The pipboy folder contains variants for the pipboy cosmetic. The _360 suffix is for the Xbox 360 controller hud. The _sc suffix is for the Steam Controller hud.

File | Description
---- | -----------
base_active.res |
base_active_teleport_target.res |
base_already_built.res |
base_cant_afford.res |
base_selectable.res |
base_unavailable.res |
base_unavailable_teleport_target.res |
dispenser_active.res |
dispenser_already_built.res |
dispenser_cant_afford.res |
dispenser_selectable.res |
dispenser_unavailable.res |
eureka_target_home_avail.res |
eureka_target_home_unavail.res |
eureka_target_tele_exit_avail.res |
eureka_target_tele_exit_unavail.res |
hudmenuengybuild.res |
hudmenueurekaeffect.res |
sentry_active.res |
sentry_already_built.res |
sentry_cant_afford.res |
sentry_selectable.res |
sentry_unavailable.res |
tele_entrance_active.res |
tele_entrance_already_built.res |
tele_entrance_cant_afford.res |
tele_entrance_unavailable.res |
tele_exit_active.res |
tele_exit_already_built.res |
tele_exit_cant_afford.res |
tele_exit_unavailable.res |
tele_selectable.res |

## resource/ui/build_menu/pipboy/

File | Description
---- | -----------
base_active.res |
base_active_teleport_target.res |
base_already_built.res |
base_cant_afford.res |
base_selectable.res |
base_unavailable.res |
base_unavailable_teleport_target.res |
dispenser_active.res |
dispenser_already_built.res |
dispenser_cant_afford.res |
dispenser_selectable.res |
dispenser_unavailable.res |
eureka_target_home_avail.res |
eureka_target_home_unavail.res |
eureka_target_tele_exit_avail.res |
eureka_target_tele_exit_unavail.res |
hudmenuengybuild.res |
hudmenueurekaeffect.res |
sentry_active.res |
sentry_already_built.res |
sentry_cant_afford.res |
sentry_selectable.res |
sentry_unavailable.res |
tele_entrance_active.res |
tele_entrance_already_built.res |
tele_entrance_cant_afford.res |
tele_entrance_unavailable.res |
tele_exit_active.res |
tele_exit_already_built.res |
tele_exit_cant_afford.res |
tele_exit_unavailable.res |
tele_selectable.res |

## resource/ui/build_menu_360/

File | Description
---- | -----------
base_active.res |
base_already_built.res |
base_cant_afford.res |
dispenser_active.res |
dispenser_already_built.res |
dispenser_cant_afford.res |
hudmenuengybuild.res |
sentry_active.res |
sentry_already_built.res |
sentry_cant_afford.res |
tele_entrance_active.res |
tele_entrance_already_built.res |
tele_entrance_cant_afford.res |
tele_exit_active.res |
tele_exit_already_built.res |
tele_exit_cant_afford.res |

## resource/ui/build_menu_sc/

File | Description
---- | -----------
base_active.res |
base_active_teleport_target.res |
base_already_built.res |
base_cant_afford.res |
base_unavailable_teleport_target.res |
dispenser_active.res |
dispenser_already_built.res |
dispenser_cant_afford.res |
eureka_target_home_avail.res |
eureka_target_home_unavail.res |
eureka_target_tele_exit_avail.res |
eureka_target_tele_exit_unavail.res |
hudmenuengybuild.res |
hudmenueurekaeffect.res |
sentry_active.res |
sentry_already_built.res |
sentry_cant_afford.res |
tele_entrance_active.res |
tele_entrance_already_built.res |
tele_entrance_cant_afford.res |
tele_exit_active.res |
tele_exit_already_built.res |
tele_exit_cant_afford.res |

## resource/ui/destroy_menu/

Like the build_menu folder, the destroy menu also contains a pipboy subfolder that contains the same files.

File | Description
---- | -----------
base_active.res |
base_inactive.res |
dispenser_active.res |
dispenser_inactive.res |
hudmenuengydestroy.res |
sentry_active.res |
sentry_inactive.res |
tele_entrance_active.res |
tele_entrance_inactive.res |
tele_exit_active.res |
tele_exit_inactive.res |

## resource/ui/destroy_menu/pipboy/

File | Description
---- | -----------
base_active.res |
base_inactive.res |
dispenser_active.res |
dispenser_inactive.res |
hudmenuengydestroy.res |
sentry_active.res |
sentry_inactive.res |
tele_entrance_active.res |
tele_entrance_inactive.res |
tele_exit_active.res |
tele_exit_inactive.res |

## resource/ui/disguise_menu/

Also like the build_menu folders, the disguise_menu also has _360 and _sc versions of it.

File | Description
---- | -----------
demoman_blue.res | class image - demoman
demoman_red.res | class image - demoman
engineer_blue.res | class image - engineer
engineer_red.res | class image - engineer
heavy_blue.res | class image - heavy
heavy_red.res | class image - heavy
hudmenuspydisguise.res | defines layout and style
medic_blue.res | class image - medic
medic_red.res | class image - medic
pyro_blue.res | class image - pyro
pyro_red.res | class image - pyro
scout_blue.res | class image - scout
scout_red.res | class image - scout
sniper_blue.res | class image - sniper
sniper_red.res | class image - sniper
soldier_blue.res | class image - soldier
soldier_red.res | class image - soldier
spy_blue.res | class image - spy
spy_red.res | class image - spy

* Credit to Doodle for these descriptions

## resource/ui/disguise_menu_360/

File | Description
---- | -----------
base.res |
demoman_blue.res | class image - demoman
demoman_red.res | class image - demoman
engineer_blue.res | class image - engineer
engineer_red.res | class image - engineer
heavy_blue.res | class image - heavy
heavy_red.res | class image - heavy
hudmenuspydisguise.res | defines layout and style
medic_blue.res | class image - medic
medic_red.res | class image - medic
pyro_blue.res | class image - pyro
pyro_red.res | class image - pyro
scout_blue.res | class image - scout
scout_red.res | class image - scout
sniper_blue.res | class image - sniper
sniper_red.res | class image - sniper
soldier_blue.res | class image - soldier
soldier_red.res | class image - soldier
spy_blue.res | class image - spy
spy_red.res | class image - spy

## resource/ui/disguise_menu_sc/

File | Description
---- | -----------
base.res |
demoman_blue.res | class image - demoman
demoman_red.res | class image - demoman
engineer_blue.res | class image - engineer
engineer_red.res | class image - engineer
heavy_blue.res | class image - heavy
heavy_red.res | class image - heavy
hudmenuspydisguise.res | defines layout and style
medic_blue.res | class image - medic
medic_red.res | class image - medic
pyro_blue.res | class image - pyro
pyro_red.res | class image - pyro
scout_blue.res | class image - scout
scout_red.res | class image - scout
sniper_blue.res | class image - sniper
sniper_red.res | class image - sniper
soldier_blue.res | class image - soldier
soldier_red.res | class image - soldier
spy_blue.res | class image - spy
spy_red.res | class image - spy

## resource/ui/econ/

File | Description
---- | -----------
backpackpanel.res | Backpack Menu
collectioncraftingdialog.res |
collectioncraftingdialog_base.res |
comboboxbackpackoverlaydialog.res | Style selection Menu
confirmapplycardupgradeapplicationdialog.res |
confirmapplydecodedialog.res |
confirmapplyducktokendialog.res | Duck token application menu
confirmapplygiftwrapdialog.res | Gift wrap application menu
confirmapplypaintcandialog.res | Paint application menu
confirmapplypaintkitdialog.res | PaintKit application menu
confirmapplystrangepartapplicationdialog.res | Strange Part application menu
confirmapplystrangerestrictionapplicationdialog.res |
confirmapplystrangifierdialog.res | Strangifier application menu
confirmapplyteamcolorpaintcandialog.res | Team colored paint application menu
confirmcustomizetexturedialog.res | Texture application menu, used for The Conscientious Objector
confirmdialogabandonnopenalty.res |
confirmdialogabandonpenalty.res |
confirmdialogabandonsafe.res |
confirmdialogoptout.res |
confirmitempreviewdialog.res |
confirmspellbookpageapplicationdialog.res | Spell Book Page application menu
confirmtransmogrifyapplicationdialog.res |
cyclingadcontainer.res |
ducksleaderboardpanel.res |
ducksleaderboards.res |
genericnotificationtoast.res | Main Menu generic notification message (example: someone gets a ring)
genericnotificationtoastmainmenu.res |
genericwaitingdialog.res |
halloweenofferingdialog.res |
inputstringforitembackpackoverlaydialog.res |
inspectionpanel.res | Inspect menu for weapons contains the war paints menu and war paints consume menus as well
inspectionpanel_cosmetic.res | Inspect panel for cosmetics in general
itemaddefault.res |
itemdiscardpanel.res |
itemmodelpanel.res |
itemmodelpanelcollectioncosmeticitem.res |
itemmodelpanelcollectionitem.res |
itempickuppanel.res | New item found panel
leaderboardpanel.res |
lobbyleaderboard.res |
manncotrade_commonstatclock.res |
notificationqueuepanel.res |
notificationspresentpanel.res | Shows up when you are in the loadout menus such as backpack and there is a new notification unchecked
notificationtoastcontainer.res | Main Menu New Item notification
notificationtoastcontrol.res | Main Menu New Item notification container (background/label)
paintkitconsumedialog.res | PaintKit consume menu
questdefinitionviewpanel.res |
questdetailspanel.res |
questeditor.res |
questlogpanel.res |
questlogpanel_halloween.res |
questmapnodepanel.res |
questmapnodetooltippanel.res |
questmappanel.res |
questmaprewarditempanel.res |
questnotificationpanel_base.res |
questnotificationpanel_pauling_standard.res |
questviewsubpanel.res |
scrollablequestdetails.res |
scrollablequestlist.res |
scrollablequestlist_halloween.res |
scrollablequestlist_toughbreak.res |
strangecounttransferdialog.res |
tradingpanel.res | Trades menu
tradingstartdialog.res | Trade exchange mode selection menu
warjoinpanel.res |
warstandingpanel.res |

## resource/ui/econ/store/v1/

File | Description
---- | -----------
storehome.res |
storehome_freetrial.res |
storehome_winter1.res |
storehome_winter2.res |
storehome_winter3.res |
storeitemcontrols.res |
storepage.res |
storepage_bundles.res |
storepage_cgtrading.res |
storepage_drgrordbort.res |
storepage_halloween.res |
storepage_maps.res |
storepage_new.res |
storepage_popular.res |
storepage_previewable.res |
storepage_summer.res |
storepanel.res |
storepreviewitempanel.res |
storepreviewitempanel_maps.res |
storeprice.res |
storeprice_bundles.res |
storeprice_jumbo.res |
storeprice_new.res |
storeprice_popular.res |
storestatusdialog.res |
storeviewcartpanel.res |

## resource/ui/econ/store/v2/

File | Description
---- | -----------
storehome_base.res |
storehome_freetrial.res |
storehome_premium.res |
storeitemcontrols.res |
storemapstampsinfodialog.res |
storepage.res |
storepage_bundles.res |
storepage_items.res |
storepage_maps.res |
storepanel.res |
storepreviewitempanel.res |
storepreviewitempanel_fullscreen.res |
storepreviewitempanel_maps.res |
storeviewcartpanel.res |

## resource/ui/notifications/

File | Description
---- | -----------
base_notification.res |
notification_manifest.txt |
notify_competitive_gc_down.res |
notify_enemy_flag_captured_blue.res |
notify_enemy_flag_captured_red.res |
notify_enemy_flag_dropped_blue.res |
notify_enemy_flag_dropped_red.res |
notify_enemy_flag_returned_blue.res |
notify_enemy_flag_returned_red.res |
notify_enemy_flag_taken_blue.res |
notify_enemy_flag_taken_red.res |
notify_golden_wrench.res |
notify_how_to_control_ghost.res |
notify_how_to_control_ghost_no_respawn.res |
notify_how_to_control_kart.res |
notify_no_invuln_with_flag_blue.res |
notify_no_invuln_with_flag_red.res |
notify_no_tele_with_flag_blue.res |
notify_no_tele_with_flag_red.res |
notify_passtime_howto.res |
notify_passtime_no_carry.res |
notify_passtime_no_cloak.res |
notify_passtime_no_disguise.res |
notify_passtime_no_holster.res |
notify_passtime_no_invuln.res |
notify_passtime_no_oob.res |
notify_passtime_no_taunt.res |
notify_passtime_no_tele.res |
notify_rd_robot_attacked_blue.res |
notify_rd_robot_attacked_red.res |
notify_special.res |
notify_touching_enemy_ctf_cap_blue.res |
notify_touching_enemy_ctf_cap_red.res |
notify_truce_end.res |
notify_truce_start.res |
notify_your_flag_captured_blue.res |
notify_your_flag_captured_red.res |
notify_your_flag_dropped_blue.res |
notify_your_flag_dropped_red.res |
notify_your_flag_returned_blue.res |
notify_your_flag_returned_red.res |
notify_your_flag_taken_blue.res |
notify_your_flag_taken_red.res |

## resource/ui/quests/

File | Description
---- | -----------
lineitem_credits.res |
lineitem_item.res |
lineitem_objective.res |
lineitem_points.res |
questitempanel_base.res |
questitemtrackerpanel_base.res |
questitemtrackerpanel_ingame_base.res |
questitemtrackerpanel_questlog_base.res |
questobjectivepanel_ingame_base.res |
questobjectivepanel_questlog_base.res |
questobjectivescorer.res |

## resource/ui/quests/cyoa/

File | Description
---- | -----------
questitemtrackerpanel_cyoa.res |
questmapregionlink.res |
questobjectivepanel_cyoa.res |

## resource/ui/quests/cyoa/regions/

File | Description
---- | -----------
region_base.res |
region_campaign_3_home.res |
region_defense.res |
region_halloween.res |
region_halloween_bosses.res |
region_halloween_community_maps.res |
region_halloween_official_maps.res |
region_maps.res |
region_offense.res |
region_overworld.res |
region_pyroland.res |
region_support.res |

## resource/ui/quests/merasmus/

File | Description
---- | -----------
questitempanel_merasmus_base.res |
questitempanel_merasmus_general.res |
questitempanel_merasmus_hhh.res |
questitempanel_merasmus_merasmus.res |
questitempanel_merasmus_monoculus.res |
questitemtrackerpanel_ingame.res |
questitemtrackerpanel_questlog.res |
questobjectivepanel_ingame.res |
questobjectivepanel_questlog.res |

## resource/ui/quests/pauling/

File | Description
---- | -----------
questitempanel_pauling_base.res |
questitempanel_pauling_borneo.res |
questitempanel_pauling_demo.res |
questitempanel_pauling_engineer.res |
questitempanel_pauling_headhunter.res |
questitempanel_pauling_heavy.res |
questitempanel_pauling_medic.res |
questitempanel_pauling_playanyclass.res |
questitempanel_pauling_powerhouse.res |
questitempanel_pauling_pyro.res |
questitempanel_pauling_scout.res |
questitempanel_pauling_sniper.res |
questitempanel_pauling_snowplow.res |
questitempanel_pauling_soldier.res |
questitempanel_pauling_spy.res |
questitempanel_pauling_suijin.res |
questitemtrackerpanel_ingame.res |
questitemtrackerpanel_questlog.res |
questobjectivepanel_ingame.res |
questobjectivepanel_questlog.res |

## resource/ui/quests/pauling/operation 2/

File | Description
---- | -----------
questitempanel_pauling_base.res | 
questitempanel_pauling_community_map_1.res | 
questitempanel_pauling_community_map_2.res | 
questitempanel_pauling_community_map_3.res | 
questitempanel_pauling_community_map_4.res | 
questitempanel_pauling_cp.res | 
questitempanel_pauling_demo.res | 
questitempanel_pauling_engineer.res | 
questitempanel_pauling_headhunter.res | 
questitempanel_pauling_heavy.res | 
questitempanel_pauling_medic.res | 
questitempanel_pauling_payload.res | 
questitempanel_pauling_playanyclass.res | 
questitempanel_pauling_pyro.res | 
questitempanel_pauling_scout.res | 
questitempanel_pauling_sniper.res | 
questitempanel_pauling_soldier.res | 
questitempanel_pauling_spy.res | 

## resource/ui/training/

File | Description
---- | -----------
main.res |

## resource/ui/training/basictraining/

File | Description
---- | -----------
classdetails.res |
classpanel.res |
classselection.res |

## resource/ui/training/modeselection/

File | Description
---- | -----------
modepanel.res |
modeselection.res |

## resource/ui/training/offlinepractice/

File | Description
---- | -----------
mapselection.res |
practicemodeselection.res |
