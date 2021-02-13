; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "LibreSprite"
#define MyAppVersion "1.0"
#define MyAppPublisher "LibreSprite"
#define MyAppURL "https://www.libresprite.org/"
#define MyAppExeName "libresprite.exe"
#define MyAppAssocName MyAppName + " File"
#define MyAppAssocExt ".ase"
#define MyAppAssocKey StringChange(MyAppAssocName, " ", "") + MyAppAssocExt

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{E50A60CE-DF57-4FDE-AF8F-91D452A4C60D}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
ChangesAssociations=yes
DisableProgramGroupPage=yes
LicenseFile=D:\Programacion\LibreSprite\LICENSE.txt
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=C:\Users\Mauricio
OutputBaseFilename=LibreSpriteWindowsSetup
SetupIconFile=D:\Programacion\LibreSprite\data\icons\ase.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "D:\Programacion\LibreSprite\build\bin\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Programacion\LibreSprite\build\bin\gen.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Programacion\LibreSprite\build\bin\~libresprite.DDF"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Programacion\LibreSprite\build\bin\gen.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Programacion\LibreSprite\build\bin\gen.ilk"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Programacion\LibreSprite\build\bin\gen.pdb"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Programacion\LibreSprite\build\bin\libresprite.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Programacion\LibreSprite\build\bin\libresprite.ilk"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Programacion\LibreSprite\build\bin\libresprite.pdb"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Programacion\LibreSprite\build\bin\data\*"; DestDir: "{app}\data"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocExt}\OpenWithProgids"; ValueType: string; ValueName: "{#MyAppAssocKey}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}"; ValueType: string; ValueName: ""; ValueData: "{#MyAppAssocName}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\{#MyAppAssocKey}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""
Root: HKA; Subkey: "Software\Classes\Applications\{#MyAppExeName}\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

