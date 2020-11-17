@echo off
call :treeProcess
goto :eof

:treeProcess
rem Do whatever you want here over the files of this subdir, for example:
for %%f in (*.html) do html2text  "%%f" "utf-8" >> "%%ff.txt"
for /D %%d in (*) do (
    cd %%d
    call :treeProcess
    cd ..
)
exit /b
