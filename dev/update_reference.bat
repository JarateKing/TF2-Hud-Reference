@echo off
setlocal ENABLEDELAYEDEXPANSION
TITLE Extracting Default TF2 HUD Files

SET "current_folder=%cd%"
SET "scheme_folder=..\reference\resource"
SET "script_folder=..\reference\scripts"
SET "resource_folder=..\reference\resource\ui"

:: Use HLExtract to get default HUD files ( https://developer.valvesoftware.com/wiki/HLLib#HLExtract )
IF EXIST "HLExtract.exe" (
	REM Extracting resource folder (schemes + main menu button actions)
	echo Extracting scheme files to: %scheme_folder%
	HLExtract.exe -p "../../../tf2_misc_dir.vpk" -d "%scheme_folder%" -e "root\resource\chatscheme.res" -m -v -s
	HLExtract.exe -p "../../../tf2_misc_dir.vpk" -d "%scheme_folder%" -e "root\resource\clientscheme.res" -m -v -s
	HLExtract.exe -p "../../../tf2_misc_dir.vpk" -d "%scheme_folder%" -e "root\resource\gamemenu.res" -m -v -s
	HLExtract.exe -p "../../../tf2_misc_dir.vpk" -d "%scheme_folder%" -e "root\resource\sourcescheme.res" -m -v -s
	echo Extracting script files to: %script_folder%
	HLExtract.exe -p "../../../tf2_misc_dir.vpk" -d "%script_folder%" -e "root\scripts\hudlayout.res" -m -v -s
	HLExtract.exe -p "../../../tf2_misc_dir.vpk" -d "%script_folder%" -e "root\scripts\hudanimations_tf.txt" -m -v -s
	HLExtract.exe -p "../../../tf2_misc_dir.vpk" -d "%script_folder%" -e "root\scripts\hudanimations_manifest.txt" -m -v -s
	HLExtract.exe -p "../../../tf2_misc_dir.vpk" -d "%script_folder%" -e "root\scripts\mod_textures.txt" -m -v -s
	echo Extracting resource files to %resource_folder%
	HLExtract.exe -p "../../../tf2_misc_dir.vpk" -d "%resource_folder%\.." -e "root\resource\ui" -m -v -s
) ELSE (
	echo HLExtract is not in the dev folder, can't obtain updated base files
)

pause