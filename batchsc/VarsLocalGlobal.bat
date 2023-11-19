@echo off
set /A g_var = 10
setlocal
set /A l_var = 20
set /A l_var1=l_var + g_var
echo LV = %l_var1%
echo GV = %g_var%
endlocal
echo GV = %g_var%
echo LV = %l_var1%