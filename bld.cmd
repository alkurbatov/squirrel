SET BUILDER=pyinstaller
SET OPTS=--onefile --console --noconfirm
SET TARGET=src\squirrel.py
SET SPEC=squirrel.spec

if exist %SPEC% (
	%BUILDER% %OPTS% %SPEC%
) else (
	%BUILDER% %OPTS% %TARGET%
)

