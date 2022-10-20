@echo off

ECHO :: DESCONECTAR UNIDADES DE RED

cd\
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

ECHO :: CONECTAR PLANTA MADRID

net use Y: \\10.24.30.41\Q$ /user:administrator 1234567890
net use X: \\10.24.30.42\Q$ /user:administrator 1234567890
net use V: \\10.24.30.43\Q$ /user:administrator 1234567890
net use U: \\10.24.30.44\Q$ /user:administrator 1234567890

ECHO :: FINALIZADA CONEXION RED QUALITRON MADRID
PAUSE

ECHO :: CONECTAR PLANTA SOPO PRESTIGIO

net use T: \\10.27.25.2\Q$ /user:administrator ""
net use S: \\10.27.25.3\Q$ /user:administrator ""

ECHO :: FINALIZADA CONEXION RED QUALITRON PRESTIGIO
pause

ECHO :: CONECTAR PLANTA SOPO PLANTA 1

net use R: \\10.27.25.4\Q$ /user:administrator ""
net use Q: \\10.27.25.5\Q$ /user:administrator ""
net use P: \\10.27.25.6\Q$ /user:administrator ""
net use O: \\10.27.25.7\Q$ /user:administrator ""
net use N: \\10.27.25.8\Q$ /user:administrator ""
net use M: \\10.27.25.9\Q$ /user:administrator ""

ECHO :: FINALIZADA CONEXION RED QUALITRON SOPO PLANTA 1
PAUSE