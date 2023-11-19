@echo off
REM if else goto
SET /A g_var=10
SET /A g_var1=20

if %g_var%==10 (
echo " this is correct value "
) else (
echo " this is wrong value " )