# File list

This is a master reference for all files used by tf2 huds.

## scripts/

File | Description
---- | -----------
chapterbackgrounds.txt | Controls the random backgrounds and characters that appear on the mainmenu
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
basechat.res | Chatbox
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
hudaccountpanel.res | Engineer metal count
hudachievementfloatingnumber.res |
hudachievementtrackeritem.res |
hudalert.res |
hudammoweapons.res | Ammo in clip and ammo in reserve
hudarenacappointcountdown.res |
hudarenaclasslayout.res |
hudarenanotification.res |
hudarenaplayercount.res |
hudarenateammenu.res |
hudarenateammenu_sc.res |
hudarenavspanel.res |
hudarenawinpanel.res |
hudbosshealth.res | Healthbar for Halloween bosses
hudbowcharge.res |
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
hudplayerclass.res | Class icon and 3d model depending on convars
hudplayerhealth.res | Health number
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
mainmenuoverride.res | central file for the main menu
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
mvmscoreboard.res | MvM specific elements for the scoreboard
mvmscoreboardenemyinfo.res | MvM enemy in wave icons
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
scoreboard.res | Scoreboard, including positioning for existing scoreboard elements in MvM
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
demoman_blue.res |
demoman_red.res |
engineer_blue.res |
engineer_red.res |
heavy_blue.res |
heavy_red.res |
hudmenuspydisguise.res |
medic_blue.res |
medic_red.res |
pyro_blue.res |
pyro_red.res |
scout_blue.res |
scout_red.res |
sniper_blue.res |
sniper_red.res |
soldier_blue.res |
soldier_red.res |
spy_blue.res |
spy_red.res |

## resource/ui/disguise_menu_sc/

File | Description
---- | -----------
base.res |
demoman_blue.res |
demoman_red.res |
engineer_blue.res |
engineer_red.res |
heavy_blue.res |
heavy_red.res |
hudmenuspydisguise.res |
medic_blue.res |
medic_red.res |
pyro_blue.res |
pyro_red.res |
scout_blue.res |
scout_red.res |
sniper_blue.res |
sniper_red.res |
soldier_blue.res |
soldier_red.res |
spy_blue.res |
spy_red.res |

## resource/ui/econ/

File | Description
---- | -----------
backpackpanel.res |
collectioncraftingdialog.res |
collectioncraftingdialog_base.res |
comboboxbackpackoverlaydialog.res |
confirmapplycardupgradeapplicationdialog.res |
confirmapplydecodedialog.res |
confirmapplyducktokendialog.res |
confirmapplygiftwrapdialog.res |
confirmapplypaintcandialog.res |
confirmapplypaintkitdialog.res |
confirmapplystrangepartapplicationdialog.res |
confirmapplystrangerestrictionapplicationdialog.res |
confirmapplystrangifierdialog.res |
confirmapplyteamcolorpaintcandialog.res |
confirmcustomizetexturedialog.res |
confirmdialogabandonnopenalty.res |
confirmdialogabandonpenalty.res |
confirmdialogabandonsafe.res |
confirmdialogoptout.res |
confirmitempreviewdialog.res |
confirmspellbookpageapplicationdialog.res |
confirmtransmogrifyapplicationdialog.res |
cyclingadcontainer.res |
ducksleaderboardpanel.res |
ducksleaderboards.res |
genericnotificationtoast.res |
genericnotificationtoastmainmenu.res |
genericwaitingdialog.res |
halloweenofferingdialog.res |
inputstringforitembackpackoverlaydialog.res |
inspectionpanel.res |
inspectionpanel_cosmetic.res |
itemaddefault.res |
itemdiscardpanel.res |
itemmodelpanel.res |
itemmodelpanelcollectioncosmeticitem.res |
itemmodelpanelcollectionitem.res |
itempickuppanel.res |
leaderboardpanel.res |
lobbyleaderboard.res |
manncotrade_commonstatclock.res |
notificationqueuepanel.res |
notificationspresentpanel.res |
notificationtoastcontainer.res |
notificationtoastcontrol.res |
paintkitconsumedialog.res |
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
tradingpanel.res |
tradingstartdialog.res |
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