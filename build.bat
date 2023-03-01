@echo off

set NAME=nodumbcafe

if "%1"=="appbg" (
    pyinstaller --name %NAME% --onefile --noconsole --icon .\icon\nocf.ico .\autolockscreen_bg.py .\avoiddumbcafe.spec
) else if "%1"=="app" (
    pyinstaller --name %NAME% --onefile --icon .\icon\nocf.ico .\autolockscreen.py .\avoiddumbcafe.spec
) else (
    echo Usage: build.bat "[appbg|app]" 
    echo "appbg: build an app running in background" 
    echo "app build gui app"
    exit /b 1
)

echo Done.
exit /b 0