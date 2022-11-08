@echo off
TITLE Bienvenid@ %USERNAME% a QUALITRON CORONA
MODE con:cols=80 lines=40

:inicio
SET var=0
cls
echo ------------------------------------------------------------------------------
echo  %DATE% ^| %TIME%
echo ------------------------------------------------------------------------------
echo  1    Conectar Madrid  
echo  2    Conectar Prestigio  
echo  3    Conecar Sopo Planta 1  
echo  4    Verificar Conexiones 
echo  5    Desconectar todo 
echo  6    Salir
echo ------------------------------------------------------------------------------
echo.

SET /p var= ^> Seleccione una opcion [1-6]:

if "%var%"=="0" goto inicio
if "%var%"=="1" goto op1
if "%var%"=="2" goto op2
if "%var%"=="3" goto op3
if "%var%"=="4" goto op4
if "%var%"=="5" goto op5
if "%var%"=="6" goto salir

::Mensaje de error, validación cuando se selecciona una opción fuera de rango
echo. El numero "%var%" no es una opcion valida, por favor intente de nuevo.
echo.
pause
echo.
goto:inicio

:op1
    echo.
    echo. Has elegido la opcion No. 1
    echo.
        ::Aquí van las líneas de comando de tu opción
        color 09
net use U: /delete /y
net use V: /delete /y
net use X: /delete /y
net use Y: /delete /y

net use Y: \\10.24.30.41\Q$ /user:administrator 1234567890
ECHO :: Se conecto MD_9
net use X: \\10.24.30.42\Q$ /user:administrator 1234567890
ECHO :: Se conecto MD_10
net use V: \\10.24.30.43\Q$ /user:administrator 1234567890
ECHO :: Se conecto MD_8
net use U: \\10.24.30.44\Q$ /user:administrator 1234567890
ECHO :: Se conecto MD_7

ECHO ::             
ECHO :: 
ECHO ::   #####             ###               ####
ECHO ::  ##                  ##              ##  ##
ECHO ::   #####              ##              ##  ##
ECHO ::       ##             ##              ##  ##
ECHO ::  ######             ####              ####
ECHO :: FINALIZADA CONEXION RED QUALITRON MADRID

    echo.
    pause
    goto:inicio

:op2
    echo.
    echo. Has elegido la opcion No. 2
    echo.
        ::Aquí van las líneas de comando de tu opción
        color 09
net use S: /delete /y
net use T: /delete /y
net use T: \\10.27.25.2\Q$ /user:administrator ""
ECHO :: Se conecto PR1_10
net use S: \\10.27.25.3\Q$ /user:administrator ""
ECHO :: Se conecto PR1_11

ECHO ::             
ECHO :: 
ECHO ::   #####             ###               ####
ECHO ::  ##                  ##              ##  ##
ECHO ::   #####              ##              ##  ##
ECHO ::       ##             ##              ##  ##
ECHO ::  ######             ####              ####
ECHO :: FINALIZADA CONEXION RED QUALITRON PRESTIGIO

    echo.
    pause
    goto:inicio

:op3
    echo.
    echo. Has elegido la opcion No. 3
    echo.
        ::Aquí van las líneas de comando de tu opción
        color 0A
net use M: /delete /y
net use N: /delete /y
net use O: /delete /y
net use P: /delete /y
net use Q: /delete /y
net use R: /delete /y
net use R: \\10.27.25.4\Q$ /user:administrator ""
ECHO :: Se conecto P1_9
net use Q: \\10.27.25.5\Q$ /user:administrator ""
ECHO :: Se conecto P1_4
net use P: \\10.27.25.6\Q$ /user:administrator ""
ECHO :: Se conecto P1_5
net use O: \\10.27.25.7\Q$ /user:administrator ""
ECHO :: Se conecto P1_6
net use N: \\10.27.25.8\Q$ /user:administrator ""
ECHO :: Se conecto P1_7
net use M: \\10.27.25.9\Q$ /user:administrator ""
ECHO :: Se conecto P1_8

ECHO ::            
ECHO :: 
ECHO ::   #####             ###               ####
ECHO ::  ##                  ##              ##  ##
ECHO ::   #####              ##              ##  ##
ECHO ::       ##             ##              ##  ##
ECHO ::  ######             ####              ####
ECHO :: FINALIZADA CONEXION RED QUALITRON SOPO PLANTA 1
    echo.
    pause
    goto:inicio
  
:op4
    echo.
    echo. Has elegido la opcion No. 4
    echo.
        ::Aquí van las líneas de comando de tu opción
        color 0B
ECHO :: EQUIPOS DE MADRID
ECHO :: QUALITRON HORNO 9
ping 10.24.30.41
ECHO :: QUALITRON HORNO 10
ping 10.24.30.42
ECHO :: QUALITRON HORNO 8
ping 10.24.30.43
ECHO :: QUALITRON HORNO 7
ping 10.24.30.44
pause
ECHO :: EQUIPOS PRESTIGIO
ECHO :: QUALITRON HORNO 10 tecno 10
ping 10.27.25.2
ECHO :: QUALITRON HORNO 11 system 11
ping 10.27.25.3
pause
ECHO :: EQUIPOS PLANTA 1 SOPO
ECHO :: QUALITRON HORNO 9 P1 System 9
ping 10.27.25.4
ECHO :: QUALITRON HORNO 4 P1 System 4
ping 10.27.25.5
ECHO :: QUALITRON HORNO 5 P1 System 5
ping 10.27.25.6
ECHO :: QUALITRON HORNO 6 P1 System 6
ping 10.27.25.7
ECHO :: QUALITRON HORNO 7 P1 System 7
ping 10.27.25.8
ECHO :: QUALITRON HORNO 8 P1 System 8
ping 10.27.25.9
pause
net use
ECHO ::                                      
ECHO ::   ####     ####    ######    ####    #####     ####
ECHO ::  ##  ##   ##  ##    ##  ##  ##  ##   ##  ##       ##
ECHO ::  ##       ##  ##    ##      ##  ##   ##  ##    #####
ECHO ::  ##  ##   ##  ##    ##      ##  ##   ##  ##   ##  ##
ECHO ::   ####     ####    ####      ####    ##  ##    #####
ECHO :: 
    echo.
    pause
    goto:inicio

:op5
    echo.
    echo. Has elegido la opcion No. 5
    echo.
        ::Aquí van las líneas de comando de tu opción
        color 0C
net use M: /delete /y
net use N: /delete /y
net use O: /delete /y
net use P: /delete /y
net use Q: /delete /y
net use R: /delete /y
net use S: /delete /y
net use T: /delete /y
net use U: /delete /y
net use V: /delete /y
net use X: /delete /y
net use Y: /delete /y
ECHO :: SE DESCONECTARON LAS MQ: MD_9;MD_10;MD_8;MD_7;PR1_10;PR1_11;P1_9;P1_4;P1_5;P1_6;P1_7;P1_8. 
ECHO ::                                      
ECHO ::   ####     ####    ######    ####    #####     ####
ECHO ::  ##  ##   ##  ##    ##  ##  ##  ##   ##  ##       ##
ECHO ::  ##       ##  ##    ##      ##  ##   ##  ##    #####
ECHO ::  ##  ##   ##  ##    ##      ##  ##   ##  ##   ##  ##
ECHO ::   ####     ####    ####      ####    ##  ##    #####
    echo.
    pause
    goto:inicio

:salir
    @cls&exit