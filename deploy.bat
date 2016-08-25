:start
echo Starting worker processes....
SET PythonPath=C:\Python27\Python.exe
SET DbPath=D:\Programs\VCScan\pogom_vc.db
SET SpawnJson=D:\Programs\VCScan\vc_spawn.json
SET Executable=D:\Programs\PokemonGo-Map\runserver.py
SET scan_delay=10
Start "VCScan - Worker" python %Executable% -u vcspawnscan11 -p vcspawnscan11 -l "200 granville st vancouver bc" -ss %SpawnJson% -D %DbPath% -ns -sd %scan_delay% -k AIzaSyDP_x9ZrPDMBYEqN4hfeJhrBp605qZbPdk
Start "VCScan - Server" python web_server.py
pause
goto start