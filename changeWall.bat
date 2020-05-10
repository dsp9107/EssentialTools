echo off
set extensions=jpg jpeg bmp png gif tiff
(for %%a in (%extensions%) do (
	if exist %~sdp0AnyBitmapImage.%%a (
		reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d  %~sdp0AnyBitmapImage.%%a /f
		echo Set wallpaper to: %~sdp0AnyBitmapImage.%%a
	)
))
RUNDLL32.EXE user32.dll, UpdatePerUserSystemParameters
pause
