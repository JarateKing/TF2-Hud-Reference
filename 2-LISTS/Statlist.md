# Stats List

This contains a list of all files and the count of different 'gotchas' like how much a file uses things like minmode, #base, or if_mvm. Generally things that a hud developer may want to know about the default files, depending on the features they want to support.

## Metrics

* `linecount` refers to the size of the file, in lines.
* `minmode` refers to the number of things that are affected by your hud minmode setting.
* `#base` refers to the number of files loaded by #base.
* `if_mvm` refers to the number of things that have different values when in mvm.
* `if_readymode` refers to the number of things that have different values when in readymode.
* `if_competitive` refers to the number of things that have different values when playing competitive.

## scripts/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>chapterbackgrounds.txt</sub> | 14 | | | | |
<sub>hudanimations.txt</sub> | 850 | | | | |
<sub>hudanimations_manifest.txt</sub> | 6 | | | | |
<sub>hudanimations_tf.txt</sub> | 2322 | | | | |
<sub>hudlayout.res</sub> | 1524 | 28 | | | |
<sub>mod_textures.txt</sub> | 3497 | | | | |
## resource/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>chatscheme.res</sub> | 816 | | | | |
<sub>chat_english.txt</sub> | 33 | | | | |
<sub>clientscheme.res</sub> | 5843 | | | | |
<sub>closecaption_english.dat</sub> | | | | | |
<sub>closecaption_english.txt</sub> | 122 | | | | |
<sub>gamemenu.res</sub> | 45 | | | | |
<sub>sourcescheme.res</sub> | 331 | | 1 | | |
## resource/ui/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>abusereportsubmitdialog.res</sub> | 377 | | | | |
<sub>achievementsdialog.res</sub> | 218 | | | | |
<sub>annotationspanelcallout.res</sub> | 88 | | | | |
<sub>badgepanel.res</sub> | 50 | | | | |
<sub>basechat.res</sub> | 72 | | | | |
<sub>casualrankpanel.res</sub> | 1 | | 1 | | |
<sub>casualwelcomedialog.res</sub> | 227 | | | | |
<sub>charinfoarmorysubpanel.res</sub> | 447 | | | | |
<sub>charinfoloadoutsubpanel.res</sub> | 2141 | | | | |
<sub>charinfopanel.res</sub> | 153 | | | | |
<sub>chatpopup.res</sub> | 67 | | | | |
<sub>cheatdetectiondialog.res</sub> | 77 | | | | |
<sub>classloadoutpanel.res</sub> | 623 | | | | |
<sub>classmenu.res</sub> | 17 | | | | |
<sub>classselection.res</sub> | 1773 | | | | |
<sub>classselection_sc.res</sub> | 2044 | | | | |
<sub>classtipsitem.res</sub> | 48 | | | | |
<sub>classtipslist.res</sub> | 18 | | | | |
<sub>coachedbypanel.res</sub> | 138 | 1 | | | |
<sub>competitiveaccessinfo.res</sub> | 442 | | | | |
<sub>competitivewelcomedialog.res</sub> | 350 | | | | |
<sub>comprankpanel.res</sub> | 1 | | 1 | | |
<sub>comprankstooltip.res</sub> | 284 | | | | |
<sub>compstats.res</sub> | 383 | | | | |
<sub>confirmabandondialog.res</sub> | 159 | | | | |
<sub>controlpointcountdown.res</sub> | 24 | 1 | | | |
<sub>controlpointicon.res</sub> | 133 | 21 | | | |
<sub>controlpointprogressbar.res</sub> | 123 | 23 | | | |
<sub>craftingpanel.res</sub> | 481 | | | | |
<sub>craftingstatusdialog.res</sub> | 120 | | | | |
<sub>dashboardpartymember.res</sub> | 170 | | | | |
<sub>disguisestatuspanel.res</sub> | 128 | 12 | | | |
<sub>dynamicrecipepanel.res</sub> | 506 | | | | |
<sub>enemycountpanel.res</sub> | 82 | | | | |
<sub>explanationpopup.res</sub> | 208 | | | | |
<sub>flagcalloutpanel.res</sub> | 49 | | | | |
<sub>flagstatus.res</sub> | 57 | | | 2 | |
<sub>freezepanelcallout.res</sub> | 58 | | | | |
<sub>freezepanelkillerhealth.res</sub> | 74 | | | | |
<sub>freezepanel_basic.res</sub> | 468 | | | | |
<sub>giveawayitempanel.res</sub> | 169 | | | | |
<sub>globalchat.res</sub> | 125 | | | | |
<sub>globalexplanations.res</sub> | 1134 | | | | |
<sub>healthiconpanel.res</sub> | 35 | 4 | | | |
<sub>hudaccountpanel.res</sub> | 75 | | | | |
<sub>hudachievementfloatingnumber.res</sub> | 31 | | | | |
<sub>hudachievementtrackeritem.res</sub> | 92 | | | | |
<sub>hudalert.res</sub> | 58 | | | | |
<sub>hudammoweapons.res</sub> | 174 | 16 | | | |
<sub>hudarenacappointcountdown.res</sub> | 23 | | | | |
<sub>hudarenaclasslayout.res</sub> | 295 | | | | |
<sub>hudarenanotification.res</sub> | 102 | | | | |
<sub>hudarenaplayercount.res</sub> | 174 | | | | |
<sub>hudarenateammenu.res</sub> | 393 | | | | |
<sub>hudarenateammenu_sc.res</sub> | 433 | | | | |
<sub>hudarenavspanel.res</sub> | 160 | | | | |
<sub>hudarenawinpanel.res</sub> | 1187 | | | | |
<sub>hudbosshealth.res</sub> | 72 | | | | |
<sub>hudbowcharge.res</sub> | 22 | 1 | | | |
<sub>hudcurrencyaccount.res</sub> | 66 | | | | |
<sub>huddamageaccount.res</sub> | 15 | | | | |
<sub>huddemomancharge.res</sub> | 22 | 1 | | | |
<sub>huddemomanpipes.res</sub> | 233 | 24 | | | |
<sub>hudhealthaccount.res</sub> | 14 | | | | |
<sub>hudinspectpanel.res</sub> | 58 | | | | |
<sub>huditemattributetracker.res</sub> | 82 | | | | |
<sub>huditemeffectmeter.res</sub> | 86 | 10 | | | |
<sub>huditemeffectmeter_cleaver.res</sub> | 86 | 11 | | | |
<sub>huditemeffectmeter_demoman.res</sub> | 102 | 6 | | | |
<sub>huditemeffectmeter_engineer.res</sub> | 102 | 6 | | | |
<sub>huditemeffectmeter_halloweensouls.res</sub> | 106 | 6 | | | |
<sub>huditemeffectmeter_heavy.res</sub> | 151 | 16 | | | |
<sub>huditemeffectmeter_kartcharge.res</sub> | 114 | 19 | | | |
<sub>huditemeffectmeter_killstreak.res</sub> | 102 | 8 | | | |
<sub>huditemeffectmeter_organs.res</sub> | 108 | 12 | | | |
<sub>huditemeffectmeter_particlecannon.res</sub> | 86 | 10 | | | |
<sub>huditemeffectmeter_pomson.res</sub> | 86 | 10 | | | |
<sub>huditemeffectmeter_powerupbottle.res</sub> | 120 | 10 | | | |
<sub>huditemeffectmeter_pyro.res</sub> | 11 | 1 | 1 | | |
<sub>huditemeffectmeter_raygun.res</sub> | 86 | 10 | | | |
<sub>huditemeffectmeter_sapper.res</sub> | 87 | 10 | | | |
<sub>huditemeffectmeter_scout.res</sub> | 88 | 11 | | | |
<sub>huditemeffectmeter_sniper.res</sub> | 103 | 6 | | | |
<sub>huditemeffectmeter_sniperfocus.res</sub> | 86 | 10 | | | |
<sub>huditemeffectmeter_sodapopper.res</sub> | 87 | 10 | | | |
<sub>huditemeffectmeter_spy.res</sub> | 102 | 6 | | | |
<sub>huditemeffectmeter_spyknife.res</sub> | 88 | 11 | | | |
<sub>hudkillstreaknotice.res</sub> | 34 | | | | |
<sub>hudmannvsmachinestatus.res</sub> | 250 | 3 | | | |
<sub>hudmatchstatus.res</sub> | 895 | 8 | | | 2 |
<sub>hudmatchsummary.res</sub> | 999 | | | | |
<sub>hudmediccharge.res</sub> | 203 | 18 | | | |
<sub>hudmenutauntselection.res</sub> | 703 | | | | |
<sub>hudmenutauntselection_sc.res</sub> | 513 | | | | |
<sub>hudminigame_base.res</sub> | 164 | | | | |
<sub>hudminigame_collection.res</sub> | 9 | | 1 | | |
<sub>hudminigame_platform.res</sub> | 14 | | 1 | | |
<sub>hudminigame_soccer.res</sub> | 9 | | 1 | | |
<sub>hudminigame_soccersuddendeath.res</sub> | 61 | | 1 | | |
<sub>hudobjectiveflagpanel.res</sub> | 531 | | | 9 | |
<sub>hudobjectivekothtimepanel.res</sub> | 192 | 27 | | | |
<sub>hudobjectiveplayerdestruction.res</sub> | 1072 | | | 2 | |
<sub>hudobjectiverobotdestruction.res</sub> | 857 | | | 2 | |
<sub>hudobjectivestatus.res</sub> | 2 | | | | |
<sub>hudobjectivetimepanel.res</sub> | 381 | 21 | | | |
<sub>hudpasstime.res</sub> | 29 | | | | |
<sub>hudpasstimeballstatus.res</sub> | 673 | | | | |
<sub>hudpasstimeoffscreenarrow.res</sub> | 16 | | | | |
<sub>hudpasstimepassnotify.res</sub> | 151 | | | | |
<sub>hudpasstimeteamscore.res</sub> | 176 | | | | |
<sub>hudplayerclass.res</sub> | 417 | 67 | | | |
<sub>hudplayerhealth.res</sub> | 613 | 42 | | | |
<sub>hudpowerupeffectmeter.res</sub> | 84 | 10 | | | |
<sub>hudpvewinpanel.res</sub> | 182 | | | | |
<sub>hudrocketpack.res</sub> | 124 | 14 | 1 | | |
<sub>hudroundcounter.res</sub> | 67 | | | | |
<sub>hudspellselection.res</sub> | 129 | 10 | | | |
<sub>hudstalemate.res</sub> | 55 | | | | |
<sub>hudstopwatch.res</sub> | 217 | 4 | | | |
<sub>hudteamgoal.res</sub> | 77 | | | | |
<sub>hudteamgoaltournament.res</sub> | 159 | | | | |
<sub>hudteamswitch.res</sub> | 78 | | | | |
<sub>hudtournament.res</sub> | 1059 | | | 21 | 23 | 28
<sub>hudtournamentsetup.res</sub> | 151 | | | | |
<sub>hudtraining.res</sub> | 119 | | | | |
<sub>hudtrainingmsg.res</sub> | 55 | | | | |
<sub>hudupgradepanel.res</sub> | 749 | | | | |
<sub>hudwarcount.res</sub> | 115 | | | | |
<sub>hudweaponselection.res</sub> | 105 | | | | |
<sub>hud_obj_dispenser.res</sub> | 327 | | | | |
<sub>hud_obj_sapper.res</sub> | 199 | | | | |
<sub>hud_obj_sentrygun.res</sub> | 429 | | | | |
<sub>hud_obj_sentrygun_disp.res</sub> | 298 | | | | |
<sub>hud_obj_tele.res</sub> | 375 | | | | |
<sub>hud_obj_tele_entrance.res</sub> | 369 | | | | |
<sub>hud_obj_tele_exit.res</sub> | 293 | | | | |
<sub>importfiledialog.res</sub> | 2316 | | | | |
<sub>importfiletexteditdialog.res</sub> | 91 | | | | |
<sub>importmaterialeditdialog.res</sub> | 1360 | | | | |
<sub>importpreviewitempanel.res</sub> | 1760 | | | | |
<sub>ingamequeuestatus.res</sub> | 55 | | | | |
<sub>intromenu.res</sub> | 280 | | | | |
<sub>intromenu_sc.res</sub> | 320 | | | | |
<sub>invitenotification.res</sub> | 176 | | | | |
<sub>itemoptionspanel.res</sub> | 90 | | | | |
<sub>itemquickswitch.res</sub> | 196 | | | | |
<sub>itemrenameconfirmationdialog.res</sub> | 309 | | | | |
<sub>itemrenamedialog.res</sub> | 397 | | | | |
<sub>itemrenameinvaliddialog.res</sub> | 244 | | | | |
<sub>itemselectionpanel.res</sub> | 436 | | | | |
<sub>itemslotpanel.res</sub> | 154 | | | | |
<sub>layeredmappanel.res</sub> | 179 | | | | |
<sub>layeredmappanelitem.res</sub> | 54 | | | | |
<sub>layeredmappaneltooltip.res</sub> | 4 | | | | |
<sub>leaderboardentry.res</sub> | 61 | | | | |
<sub>leaderboardentryrank.res</sub> | 131 | | | | |
<sub>leaderboardentryscore.res</sub> | 79 | | | | |
<sub>leaderboardspreadentry.res</sub> | 148 | | | | |
<sub>loadoutpresetpanel.res</sub> | 29 | | | | |
<sub>lobbycontainerframe.res</sub> | 292 | | | | |
<sub>lobbycontainerframe_casual.res</sub> | 1062 | | 1 | | |
<sub>lobbycontainerframe_comp.res</sub> | 1027 | | 1 | | |
<sub>lobbycontainerframe_mvm.res</sub> | 177 | | 1 | | |
<sub>lobbypanel.res</sub> | 741 | | | | |
<sub>lobbypanel_casual.res</sub> | 281 | | 1 | | |
<sub>lobbypanel_comp.res</sub> | 606 | | 1 | | |
<sub>lobbypanel_mvm.res</sub> | 37 | | 1 | | |
<sub>mainmenueventplaylistentry.res</sub> | 161 | | 1 | | |
<sub>mainmenuoverride.res</sub> | 2894 | | | | |
<sub>mainmenuplaylistentry.res</sub> | 247 | | | | |
<sub>mainmenu_saxxyawards.res</sub> | 335 | | | | |
<sub>mapinfomenu.res</sub> | 272 | | | | |
<sub>mapinfomenu_sc.res</sub> | 333 | | | | |
<sub>matchhistoryentrypanel.res</sub> | 510 | | | | |
<sub>matchmakingcasualcriteria.res</sub> | 286 | | | | |
<sub>matchmakingcategorymappanel.res</sub> | 67 | | | | |
<sub>matchmakingcategorypanel.res</sub> | 281 | | | | |
<sub>matchmakingdashboard.res</sub> | 818 | | | | |
<sub>matchmakingdashboardcasualcriteria.res</sub> | 96 | | 1 | | |
<sub>matchmakingdashboardcomp.res</sub> | 139 | | 1 | | |
<sub>matchmakingdashboardcompaccess.res</sub> | 29 | | 1 | | |
<sub>matchmakingdashboardeventmatch.res</sub> | 246 | | 1 | | |
<sub>matchmakingdashboardleftsidepanel.res</sub> | 136 | | | | |
<sub>matchmakingdashboardmvmcriteria.res</sub> | 215 | | 1 | | |
<sub>matchmakingdashboardmvmmodeselect.res</sub> | 273 | | 1 | | |
<sub>matchmakingdashboardplaylist.res</sub> | 63 | | 1 | | |
<sub>matchmakingdashboardpopup.res</sub> | 712 | | | | |
<sub>matchmakingdashboardpopup_mapvotepanel.res</sub> | 98 | | | | |
<sub>matchmakingdashboardpopup_newmatch.res</sub> | 244 | | | | |
<sub>matchmakingdashboardpopup_nextmapvoting.res</sub> | 231 | | | | |
<sub>matchmakingdashboardpopup_nextmapwinner.res</sub> | 121 | | | | |
<sub>matchmakingdashboardsidepanel.res</sub> | 170 | | | | |
<sub>matchmakingdatacenterpopulationpanel.res</sub> | 47 | | | | |
<sub>matchmakinggrouppanel.res</sub> | 44 | | | | |
<sub>matchmakingpanel.res</sub> | 582 | | | | |
<sub>matchmakingpingpanel.res</sub> | 352 | | 1 | | |
<sub>matchmakingplaylist.res</sub> | 176 | | | | |
<sub>matchmakingtooltip.res</sub> | 55 | | | | |
<sub>mediccallerpanel.res</sub> | 115 | | | | |
<sub>mvmbombcarrierprogresspanel.res</sub> | 54 | | | | |
<sub>mvmcreditspendpanel.res</sub> | 113 | | | | |
<sub>mvmcreditsubpanel.res</sub> | 141 | | | | |
<sub>mvmcriteria.res</sub> | 666 | | | | |
<sub>mvmeconrequirementdialog.res</sub> | 100 | | | | |
<sub>mvminworldcurrency.res</sub> | 81 | | | | |
<sub>mvmscoreboard.res</sub> | 218 | | | | |
<sub>mvmscoreboardenemyinfo.res</sub> | 46 | | | | |
<sub>mvmstatentry.res</sub> | 28 | | | | |
<sub>mvmvictorycontainer.res</sub> | 101 | | | | |
<sub>mvmvictorymannupentry.res</sub> | 660 | | | | |
<sub>mvmvictorymannuploot.res</sub> | 46 | | | | |
<sub>mvmvictorymannuppanel.res</sub> | 317 | | | | |
<sub>mvmvictorymannuptab.res</sub> | 130 | | | | |
<sub>mvmvictorypanel.res</sub> | 199 | | | | |
<sub>mvmvictorysplash.res</sub> | 56 | | | | |
<sub>mvmwavelosspanel.res</sub> | 553 | | | | |
<sub>navigationpaneltest.res</sub> | 186 | | | | |
<sub>newrecipefounddialog.res</sub> | 103 | | | | |
<sub>objectivestatusescort.res</sub> | 648 | 56 | | | |
<sub>objectivestatusmultipleescort.res</sub> | 54 | | | | |
<sub>playerticketstatus.res</sub> | 81 | | | | |
<sub>publishedfilebrowserdialog.res</sub> | 270 | | | | |
<sub>publishfiledialog.res</sub> | 1252 | | | | |
<sub>pvpcasualrankpanel.res</sub> | 21 | | 1 | | |
<sub>pvpcomprankpanel.res</sub> | 95 | | 1 | | |
<sub>pvprankpanel.res</sub> | 579 | | | | |
<sub>quickplaybusydialog.res</sub> | 245 | | | | |
<sub>quickplaydialog.res</sub> | 1027 | | | | |
<sub>revivedialog.res</sub> | 109 | | | | |
<sub>robotdestructionstatus.res</sub> | 57 | | | 2 | |
<sub>roundinfo.res</sub> | 193 | | | | |
<sub>saxxyawards_submitform.res</sub> | 163 | | | | |
<sub>scoreboard.res</sub> | 1885 | | | 36 | |
<sub>selectmosthelpfulfrienddialog.res</sub> | 338 | | | | |
<sub>selectplayerdialog.res</sub> | 316 | | | | |
<sub>selectplayerdialog_coach.res</sub> | 264 | | | | |
<sub>selectplayerdialog_duel.res</sub> | 403 | | | | |
<sub>servernotconnectedtosteam.res</sub> | 78 | | | | |
<sub>spectator.res</sub> | 392 | 22 | | | |
<sub>spectatorcoach.res</sub> | 408 | 12 | | | |
<sub>spectatorguihealth.res</sub> | 110 | 21 | | | |
<sub>spectatortournament.res</sub> | 459 | | | 10 | |
<sub>spectatortournamentguihealth.res</sub> | 76 | 2 | | | |
<sub>spectator_sc.res</sub> | 328 | 17 | | | |
<sub>stampdonationadd.res</sub> | 178 | | | | |
<sub>staticbadgepanel.res</sub> | 113 | | | | |
<sub>statpanel_base.res</sub> | 151 | | | | |
<sub>statsummary.res</sub> | 2748 | | | | |
<sub>statsummary_embedded.res</sub> | 2589 | | | | |
<sub>steamfriendpanel.res</sub> | 77 | | | | |
<sub>steamworkshopdialog.res</sub> | 728 | | | | |
<sub>steamworkshopitem.res</sub> | 67 | | | | |
<sub>streamlistpanel.res</sub> | 212 | | | | |
<sub>streampanel.res</sub> | 166 | | | | |
<sub>supportnotificationdialog.res</sub> | 126 | | | | |
<sub>surveypanel_base.res</sub> | 174 | | | | |
<sub>surveypanel_casualinquiry.res</sub> | 302 | | 1 | | |
<sub>surveypanel_compinquiry.res</sub> | 302 | | 1 | | |
<sub>surveypanel_mapquality.res</sub> | 285 | | 1 | | |
<sub>surveypanel_matchquality.res</sub> | 264 | | 1 | | |
<sub>surveypanel_randomcrit.res</sub> | 264 | | 1 | | |
<sub>tankprogressbar.res</sub> | 70 | | | | |
<sub>tankstatuspanel.res</sub> | 24 | | | | |
<sub>targetid.res</sub> | 271 | 14 | | | |
<sub>tauntcallerpanel.res</sub> | 17 | | | | |
<sub>teammenu.res</sub> | 772 | | | | |
<sub>teammenu_sc.res</sub> | 846 | | | | |
<sub>testitembotcontrols.res</sub> | 250 | | | | |
<sub>testitemdialog.res</sub> | 625 | | | | |
<sub>testitemroot.res</sub> | 1007 | | | | |
<sub>textwindow.res</sub> | 162 | | | | |
<sub>textwindowcustomserver.res</sub> | 162 | | | | |
<sub>textwindowcustomserver_sc.res</sub> | 182 | | | | |
<sub>textwindow_sc.res</sub> | 182 | | | | |
<sub>tfadvancedoptionsdialog.res</sub> | 145 | | | | |
<sub>tfhudrobotdestruction_activestate.res</sub> | 62 | | | | |
<sub>tfhudrobotdestruction_deadstate.res</sub> | 69 | 1 | | | |
<sub>tfhudrobotdestruction_robotindicator.res</sub> | 56 | | | | |
<sub>tfhudrobotdestruction_shieldedstate.res</sub> | 46 | | | | |
<sub>trainingcomplete.res</sub> | 223 | | | | |
<sub>trainingdialog.res</sub> | 49 | | | | |
<sub>trainingdialog_old.res</sub> | 49 | | | | |
<sub>trainingitempanel.res</sub> | 127 | | | | |
<sub>upgradeboxdialog.res</sub> | 111 | | | | |
<sub>upgradebuypanel.res</sub> | 223 | | | | |
<sub>videopanel.res</sub> | 8 | | | | |
<sub>viewrecipespanel.res</sub> | 233 | | | | |
<sub>votehud.res</sub> | 702 | | | | |
<sub>vrcalibration.res</sub> | 436 | | | | |
<sub>waitingforplayerspanel.res</sub> | 59 | | | | |
<sub>wavecompletesummarypanel.res</sub> | 283 | | | | |
<sub>wavestatuspanel.res</sub> | 133 | 9 | | | |
<sub>winpanel.res</sub> | 812 | | | | |
<sub>xboxdialogs.res</sub> | 4223 | | | | |
<sub>xpsourcepanel.res</sub> | 52 | | | | |
## resource/ui/build_menu/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>base_active.res</sub> | 146 | | | | |
<sub>base_active_teleport_target.res</sub> | 111 | | | | |
<sub>base_already_built.res</sub> | 150 | | | | |
<sub>base_cant_afford.res</sub> | 149 | | | | |
<sub>base_selectable.res</sub> | 107 | | | | |
<sub>base_unavailable.res</sub> | 150 | | | | |
<sub>base_unavailable_teleport_target.res</sub> | 115 | | | | |
<sub>dispenser_active.res</sub> | 19 | | 1 | | |
<sub>dispenser_already_built.res</sub> | 14 | | 1 | | |
<sub>dispenser_cant_afford.res</sub> | 14 | | 1 | | |
<sub>dispenser_selectable.res</sub> | 14 | | 1 | | |
<sub>dispenser_unavailable.res</sub> | 14 | | 1 | | |
<sub>eureka_target_home_avail.res</sub> | 19 | | 1 | | |
<sub>eureka_target_home_unavail.res</sub> | 14 | | 1 | | |
<sub>eureka_target_tele_exit_avail.res</sub> | 19 | | 1 | | |
<sub>eureka_target_tele_exit_unavail.res</sub> | 14 | | 1 | | |
<sub>hudmenuengybuild.res</sub> | 315 | | | | |
<sub>hudmenueurekaeffect.res</sub> | 159 | | | | |
<sub>sentry_active.res</sub> | 20 | | 1 | | |
<sub>sentry_already_built.res</sub> | 15 | | 1 | | |
<sub>sentry_cant_afford.res</sub> | 15 | | 1 | | |
<sub>sentry_selectable.res</sub> | 15 | | 1 | | |
<sub>sentry_unavailable.res</sub> | 15 | | 1 | | |
<sub>tele_entrance_active.res</sub> | 19 | | 1 | | |
<sub>tele_entrance_already_built.res</sub> | 14 | | 1 | | |
<sub>tele_entrance_cant_afford.res</sub> | 14 | | 1 | | |
<sub>tele_entrance_unavailable.res</sub> | 14 | | 1 | | |
<sub>tele_exit_active.res</sub> | 19 | | 1 | | |
<sub>tele_exit_already_built.res</sub> | 14 | | 1 | | |
<sub>tele_exit_cant_afford.res</sub> | 14 | | 1 | | |
<sub>tele_exit_unavailable.res</sub> | 14 | | 1 | | |
<sub>tele_selectable.res</sub> | 14 | | 1 | | |
## resource/ui/build_menu/pipboy/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>base_active.res</sub> | 148 | | | | |
<sub>base_active_teleport_target.res</sub> | 112 | | | | |
<sub>base_already_built.res</sub> | 154 | | | | |
<sub>base_cant_afford.res</sub> | 150 | | | | |
<sub>base_selectable.res</sub> | 107 | | | | |
<sub>base_unavailable.res</sub> | 152 | | | | |
<sub>base_unavailable_teleport_target.res</sub> | 117 | | | | |
<sub>dispenser_active.res</sub> | 19 | | 1 | | |
<sub>dispenser_already_built.res</sub> | 14 | | 1 | | |
<sub>dispenser_cant_afford.res</sub> | 14 | | 1 | | |
<sub>dispenser_selectable.res</sub> | 14 | | 1 | | |
<sub>dispenser_unavailable.res</sub> | 14 | | 1 | | |
<sub>eureka_target_home_avail.res</sub> | 19 | | 1 | | |
<sub>eureka_target_home_unavail.res</sub> | 14 | | 1 | | |
<sub>eureka_target_tele_exit_avail.res</sub> | 19 | | 1 | | |
<sub>eureka_target_tele_exit_unavail.res</sub> | 14 | | 1 | | |
<sub>hudmenuengybuild.res</sub> | 299 | | | | |
<sub>hudmenueurekaeffect.res</sub> | 156 | | | | |
<sub>sentry_active.res</sub> | 20 | | 1 | | |
<sub>sentry_already_built.res</sub> | 15 | | 1 | | |
<sub>sentry_cant_afford.res</sub> | 15 | | 1 | | |
<sub>sentry_selectable.res</sub> | 15 | | 1 | | |
<sub>sentry_unavailable.res</sub> | 15 | | 1 | | |
<sub>tele_entrance_active.res</sub> | 19 | | 1 | | |
<sub>tele_entrance_already_built.res</sub> | 14 | | 1 | | |
<sub>tele_entrance_cant_afford.res</sub> | 14 | | 1 | | |
<sub>tele_entrance_unavailable.res</sub> | 14 | | 1 | | |
<sub>tele_exit_active.res</sub> | 19 | | 1 | | |
<sub>tele_exit_already_built.res</sub> | 14 | | 1 | | |
<sub>tele_exit_cant_afford.res</sub> | 14 | | 1 | | |
<sub>tele_exit_unavailable.res</sub> | 14 | | 1 | | |
<sub>tele_selectable.res</sub> | 14 | | 1 | | |
## resource/ui/build_menu_360/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>base_active.res</sub> | 89 | | | | |
<sub>base_already_built.res</sub> | 105 | | | | |
<sub>base_cant_afford.res</sub> | 92 | | | | |
<sub>dispenser_active.res</sub> | 14 | | 1 | | |
<sub>dispenser_already_built.res</sub> | 19 | | 1 | | |
<sub>dispenser_cant_afford.res</sub> | 9 | | 1 | | |
<sub>hudmenuengybuild.res</sub> | 430 | | | | |
<sub>sentry_active.res</sub> | 15 | | 1 | | |
<sub>sentry_already_built.res</sub> | 18 | | 1 | | |
<sub>sentry_cant_afford.res</sub> | 9 | | 1 | | |
<sub>tele_entrance_active.res</sub> | 14 | | 1 | | |
<sub>tele_entrance_already_built.res</sub> | 14 | | 1 | | |
<sub>tele_entrance_cant_afford.res</sub> | 9 | | 1 | | |
<sub>tele_exit_active.res</sub> | 14 | | 1 | | |
<sub>tele_exit_already_built.res</sub> | 14 | | 1 | | |
<sub>tele_exit_cant_afford.res</sub> | 9 | | 1 | | |
## resource/ui/build_menu_sc/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>base_active.res</sub> | 109 | | | | |
<sub>base_active_teleport_target.res</sub> | 90 | | | | |
<sub>base_already_built.res</sub> | 105 | | | | |
<sub>base_cant_afford.res</sub> | 92 | | | | |
<sub>base_unavailable_teleport_target.res</sub> | 94 | | | | |
<sub>dispenser_active.res</sub> | 14 | | 1 | | |
<sub>dispenser_already_built.res</sub> | 19 | | 1 | | |
<sub>dispenser_cant_afford.res</sub> | 9 | | 1 | | |
<sub>eureka_target_home_avail.res</sub> | 19 | | 1 | | |
<sub>eureka_target_home_unavail.res</sub> | 14 | | 1 | | |
<sub>eureka_target_tele_exit_avail.res</sub> | 19 | | 1 | | |
<sub>eureka_target_tele_exit_unavail.res</sub> | 14 | | 1 | | |
<sub>hudmenuengybuild.res</sub> | 468 | | | | |
<sub>hudmenueurekaeffect.res</sub> | 139 | | | | |
<sub>sentry_active.res</sub> | 15 | | 1 | | |
<sub>sentry_already_built.res</sub> | 18 | | 1 | | |
<sub>sentry_cant_afford.res</sub> | 9 | | 1 | | |
<sub>tele_entrance_active.res</sub> | 14 | | 1 | | |
<sub>tele_entrance_already_built.res</sub> | 14 | | 1 | | |
<sub>tele_entrance_cant_afford.res</sub> | 9 | | 1 | | |
<sub>tele_exit_active.res</sub> | 14 | | 1 | | |
<sub>tele_exit_already_built.res</sub> | 14 | | 1 | | |
<sub>tele_exit_cant_afford.res</sub> | 9 | | 1 | | |
## resource/ui/destroy_menu/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>base_active.res</sub> | 107 | | | | |
<sub>base_inactive.res</sub> | 95 | | | | |
<sub>dispenser_active.res</sub> | 107 | | | | |
<sub>dispenser_inactive.res</sub> | 115 | | | | |
<sub>hudmenuengydestroy.res</sub> | 251 | | | | |
<sub>sentry_active.res</sub> | 108 | | | | |
<sub>sentry_inactive.res</sub> | 116 | | | | |
<sub>tele_entrance_active.res</sub> | 107 | | | | |
<sub>tele_entrance_inactive.res</sub> | 115 | | | | |
<sub>tele_exit_active.res</sub> | 107 | | | | |
<sub>tele_exit_inactive.res</sub> | 115 | | | | |
## resource/ui/destroy_menu/pipboy/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>base_active.res</sub> | 107 | | | | |
<sub>base_inactive.res</sub> | 95 | | | | |
<sub>dispenser_active.res</sub> | 109 | | | | |
<sub>dispenser_inactive.res</sub> | 118 | | | | |
<sub>hudmenuengydestroy.res</sub> | 251 | | | | |
<sub>sentry_active.res</sub> | 110 | | | | |
<sub>sentry_inactive.res</sub> | 119 | | | | |
<sub>tele_entrance_active.res</sub> | 109 | | | | |
<sub>tele_entrance_inactive.res</sub> | 118 | | | | |
<sub>tele_exit_active.res</sub> | 109 | | | | |
<sub>tele_exit_inactive.res</sub> | 119 | | | | |
## resource/ui/disguise_menu/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>demoman_blue.res</sub> | 95 | | | | |
<sub>demoman_red.res</sub> | 95 | | | | |
<sub>engineer_blue.res</sub> | 95 | | | | |
<sub>engineer_red.res</sub> | 95 | | | | |
<sub>heavy_blue.res</sub> | 95 | | | | |
<sub>heavy_red.res</sub> | 95 | | | | |
<sub>hudmenuspydisguise.res</sub> | 454 | | | | |
<sub>medic_blue.res</sub> | 95 | | | | |
<sub>medic_red.res</sub> | 95 | | | | |
<sub>pyro_blue.res</sub> | 95 | | | | |
<sub>pyro_red.res</sub> | 95 | | | | |
<sub>scout_blue.res</sub> | 95 | | | | |
<sub>scout_red.res</sub> | 95 | | | | |
<sub>sniper_blue.res</sub> | 95 | | | | |
<sub>sniper_red.res</sub> | 95 | | | | |
<sub>soldier_blue.res</sub> | 95 | | | | |
<sub>soldier_red.res</sub> | 95 | | | | |
<sub>spy_blue.res</sub> | 95 | | | | |
<sub>spy_red.res</sub> | 95 | | | | |
## resource/ui/disguise_menu_360/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>base.res</sub> | 17 | | | | |
<sub>demoman_blue.res</sub> | 14 | | 1 | | |
<sub>demoman_red.res</sub> | 14 | | 1 | | |
<sub>engineer_blue.res</sub> | 14 | | 1 | | |
<sub>engineer_red.res</sub> | 14 | | 1 | | |
<sub>heavy_blue.res</sub> | 14 | | 1 | | |
<sub>heavy_red.res</sub> | 14 | | 1 | | |
<sub>hudmenuspydisguise.res</sub> | 459 | | | | |
<sub>medic_blue.res</sub> | 14 | | 1 | | |
<sub>medic_red.res</sub> | 14 | | 1 | | |
<sub>pyro_blue.res</sub> | 14 | | 1 | | |
<sub>pyro_red.res</sub> | 14 | | 1 | | |
<sub>scout_blue.res</sub> | 14 | | 1 | | |
<sub>scout_red.res</sub> | 14 | | 1 | | |
<sub>sniper_blue.res</sub> | 14 | | 1 | | |
<sub>sniper_red.res</sub> | 14 | | 1 | | |
<sub>soldier_blue.res</sub> | 14 | | 1 | | |
<sub>soldier_red.res</sub> | 14 | | 1 | | |
<sub>spy_blue.res</sub> | 14 | | 1 | | |
<sub>spy_red.res</sub> | 14 | | 1 | | |
## resource/ui/disguise_menu_sc/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>base.res</sub> | 17 | | | | |
<sub>demoman_blue.res</sub> | 14 | | 1 | | |
<sub>demoman_red.res</sub> | 14 | | 1 | | |
<sub>engineer_blue.res</sub> | 14 | | 1 | | |
<sub>engineer_red.res</sub> | 14 | | 1 | | |
<sub>heavy_blue.res</sub> | 14 | | 1 | | |
<sub>heavy_red.res</sub> | 14 | | 1 | | |
<sub>hudmenuspydisguise.res</sub> | 485 | | | | |
<sub>medic_blue.res</sub> | 14 | | 1 | | |
<sub>medic_red.res</sub> | 14 | | 1 | | |
<sub>pyro_blue.res</sub> | 14 | | 1 | | |
<sub>pyro_red.res</sub> | 14 | | 1 | | |
<sub>scout_blue.res</sub> | 14 | | 1 | | |
<sub>scout_red.res</sub> | 14 | | 1 | | |
<sub>sniper_blue.res</sub> | 14 | | 1 | | |
<sub>sniper_red.res</sub> | 14 | | 1 | | |
<sub>soldier_blue.res</sub> | 14 | | 1 | | |
<sub>soldier_red.res</sub> | 14 | | 1 | | |
<sub>spy_blue.res</sub> | 14 | | 1 | | |
<sub>spy_red.res</sub> | 14 | | 1 | | |
## resource/ui/econ/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>backpackpanel.res</sub> | 1580 | | | | |
<sub>collectioncraftingdialog.res</sub> | 239 | | 1 | | |
<sub>collectioncraftingdialog_base.res</sub> | 1821 | | | | |
<sub>comboboxbackpackoverlaydialog.res</sub> | 147 | | | | |
<sub>confirmapplycardupgradeapplicationdialog.res</sub> | 271 | | | | |
<sub>confirmapplydecodedialog.res</sub> | 290 | | | | |
<sub>confirmapplyducktokendialog.res</sub> | 271 | | | | |
<sub>confirmapplygiftwrapdialog.res</sub> | 290 | | | | |
<sub>confirmapplypaintcandialog.res</sub> | 320 | | | | |
<sub>confirmapplypaintkitdialog.res</sub> | 138 | | 1 | | |
<sub>confirmapplystrangepartapplicationdialog.res</sub> | 271 | | | | |
<sub>confirmapplystrangerestrictionapplicationdialog.res</sub> | 271 | | | | |
<sub>confirmapplystrangifierdialog.res</sub> | 272 | | | | |
<sub>confirmapplyteamcolorpaintcandialog.res</sub> | 350 | | | | |
<sub>confirmcustomizetexturedialog.res</sub> | 955 | | | | |
<sub>confirmdialogabandonnopenalty.res</sub> | 165 | | | | |
<sub>confirmdialogabandonpenalty.res</sub> | 165 | | | | |
<sub>confirmdialogabandonsafe.res</sub> | 151 | | | | |
<sub>confirmdialogoptout.res</sub> | 131 | | | | |
<sub>confirmitempreviewdialog.res</sub> | 209 | | | | |
<sub>confirmspellbookpageapplicationdialog.res</sub> | 271 | | | | |
<sub>confirmtransmogrifyapplicationdialog.res</sub> | 271 | | | | |
<sub>cyclingadcontainer.res</sub> | 121 | | | | |
<sub>ducksleaderboardpanel.res</sub> | 186 | | | | |
<sub>ducksleaderboards.res</sub> | 446 | | | | |
<sub>genericnotificationtoast.res</sub> | 84 | | | | |
<sub>genericnotificationtoastmainmenu.res</sub> | 94 | | | | |
<sub>genericwaitingdialog.res</sub> | 104 | | | | |
<sub>halloweenofferingdialog.res</sub> | 263 | | 1 | | |
<sub>inputstringforitembackpackoverlaydialog.res</sub> | 351 | | | | |
<sub>inspectionpanel.res</sub> | 618 | | | | |
<sub>inspectionpanel_cosmetic.res</sub> | 1109 | | | | |
<sub>itemaddefault.res</sub> | 216 | | | | |
<sub>itemdiscardpanel.res</sub> | 851 | | | | |
<sub>itemmodelpanel.res</sub> | 319 | | | | |
<sub>itemmodelpanelcollectioncosmeticitem.res</sub> | 357 | | | | |
<sub>itemmodelpanelcollectionitem.res</sub> | 386 | | | | |
<sub>itempickuppanel.res</sub> | 373 | | | | |
<sub>leaderboardpanel.res</sub> | 32 | | | | |
<sub>lobbyleaderboard.res</sub> | 48 | | | | |
<sub>manncotrade_commonstatclock.res</sub> | 272 | | 1 | | |
<sub>notificationqueuepanel.res</sub> | 19 | | | | |
<sub>notificationspresentpanel.res</sub> | 37 | | | | |
<sub>notificationtoastcontainer.res</sub> | 40 | | | | |
<sub>notificationtoastcontrol.res</sub> | 236 | | | | |
<sub>paintkitconsumedialog.res</sub> | 295 | | | | |
<sub>questdefinitionviewpanel.res</sub> | 433 | | | | |
<sub>questdetailspanel.res</sub> | 390 | | | | |
<sub>questeditor.res</sub> | 281 | | | | |
<sub>questlogpanel.res</sub> | 430 | | | | |
<sub>questlogpanel_halloween.res</sub> | 51 | | 1 | | |
<sub>questmapnodepanel.res</sub> | 186 | | | | |
<sub>questmapnodetooltippanel.res</sub> | 67 | | | | |
<sub>questmappanel.res</sub> | 1591 | | | | |
<sub>questmaprewarditempanel.res</sub> | 101 | | 1 | | |
<sub>questnotificationpanel_base.res</sub> | 66 | | | | |
<sub>questnotificationpanel_pauling_standard.res</sub> | 12 | | 1 | | |
<sub>questviewsubpanel.res</sub> | 376 | | | | |
<sub>scrollablequestdetails.res</sub> | 110 | | | | |
<sub>scrollablequestlist.res</sub> | 101 | | | | |
<sub>scrollablequestlist_halloween.res</sub> | 49 | | 1 | | |
<sub>scrollablequestlist_toughbreak.res</sub> | 9 | | 1 | | |
<sub>strangecounttransferdialog.res</sub> | 220 | | | | |
<sub>tradingpanel.res</sub> | 853 | | | | |
<sub>tradingstartdialog.res</sub> | 485 | | | | |
<sub>warjoinpanel.res</sub> | 1129 | | | | |
<sub>warstandingpanel.res</sub> | 175 | | | | |
## resource/ui/econ/store/v1/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>storehome.res</sub> | 565 | | | | |
<sub>storehome_freetrial.res</sub> | 577 | | | | |
<sub>storehome_winter1.res</sub> | 564 | | | | |
<sub>storehome_winter2.res</sub> | 564 | | | | |
<sub>storehome_winter3.res</sub> | 564 | | | | |
<sub>storeitemcontrols.res</sub> | 69 | | | | |
<sub>storepage.res</sub> | 2767 | | | | |
<sub>storepage_bundles.res</sub> | 2747 | | | | |
<sub>storepage_cgtrading.res</sub> | 2781 | | | | |
<sub>storepage_drgrordbort.res</sub> | 2781 | | | | |
<sub>storepage_halloween.res</sub> | 2777 | | | | |
<sub>storepage_maps.res</sub> | 2744 | | | | |
<sub>storepage_new.res</sub> | 2772 | | | | |
<sub>storepage_popular.res</sub> | 2790 | | | | |
<sub>storepage_previewable.res</sub> | 2786 | | | | |
<sub>storepage_summer.res</sub> | 2777 | | | | |
<sub>storepanel.res</sub> | 165 | | | | |
<sub>storepreviewitempanel.res</sub> | 752 | | | | |
<sub>storepreviewitempanel_maps.res</sub> | 667 | | | | |
<sub>storeprice.res</sub> | 169 | | | | |
<sub>storeprice_bundles.res</sub> | 35 | | 1 | | |
<sub>storeprice_jumbo.res</sub> | 105 | | | | |
<sub>storeprice_new.res</sub> | 127 | | | | |
<sub>storeprice_popular.res</sub> | 166 | | | | |
<sub>storestatusdialog.res</sub> | 65 | | | | |
<sub>storeviewcartpanel.res</sub> | 448 | | | | |
## resource/ui/econ/store/v2/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>storehome_base.res</sub> | 598 | | | | |
<sub>storehome_freetrial.res</sub> | 282 | | 1 | | |
<sub>storehome_premium.res</sub> | 43 | | 1 | | |
<sub>storeitemcontrols.res</sub> | 65 | | | | |
<sub>storemapstampsinfodialog.res</sub> | 209 | | | | |
<sub>storepage.res</sub> | 2716 | | | | |
<sub>storepage_bundles.res</sub> | 5 | | 1 | | |
<sub>storepage_items.res</sub> | 5 | | 1 | | |
<sub>storepage_maps.res</sub> | 116 | | 1 | | |
<sub>storepanel.res</sub> | 222 | | | | |
<sub>storepreviewitempanel.res</sub> | 1572 | | | | |
<sub>storepreviewitempanel_fullscreen.res</sub> | 360 | | | | |
<sub>storepreviewitempanel_maps.res</sub> | 620 | | | | |
<sub>storeviewcartpanel.res</sub> | 501 | | | | |
## resource/ui/notifications/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>base_notification.res</sub> | 52 | | | | |
<sub>notification_manifest.txt</sub> | 35 | | | | |
<sub>notify_competitive_gc_down.res</sub> | 19 | | 1 | | |
<sub>notify_enemy_flag_captured_blue.res</sub> | 19 | | 1 | | |
<sub>notify_enemy_flag_captured_red.res</sub> | 19 | | 1 | | |
<sub>notify_enemy_flag_dropped_blue.res</sub> | 19 | | 1 | | |
<sub>notify_enemy_flag_dropped_red.res</sub> | 19 | | 1 | | |
<sub>notify_enemy_flag_returned_blue.res</sub> | 19 | | 1 | | |
<sub>notify_enemy_flag_returned_red.res</sub> | 19 | | 1 | | |
<sub>notify_enemy_flag_taken_blue.res</sub> | 19 | | 1 | | |
<sub>notify_enemy_flag_taken_red.res</sub> | 19 | | 1 | | |
<sub>notify_golden_wrench.res</sub> | 52 | | | | |
<sub>notify_how_to_control_ghost.res</sub> | 52 | | | | |
<sub>notify_how_to_control_ghost_no_respawn.res</sub> | 9 | | 1 | | |
<sub>notify_how_to_control_kart.res</sub> | 52 | | | | |
<sub>notify_no_invuln_with_flag_blue.res</sub> | 19 | | 1 | | |
<sub>notify_no_invuln_with_flag_red.res</sub> | 19 | | 1 | | |
<sub>notify_no_tele_with_flag_blue.res</sub> | 19 | | 1 | | |
<sub>notify_no_tele_with_flag_red.res</sub> | 19 | | 1 | | |
<sub>notify_passtime_howto.res</sub> | 52 | | | | |
<sub>notify_passtime_no_carry.res</sub> | 19 | | 1 | | |
<sub>notify_passtime_no_cloak.res</sub> | 19 | | 1 | | |
<sub>notify_passtime_no_disguise.res</sub> | 19 | | 1 | | |
<sub>notify_passtime_no_holster.res</sub> | 19 | | 1 | | |
<sub>notify_passtime_no_invuln.res</sub> | 19 | | 1 | | |
<sub>notify_passtime_no_oob.res</sub> | 19 | | 1 | | |
<sub>notify_passtime_no_taunt.res</sub> | 19 | | 1 | | |
<sub>notify_passtime_no_tele.res</sub> | 19 | | 1 | | |
<sub>notify_rd_robot_attacked_blue.res</sub> | 19 | | 1 | | |
<sub>notify_rd_robot_attacked_red.res</sub> | 19 | | 1 | | |
<sub>notify_special.res</sub> | 14 | | 1 | | |
<sub>notify_touching_enemy_ctf_cap_blue.res</sub> | 19 | | 1 | | |
<sub>notify_touching_enemy_ctf_cap_red.res</sub> | 19 | | 1 | | |
<sub>notify_truce_end.res</sub> | 19 | | 1 | | |
<sub>notify_truce_start.res</sub> | 19 | | 1 | | |
<sub>notify_your_flag_captured_blue.res</sub> | 19 | | 1 | | |
<sub>notify_your_flag_captured_red.res</sub> | 19 | | 1 | | |
<sub>notify_your_flag_dropped_blue.res</sub> | 19 | | 1 | | |
<sub>notify_your_flag_dropped_red.res</sub> | 19 | | 1 | | |
<sub>notify_your_flag_returned_blue.res</sub> | 19 | | 1 | | |
<sub>notify_your_flag_returned_red.res</sub> | 19 | | 1 | | |
<sub>notify_your_flag_taken_blue.res</sub> | 19 | | 1 | | |
<sub>notify_your_flag_taken_red.res</sub> | 19 | | 1 | | |
## resource/ui/quests/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>lineitem_credits.res</sub> | 29 | | | | |
<sub>lineitem_item.res</sub> | 52 | | | | |
<sub>lineitem_objective.res</sub> | 29 | | | | |
<sub>lineitem_points.res</sub> | 29 | | | | |
<sub>questitempanel_base.res</sub> | 1188 | | | | |
<sub>questitemtrackerpanel_base.res</sub> | 54 | | | | |
<sub>questitemtrackerpanel_ingame_base.res</sub> | 411 | | 1 | | |
<sub>questitemtrackerpanel_questlog_base.res</sub> | 69 | | 1 | | |
<sub>questobjectivepanel_ingame_base.res</sub> | 76 | | | | |
<sub>questobjectivepanel_questlog_base.res</sub> | 61 | | | | |
<sub>questobjectivescorer.res</sub> | 44 | | | | |
## resource/ui/quests/cyoa/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>questitemtrackerpanel_cyoa.res</sub> | 339 | | 1 | | |
<sub>questmapregionlink.res</sub> | 117 | | | | |
<sub>questobjectivepanel_cyoa.res</sub> | 84 | | 1 | | |
## resource/ui/quests/cyoa/regions/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>region_base.res</sub> | 120 | | | | |
<sub>region_campaign_3_home.res</sub> | 38 | | 1 | | |
<sub>region_defense.res</sub> | 86 | | 1 | | |
<sub>region_halloween.res</sub> | 38 | | 1 | | |
<sub>region_halloween_bosses.res</sub> | 38 | | 1 | | |
<sub>region_halloween_community_maps.res</sub> | 38 | | 1 | | |
<sub>region_halloween_official_maps.res</sub> | 38 | | 1 | | |
<sub>region_maps.res</sub> | 38 | | 1 | | |
<sub>region_offense.res</sub> | 86 | | 1 | | |
<sub>region_overworld.res</sub> | 38 | | 1 | | |
<sub>region_pyroland.res</sub> | 38 | | 1 | | |
<sub>region_support.res</sub> | 86 | | 1 | | |
## resource/ui/quests/merasmus/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>questitempanel_merasmus_base.res</sub> | 533 | | 1 | | |
<sub>questitempanel_merasmus_general.res</sub> | 23 | | 1 | | |
<sub>questitempanel_merasmus_hhh.res</sub> | 23 | | 1 | | |
<sub>questitempanel_merasmus_merasmus.res</sub> | 23 | | 1 | | |
<sub>questitempanel_merasmus_monoculus.res</sub> | 23 | | 1 | | |
<sub>questitemtrackerpanel_ingame.res</sub> | 22 | | 1 | | |
<sub>questitemtrackerpanel_questlog.res</sub> | 45 | | 1 | | |
<sub>questobjectivepanel_ingame.res</sub> | 10 | | 1 | | |
<sub>questobjectivepanel_questlog.res</sub> | 23 | | 1 | | |
## resource/ui/quests/pauling/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>questitempanel_pauling_base.res</sub> | 34 | | 1 | | |
<sub>questitempanel_pauling_borneo.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_demo.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_engineer.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_headhunter.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_heavy.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_medic.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_playanyclass.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_powerhouse.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_pyro.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_scout.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_sniper.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_snowplow.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_soldier.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_spy.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_suijin.res</sub> | 18 | | 1 | | |
<sub>questitemtrackerpanel_ingame.res</sub> | 12 | | 1 | | |
<sub>questitemtrackerpanel_questlog.res</sub> | 43 | | 1 | | |
<sub>questobjectivepanel_ingame.res</sub> | 10 | | 1 | | |
<sub>questobjectivepanel_questlog.res</sub> | 5 | | 1 | | |
## resource/ui/quests/pauling/operation 2/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>questitempanel_pauling_base.res</sub> | 345 | | 1 | | |
<sub>questitempanel_pauling_community_map_1.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_community_map_2.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_community_map_3.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_community_map_4.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_cp.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_demo.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_engineer.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_headhunter.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_heavy.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_medic.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_payload.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_playanyclass.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_pyro.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_scout.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_sniper.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_soldier.res</sub> | 18 | | 1 | | |
<sub>questitempanel_pauling_spy.res</sub> | 18 | | 1 | | |
## resource/ui/training/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>main.res</sub> | 279 | | | | |
## resource/ui/training/basictraining/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>classdetails.res</sub> | 223 | | | | |
<sub>classpanel.res</sub> | 61 | | | | |
<sub>classselection.res</sub> | 20 | | | | |
## resource/ui/training/modeselection/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>modepanel.res</sub> | 118 | | | | |
<sub>modeselection.res</sub> | 44 | | | | |
## resource/ui/training/offlinepractice/
Filename | <sub>linecount</sub> | <sub>minmode</sub> | <sub>#base</sub> | <sub>if_mvm</sub> | <sub>if_readymode</sub> | <sub>if_competitive</sub>
-------- | --------- | ------- | ----- | ------ | ------------ | --------------
<sub>mapselection.res</sub> | 291 | | | | |
<sub>practicemodeselection.res</sub> | 174 | | | | |
