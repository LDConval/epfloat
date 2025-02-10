from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x664534, Add, -37888),# units:Graphics  index:61    from 188 To 40
        SetMemory(0x664540, Add, -393216),# units:Graphics  index:74    from 46 To 40
        SetMemory(0x6647F4, Add, -65536),# units:Shield Enable  index:70    from 1 To 0
        SetMemory(0x660E78, Add, 0),# units:Shield Amount  index:61    from 80 To 80
        SetMemory(0x662444, Add, 0),# units:Hit Points  index:61    from 2560 To 2560
        SetMemory(0x662478, Add, 0),# units:Hit Points  index:74    from 2560 To 2560
        SetMemory(0x663DD8, Add, 33),# units:Rank/Sublabel  index:8    from 10 To 43
        SetMemory(0x663DF8, Add, 671088640),# units:Rank/Sublabel  index:43    from 10 To 50
        SetMemory(0x663E0C, Add, -2048),# units:Rank/Sublabel  index:61    from 12 To 4
        SetMemory(0x663E14, Add, 1769472),# units:Rank/Sublabel  index:70    from 8 To 35
        SetMemory(0x663E18, Add, -524288),# units:Rank/Sublabel  index:74    from 12 To 4
        SetMemory(0x6636F4, Add, -11264),# units:Ground Weapon  index:61    from 111 To 67
        SetMemory(0x663700, Add, -1179648),# units:Ground Weapon  index:74    from 86 To 68
        SetMemory(0x66171C, Add, -16128),# units:Air Weapon  index:61    from 130 To 67
        SetMemory(0x661728, Add, -4063232),# units:Air Weapon  index:74    from 130 To 68
        SetMemory(0x65FC54, Add, 256),# units:Max Air Hits  index:61    from 0 To 1
        SetMemory(0x65FC60, Add, 65536),# units:Max Air Hits  index:74    from 0 To 1
        SetMemory(0x660180, Add, 3),# units:AI Internal  index:8    from 0 To 3
        SetMemory(0x6601A0, Add, 50331648),# units:AI Internal  index:43    from 0 To 3
        SetMemory(0x6601BC, Add, 196608),# units:AI Internal  index:70    from 0 To 3
        SetMemory(0x6601C0, Add, -196608),# units:AI Internal  index:74    from 3 To 0
        SetMemory(0x66412C, Add, 1073676160),# units:Special Ability Flags  index:43    from 436273284 To 1509949444
        SetMemory(0x664174, Add, 1103036544),# units:Special Ability Flags  index:61    from 406913024 To 1509949568
        SetMemory(0x664188, Add, 128),# units:Special Ability Flags  index:66    from 1509949440 To 1509949568
        SetMemory(0x6641A8, Add, 1103036544),# units:Special Ability Flags  index:74    from 406913024 To 1509949568
        SetMemory(0x662DF4, Add, 256),# units:Target Acquisition Range  index:61    from 3 To 4
        SetMemory(0x662E00, Add, 65536),# units:Target Acquisition Range  index:74    from 3 To 4
        SetMemory(0x663274, Add, 256),# units:Sight Range  index:61    from 7 To 8
        SetMemory(0x663280, Add, 65536),# units:Sight Range  index:74    from 7 To 8
        SetMemory(0x6632A0, Add, -655360),# units:Sight Range  index:106    from 10 To 0
        SetMemory(0x6632A4, Add, -134217728),# units:Sight Range  index:111    from 8 To 0
        SetMemory(0x6632A8, Add, -2048),# units:Sight Range  index:113    from 8 To 0
        SetMemory(0x6632A8, Add, -655360),# units:Sight Range  index:114    from 10 To 0
        SetMemory(0x6621A8, Add, 33554432),# units:Unit Size  index:43    from 1 To 3
        SetMemory(0x6621BC, Add, 512),# units:Unit Size  index:61    from 1 To 3
        SetMemory(0x6621C8, Add, 131072),# units:Unit Size  index:74    from 1 To 3
        SetMemory(0x65FF10, Add, 0),# units:Armor  index:74    from 1 To 1
        SetMemory(0x662038, Add, -15466496),# units:Ready Sound  index:61    from 728 To 492
        SetMemory(0x662054, Add, -236),# units:Ready Sound  index:74    from 728 To 492
        SetMemory(0x660028, Add, -15400960),# units:What Sound Start  index:61    from 733 To 498
        SetMemory(0x660044, Add, -235),# units:What Sound Start  index:74    from 733 To 498
        SetMemory(0x662C68, Add, -15138816),# units:What Sound End  index:61    from 736 To 505
        SetMemory(0x662C84, Add, -231),# units:What Sound End  index:74    from 736 To 505
        SetMemory(0x663BB0, Add, -15400960),# units:Piss Sound Start  index:61    from 729 To 494
        SetMemory(0x663BCC, Add, -235),# units:Piss Sound Start  index:74    from 729 To 494
        SetMemory(0x661F60, Add, -15400960),# units:Piss Sound End  index:61    from 732 To 497
        SetMemory(0x661F7C, Add, -235),# units:Piss Sound End  index:74    from 732 To 497
        SetMemory(0x663C88, Add, -15138816),# units:Yes Sound Start  index:61    from 737 To 506
        SetMemory(0x663CA4, Add, -231),# units:Yes Sound Start  index:74    from 737 To 506
        SetMemory(0x6614B8, Add, -14942208),# units:Yes Sound End  index:61    from 740 To 512
        SetMemory(0x6614D4, Add, -228),# units:Yes Sound End  index:74    from 740 To 512
        SetMemory(0x662954, Add, 1),# units:StarEdit Placement Box Width  index:61    from 24 To 25
        SetMemory(0x662968, Add, -7),# units:StarEdit Placement Box Width  index:66    from 32 To 25
        SetMemory(0x662988, Add, 1),# units:StarEdit Placement Box Width  index:74    from 24 To 25
        SetMemory(0x662A08, Add, -128),# units:StarEdit Placement Box Width  index:106    from 128 To 0
        SetMemory(0x662A1C, Add, -128),# units:StarEdit Placement Box Width  index:111    from 128 To 0
        SetMemory(0x662A24, Add, -128),# units:StarEdit Placement Box Width  index:113    from 128 To 0
        SetMemory(0x662A28, Add, -128),# units:StarEdit Placement Box Width  index:114    from 128 To 0
        SetMemory(0x662954, Add, -327680),# units:StarEdit Placement Box Height  index:61    from 30 To 25
        SetMemory(0x662968, Add, -458752),# units:StarEdit Placement Box Height  index:66    from 32 To 25
        SetMemory(0x662988, Add, -327680),# units:StarEdit Placement Box Height  index:74    from 30 To 25
        SetMemory(0x662A08, Add, -6291456),# units:StarEdit Placement Box Height  index:106    from 96 To 0
        SetMemory(0x662A1C, Add, -6291456),# units:StarEdit Placement Box Height  index:111    from 96 To 0
        SetMemory(0x662A24, Add, -6291456),# units:StarEdit Placement Box Height  index:113    from 96 To 0
        SetMemory(0x662A28, Add, -6291456),# units:StarEdit Placement Box Height  index:114    from 96 To 0
        SetMemory(0x6619B0, Add, 0),# units:Unit Size Left  index:61    from 12 To 12
        SetMemory(0x6619D8, Add, -3),# units:Unit Size Left  index:66    from 15 To 12
        SetMemory(0x661A18, Add, 0),# units:Unit Size Left  index:74    from 12 To 12
        SetMemory(0x6619B0, Add, 393216),# units:Unit Size Up  index:61    from 6 To 12
        SetMemory(0x6619D8, Add, -196608),# units:Unit Size Up  index:66    from 15 To 12
        SetMemory(0x661A18, Add, 393216),# units:Unit Size Up  index:74    from 6 To 12
        SetMemory(0x6619B4, Add, 1),# units:Unit Size Right  index:61    from 11 To 12
        SetMemory(0x6619DC, Add, -4),# units:Unit Size Right  index:66    from 16 To 12
        SetMemory(0x661A1C, Add, 1),# units:Unit Size Right  index:74    from 11 To 12
        SetMemory(0x6619B4, Add, -458752),# units:Unit Size Down  index:61    from 19 To 12
        SetMemory(0x6619DC, Add, -262144),# units:Unit Size Down  index:66    from 16 To 12
        SetMemory(0x661A1C, Add, -458752),# units:Unit Size Down  index:74    from 19 To 12
        SetMemory(0x663000, Add, -524288),# units:Portrait  index:61    from 49 To 41
        SetMemory(0x66301C, Add, -8),# units:Portrait  index:74    from 49 To 41
        SetMemory(0x663900, Add, 0),# units:Mineral Cost  index:61    from 100 To 100
        SetMemory(0x66391C, Add, 0),# units:Mineral Cost  index:74    from 100 To 100
        SetMemory(0x65FD78, Add, 0),# units:Vespene Cost  index:61    from 0 To 0
        SetMemory(0x65FD94, Add, 0),# units:Vespene Cost  index:74    from 0 To 0
        SetMemory(0x6604A0, Add, 0),# units:Build Time  index:61    from 150 To 150
        SetMemory(0x6604BC, Add, 0),# units:Build Time  index:74    from 150 To 150
        SetMemory(0x6637C8, Add, 16777216),# units:Staredit Group Flags  index:43    from 9 To 10
        SetMemory(0x6637E4, Add, -131072),# units:Staredit Group Flags  index:70    from 12 To 10
        SetMemory(0x663D24, Add, -1024),# units:Supply Required  index:61    from 4 To 0
        SetMemory(0x663D28, Add, -262144),# units:Supply Required  index:66    from 4 To 0
        SetMemory(0x663D30, Add, -131072),# units:Supply Required  index:74    from 2 To 0
        SetMemory(0x66444C, Add, 512),# units:Space Required  index:61    from 2 To 4
        SetMemory(0x664458, Add, 131072),# units:Space Required  index:74    from 2 To 4
        SetMemory(0x663480, Add, -4915200),# units:Build Score  index:61    from 325 To 250
        SetMemory(0x66349C, Add, 250),# units:Build Score  index:74    from 0 To 250
        SetMemory(0x663EC8, Add, 200),# units:Destroy Score  index:8    from 800 To 1000
        SetMemory(0x663F0C, Add, 26214400),# units:Destroy Score  index:43    from 600 To 1000
        SetMemory(0x663F30, Add, -9830400),# units:Destroy Score  index:61    from 650 To 500
        SetMemory(0x663F44, Add, -300),# units:Destroy Score  index:70    from 1300 To 1000
        SetMemory(0x663F4C, Add, 100),# units:Destroy Score  index:74    from 400 To 500
        SetMemory(0x660714, Add, -256),# units:Broodwar Unit Flag  index:61    from 1 To 0
        SetMemory(0x661590, Add, -33554432),# units:Staredit Availability Flags  index:61    from 975 To 463
        SetMemory(0x6615AC, Add, 8),# units:Staredit Availability Flags  index:74    from 455 To 463
        SetMemory(0x657364, Add, 618),# weapons:Label  index:66    from 286 To 904
        SetMemory(0x657364, Add, 41746432),# weapons:Label  index:67    from 287 To 924
        SetMemory(0x657368, Add, 656),# weapons:Label  index:68    from 288 To 944
        SetMemory(0x656DB4, Add, 2),# weapons:Graphics  index:67    from 159 To 161
        SetMemory(0x656DB8, Add, 19),# weapons:Graphics  index:68    from 143 To 162
        SetMemory(0x657A20, Add, 1),# weapons:Target Flags  index:68    from 2 To 3
        SetMemory(0x65757C, Add, 0),# weapons:Maximum Range  index:67    from 128 To 128
        SetMemory(0x657580, Add, 32),# weapons:Maximum Range  index:68    from 96 To 128
        SetMemory(0x65729C, Add, -2),# weapons:Weapon Type  index:68    from 3 To 1
        SetMemory(0x6566B4, Add, -1),# weapons:Weapon Behavior  index:68    from 2 To 1
        SetMemory(0x656F34, Add, -1638400),# weapons:Damage Amount  index:67    from 45 To 20
        SetMemory(0x656F38, Add, 15),# weapons:Damage Amount  index:68    from 5 To 20
        SetMemory(0x657700, Add, 1),# weapons:Damage Bonus  index:68    from 1 To 2
        SetMemory(0x656FF8, Add, 134217728),# weapons:Weapon Cooldown  index:67    from 22 To 30
        SetMemory(0x6569D4, Add, 112),# weapons:Attack Angle  index:68    from 16 To 128
        SetMemory(0x656808, Add, -1),# weapons:Icon  index:68    from 355 To 354
        SetMemory(0x6CA458, Add, -1179648),# flingy:Sprite  index:161    from 355 To 337
        SetMemory(0x6CA45C, Add, -19),# flingy:Sprite  index:162    from 356 To 337
        SetMemory(0x6C9FA4, Add, 427),# flingy:Speed  index:43    from 1280 To 1707
        SetMemory(0x6CA17C, Add, 17067),# flingy:Speed  index:161    from 0 To 17067
        SetMemory(0x6CA180, Add, 8534),# flingy:Speed  index:162    from 8533 To 17067
        SetMemory(0x6C9CCC, Add, 1245184),# flingy:Acceleration  index:43    from 48 To 67
        SetMemory(0x6C9DB8, Add, 55705600),# flingy:Acceleration  index:161    from 0 To 850
        SetMemory(0x6C9DBC, Add, 183),# flingy:Acceleration  index:162    from 667 To 850
        SetMemory(0x6C99DC, Add, 4678),# flingy:Halt Distance  index:43    from 17067 To 21745
        SetMemory(0x6C9BB4, Add, 171343),# flingy:Halt Distance  index:161    from 0 To 171343
        SetMemory(0x6C9BB8, Add, 116761),# flingy:Halt Distance  index:162    from 54582 To 171343
        SetMemory(0x6C9EC0, Add, 32512),# flingy:Turn Radius  index:161    from 0 To 127
        SetMemory(0x6C9EC0, Add, 5701632),# flingy:Turn Radius  index:162    from 40 To 127
        SetMemory(0x6C98F8, Add, -256),# flingy:Movement Control  index:161    from 2 To 1
        SetMemory(0x655768, Add, -100),# upgrades:Mineral Cost Base  index:20    from 100 To 0
        SetMemory(0x655768, Add, -9830400),# upgrades:Mineral Cost Base  index:21    from 150 To 0
        SetMemory(0x65576C, Add, -200),# upgrades:Mineral Cost Base  index:22    from 200 To 0
        SetMemory(0x6559E8, Add, 0),# upgrades:Mineral Cost Factor  index:20    from 0 To 0
        SetMemory(0x6559E8, Add, 0),# upgrades:Mineral Cost Factor  index:21    from 0 To 0
        SetMemory(0x6559EC, Add, 0),# upgrades:Mineral Cost Factor  index:22    from 0 To 0
        SetMemory(0x655868, Add, -100),# upgrades:Vespene Cost Base  index:20    from 100 To 0
        SetMemory(0x655868, Add, -9830400),# upgrades:Vespene Cost Base  index:21    from 150 To 0
        SetMemory(0x65586C, Add, -200),# upgrades:Vespene Cost Base  index:22    from 200 To 0
        SetMemory(0x6557E8, Add, 0),# upgrades:Vespene Cost Factor  index:20    from 0 To 0
        SetMemory(0x6557E8, Add, 0),# upgrades:Vespene Cost Factor  index:21    from 0 To 0
        SetMemory(0x6557EC, Add, 0),# upgrades:Vespene Cost Factor  index:22    from 0 To 0
        SetMemory(0x655BA8, Add, -14),# upgrades:Research Time Base  index:20    from 15 To 1
        SetMemory(0x655BA8, Add, -917504),# upgrades:Research Time Base  index:21    from 15 To 1
        SetMemory(0x655BAC, Add, -14),# upgrades:Research Time Base  index:22    from 15 To 1
        SetMemory(0x655968, Add, 1),# upgrades:Research Time Factor  index:20    from 0 To 1
        SetMemory(0x655968, Add, 65536),# upgrades:Research Time Factor  index:21    from 0 To 1
        SetMemory(0x65596C, Add, 1),# upgrades:Research Time Factor  index:22    from 0 To 1
        SetMemory(0x655AE8, Add, 56),# upgrades:Icon  index:20    from 249 To 305
        SetMemory(0x655AE8, Add, 3211264),# upgrades:Icon  index:21    from 256 To 305
        SetMemory(0x655AEC, Add, 21),# upgrades:Icon  index:22    from 284 To 305
        SetMemory(0x655A68, Add, -7),# upgrades:Label  index:20    from 431 To 424
        SetMemory(0x655A68, Add, -524288),# upgrades:Label  index:21    from 432 To 424
        SetMemory(0x655A6C, Add, -9),# upgrades:Label  index:22    from 433 To 424
        SetMemory(0x655C10, Add, 1),# upgrades:Race  index:20    from 1 To 2
        SetMemory(0x655C10, Add, 256),# upgrades:Race  index:21    from 1 To 2
        SetMemory(0x655C10, Add, 65536),# upgrades:Race  index:22    from 1 To 2
        SetMemory(0x655714, Add, 0),# upgrades:Max. Repeats  index:20    from 1 To 1
        SetMemory(0x655714, Add, 0),# upgrades:Max. Repeats  index:21    from 1 To 1
        SetMemory(0x655714, Add, 0),# upgrades:Max. Repeats  index:22    from 1 To 1
    ])

