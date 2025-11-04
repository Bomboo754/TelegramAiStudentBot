@echo off
echo Устанавливаем нужные библиотеки...
python -m pip install --upgrade pip
python -m pip install "python-telegram-bot[async]" openai
echo.
echo ГОТОВО! Теперь запусти start_bot.bat
pause