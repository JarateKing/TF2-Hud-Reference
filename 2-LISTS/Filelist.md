# File list

This is a master reference for all files used by tf2 huds.

For images of some of these files to make it clear what they might be, see [here](https://github.com/cooolbros/tf2-res-file-list).

## scripts/

File | Description
---- | -----------
chapterbackgrounds.txt | **Controls the random backgrounds and characters that appear on the mainmenu**
hudanimations.txt | **Controls hl2 animations**
hudanimations_manifest.txt | **Controls which animations files are used**
hudanimations_tf.txt | **Controls the majority of animations**
hudlayout.res | **Controls the positioning of the majority of elements**
mod_textures.txt | **Controls many miscellaneous icons and textures (such as killfeed icons)**

## resource/

File | Description
---- | -----------
chatscheme.res | **Like clientscheme, but for the chat box**
chat_english.txt | **Controls some chat-related localization. Can add new localization to custom HUDs.**
clientscheme.res | **Controls definitions for font declarations, font sizes, colors, borders**
closecaption_english.dat | **Controls captions**
closecaption_english.txt | **Source file to compile into closecaption_english.dat. Also acts as localization like `chat_english.txt`**
gamemenu.res | **Controls tooltips, visibility ingame/inmenu, etc. of some main menu elements**
sourcescheme.res | **Like clientscheme, but for old-style windows like the console**

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
abusereportsubmitdialog.res | **Abuse report compilation menu**
achievementsdialog.res | **Achievements menu**
annotationspanelcallout.res | **Ingame callout panel, arrows used in training mode**
badgepanel.res |
basechat.res | **Ingame chatbox**
casualrankpanel.res | **Rank panel specifics for casual menu**
casualwelcomedialog.res | *No longer in use*
charinfoarmorysubpanel.res | **Mann co. Catalog**
charinfoloadoutsubpanel.res | **Main loadout menu, contains buttons for each TF2 class as well as backpack, crafting, catalog, trading and warpaints**
charinfopanel.res | **Loadout pages header and footer**
chatpopup.res | **Party popup messages**
cheatdetectiondialog.res | **Dialog displayed when a player gets detected with cheats**
classloadoutpanel.res | **Class loadout menu**
classmenu.res | **Contains the parent element of classselection.res**
classselection.res | **Ingame class selection menu**
classselection_sc.res | **Ingame Class selection menu** *[for steam controller]*
classtipsitem.res | **Class tips displayed in the class selection screen** *[part of classselection.res]*
classtipslist.res | **Contains the parent element of classtipsitem.res**
coachedbypanel.res | **Ingame Coach panel, information shown when you're being coached** *[also in HudLayout.res > CoachedByPanel]*
competitiveaccessinfo.res | **Competitive Menu - requirements needed for access message**
competitivewelcomedialog.res | *No longer in use*
comprankpanel.res | **Rank panel specifics for competitive menu**
comprankstooltip.res | **Competitive Menu - shows the list of the achievable competitive mode ranks**
compstats.res | **Competitive Menu - list of previous games played and statistics menu**
confirmabandondialog.res | **Server disconnect confirmation dialog**
controlpointcountdown.res | **Control point activation countdown**
controlpointicon.res | **Control point icons used for CP, Koth, A/D gamemodes, includes the amount and icon of players capping** *[also in HudLayout.res > HudControlPointIcons]*
controlpointprogressbar.res | **Control Point capture progress circle bar**
craftingpanel.res | **Crafting Panel**
craftingstatusdialog.res | **Successful crafting confirmation dialog**
dashboardpartymember.res | **Dashboard's party members (avatar, name and status)**
disguisestatuspanel.res | **Current spy disguise status** *[also in HudLayout.res > DisguiseStatus]*
dynamicrecipepanel.res | **Killsteak Kits recipe menu**
enemycountpanel.res | **MvM - attacking robots wave icons**
explanationpopup.res | **Explanation messages box properties**
flagcalloutpanel.res | 
flagstatus.res | **Flag icon and arrow** *[part of hudobjectiveflagpanel.res]*
freezepanelcallout.res | **Indicates your body parts after death** *[also in HudLayout.res > FreezePanelCallout]*
freezepanelkillerhealth.res | **Enemy health displayed on the freezecam** *[part of freezepanel_basic.res]*
freezepanel_basic.res | **Freezecam of your killer** *[also in HudLayout.res > FreezePanel]*
giveawayitempanel.res | 
globalchat.res | **Dashboard's party chat**
globalexplanations.res | **Explanations for casual, competitive, tutorial, warpaints, loadout, store**
healthiconpanel.res | **Teammates health displayed above their head** *[only visible with tf_hud_target_id_disable_floating_health "0"]*
hudaccountpanel.res | **Engineer metal count** *[also in HudLayout.res > CHudAccountPanel]*
hudachievementfloatingnumber.res |
hudachievementtrackeritem.res | **On screen achievement progress tracking panel** *[also in HudLayout.res > HudAchievementTracker]*
hudalert.res | **Incoming team balance warning** *[also in HudLayout.res > HudAlert]*
hudammoweapons.res | **Personal ammo in clip and ammo in reserve** *[also in HudLayout.res > HudWeaponAmmo]*
hudarenacappointcountdown.res | **Arena - control point activation countdown** *[also in HudLayout.res > HudArenaCapPointCountdown]*
hudarenaclasslayout.res | **Arena - team composition panel** *[also in HudLayout.res > HudArenaClassLayout]*
hudarenanotification.res | **Arena - notifications and tips** *[also in HudLayout.res > HudArenaNotification]*
hudarenaplayercount.res | **Arena - alive palyers count** *[also in HudLayout.res > HudArenaPlayerCount]*
hudarenateammenu.res | **Arena - Spectate/Fight selection menu**
hudarenateammenu_sc.res | **Arena - Spectate/Fight selection menu** *[for steam controller]*
hudarenavspanel.res | **Arena - Blue VS Red panel** *[also in HudLayout.res > HudArenaVsPanel]*
hudarenawinpanel.res | **Arena - End round win/loss panel + scoreboard** *[also in HudLayout.res > ArenaWinPanel]*
hudbosshealth.res | **Healthbar for Halloween bosses** *[also in HudLayout.res > HudBossHealth]*
hudbowcharge.res | **Old charge meter for Huntsman** *[also in HudLayout.res > HudBowCharge]*
hudcurrencyaccount.res | **MvM - Player's collected currency**
huddamageaccount.res | **Damage numbers when hitting other players** *[also in HudLayout.res > CDamageAccountPanel]*
huddemomancharge.res | **Charge meter for Stickybomb Launcher and Huntsman** *[also in HudLayout.res > HudDemomanCharge]*
huddemomanpipes.res | **Demoman Stickies count and shields charge** *[also in HudLayout.res > HudDemomanPipes]*
hudhealthaccount.res | **Plus health value displayed on health gain, ex: health kit pick up** *[also in HudLayout.res > CHealthAccountPanel]*
hudinspectpanel.res | **Teammate carried items inspection panel** *[also in HudLayout.res > HudInspectPanel]*
huditemattributetracker.res | **Contract progress tracker** *[also in HudLayout.res > ItemAttributeTracker]*
huditemeffectmeter.res | **Charge meter for:  Sandman / Wrap Assassin / Sandvich / Spy Watches / Jarate / Razorback / Cleaner's Carbine / Soldier Banners / Gas Passer**
huditemeffectmeter_cleaver.res | **Charge meter for: Flying Guillotine**
huditemeffectmeter_demoman.res | **Counter for: Eyelander heads and AirStrike**
huditemeffectmeter_engineer.res | **Counter for: Frontier Justice and Manmelter**
huditemeffectmeter_halloweensouls.res | *No longer in use*
huditemeffectmeter_heavy.res | **Charge meter for: Heavy rage in MvM**
huditemeffectmeter_kartcharge.res | **Charge meter for: Halloween Karts**
huditemeffectmeter_killstreak.res | **Counter for: killstreak weapons**
huditemeffectmeter_organs.res | **Counter for: Vita-Saw**
huditemeffectmeter_particlecannon.res | **Charge meter for: Cow Mangler**
huditemeffectmeter_pomson.res | **Charge meter for: Pomson**
huditemeffectmeter_powerupbottle.res | **Counter for: PowerUp Canteen in MvM**
huditemeffectmeter_pyro.res | **Charge meter for: Phlogistinator**
huditemeffectmeter_raygun.res | **Charge meter for: Righteous Bison**
huditemeffectmeter_sapper.res | **Charge meter for: Sapper**
huditemeffectmeter_scout.res | **Charge meter for: Bonk! Atomic Punch/Crit-a-Cola/Mad Milk and MvM medic shield**
huditemeffectmeter_sniper.res | **Counter for: Bazaar Bargain**
huditemeffectmeter_sniperfocus.res | **Charge meter for: Hitman's Heatmaker**
huditemeffectmeter_sodapopper.res | **Charge meter for: Sodapopper**
huditemeffectmeter_spy.res | **Counter for: Diamondback**
huditemeffectmeter_spyknife.res | **Charge for: Spy-cicle**
hudkillstreaknotice.res | **Server's killstreaks notification, someone on the server has reached a Killstreak milestone**
hudmannvsmachinestatus.res | **MvM - Main file, holds the positioning of most MvM elements such as money and wave status** *[also in HudLayout.res > HudMannVsMachineStatus]*
hudmatchstatus.res | **Round Timer and Red & Blue team players status also contains the casual and competitive prematch doors animation** *[also in HudLayout.res > HudMatchStatus]*
hudmatchsummary.res | **End of match summary scoreboard used for Casuals and Competitive gamemodes** *[also in HudLayout.res > MatchSummary]*
hudmediccharge.res | **Medic's Ubercharge percentage, Vaccinator charges and resist icon** *[also in HudLayout.res > HudMedicCharge]*
hudmenutauntselection.res | **Ingame taunt selection menu** *[also in HudLayout.res > HudMenuTauntSelection]*
hudmenutauntselection_sc.res | **Ingame taunt selection menu** *[for steam controller]*
hudminigame_base.res | **Main Halloween minigame file for sd_doomsday_event** *[also in HudLayout.res > HudMiniGame]*
hudminigame_collection.res | **Halloween ducks collection race minigame for sd_doomsday_event**
hudminigame_platform.res | **Halloween platform elimination minigame for sd_doomsday_event**
hudminigame_soccer.res | **Halloween soccer minigame for sd_doomsday_event**
hudminigame_soccersuddendeath.res | **Halloween soccer sudden death minigame for sd_doomsday_event**
hudobjectiveflagpanel.res | **Flag/Intelligence status and blue & red scores for CTF mode**
hudobjectivekothtimepanel.res | **King of the hill red and blue timers** *[also in HudLayout.res > HudKothTimeStatus]*
hudobjectiveplayerdestruction.res | **Player destruction mode status**
hudobjectiverobotdestruction.res | **Robot destruction counter for the robots destroyed**
hudobjectivestatus.res | *No longer in use*
hudobjectivetimepanel.res | **Contains the round timer background, clock icon and server timer as well as the labels for setup, overtime, waiting for players and sudden death**
hudpasstime.res | **Parent element of the passtime HUD**
hudpasstimeballstatus.res | **Passtime Ball status bar**
hudpasstimeoffscreenarrow.res | **Passtime ball arrow**
hudpasstimepassnotify.res | **Passtime in pass range and incominc pass notifications**
hudpasstimeteamscore.res | **Passtime blue & red teams score panel**
hudplayerclass.res | **Controls the 2D Class icon or 3D player model depending on convars, the spy diguise 2D model, spy silhouette and the carried weapon info**
hudplayerhealth.res | **Personal health value and status icons**
hudpowerupeffectmeter.res | **MannPower Supernova powerup meter**
hudpvewinpanel.res | **MvM - Wave lost panel**
hudrocketpack.res | **Charge meter for: Thermal Thruster**
hudroundcounter.res | **Red and blue rounds won counter dots and backgrounds**
hudspellselection.res | **Owned spells selection for halloween modes** *[also in HudLayout.res > HudSpellMenu]*
hudstalemate.res | **Arena stalemate message** *[also in HudLayout.res > HudStalemate]*
hudstopwatch.res | **Time to beat in Tournament Mode for payload and attack/defense maps** *[also in HudLayout.res > HudStopWatch]*
hudteamgoal.res | **Summary of the game mode goals at the start of the round** *[also in HudLayout.res > HudTeamGoal]*
hudteamgoaltournament.res | **Summary of the game mode goals for tounament game modes** *[also in HudLayout.res > HudTeamGoalTournament]*
hudteamswitch.res | **Teams auto-balance message** *[also in HudLayout.res > HudTeamSwitch]*
hudtournament.res | **Tournament mode Blue-Red teams ready status and game win conditions** *[also in HudLayout.res > HudTournament]*
hudtournamentsetup.res | **Ready/Unready and team name change PopUp menu for tournament mode** *[also in HudLayout.res > HudTournamentSetup]*
hudtraining.res | **Training mode instructor positioning messages**
hudtrainingmsg.res | **Training mode instructor messages**
hudupgradepanel.res | **MvM - upgrades menu** *[also in HudLayout.res > HudUpgradePanel]*
hudwarcount.res | *No longer in use*
hudweaponselection.res | **Ingame weapon selection menu, used with hud_fastswitch "0"**
hud_obj_dispenser.res | **Engineer dispenser build status and Health** *[also in HudLayout.res > BuildingStatus_Engineer]*
hud_obj_sapper.res | **Building sapped status** *[also in HudLayout.res > BuildingStatus_Spy]*
hud_obj_sentrygun.res | **Engineer sentrygun build status, health, ammo** *[also in HudLayout.res > BuildingStatus_Engineer]*
hud_obj_sentrygun_disp.res | **Optional MvM Minisentry build status, health, ammo** *[also in HudLayout.res > BuildingStatus_Engineer]*
hud_obj_tele.res | **Engineer Teleport build status, health** *[also in HudLayout.res > BuildingStatus_Engineer]*
hud_obj_tele_entrance.res | **Engineer Teleport entrance health** *[also in HudLayout.res > BuildingStatus_Engineer]*
hud_obj_tele_exit.res | **Engineer Teleport exit health** *[also in HudLayout.res > BuildingStatus_Engineer]*
importfiledialog.res | **Workshop Import menu**
importfiletexteditdialog.res | **Workshop text edit menu**
importmaterialeditdialog.res | **Workshop material edit menu**
importpreviewitempanel.res | **Workshop preview menu**
ingamequeuestatus.res | **Currently queued for Casual/Competitive/MvM ingame icon** *[also in HudLayout.res > QueueHUDStatus]*
intromenu.res | **Gamemode explanation video displayed after joining a server**
intromenu_sc.res | **Gamemode explanation video displayed after joining a server** *[for steam controller]*
invitenotification.res | **Invite to party received message**
itemoptionspanel.res | **Item style selection menu**
itemquickswitch.res | **Ingame loadout and weapons quickswitch menu** *[also in HudLayout.res > ItemQuickSwitchPanel]*
itemrenameconfirmationdialog.res | **Name Tag - Description Tag confirmation menu**
itemrenamedialog.res | **Name Tag - Description Tag appliaction menus**
itemrenameinvaliddialog.res | **Name Tag - Description Tag appliaction failed menu**
itemselectionpanel.res | **Loadout item/weapon selection menu**
itemslotpanel.res | 
layeredmappanel.res | *No longer in use*
layeredmappanelitem.res | *No longer in use*
layeredmappaneltooltip.res | *No longer in use*
leaderboardentry.res | **Duels Leaderboard displayed in the loading screen**
leaderboardentryrank.res | **Leaderboard displayed in the competitive menu**
leaderboardentryscore.res | 
leaderboardspreadentry.res | 
loadoutpresetpanel.res | **Loadout's A - B - C - D buttons**
lobbycontainerframe.res | *No longer in use*
lobbycontainerframe_casual.res | *No longer in use*
lobbycontainerframe_comp.res | *No longer in use*
lobbycontainerframe_mvm.res | *No longer in use*
lobbypanel.res | *No longer in use*
lobbypanel_casual.res | *No longer in use*
lobbypanel_comp.res | *No longer in use*
lobbypanel_mvm.res | *No longer in use*
mainmenueventplaylistentry.res |
mainmenuoverride.res | **Central main menu file, holds most main menu elements**
mainmenuplaylistentry.res | **Controls the buttons and descriptions of the casual, competitive, mvm, training, server browser gamemodes when the find a game button is clicked**
mainmenu_saxxyawards.res | **Saxxy awards main menu elements**
mapinfomenu.res | **Map informations menu**
mapinfomenu_sc.res | **Map information menu** *[for steam controller]*
matchhistoryentrypanel.res | **Comptitive Menu - matches history menu**
matchmakingcasualcriteria.res | **Casual Menu - Main Casual mode menu file**
matchmakingcategorymappanel.res | **Casual Menu - popup map list for each gamemode**
matchmakingcategorypanel.res | **Casual Menu - game mode category panels**
matchmakingdashboard.res | **Main Dashboard file that includes the party members, chat button, find a game, quit button and the queue status panels**
matchmakingdashboardcasualcriteria.res | **Casual Menu - controls the queue button and moves/resizes the gamemodes list**
matchmakingdashboardcomp.res | **Comptitive Menu - main competitive mode menu file**
matchmakingdashboardcompaccess.res | **Comptitive Menu - parent panel of the comp access requirements list**
matchmakingdashboardeventmatch.res | **Special events menu such as Halloween etc...**
matchmakingdashboardleftsidepanel.res | **Contains the matchmaking panels backgrounds, shadows, close buttons used for the leftside panels (only ping panel currently)**
matchmakingdashboardmvmcriteria.res | **MvM Menu - Main MvM Mode menu file**
matchmakingdashboardmvmmodeselect.res | **MvM Menu - Practice/MannUp mode selection menu**
matchmakingdashboardplaylist.res | **Similiar to matchmakingdashboardsidepanel.res but affects only *find a game* main panel**
matchmakingdashboardpopup.res | *No longer in use*
matchmakingdashboardpopup_mapvotepanel.res | **End of game next map vote buttons**
matchmakingdashboardpopup_newmatch.res | **Popup panel displayed when a new matchmaking game is found**
matchmakingdashboardpopup_nextmapvoting.res | **End of game next map vote panel**
matchmakingdashboardpopup_nextmapwinner.res | **Next map vote winner**
matchmakingdashboardsidepanel.res | **Contains the matchmaking panels backgrounds, shadows, close buttons used for the Casual,Comp,MvM... panels**
matchmakingdatacenterpopulationpanel.res | **Server population panel used for matchmakingpingpanel**
matchmakinggrouppanel.res | **Casual Menu - Controls the Casual enable/disable gamemode checkbutton bar**
matchmakingpanel.res | *No longer in use*
matchmakingpingpanel.res | **Ping and Party settings panel**
matchmakingplaylist.res | **Contains the main *find a game* buttons (Casual,Comp,MvM,Training,Server,Create)**
matchmakingtooltip.res | **Matchmaking tips**
mediccallerpanel.res | **Medic call bubbles**
mvmbombcarrierprogresspanel.res | **MvM - bomb progress bar**
mvmcreditspendpanel.res | **MvM - Part of the MvM Scoreboard, shows the wave credits**
mvmcreditsubpanel.res | **MvM - Part of the MvM Scoreboard, shows the full game credits**
mvmcriteria.res | **MvM Menu - tour selection menus**
mvmeconrequirementdialog.res | **MvM Menu - Mann up requirements panel**
mvminworldcurrency.res | **MvM - wave gained/lost money**
mvmscoreboard.res | **MvM - main scoreboard file**
mvmscoreboardenemyinfo.res | **MvM - enemy wave icons**
mvmstatentry.res |
mvmvictorycontainer.res | **MvM - Main container for MvM victory MannUp and Normal**
mvmvictorymannupentry.res | **MvM - MannUp victory loot collect panel**
mvmvictorymannuploot.res | **MvM - MannUp victory received item icon**
mvmvictorymannuppanel.res | **MvM - MannUp victory player tabs**
mvmvictorymannuptab.res | **MvM - MannUp victory player tab specifics**
mvmvictorypanel.res | **MvM - map victory panel**
mvmvictorysplash.res | **MvM - course victory message**
mvmwavelosspanel.res | **MvM - wave lost panel**
navigationpaneltest.res | *no longer in use*
newrecipefounddialog.res |
objectivestatusescort.res | **Payload cart progress bar**
objectivestatusmultipleescort.res | **Payload race carts red and blue progress bars**
playerticketstatus.res |
publishedfilebrowserdialog.res |
publishfiledialog.res |
pvpcasualrankpanel.res | **Rank panel specifics for casual**
pvpcomprankpanel.res | **Rank panel specifics for competitive**
pvprankpanel.res | **Player Name, Level, Experience bar used for MainMenu and end game scoreboard**
quickplaybusydialog.res | *No longer in use*
quickplaydialog.res | *No longer in use*
revivedialog.res | **MvM - teammate revive panel**
robotdestructionstatus.res | **Robot destruction status icon and arrow**
roundinfo.res | **Territorial control map information**
saxxyawards_submitform.res | **Form application submit panel for the saxxy awards**
scoreboard.res | **Scoreboard, Includes a list of the all the players currently in the server, all the personal stats and the server's timer and map name**
selectmosthelpfulfrienddialog.res | **Helpful friend selection dialog, shows when F2P account upgrades to premium and the selected friend will receive the professors speks**
selectplayerdialog.res | **Generic player selection Panel**
selectplayerdialog_coach.res | **Select a player to be your coach Panel**
selectplayerdialog_duel.res | **Select a player to duel Menu**
servernotconnectedtosteam.res | **Lost connection to steam message**
spectator.res | **Spectator panel, includes the respawn time and the spectated player carried items panel**
spectatorcoach.res | **Spectator panel coach variant**
spectatorguihealth.res | **Teammate Health** *[Part of TargetUI.res]*
spectatortournament.res | **Spectator panel for tournament modes, includes Health,Name,Uber,Respawntimes for each teammate as well as the personal respawntime**
spectatortournamentguihealth.res | **Teammates Health** *[part of spectatortournament.res]
spectator_sc.res | **Spectator panel** *[for steam controller]*
stampdonationadd.res | **Mann.co store stamp donation menu**
staticbadgepanel.res |
statpanel_base.res | **After death stats panel** *[also in HudLayout.res > StatPanel]*
statsummary.res | **Connecting to server screen, includes the Map name/Category as well as all your personal stats**
statsummary_embedded.res | **Personal stats for each class displayed on the loadout menu tab**
steamfriendpanel.res | **Steam friends avatar, name and status displayed in the main menu's friends list**
steamworkshopdialog.res | **Workshop menu**
steamworkshopitem.res | **Workshop item import/preview**
streamlistpanel.res | *No longer in use*
streampanel.res | *No longer in use*
supportnotificationdialog.res | **Valve's customer support messages**
surveypanel_base.res | **Main file for the end of game surevey panel**
surveypanel_casualinquiry.res | **End of game surevey for casual quality**
surveypanel_compinquiry.res | **End of game surevey for competitive quality**
surveypanel_mapquality.res | **End of game surevey for map quality**
surveypanel_matchquality.res |  **End of game surevey for match quality**
surveypanel_randomcrit.res |  **End of game surevey for random crits**
tankprogressbar.res | **MvM - Tank Health bar**
tankstatuspanel.res | **MvM - Tank Health bar background**
targetid.res | **Teammates Name/Health/Ammo/Ubercharge displayed when looking at them or beign healed** *[also ins HudLayout.res > CMainTargetID, CSecondaryTargetID]*
tauntcallerpanel.res | **Bubble displayed above a taunt player when you are able to join the taunt**
teammenu.res | **Team selection Menu**
teammenu_sc.res | **Team selection Menu** *[for steam controller]*
testitembotcontrols.res | **ItemTest bot controls**
testitemdialog.res | **ItemTest items panel**
testitemroot.res | **ItemTest Main panel**
textwindow.res | **MOTD message when joining a server**
textwindowcustomserver.res | **Server intro message and HTML panel**
textwindowcustomserver_sc.res | **Server intro message and HTML panel** *[for steam controller]*
textwindow_sc.res | **MOTD message when joining a server** *[for steam controller]*
tfadvancedoptionsdialog.res | **Advance Options Menu**
tfhudrobotdestruction_activestate.res | **Robot destruction indicators, active state**
tfhudrobotdestruction_deadstate.res | **Robot destruction indicators, dead state**
tfhudrobotdestruction_robotindicator.res | **Robot destruction indicators**
tfhudrobotdestruction_shieldedstate.res | **Robot destruction shiel state**
trainingcomplete.res | **You have completed the training dialog**
trainingdialog.res | *No longer in use*
trainingdialog_old.res | *No longer in use*
trainingitempanel.res | *No longer in use*
upgradeboxdialog.res | **Free to Play / litimed account needs upgrade message**
upgradebuypanel.res | **MvM - upgrade icon and buy/sell buttons** *[part of hudupgradepanel.res]*
videopanel.res | **Video frame settings for the video panel**
viewrecipespanel.res |
votehud.res | **Controls both vote menu and ingame vote popup** *[also in HudLayout.res > CHudVote]*
vrcalibration.res | **Virtual reality device calibration instructions**
waitingforplayerspanel.res |
wavecompletesummarypanel.res | **MvM - Wave complete message**
wavestatuspanel.res | **MvM - Wave progress bar**
winpanel.res | **Win/loss panel, displays the round's most valuable players and the blue and red current score** *[also in HudLayout.res > WinPanel]*
xboxdialogs.res | **XBOX dialogs**
xpsourcepanel.res | **Label for the experience gained at the end of a casual match**

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
base_active.res | **Base file used when a building can be actively built**
base_active_teleport_target.res | **Eureka effect teleport target**
base_already_built.res | **Base file used when a building is already built**
base_cant_afford.res | **Base file used when a building can't be afforded**
base_selectable.res | 
base_unavailable.res | **Base file used for unavailable buildings** *[can only happen during the tutorial]*
base_unavailable_teleport_target.res | **Eureka effect teleport target unavailable**
dispenser_active.res | **Dispenser active panel**
dispenser_already_built.res | **Dispenser already built panel**
dispenser_cant_afford.res | **Dispenser can't be afforded panel**
dispenser_selectable.res |
dispenser_unavailable.res | **Dispenser unavailable** *[can only happen during the tutorial]*
eureka_target_home_avail.res | **Eureka effect home target selectable**
eureka_target_home_unavail.res | **Eureka effect home target unavailable**
eureka_target_tele_exit_avail.res | **Eureka effect teleport target selectable**
eureka_target_tele_exit_unavail.res | **Eureka effect teleport target unavailable**
hudmenuengybuild.res | **Defines layout and style of the build menu** *[also in HudLayout.res > HudMenuEngyBuild]*
hudmenueurekaeffect.res | **Defines layout and style of the eureka effect menu** *[also in HudLayout.res > HudEurekaEffectTeleportMenu]*
sentry_active.res | **Sentry active panel**
sentry_already_built.res | **Sentry already built panel**
sentry_cant_afford.res | **Sentry can't be afforded panel**
sentry_selectable.res |
sentry_unavailable.res | **Sentry unavailable** *[can only happen during the tutorial]*
tele_entrance_active.res | **Teleport entrance active panel**
tele_entrance_already_built.res | **Teleport entrance already built panel**
tele_entrance_cant_afford.res | **Teleport entrance can't be afforded panel**
tele_entrance_unavailable.res | **Teleport entrance unavailable** *[can only happen during the tutorial]*
tele_exit_active.res | **Teleport exit active panel**
tele_exit_already_built.res | **Teleport exit already built panel**
tele_exit_cant_afford.res | **Teleport exit can't be afforded panel**
tele_exit_unavailable.res | **Teleport exit unavailable** *[can only happen during the tutorial]*
tele_selectable.res |

## resource/ui/build_menu/pipboy/

File | Description
---- | -----------
base_active.res | **PipBoy Base file used when a building can be actively built**
base_active_teleport_target.res | **PipBoy Eureka effect teleport target**
base_already_built.res | **PipBoy Base file used when a building is already built**
base_cant_afford.res | **PipBoy Base file used when a building can't be afforded**
base_selectable.res | 
base_unavailable.res | **PipBoy Base file used for unavailable buildings** *[can only happen during the tutorial]*
base_unavailable_teleport_target.res | **PipBoy Eureka effect teleport target unavailable**
dispenser_active.res | **PipBoy Dispenser active panel**
dispenser_already_built.res | **PipBoy Dispenser already built panel**
dispenser_cant_afford.res | **PipBoy Dispenser can't be afforded panel**
dispenser_selectable.res |
dispenser_unavailable.res | **PipBoy Dispenser unavailable** *[can only happen during the tutorial]*
eureka_target_home_avail.res | **PipBoy Eureka effect home target selectable**
eureka_target_home_unavail.res | **PipBoy Eureka effect home target unavailable**
eureka_target_tele_exit_avail.res | **PipBoy Eureka effect teleport target selectable**
eureka_target_tele_exit_unavail.res | **PipBoy Eureka effect teleport target unavailable**
hudmenuengybuild.res | **Defines layout and style of the PipBoy build menu** *[also in HudLayout.res > HudMenuEngyBuild]*
hudmenueurekaeffect.res | **Defines layout and style of the PipBoy eureka effect menu** *[also in HudLayout.res > HudEurekaEffectTeleportMenu]*
sentry_active.res | **PipBoy Sentry active panel**
sentry_already_built.res | **PipBoy Sentry already built panel**
sentry_cant_afford.res | **PipBoy Sentry can't be afforded panel**
sentry_selectable.res |
sentry_unavailable.res | **PipBoy Sentry unavailable** *[can only happen during the tutorial]*
tele_entrance_active.res | **PipBoy Teleport entrance active panel**
tele_entrance_already_built.res | **PipBoy Teleport entrance already built panel**
tele_entrance_cant_afford.res | **PipBoy Teleport entrance can't be afforded panel**
tele_entrance_unavailable.res | **PipBoy Teleport entrance unavailable** *[can only happen during the tutorial]*
tele_exit_active.res | **PipBoy Teleport exit active panel**
tele_exit_already_built.res | **PipBoy Teleport exit already built panel**
tele_exit_cant_afford.res | **PipBoy Teleport exit can't be afforded panel**
tele_exit_unavailable.res | **PipBoy Teleport exit unavailable** *[can only happen during the tutorial]*
tele_selectable.res |

## resource/ui/build_menu_360/

File | Description
---- | -----------
base_active.res | **XBOX Base file used when a building can be actively built**
base_already_built.res | **XBOX Base file used when a building is already built**
base_cant_afford.res | **XBOX Base file used when a building can't be afforded**
dispenser_active.res | **XBOX Dispenser active panel**
dispenser_already_built.res | **XBOX Dispenser already built panel**
dispenser_cant_afford.res | **XBOX Dispenser can't be afforded panel**
hudmenuengybuild.res | **Defines layout and style of the XBOX build menu**
sentry_active.res | **XBOX Sentry active panel**
sentry_already_built.res | **XBOX Sentry already built panel**
sentry_cant_afford.res | **XBOX Sentry can't be afforded panel**
tele_entrance_active.res | **XBOX Teleport entrance active panel**
tele_entrance_already_built.res | **XBOX Teleport entrance already built panel**
tele_entrance_cant_afford.res | **XBOX Teleport entrance can't be afforded panel**
tele_exit_active.res | **XBOX Teleport exit active panel**
tele_exit_already_built.res | **XBOX Teleport exit already built panel**
tele_exit_cant_afford.res | **XBOX Teleport exit can't be afforded panel**

## resource/ui/build_menu_sc/

File | Description
---- | -----------
base_active.res | **Base file used when a building can be actively built** *[for steam controller]*
base_active_teleport_target.res | **Eureka effect teleport target** *[for steam controller]*
base_already_built.res | **Base file used when a building is already built** *[for steam controller]*
base_cant_afford.res | **Base file used when a building can't be afforded** *[for steam controller]*
base_unavailable_teleport_target.res | **Eureka effect teleport target unavailable** *[for steam controller]*
dispenser_active.res | **Dispenser active panel** *[for steam controller]*
dispenser_already_built.res | **Dispenser already built panel** *[for steam controller]*
dispenser_cant_afford.res | **Dispenser can't be afforded panel** *[for steam controller]*
eureka_target_home_avail.res | **Eureka effect home target selectable** *[for steam controller]*
eureka_target_home_unavail.res | **Eureka effect home target unavailable** *[for steam controller]*
eureka_target_tele_exit_avail.res | **Eureka effect teleport target selectable** *[for steam controller]*
eureka_target_tele_exit_unavail.res | **Eureka effect teleport target unavailable** *[for steam controller]*
hudmenuengybuild.res | **Defines layout and style of the build menu** *[for steam controller]* *[also in HudLayout.res > HudMenuEngyBuild]*
hudmenueurekaeffect.res | **Defines layout and style of the eureka effect menu** *[for steam controller]* *[also in HudLayout.res > HudEurekaEffectTeleportMenu]*
sentry_active.res | **Sentry active panel** *[for steam controller]*
sentry_already_built.res | **Sentry already built panel** *[for steam controller]*
sentry_cant_afford.res | **Sentry can't be afforded panel** *[for steam controller]*
tele_entrance_active.res | **Teleport entrance active panel** *[for steam controller]*
tele_entrance_already_built.res | **Teleport entrance already built panel** *[for steam controller]*
tele_entrance_cant_afford.res | **Teleport entrance can't be afforded panel** *[for steam controller]*
tele_exit_active.res | **Teleport exit active panel** *[for steam controller]*
tele_exit_already_built.res | **Teleport exit already built panel** *[for steam controller]*
tele_exit_cant_afford.res | **Teleport exit can't be afforded panel** *[for steam controller]*

## resource/ui/destroy_menu/

Like the build_menu folder, the destroy menu also contains a pipboy subfolder that contains the same files.

File | Description
---- | -----------
base_active.res | **Base file used when a building can be actively destoyed**
base_inactive.res | **Base file used when a building isn't yet built**
dispenser_active.res | **Dispenser destroy panel**
dispenser_inactive.res | **Dispenser not built panel**
hudmenuengydestroy.res | **Defines layout and style of the destroy menu** *[also in HudLayout.res > HudMenuEngyDestroy]*
sentry_active.res | **Sentry destroy panel**
sentry_inactive.res | **Sentry not built panel**
tele_entrance_active.res | **Tele Entrance destroy panel**
tele_entrance_inactive.res | **Tele Entrance not built panel**
tele_exit_active.res | **Tele Exit destroy panel**
tele_exit_inactive.res | **Tele Exit not built panel**

## resource/ui/destroy_menu/pipboy/

File | Description
---- | -----------
base_active.res | **PipBoy Base file used when a building can be actively destoyed**
base_inactive.res | **PipBoy Base file used when a building isn't yet built**
dispenser_active.res | **PipBoy Dispenser destroy panel**
dispenser_inactive.res | **PipBoy Dispenser not built panel**
hudmenuengydestroy.res | **Defines layout and style of the PipBoy destroy menu** *[also in HudLayout.res > HudMenuEngyDestroy]*
sentry_active.res | **PipBoy Sentry destroy panel**
sentry_inactive.res | **PipBoy Sentry not built panel**
tele_entrance_active.res | **PipBoy Tele Entrance destroy panel**
tele_entrance_inactive.res | **PipBoy Tele Entrance not built panel**
tele_exit_active.res | **PipBoy Tele Exit destroy panel**
tele_exit_inactive.res | **PipBoy Tele Exit not built panel**

## resource/ui/disguise_menu/

Also like the build_menu folders, the disguise_menu also has _360 and _sc versions of it.

File | Description
---- | -----------
demoman_blue.res | **class image - demoman**
demoman_red.res | **class image - demoman**
engineer_blue.res | **class image - engineer**
engineer_red.res | **class image - engineer**
heavy_blue.res | **class image - heavy**
heavy_red.res | **class image - heavy**
hudmenuspydisguise.res | **defines layout and style** *[also in HudLayout.res > HudMenuSpyDisguise]*
medic_blue.res | **class image - medic**
medic_red.res | **class image - medic**
pyro_blue.res | **class image - pyro**
pyro_red.res | **class image - pyro**
scout_blue.res | **class image - scout**
scout_red.res | **class image - scout**
sniper_blue.res | **class image - sniper**
sniper_red.res | **class image - sniper**
soldier_blue.res | **class image - soldier**
soldier_red.res | **class image - soldier**
spy_blue.res | **class image - spy**
spy_red.res | **class image - spy**

* Credit to Doodle for these descriptions

## resource/ui/disguise_menu_360/

File | Description
---- | -----------
base.res |
demoman_blue.res | **class image - demoman** *[for XBOX]*
demoman_red.res | **class image - demoman** *[for XBOX]*
engineer_blue.res | **class image - engineer** *[for XBOX]*
engineer_red.res | **class image - engineer** *[for XBOX]*
heavy_blue.res | **class image - heavy** *[for XBOX]*
heavy_red.res | **class image - heavy** *[for XBOX]*
hudmenuspydisguise.res | **defines layout and style** *[for XBOX]*
medic_blue.res | **class image - medic** *[for XBOX]*
medic_red.res | **class image - medic** *[for XBOX]*
pyro_blue.res | **class image - pyro** *[for XBOX]*
pyro_red.res | **class image - pyro** *[for XBOX]*
scout_blue.res | **class image - scout** *[for XBOX]*
scout_red.res | **class image - scout** *[for XBOX]*
sniper_blue.res | **class image - sniper** *[for XBOX]*
sniper_red.res | **class image - sniper** *[for XBOX]*
soldier_blue.res | **class image - soldier** *[for XBOX]*
soldier_red.res | **class image - soldier** *[for XBOX]*
spy_blue.res | **class image - spy** *[for XBOX]*
spy_red.res | **class image - spy** *[for XBOX]*

## resource/ui/disguise_menu_sc/

File | Description
---- | -----------
base.res |
demoman_blue.res | **class image - demoman** *[for steam controller]*
demoman_red.res | **class image - demoman** *[for steam controller]*
engineer_blue.res | **class image - engineer** *[for steam controller]*
engineer_red.res | **class image - engineer** *[for steam controller]*
heavy_blue.res | **class image - heavy** *[for steam controller]*
heavy_red.res | **class image - heavy** *[for steam controller]*
hudmenuspydisguise.res | **defines layout and style** *[for steam controller]*
medic_blue.res | **class image - medic** *[for steam controller]*
medic_red.res | **class image - medic** *[for steam controller]*
pyro_blue.res | **class image - pyro** *[for steam controller]*
pyro_red.res | **class image - pyro** *[for steam controller]*
scout_blue.res | **class image - scout** *[for steam controller]*
scout_red.res | **class image - scout** *[for steam controller]*
sniper_blue.res | **class image - sniper** *[for steam controller]*
sniper_red.res | **class image - sniper** *[for steam controller]*
soldier_blue.res | **class image - soldier** *[for steam controller]*
soldier_red.res | **class image - soldier** *[for steam controller]*
spy_blue.res | **class image - spy** *[for steam controller]*
spy_red.res | **class image - spy** *[for steam controller]*

## resource/ui/econ/

File | Description
---- | -----------
backpackpanel.res | **Backpack Menu**
collectioncraftingdialog.res | **Contains some collectioncraftingdialog_base.res overrides for the trade up contract**
collectioncraftingdialog_base.res | **Contains the elements for the unboxing screen and trade up contract**
comboboxbackpackoverlaydialog.res | **Item Style selection Menu**
confirmapplycardupgradeapplicationdialog.res | **Spell application menu**
confirmapplydecodedialog.res | **Crate unbox confirmation menu**
confirmapplyducktokendialog.res | **Duck token application menu**
confirmapplygiftwrapdialog.res | **Gift wrap application menu**
confirmapplypaintcandialog.res | **Paint application menu**
confirmapplypaintkitdialog.res | **PaintKit application menu**
confirmapplystrangepartapplicationdialog.res | **Strange Part application menu**
confirmapplystrangerestrictionapplicationdialog.res | **Strange restriction application menu**
confirmapplystrangifierdialog.res | **Strangifier application menu**
confirmapplyteamcolorpaintcandialog.res | **Team colored paint application menu**
confirmcustomizetexturedialog.res | **Texture application menu, used for The Conscientious Objector**
confirmdialog.res | **Quit game confirmation message**
confirmdialogabandonnopenalty.res | **Disconnect confirmation with no penalty**
confirmdialogabandonpenalty.res | **Disconnect confirmation with penalty**
confirmdialogabandonsafe.res | **Disconnect confirmation**
confirmdialogoptout.res |
confirmitempreviewdialog.res | **Item rent confirmation menu, used when you test an item from the mann.co store for a week**
confirmspellbookpageapplicationdialog.res | **Spell Book Page application menu**
confirmtransmogrifyapplicationdialog.res | **Costume Transmogrifier application menu**
cyclingadcontainer.res | **Advertisement box**
ducksleaderboardpanel.res | **Duck collection leaderboard**
ducksleaderboards.res | **Duck collection leaderboard**
genericnotificationtoast.res | **Ingame notification for trade, duel challenge, ringe received, new game found, you should equip the spellbook or powerupbottle message and more...**
genericnotificationtoastmainmenu.res | **Main Menu generic notification message** *[example: You have a new item! label or when someone gets a ring etc...]*
genericwaitingdialog.res | **Waiting for player to respond message**
halloweenofferingdialog.res | **Contains some collectioncraftingdialog_base.res overrides for Gargoyle Halloween Transmuting trade up contract**
inputstringforitembackpackoverlaydialog.res | **Taunt selection entry for Mann Co. Director's Cut Reel**
inspectionpanel.res | **Inspect menu for weapons contains the war paints menu and war paints consume menus as well**
inspectionpanel_cosmetic.res | **Inspect panel for cosmetics in general**
itemaddefault.res |
itemdiscardpanel.res | **Item discard panel used when the backpack is full**
itemmodelpanel.res | **Item properties: unusual, halloween, paint, strange, equipped icons**
itemmodelpanelcollectioncosmeticitem.res | **Item properties for collection items**
itemmodelpanelcollectionitem.res | **Item properties collection items**
itempickuppanel.res | **New item found/received panel**
leaderboardpanel.res |
lobbyleaderboard.res |
manncotrade_commonstatclock.res | **Contains some collectioncraftingdialog_base.res overrides for the Civilian Stat Clock trade up contract**
messageboxdialog | **Generic confirm action message**
notificationqueuepanel.res | **Controls the buffer time between present ingame notifications**
notificationspresentpanel.res | **Shows up when you are in the loadout menus such as backpack and there is a new notification unchecked**
notificationtoastcontainer.res | **Ingame popup notification, contains the background and parent element of genericnotificationtoast.res**
notificationtoastcontrol.res | **Main menu notification accept/decline buttons** 
paintkitconsumedialog.res | **PaintKit redeem menu**
questdefinitionviewpanel.res |
questdetailspanel.res |
questeditor.res |
questlogpanel.res |
questlogpanel_halloween.res |
questmapnodepanel.res |
questmapnodetooltippanel.res |
questmappanel.res | **Main Contracker file**
questmaprewarditempanel.res |
questnotificationpanel_base.res | **Miss Pauling annoying incoming message for quests**
questnotificationpanel_pauling_standard.res |
questviewsubpanel.res |
scrollablequestdetails.res | *No longer in use*
scrollablequestlist.res | *No longer in use*
scrollablequestlist_halloween.res | *No longer in use*
scrollablequestlist_toughbreak.res | *No longer in use*
strangecounttransferdialog.res | **Strange count transfer tool menu**
tradingpanel.res | *No longer in use*
tradingstartdialog.res | **Trade exchange mode selection menu**
warjoinpanel.res | **Pyro vs Heavy update, join war panel**
warstandingpanel.res | **Pyro vs Heavy war update panel**

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
storehome_base.res | **Store home**
storehome_freetrial.res | **Store free trial panel**
storehome_premium.res | **Premium callout mann.co image**
storeitemcontrols.res | **Add to cart button**
storemapstampsinfodialog.res | **Store map stamp preview**
storepage.res | **Main file**
storepage_bundles.res | **Store bundles** *[part of storepage.res]*
storepage_items.res | **Store items** *[part of storepage.res]*
storepage_maps.res | **Store maps** *[part of storepage.res]*
storepanel.res | **Store pages header and footer**
storepreviewitempanel.res | **Store item preview**
storepreviewitempanel_fullscreen.res | **Store item fullscreen preview**
storepreviewitempanel_maps.res | **Store map preview**
storeviewcartpanel.res | **Store cart**

## resource/ui/notifications/

File | Description
---- | -----------
base_notification.res | **Main notification file**  *[also in HudLayout.res > NotificationPanel]*
notification_manifest.txt |
notify_competitive_gc_down.res | **Competitive game coordinatior down notification**
notify_enemy_flag_captured_blue.res | **Enemy blue flag captured notification**
notify_enemy_flag_captured_red.res | **Enemy red flag captured notification**
notify_enemy_flag_dropped_blue.res | **Enemy blue flag dropped notification**
notify_enemy_flag_dropped_red.res | **Enemy red flag dropped notification**
notify_enemy_flag_returned_blue.res | **Enemy blue flag returned notification**
notify_enemy_flag_returned_red.res | **Enemy red flag returned notification**
notify_enemy_flag_taken_blue.res | **Enemy blue flag taken notification**
notify_enemy_flag_taken_red.res | **Enemy red flag taken notification**
notify_golden_wrench.res |
notify_how_to_control_ghost.res | **Ghost controls explanation**
notify_how_to_control_ghost_no_respawn.res | **Ghost controls explanation**
notify_how_to_control_kart.res | **Kart controls explanation**
notify_no_invuln_with_flag_blue.res | **Can't take the blue flag while ubered notification**
notify_no_invuln_with_flag_red.res | **Can't take the red flag while ubered notification**
notify_no_tele_with_flag_blue.res | **Can't teleport with blue flag notification**
notify_no_tele_with_flag_red.res |**Can't teleport with red flag notification**
notify_passtime_howto.res | **Passtime controls explanation**
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
notify_your_flag_captured_blue.res | **Own blue flag captured notification**
notify_your_flag_captured_red.res | **Own red flag captured notification**
notify_your_flag_dropped_blue.res | **Own blue flag dropped notification**
notify_your_flag_dropped_red.res | **Own red flag dropped notification**
notify_your_flag_returned_blue.res | **Own blue flag returned notification**
notify_your_flag_returned_red.res | **Own red flag returned notification**
notify_your_flag_taken_blue.res | **Own blue flag taken notification**
notify_your_flag_taken_red.res | **Own red flag taken notification**

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
main.res | **Main training window file**

## resource/ui/training/basictraining/

File | Description
---- | -----------
classdetails.res | **Training selected class details**
classpanel.res | **Training class image and progress label**
classselection.res | **Training class selection panel**

## resource/ui/training/modeselection/

File | Description
---- | -----------
modepanel.res | **Contains the parents for Basic Training and Offline Practice**
modeselection.res | **Training style selection**

## resource/ui/training/offlinepractice/

File | Description
---- | -----------
mapselection.res | **Offline practice map selection**
practicemodeselection.res | **Offline practice gamemode selection**

## resource/ui/replaybrowser/

File | Description
---- | -----------
basepage.res | **Main replays panel**
confirmquitdlg.res | **Quit confirmation message**
cutspanel.res | **Replay cuts/takes list**
detailspanel.res | **Replay details page, when a replay is selected**
listthumbnail.res | **Replay thumbnail**
mainpanel.res | **Header and footer, similiar to charinfopanel.res**
playbackpanel.res | **Video playback panel**
playbackpanelslideshow.res | 
previewpanel.res | **Replay preview panel, when hovering a replay**
recordspanel.res | **Replay's class played, score etc...**
renderdialog.res | **Replay render dialogs**
replaylistpanel.res | **Replays and movies list panel**
thumbnailcollection.res | **Unrendered replays panel**
thumbnailrow.res | **Parent of listthumbnail.res**
titleeditpanel.res | **Title edit panel, inside the details page**
