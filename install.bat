@echo off
echo Installing needed libraries...
python -m pip install --upgrade pip
python -m pip install "python-telegram-bot[async]" openai
echo.
echo Set up is Ready! now open start_bot.bat
pause