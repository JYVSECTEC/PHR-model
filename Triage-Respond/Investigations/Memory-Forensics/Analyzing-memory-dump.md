# Analysing memory dump

This documentation shows basic analysis of a memory dump from a system that is infected with Cridex malware. The dump can be downloaded from [here](http://files.sempersecurus.org/dumps/cridex_memdump.zip). Both Volatility 2 and 3 will be used during the analysis.

## Analysis

Before analysis can be started, both Volatility versions are downloaded. Download commands for Volatility 2:

```
git clone https://github.com/volatilityfoundation/volatility
cd volatility
sudo python setup.py install
```

And for Volatility 3:

```
git clone https://github.com/volatilityfoundation/volatility3
cd volatility3
sudo python3 setup.py install
```

Some plugins may require external Python packages and Volatility should notify user about those packages when it is ran. These packages can be downloaded using pip.

Analysis will follow [SANS Memory Forensics Cheat Sheet](https://assets.contentstack.io/v3/assets/blt36c2e63521272fdc/bltc7925ba3238b6e04/5e345fb87ca70442647a61f7/Memory-Forensics-Cheat-Sheet-v1_2.pdf) 6 step process. The cheat sheet also contains useful Volatility 2 commands inside related categories.

### Image information for Volatility 2

We start by determining appropriate profile for Volatility 2. As shown in the [README](https://github.com/JYVSECTEC/PHR-model/blob/master/Triage-Respond/Investigations/Memory-Forensics/README.md) example, we can use `imageinfo` plugin for that:

<pre>
python vol.py -f ~/Documents/malware-samples/cridex.vmem imageinfo
Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : <b>WinXPSP2x86</b>, WinXPSP3x86 (Instantiated with WinXPSP2x86)
                     AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/tuomo/Documents/malware-samples/cridex.vmem)
                      PAE type : PAE
                           DTB : 0x2fe000L
                          KDBG : 0x80545ae0L
          Number of Processors : 1
     Image Type (Service Pack) : 3
                KPCR for CPU 0 : 0xffdff000L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2012-07-22 02:45:08 UTC+0000
     Image local date and time : 2012-07-21 22:45:08 -0400
</pre>

Imageinfo suggested a profile called WinXPSP2x86, which means that the system is likely 32-bit Windows XP with Service Pack 2.


### Processes

The actual analysis is started by checking processes found from the dump. **Pslist** plugin goes through doubly-linked list pointed to by global variable called PsActiveProcessHead. All the active processes are added to this linked list and when any of these processes dies, it is removed from the list. Pslist  displays common information about each process like their offsets, PIDs, PPIDs etc. **Pstree** plugin takes pslist output and turns it into a tree view making it easier to see parent and child processes. Running Volatility 3 Pstree plugin to the memory dump:

<pre>
python3 vol.py -f ~/Documents/malware-samples/cridex.vmem windows.pstree.PsTree
Volatility 3 Framework 1.0.1
Progress:  100.00		PDB scanning finished                     
PID	PPID	ImageFileName	Offset(V)	Threads	Handles	SessionId	Wow64	CreateTime	ExitTime

4	0	System	0x8205bda0	53	240	N/A	False	N/A	N/A
* 368	4	smss.exe	0x8205bda0	3	19	N/A	False	2012-07-22 02:42:31.000000 	N/A
** 584	368	csrss.exe	0x8205bda0	9	326	0	False	2012-07-22 02:42:32.000000 	N/A
** 608	368	winlogon.exe	0x8205bda0	23	519	0	False	2012-07-22 02:42:32.000000 	N/A
*** 664	608	lsass.exe	0x8205bda0	24	330	0	False	2012-07-22 02:42:32.000000 	N/A
*** 652	608	services.exe	0x8205bda0	16	243	0	False	2012-07-22 02:42:32.000000 	N/A
**** 1056	652	svchost.exe	0x8205bda0	5	60	0	False	2012-07-22 02:42:33.000000 	N/A
**** 1220	652	svchost.exe	0x8205bda0	15	197	0	False	2012-07-22 02:42:35.000000 	N/A
**** 1512	652	spoolsv.exe	0x8205bda0	14	113	0	False	2012-07-22 02:42:36.000000 	N/A
**** 908	652	svchost.exe	0x8205bda0	9	226	0	False	2012-07-22 02:42:33.000000 	N/A
**** 1004	652	svchost.exe	0x8205bda0	64	1118	0	False	2012-07-22 02:42:33.000000 	N/A
***** 1136	1004	wuauclt.exe	0x8205bda0	8	173	0	False	2012-07-22 02:43:46.000000 	N/A
***** 1588	1004	wuauclt.exe	0x8205bda0	5	132	0	False	2012-07-22 02:44:01.000000 	N/A
**** 788	652	alg.exe	0x8205bda0	7	104	0	False	2012-07-22 02:43:01.000000 	N/A
**** 824	652	svchost.exe	0x8205bda0	20	194	0	False	2012-07-22 02:42:33.000000 	N/A
1484	1464	explorer.exe	0x8205bda0	17	415	0	False	2012-07-22 02:42:36.000000 	N/A
* 1640	1484	reader_sl.exe	0x8205bda0	5	39	0	False	2012-07-22 02:42:36.000000 	N/A
</pre>

Pslist/PsTree does not usually show terminated or hidden processes. **Psscan** plugin is able to spot those kind of processes. Psscan uses pool tag scanning to find \_EPROCESS objects from dump. Kernel pool is an area of memory that stores allocations for different kernel objects. Objects of the same type have the same 4 byte pool tag. E.g. tag for processes is "Proc" and the tag for threads is "Thrd". "Proc" tag is associated with the \_EPROCESS object that psscan looks for. There are different Volatility plugins that look for different pool tags. E.g. mutantscan plugin looks for "Mute" tag and driverscan plugin looks for "Driv" tag. These plugins are not only looking at the tag, but also for memory around the allocation to remove false positives from results. Some rootkits may be able to modify pool tags and other data in the objects, which could negatively affect poolscanner plugins results.

Running Volatility 3 psscan to the dump: 

<pre>
python3 vol.py -f ~/Documents/malware-samples/cridex.vmem windows.psscan.PsScan
Volatility 3 Framework 1.0.1
Progress:  100.00		PDB scanning finished                     
PID	PPID	ImageFileName	Offset	Threads	Handles	SessionId	Wow64	CreateTime	ExitTime	File output

908	652	svchost.exe	0x2029ab8	9	226	0	False	2012-07-22 02:42:33.000000 	N/A	Disabled
664	608	lsass.exe	0x202a3b8	24	330	0	False	2012-07-22 02:42:32.000000 	N/A	Disabled
652	608	services.exe	0x202ab28	16	243	0	False	2012-07-22 02:42:32.000000 	N/A	Disabled
1640	1484	reader_sl.exe	0x207bda0	5	39	0	False	2012-07-22 02:42:36.000000 	N/A	Disabled
1512	652	spoolsv.exe	0x20b17b8	14	113	0	False	2012-07-22 02:42:36.000000 	N/A	Disabled
1588	1004	wuauclt.exe	0x225bda0	5	132	0	False	2012-07-22 02:44:01.000000 	N/A	Disabled
788	652	alg.exe	0x22e8da0	7	104	0	False	2012-07-22 02:43:01.000000 	N/A	Disabled
1484	1464	explorer.exe	0x23dea70	17	415	0	False	2012-07-22 02:42:36.000000 	N/A	Disabled
1056	652	svchost.exe	0x23dfda0	5	60	0	False	2012-07-22 02:42:33.000000 	N/A	Disabled
1136	1004	wuauclt.exe	0x23fcda0	8	173	0	False	2012-07-22 02:43:46.000000 	N/A	Disabled
1220	652	svchost.exe	0x2495650	15	197	0	False	2012-07-22 02:42:35.000000 	N/A	Disabled
608	368	winlogon.exe	0x2498700	23	519	0	False	2012-07-22 02:42:32.000000 	N/A	Disabled
584	368	csrss.exe	0x24a0598	9	326	0	False	2012-07-22 02:42:32.000000 	N/A	Disabled
368	4	smss.exe	0x24f1020	3	19	N/A	False	2012-07-22 02:42:31.000000 	N/A	Disabled
1004	652	svchost.exe	0x25001d0	64	1118	0	False	2012-07-22 02:42:33.000000 	N/A	Disabled
824	652	svchost.exe	0x2511360	20	194	0	False	2012-07-22 02:42:33.000000 	N/A	Disabled
4	0	System	0x25c89c8	53	240	N/A	False	N/A	N/A	Disabled
</pre>

As we can see from the psscan output, it found the same processes as pstree.

**Psxview** is a plugin that uses alternate process listing, which consists of 7 different ways to enumerate processes. It does the same pool scanning as psscan and linked list check as pslist, but also thread scanning, CSRSS handle table scan (csrss.exe is used in the creation of all processes and it contains handles to them), PspCid table scan (handle table in kernel memory that has references to all active processes and thread objects), session processes scan (SessionProcessLinks contains all user's session processes) and desktop thread scan (Looks for tagDESKTOP structure that contains list of all threads attached to desktops and these threads can be used to locate their processes). Psxview output contains column for each of these scans and the columns contain False or True for each process depending on was the process found using that technique.

Psxview is currently not included in Volatility 3 (version 1.0.1), so Volatility 2 will be used to run the plugin. Option called *--apply-rules* was added as part of the command. If the process was not found using certain technique, but it meets certain requirements, Okay will be displayed instead of false. Running the command with Volatility 2:

<pre>
python vol.py -f ~/Documents/malware-samples/cridex.vmem --profile=WinXPSP2x86 psxview --apply-rules
Volatility Foundation Volatility Framework 2.6.1
Offset(P)  Name                    PID pslist psscan thrdproc pspcid csrss session deskthrd ExitTime
---------- -------------------- ------ ------ ------ -------- ------ ----- ------- -------- --------
0x02498700 winlogon.exe            608 True   True   True     True   True  True    True     
0x02511360 svchost.exe             824 True   True   True     True   True  True    True     
0x022e8da0 alg.exe                 788 True   True   True     True   True  True    True     
0x020b17b8 spoolsv.exe            1512 True   True   True     True   True  True    True     
0x0202ab28 services.exe            652 True   True   True     True   True  True    True     
0x02495650 svchost.exe            1220 True   True   True     True   True  True    True     
0x0207bda0 reader_sl.exe          1640 True   True   True     True   True  True    True     
0x025001d0 svchost.exe            1004 True   True   True     True   True  True    True     
0x02029ab8 svchost.exe             908 True   True   True     True   True  True    True     
0x023fcda0 wuauclt.exe            1136 True   True   True     True   True  True    True     
0x0225bda0 wuauclt.exe            1588 True   True   True     True   True  True    True     
0x0202a3b8 lsass.exe               664 True   True   True     True   True  True    True     
0x023dea70 explorer.exe           1484 True   True   True     True   True  True    True     
0x023dfda0 svchost.exe            1056 True   True   True     True   True  True    True     
0x024f1020 smss.exe                368 True   True   True     True   Okay  Okay    Okay     
0x025c89c8 System                    4 True   True   True     True   Okay  Okay    Okay     
0x024a0598 csrss.exe               584 True   True   True     True   Okay  True    True 
</pre>

When looking at the psxview output, it seems that there was no hidden processes in the system, since all the scans pass for each process. What comes to the processes found from the system, most of them seem to be background processes. Then there is explorer.exe (GUI), which has a child process called reader\_sl.exe. Since reader\_sl.exe is explorer.exe's child process, you can assume that user started reader\_sl.exe from GUI. Explorer.exe's parent process with PID 1464 is not found from the process listings, but that is because it was started by userinit.exe, which exits shortly after.

### Deeper investigation of the processes

Reader\_sl.exe could be part of Adobe Acrobat, since that software has a component called reader\_sl.exe. One way to check the binary from which the process was started from is to use **cmdline** plugin in Volatility. Cmdline lists command line arguments used to start the process and this line of information also includes the binary path. Running cmdline with Volatility 2:

<pre>
python2 vol.py -f ~/Documents/malware-samples/cridex.vmem --profile=WinXPSP2x86 cmdline

[SNIP]
explorer.exe pid:   1484
Command line : C:\WINDOWS\Explorer.EXE
************************************************************************
spoolsv.exe pid:   1512
Command line : C:\WINDOWS\system32\spoolsv.exe
************************************************************************
reader_sl.exe pid:   1640
Command line : "C:\Program Files\Adobe\Reader 9.0\Reader\Reader_sl.exe" 
[SNIP]
</pre>

The path for Reader\_sl.exe binary seems legitimate. Though malware can always modify the binaries or replace them with something else, so even if the path seems correct, the binary could not be legitimate. DLLs loaded by processes can be checked with **Dlllist** plugin. To target a certain process, *--pid* flag can be used to specify process ID. Checking DLLs loaded by reader\_sl.exe:

<pre>
python2 vol.py -f ~/Documents/malware-samples/cridex.vmem --profile=WinXPSP2x86 dlllist --pid 1640
Volatility Foundation Volatility Framework 2.6.1
************************************************************************
reader_sl.exe pid:   1640
Command line : "C:\Program Files\Adobe\Reader 9.0\Reader\Reader_sl.exe" 
Service Pack 3

Base             Size  LoadCount LoadTime                       Path
---------- ---------- ---------- ------------------------------ ----
0x00400000     0xa000     0xffff                                C:\Program Files\Adobe\Reader 9.0\Reader\Reader_sl.exe
0x7c900000    0xaf000     0xffff                                C:\WINDOWS\system32\ntdll.dll
0x7c800000    0xf6000     0xffff                                C:\WINDOWS\system32\kernel32.dll
0x7e410000    0x91000     0xffff                                C:\WINDOWS\system32\USER32.dll
0x77f10000    0x49000     0xffff                                C:\WINDOWS\system32\GDI32.dll
0x77dd0000    0x9b000     0xffff                                C:\WINDOWS\system32\ADVAPI32.dll
0x77e70000    0x92000     0xffff                                C:\WINDOWS\system32\RPCRT4.dll
0x77fe0000    0x11000     0xffff                                C:\WINDOWS\system32\Secur32.dll
0x7c9c0000   0x817000     0xffff                                C:\WINDOWS\system32\SHELL32.dll
0x77c10000    0x58000     0xffff                                C:\WINDOWS\system32\msvcrt.dll
0x77f60000    0x76000     0xffff                                C:\WINDOWS\system32\SHLWAPI.dll
0x7c420000    0x87000     0xffff                                C:\WINDOWS\WinSxS\x86_Microsoft.VC80.CRT_1fc8b3b9a1e18e3b_8.0.50727.762_x-ww_6b128700\MSVCP80.dll
0x78130000    0x9b000     0xffff                                C:\WINDOWS\WinSxS\x86_Microsoft.VC80.CRT_1fc8b3b9a1e18e3b_8.0.50727.762_x-ww_6b128700\MSVCR80.dll
0x773d0000   0x103000        0x1                                C:\WINDOWS\WinSxS\x86_Microsoft.Windows.Common-Controls_6595b64144ccf1df_6.0.2600.5512_x-ww_35d4ce83\comctl32.dll
0x5d090000    0x9a000        0x1                                C:\WINDOWS\system32\comctl32.dll
0x5ad70000    0x38000        0x2                                C:\WINDOWS\system32\uxtheme.dll
0x71ab0000    0x17000        0x1                                C:\WINDOWS\system32\WS2_32.dll
0x71aa0000     0x8000        0x1                                C:\WINDOWS\system32\WS2HELP.dll
</pre>

Dlllist output contains information like names, sizes and paths of the loaded DLLs. Binary loads first into the address space, so it is first on the list. Values under LoadCount specify if the DLL was statically or dynamically loaded. 0xffff value means that the DLL was specified in IAT (Import Address Table) and the other values in output mean that the DLLs were loaded using LoadLibrary. The paths and names for the DLLs seem legitimate. Further examination of the DLLs would be required to check them for potential injections. **Dlldump** plugin can be used to dump processes DLLs from the memory dump if the DLLs need more investigation. 

Processes can access other objects in the system using handles. Handles allow objects to be referenced and their data to be read or modified. Volatility has a plugin called **handles**, which can be used to display handles found from memory dump. It does this by going through handle data structures. We can check reader\_sl.exe's handles by specifying its PID like when using dlllist earlier:

<pre>
python3 vol.py -f ~/Documents/malware-samples/cridex.vmem windows.handles.Handles --pid 1640
Volatility 3 Framework 1.0.1
Progress:  100.00		PDB scanning finished                     
PID	Process	Offset	HandleValue	Type	GrantedAccess	Name

1640	reader_sl.exe	0xe10096e0	0x4	KeyedEvent	0xf0003	CritSecOutOfMemoryEvent
1640	reader_sl.exe	0xe159c978	0x8	Directory	0x3	KnownDlls
1640	reader_sl.exe	0x82211678	0xc	File	0x100020	\Device\HarddiskVolume1\Documents and Settings\Robert
1640	reader_sl.exe	0x82210208	0x10	File	0x100020	\Device\HarddiskVolume1\WINDOWS\WinSxS\x86_Microsoft.VC80.CRT_1fc8b3b9a1e18e3b_8.0.50727.762_x-ww_6b128700
1640	reader_sl.exe	0xe14916d0	0x14	Directory	0xf000f	Windows
1640	reader_sl.exe	0xe1c6a588	0x18	Port	0x21f0001	
1640	reader_sl.exe	0x82319610	0x1c	Event	0x21f0003	
1640	reader_sl.exe	0x8205a2a0	0x20	WindowStation	0xf037f	WinSta0
1640	reader_sl.exe	0x822f8168	0x24	Desktop	0xf01ff	Default
1640	reader_sl.exe	0x8205a2a0	0x28	WindowStation	0xf037f	WinSta0
1640	reader_sl.exe	0x82311280	0x2c	Semaphore	0x100003	
1640	reader_sl.exe	0x82234dd0	0x30	Semaphore	0x100003	
1640	reader_sl.exe	0xe1c042d0	0x34	Key	0x20f003f	MACHINE
1640	reader_sl.exe	0xe16ce308	0x38	Directory	0x2000f	BaseNamedObjects
1640	reader_sl.exe	0x8213d0e0	0x3c	Semaphore	0x1f0003	shell.{A48F1A32-A340-11D1-BC6B-00A0C90312E1}
1640	reader_sl.exe	0xe1835648	0x40	Key	0x20f003f	USER\S-1-5-21-789336058-261478967-1417001333-1003
1640	reader_sl.exe	0x820d2f28	0x44	File	0x100020	\Device\HarddiskVolume1\WINDOWS\WinSxS\x86_Microsoft.Windows.Common-Controls_6595b64144ccf1df_6.0.2600.5512_x-ww_35d4ce83
1640	reader_sl.exe	0xe1c72300	0x48	Port	0x1f0001	
1640	reader_sl.exe	0xe17d3938	0x4c	Section	0x4	
1640	reader_sl.exe	0x81de10c8	0x50	Event	0x1f0003	
1640	reader_sl.exe	0x822924c8	0x54	Thread	0x1f03ff	Tid 1648 Pid 1640
1640	reader_sl.exe	0x821dd728	0x58	Event	0x1f0003	
1640	reader_sl.exe	0x82196418	0x5c	Event	0x1f0003	
1640	reader_sl.exe	0x820022e0	0x60	Event	0x1f0003	
1640	reader_sl.exe	0x82002a18	0x64	Event	0x1f0003	
1640	reader_sl.exe	0x822924c8	0x68	Thread	0x1f03ff	Tid 1648 Pid 1640
1640	reader_sl.exe	0x821dc270	0x6c	File	0x100001	\Device\KsecDD
<b>1640	reader_sl.exe	0xe1c5cfb8	0x70	Key	0x10	USER\S-1-5-21-789336058-261478967-1417001333-1003\SOFTWARE\MICROSOFT\WSH\8149A9A8</b>
1640	reader_sl.exe	0xe1c6c030	0x74	Token	0x18	
1640	reader_sl.exe	0x81de1e68	0x78	Event	0x1f0003	
1640	reader_sl.exe	0x81dd2e08	0x7c	IoCompletion	0x1f0003	
1640	reader_sl.exe	0x81de3c70	0x80	IoCompletion	0x1f0003	
1640	reader_sl.exe	0x81dd2e08	0x84	IoCompletion	0x1f0003	
1640	reader_sl.exe	0x822fdb00	0x88	Mutant	0x1f0001	XMM00000668
1640	reader_sl.exe	0x822d0d98	0x8c	Event	0x1f0003	XME00000668
<b>1640	reader_sl.exe	0xe154db20	0x90	Key	0x10	USER\S-1-5-21-789336058-261478967-1417001333-1003\SOFTWARE\MICROSOFT\WSH\9DBBCFAD</b>
1640	reader_sl.exe	0x820fd260	0x94	Semaphore	0x1f0003	shell.{210A4BA0-3AEA-1069-A2D9-08002B30309D}
1640	reader_sl.exe	0x81e9d708	0x98	Mutant	0x1f0001	XMR8149A9A8
1640	reader_sl.exe	0x81e1d3c0	0x9c	Event	0x1f0003	
</pre>

Output contains information like handle's value, type of the object (E.g. File, Mutant, Event, Key etc.), granted access mask that specifies the granted rights (read, write, delete etc.) and name of the object. Not all the objects have names, so the value under name column is empty for some handles. *--silent"*flag can be used to remove those handles from the output. From the output we can see that the program has atleast accessed some keys in registry under ```SOFTWARE\MICROSOFT\WSH```.

Volatility offers tools so analyze Windows registry artifacts from the dump. **Hivelist** plugin can be used to find virtual and physical offsets of hives and names of the hives. Hivelist uses pool scanning to find structures with tag CM10. Running hivelist in Volatility 2:

<pre>
python2 vol.py -f ~/Documents/malware-samples/cridex.vmem --profile=WinXPSP2x86 hivelist
Volatility Foundation Volatility Framework 2.6.1
Virtual    Physical   Name
---------- ---------- ----
0xe18e5b60 0x093f8b60 \Device\HarddiskVolume1\Documents and Settings\Robert\Local Settings\Application Data\Microsoft\Windows\UsrClass.dat
<b>0xe1a19b60 0x0a5a9b60 \Device\HarddiskVolume1\Documents and Settings\Robert\NTUSER.DAT</b>
0xe18398d0 0x08a838d0 \Device\HarddiskVolume1\Documents and Settings\LocalService\Local Settings\Application Data\Microsoft\Windows\UsrClass.dat
0xe18614d0 0x08e624d0 \Device\HarddiskVolume1\Documents and Settings\LocalService\NTUSER.DAT
0xe183bb60 0x08e2db60 \Device\HarddiskVolume1\Documents and Settings\NetworkService\Local Settings\Application Data\Microsoft\Windows\UsrClass.dat
0xe17f2b60 0x08519b60 \Device\HarddiskVolume1\Documents and Settings\NetworkService\NTUSER.DAT
0xe1570510 0x07669510 \Device\HarddiskVolume1\WINDOWS\system32\config\software
0xe1571008 0x0777f008 \Device\HarddiskVolume1\WINDOWS\system32\config\default
0xe15709b8 0x076699b8 \Device\HarddiskVolume1\WINDOWS\system32\config\SECURITY
0xe15719e8 0x0777f9e8 \Device\HarddiskVolume1\WINDOWS\system32\config\SAM
0xe13ba008 0x02e4b008 [no name]
0xe1035b60 0x02ac3b60 \Device\HarddiskVolume1\WINDOWS\system32\config\system
0xe102e008 0x02a7d008 [no name]
</pre>

Now that offsets and names of the hives are known, specific hive's keys and entries can be examined. **Printkey** plugin takes desired registry key path as argument and displays values in equivalent key paths that it finds. Different hives may contain same registry key paths in them, so printkey displays them all. Virtual offset of the hive can be given as a parameter to printkey, so that it only prints the path in that hive if the path exists. In Windows each user profile contains NTUSER.DAT where HKCU hive's data is saved when user logs out or system shuts down. User called Robert has his NTUSER.dat file located in virtual offset ```0xe1a19b60```. Using that value to specify the hive and checking the registry keys that reader_sl.exe accessed:

<pre>
python2 vol.py -f ~/Documents/malware-samples/cridex.vmem --profile=WinXPSP2x86 -o 0xe1a19b60 printkey -K "SOFTWARE\MICROSOFT\WSH\8149A9A8"
Volatility Foundation Volatility Framework 2.6.1
Legend: (S) = Stable   (V) = Volatile

----------------------------
Registry: \Device\HarddiskVolume1\Documents and Settings\Robert\NTUSER.DAT
Key name: 8149A9A8 (S)
Last updated: 2012-07-22 02:33:06 UTC+0000

Subkeys:

Values:
REG_BINARY                    : (S) 
[SNIP]
0x00000900  00 00 00 2a 62 75 73 69 6e 65 73 73 6d 61 6e 61   ...*businessmana
0x00000910  67 65 72 2e 63 6f 6d 2f 73 69 67 6e 6f 6e 2a 00   ger.com/signon*.
0x00000920  23 00 00 00 80 00 00 00 2a 62 61 6e 6b 69 6e 67   #.......*banking
0x00000930  2e 63 61 6c 62 61 6e 6b 74 72 75 73 74 2e 63 6f   .calbanktrust.co
0x00000940  6d 2a 00 26 00 00 00 80 00 00 00 2a 74 6f 77 65   m*.&.......*towe
0x00000950  72 6e 65 74 2e 63 61 70 69 74 61 6c 6f 6e 65 62   rnet.capitaloneb
0x00000960  61 6e 6b 2e 63 6f 6d 2a 00 15 00 00 00 80 00 00   ank.com*........
0x00000970  00 2a 2f 63 6d 73 65 72 76 65 72 2f 2a 00 13 00   .*/cmserver/*...
0x00000980  00 00 80 00 00 00 2a 2e 63 6f 6d 2f 4b 31 2f 2a   ......*.com/K1/*
0x00000990  00 13 00 00 00 80 00 00 00 2a 70 75 62 2f 68 74   .........*pub/ht
0x000009a0  6d 6c 2a 00 30 00 00 00 80 00 00 00 2a 62 75 73   ml*.0.......*bus
0x000009b0  69 6e 65 73 73 61 63 63 65 73 73 2e 63 69 74 69   inessaccess.citi
0x000009c0  62 61 6e 6b 2e 63 69 74 69 67 72 6f 75 70 2e 63   bank.citigroup.c
0x000009d0  6f 6d 2a 00 29 00 00 00 80 00 00 00 2a 61 63 68   om*.).......*ach
0x000009e0  69 65 76 65 61 63 63 65 73 73 2e 63 69 74 69 7a   ieveaccess.citiz
0x000009f0  65 6e 73 62 61 6e 6b 2e 63 6f 6d 2a 00 17 00 00   ensbank.com*....
[SNIP]
0x00003340  6b 2a 00 4a 00 00 00 82 00 00 00 2a 6a 71 75 65   k*.J.......*jque
0x00003350  72 79 61 64 64 6f 6e 73 76 32 2e 6a 73 2a 00 68   ryaddonsv2.js*.<b>h</b>
0x00003360  74 74 70 3a 2f 2f 31 38 38 2e 34 30 2e 30 2e 31   <b>ttp://188.40.0.1</b>
0x00003370  33 38 3a 38 30 38 30 2f 7a 62 2f 76 5f 30 31 5f   <b>38:8080/zb/v_01_</b>
0x00003380  61 2f 69 6e 2f 63 70 2e 70 68 70 00 00 0e 00 00   <b>a/in/cp.php</b>.....
[SNIP] 
0x00006a00  3c 74 64 3e 3c 61 20 69 64 3d 22 4e 65 78 74 42   &lt;td&gt;&lt;a.id="NextB
0x00006a10  75 74 74 6f 6e 31 22 20 68 72 65 66 3d 22 23 22   utton1".href="#"
0x00006a20  20 6f 6e 43 4c 69 63 6b 3d 22 44 6f 4c 6f 67 69   .onCLick="DoLogi
0x00006a30  6e 41 28 29 3b 72 65 74 75 72 6e 20 66 61 6c 73   nA();return.fals
0x00006a40  65 3b 22 20 74 69 74 6c 65 3d 22 47 6f 20 74 6f   e;".title="Go.to
0x00006a50  20 63 6f 6e 66 69 72 6d 20 63 72 65 64 69 74 20   .confirm.credit.
0x00006a60  63 61 72 64 20 69 6e 66 6f 22 20 63 6c 61 73 73   card.info".class
0x00006a70  3d 22 62 75 74 74 6f 6e 66 77 64 22 20 61 6c 74   ="buttonfwd".alt
...
</pre>

The key 9DBBCFAD didn't contain any data, but the printkey output from key 8149A9A8 contains interesting binary data. The value contains many bank domains and an URL: `http://188.40.0.1.38:8080/zb/v\_01\_a/in/cp.php`. There also seems to be HTML code that could be used to mimic banking websites. Since it is known that the system was infected with banking trojan Citrix, this registry key seems like a location where the malware hides some of its data. Since reader\_sl.exe accessed this location, the malware has most likely a control of the process.

### Network connections

Next part of the analysis is to check for network activity. **Sockscan** plugin uses pool tag scanning to find \_ADDRESS\_OBJECT structures. It can find information from active and previous sockets. Volatility 3 has plugins called **netscan** and **netstat** for analyzing network connections, but they seem not to work with this version of Windows when used on the dump: ```NotImplementedError: This version of Windows is not supported: 5.1 15.2600!```. Running sockscan to the dump with Volatility 2:

<pre>
python2 vol.py -f ~/Documents/malware-samples/cridex.vmem --profile=WinXPSP2x86 sockscan
Volatility Foundation Volatility Framework 2.6.1
Offset(P)       PID   Port  Proto Protocol        Address         Create Time
---------- -------- ------ ------ --------------- --------------- -----------
0x01fd7618     1220   1900     17 UDP             172.16.112.128  2012-07-22 02:43:01 UTC+0000
0x01fdb780      664    500     17 UDP             0.0.0.0         2012-07-22 02:42:53 UTC+0000
0x0203f460        4    138     17 UDP             172.16.112.128  2012-07-22 02:42:38 UTC+0000
0x02076620     1004    123     17 UDP             127.0.0.1       2012-07-22 02:43:01 UTC+0000
0x020c23b0      908    135      6 TCP             0.0.0.0         2012-07-22 02:42:33 UTC+0000
0x02325610      788   1028      6 TCP             127.0.0.1       2012-07-22 02:43:01 UTC+0000
0x02372808      664      0    255 Reserved        0.0.0.0         2012-07-22 02:42:53 UTC+0000
0x02372c50      664   4500     17 UDP             0.0.0.0         2012-07-22 02:42:53 UTC+0000
0x0239cc08        4    445      6 TCP             0.0.0.0         2012-07-22 02:42:31 UTC+0000
0x023f0630     1004    123     17 UDP             172.16.112.128  2012-07-22 02:43:01 UTC+0000
0x023f0d00        4    445     17 UDP             0.0.0.0         2012-07-22 02:42:31 UTC+0000
0x02440d08     1484   1038      6 TCP             0.0.0.0         2012-07-22 02:44:45 UTC+0000
0x02476878        4    139      6 TCP             172.16.112.128  2012-07-22 02:42:38 UTC+0000
0x02477460        4    137     17 UDP             172.16.112.128  2012-07-22 02:42:38 UTC+0000
0x024cd2b0     1220   1900     17 UDP             127.0.0.1       2012-07-22 02:43:01 UTC+0000
</pre>

Output contains information about processes with sockets. Each line means a single socket and the line shows data about the socket like its physical offset, port, protocol, interface's IP address and creation time. The address `172.16.112.128` is the internal IP address of the system. You cannot actually tell if the socket is listening for connections or if it has established one, since \_ADDRESS\_OBJECT is for both client and server sockets. 

**Connections** plugin shows TCP connections that were active during the time of memory acquisition. Running connections with Volatility 2:

<pre>
python2 vol.py -f ~/Documents/malware-samples/cridex.vmem --profile=WinXPSP2x86 connections
Volatility Foundation Volatility Framework 2.6.1
Offset(V)  Local Address             Remote Address            Pid
---------- ------------------------- ------------------------- ---
0x81e87620 172.16.112.128:1038       41.168.5.140:8080         1484
</pre>

Output shows that process with PID 1484 (Explorer.exe) has TCP connection to external IP address 41.168.5.140 port 8080. That port is usually associated with HTTP connections, since it is alternative port for HTTP. Explorer.exe having a connection like that could mean that the malware has injected code into the process, so it can work within explorer.exe's context, which makes it harder to spot for anti-virus and users.

**Connscan** can be used to find active and previously established connections (Works only with x64 and x86 XP and Windows server 2003). Connscan looks for kernel pool allocations with right tag, size and type. Running connscan with Volatility 2:

<pre>
python2 vol.py -f ~/Documents/malware-samples/cridex.vmem --profile=WinXPSP2x86 connscan
Volatility Foundation Volatility Framework 2.6.1
Offset(P)  Local Address             Remote Address            Pid
---------- ------------------------- ------------------------- ---
0x02087620 172.16.112.128:1038       41.168.5.140:8080         1484
<b>0x023a8008 172.16.112.128:1037       125.19.103.198:8080       1484</b>
</pre>

Connscan output shows the same connection by explorer.exe as connections plugin did. There is also a connection to IP address 125.19.103.198 port 8080. This connection was likely not active during the memory acquisition, because it was not found by connections plugin. 

### Code injections

Next step is to look for potential code injections. Since explorer.exe's and reader\_sl.exe's activity signals that they could have something to do with Cridex, they will be checked for code injections. **Malfind** plugin is able to find hidden and injected code or DLLs from user memory by looking at data like VAD tags and page permissions. Running malfind with Volatility 2: 

<pre>
python2 vol.py -f ~/Documents/malware-samples/cridex.vmem --profile=WinXPSP2x86 malfind
Volatility Foundation Volatility Framework 2.6.1
[SNIP]
Process: explorer.exe Pid: 1484 Address: 0x1460000
Vad Tag: <b>VadS</b> Protection: <b>PAGE_EXECUTE_READWRITE</b>
Flags: CommitCharge: 33, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x0000000001460000  4d 5a 90 00 03 00 00 00 04 00 00 00 ff ff 00 00   <b>MZ</b>..............
0x0000000001460010  b8 00 00 00 00 00 00 00 40 00 00 00 00 00 00 00   ........@.......
0x0000000001460020  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x0000000001460030  00 00 00 00 00 00 00 00 00 00 00 00 e0 00 00 00   ................

0x0000000001460000 4d               DEC EBP
0x0000000001460001 5a               POP EDX
0x0000000001460002 90               NOP
0x0000000001460003 0003             ADD [EBX], AL
0x0000000001460005 0000             ADD [EAX], AL
0x0000000001460007 000400           ADD [EAX+EAX], AL
0x000000000146000a 0000             ADD [EAX], AL
0x000000000146000c ff               DB 0xff
[SNIP]
Process: reader_sl.exe Pid: 1640 Address: 0x3d0000
Vad Tag: <b>VadS</b> Protection: <b>PAGE_EXECUTE_READWRITE</b>
Flags: CommitCharge: 33, MemCommit: 1, PrivateMemory: 1, Protection: 6

0x00000000003d0000  4d 5a 90 00 03 00 00 00 04 00 00 00 ff ff 00 00   <b>MZ</b>..............
0x00000000003d0010  b8 00 00 00 00 00 00 00 40 00 00 00 00 00 00 00   ........@.......
0x00000000003d0020  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x00000000003d0030  00 00 00 00 00 00 00 00 00 00 00 00 e0 00 00 00   ................

0x00000000003d0000 4d               DEC EBP
0x00000000003d0001 5a               POP EDX
0x00000000003d0002 90               NOP
0x00000000003d0003 0003             ADD [EBX], AL
0x00000000003d0005 0000             ADD [EAX], AL
0x00000000003d0007 000400           ADD [EAX+EAX], AL
0x00000000003d000a 0000             ADD [EAX], AL
[SNIP]
</pre>

Malfind output contains information like address, flags, hex dump and disassembly of the suspected injection. Malfind output shows that both explorer.exe and reader\_sl.exe contain executable, which is indicated by MZ signature at the start of hex dump. Vad tag "Vads" means that the memory region is not backed up by a file. Memory protection value PAGE\_EXECUTE\_READWRITE indicates that the memory area can be executed, read and written. Malfind output contained overall 12 different sections, which all had PAGE\_EXECUTE\_READWRITE protection. Programs can also allocate executable private memory for legitimate reasons, so malfind output usually contains several false positives.

The memory segments found by malfind can be saved to disk by using *-D* or *--dump-dir* flag. *-p* flag can be used to specify targeted processes and it can be combined with *-D* to only write certain memory segments to disk. Writing suspicious memory segments of explorer.exe and reader\_sl.exe to disk:

<pre>
python2 vol.py -f ~/Documents/malware-samples/cridex.vmem --profile=WinXPSP2x86 malfind -p 1640 -p 1484 -D malfind-dumps
</pre>

Outputted segments can be analyzed further manually or you can calculate their hashes and pass the hashes to a service like VirusTotal. Calculating hashes from the segments:

<pre>
~/volatility/malfind-dumps$ sha256sum process.0x81e7bda0.0x3d0000.dmp && sha256sum process.0x821dea70.0x1460000.dmp 
cbe5f4afd18753839d7e47ee41e6a6c1a1d03e806a77ba7a585ac7b7cad92450  process.0x81e7bda0.0x3d0000.dmp
e00a1143fea8568f5bcbe2793c6b87032ba57f2fdd122266ea799658169d36b2  process.0x821dea70.0x1460000.dmp
</pre>

VirusTotal gave 61 hits for both of these segments and Cridex was mentioned by several different AV vendors, which most likely means that the processes were injected by Cridex or Cridex has modified the processes binaries causing them to run malicious code when executed.

![VirusTotal results](https://github.com/JYVSECTEC/PHR-model/blob/master/Triage-Respond/Investigations/Memory-Forensics/malfind-virustotal-results.png?raw=true)

### Checking for rootkits

Next part is to check for malicious kernel modules. Volatility has several plugins that can be used to find kernel mode rootkits from the memory. **Modules** goes through LDR\_DATA\_TABLE\_ENTRY metadata structures pointed by PsLoadedModuleList and shows modules found from the structures and also the load order of the modules. Running modules on Volatility 2:

<pre>
python2 vol.py -f ~/Documents/malware-samples/cridex.vmem --profile=WinXPSP2x86 modules
Volatility Foundation Volatility Framework 2.6.1
Offset(V)  Name                 Base             Size File
---------- -------------------- ---------- ---------- ----
0x823fc3b0 ntoskrnl.exe         0x804d7000   0x1f8580 \WINDOWS\system32\ntkrnlpa.exe
0x823fc348 hal.dll              0x806d0000    0x20300 \WINDOWS\system32\hal.dll
0x823fc2e0 kdcom.dll            0xf8b9a000     0x2000 \WINDOWS\system32\KDCOM.DLL
0x823fc270 BOOTVID.dll          0xf8aaa000     0x3000 \WINDOWS\system32\BOOTVID.dll
0x823fc208 ACPI.sys             0xf856b000    0x2e000 ACPI.sys
0x823fc198 WMILIB.SYS           0xf8b9c000     0x2000 \WINDOWS\system32\DRIVERS\WMILIB.SYS
0x823fc130 pci.sys              0xf855a000    0x11000 pci.sys
0x823fc0c0 isapnp.sys           0xf869a000     0xa000 isapnp.sys
0x823fc050 compbatt.sys         0xf8aae000     0x3000 compbatt.sys
0x823ed008 BATTC.SYS            0xf8ab2000     0x4000 \WINDOWS\system32\DRIVERS\BATTC.SYS
0x823edf98 intelide.sys         0xf8b9e000     0x2000 intelide.sys
0x823edf28 PCIIDEX.SYS          0xf891a000     0x7000 \WINDOWS\system32\DRIVERS\PCIIDEX.SYS
0x823edeb8 MountMgr.sys         0xf86aa000     0xb000 MountMgr.sys
0x823ede48 ftdisk.sys           0xf853b000    0x1f000 ftdisk.sys
0x823eddd8 dmload.sys           0xf8ba0000     0x2000 dmload.sys
[SNIP]
</pre>

**Modules** displays information like virtual offset, module name, size and file path of each kernel module it found. **Modscan** uses pool tag scanning (tag: MmLd) to find LDR\_DATA\_TABLE\_ENTRY structures. Plugin also looks for the tags in freed and deallocated memory. Modscan can find unlinked and previously loaded modules. Running **modscan** on Volatility 2:

<pre>
python2 vol.py -f ~/Documents/malware-samples/cridex.vmem --profile=WinXPSP2x86 modscan
Volatility Foundation Volatility Framework 2.6.1
Offset(P)          Name                 Base             Size File
------------------ -------------------- ---------- ---------- ----
0x00000000020296b8 ndisuio.sys          0xf7c6f000     0x4000 \SystemRoot\system32\DRIVERS\ndisuio.sys
0x000000000202fe80 ndistapi.sys         0xf8b46000     0x3000 \SystemRoot\system32\DRIVERS\ndistapi.sys
0x00000000020350c8 HIDPARSE.SYS         0xf89b2000     0x7000 \SystemRoot\system32\DRIVERS\HIDPARSE.SYS
0x0000000002078108 flpydisk.sys         0xf8982000     0x5000 \SystemRoot\system32\DRIVERS\flpydisk.sys
0x0000000002085008 framebuf.dll         0xbff50000     0x3000 \SystemRoot\System32\framebuf.dll
0x00000000020858d8 redbook.sys          0xf877a000     0xf000 \SystemRoot\system32\DRIVERS\redbook.sys
0x0000000002085b10 serial.sys           0xf875a000    0x10000 \SystemRoot\system32\DRIVERS\serial.sys
0x0000000002086090 HIDCLASS.SYS         0xf88aa000     0x9000 \SystemRoot\system32\DRIVERS\HIDCLASS.SYS
0x00000000020a11d8 kbdclass.sys         0xf8942000     0x6000 \SystemRoot\system32\DRIVERS\kbdclass.sys
0x00000000020a6520 raspti.sys           0xf897a000     0x5000 \SystemRoot\system32\DRIVERS\raspti.sys
0x00000000020a6d78 swenum.sys           0xf8ba2000     0x2000 \SystemRoot\system32\DRIVERS\swenum.sys
0x000000000225f2f8 wanarp.sys           0xf888a000     0x9000 \SystemRoot\system32\DRIVERS\wanarp.sys
0x0000000002266e80 dxgthk.sys           0xf8d43000     0x1000 \SystemRoot\System32\drivers\dxgthk.sys
0x000000000227c0a8 termdd.sys           0xf880a000     0xa000 \SystemRoot\system32\DRIVERS\termdd.sys
[SNIP]
</pre>

Compared to modules output, modscan shows physical offset rather than virtual offset and the modules are not listed in their load order. Both modscan and modules displayed same modules, so modscan did not find any hidden modules. This doesn't necessarily mean that they wouldn't exist, since malware can have very advanced ways to hide its components. Brute force scanning PE headers from kernel memory is one way to find hidden rootkits. **Unloadedmodules** plugin is able to find plugins that have been recently unloaded. This works because kernel has a list of modules that have been recently unloaded for debugging purposes. Running unloadedmodules with Volatility 2:

<pre>
python2 vol.py -f ~/Documents/malware-samples/cridex.vmem --profile=WinXPSP2x86 unloadedmodules
Volatility Foundation Volatility Framework 2.6.1
Name                 StartAddress EndAddress Time
-------------------- ------------ ---------- ----
Sfloppy.SYS          0x00f8b92000 0xf8b95000 2012-07-22 02:42:30 
Cdaudio.SYS          0x00f898a000 0xf898f000 2012-07-22 02:42:30 
imapi.sys            0x00f885a000 0xf8865000 2012-07-22 02:42:31 
splitter.sys         0x00f8bcc000 0xf8bce000 2012-07-22 02:42:52 
swmidi.sys           0x00f8268000 0xf8276000 2012-07-22 02:42:52 
DMusic.sys           0x00f7b8f000 0xf7b9c000 2012-07-22 02:42:52 
aec.sys              0x00f7907000 0xf792a000 2012-07-22 02:42:52 
drmkaud.sys          0x00f8d1c000 0xf8d1d000 2012-07-22 02:42:52 
kmixer.sys           0x00f78dc000 0xf7907000 2012-07-22 02:42:57 
</pre>

Each row in output contains module name, kernel memory area (StartAddress - EndAddress) where the module was located and unloading time. Since the modules have been unloaded, they cannot be dumped from memory anymore, but their names are known so they can be potentially found from file system. 

### Dumping processes and drivers

At the last phase processes and drivers are dumped for further examination. **Procdump** plugin allows to dump a process executable. Process can be specified with *--pid* or physical offset *--offset* flag. *--offset* can also be used to dump hidden processes. Dumping explorer.exe and reader\_sl.exe by using *--pid*:

<pre>
python2 vol.py -f ~/Documents/malware-samples/cridex.vmem --profile=WinXPSP2x86 procdump --pid 1484,1640 -D proc-dumps
Volatility Foundation Volatility Framework 2.6.1
Process(V) ImageBase  Name                 Result
---------- ---------- -------------------- ------
0x821dea70 0x01000000 explorer.exe         OK: executable.1484.exe
0x81e7bda0 0x00400000 reader_sl.exe        OK: executable.1640.exe
</pre>

Taking 256 bit SHA hashes of the 2 binaries:

<pre>
sha256sum executable.1484.exe executable.1640.exe
48db195007e5ae9fc1246506564af154927e9f3fbfca0b4054552804027abbf2  executable.1484.exe
5b136147911b041f0126ce82dfd24c4e2c79553b65d3240ecea2dcab4452dcb5  executable.1640.exe
</pre>

VirusTotal hits for the binaries:

![Binary virustotal results](https://github.com/JYVSECTEC/PHR-model/blob/master/Triage-Respond/Investigations/Memory-Forensics/binary-virustotal-results.png?raw=true)

Since several AV vendors found the process binaries malicious, Cridex may have modified explorer.exe and reader\sl.exe or replaced them with a modified version. These processes memory can be dumped to disk using **memdump**, which extracts all pages accessible to a process and saves the acquired pages to disk. Running memdump to save explorer.exe's and reader\_sl.exe's memory to disk using Volatility 2: 

<pre>
python2 vol.py -f ~/Documents/malware-samples/cridex.vmem --profile=WinXPSP2x86 memdump --pid 1484,1640 -D proc-mem-dumps
Volatility Foundation Volatility Framework 2.6.1
************************************************************************
Writing explorer.exe [  1484] to 1484.dmp
************************************************************************
Writing reader_sl.exe [  1640] to 1640.dmp
</pre>

Strings program can be used to find text strings from binary files like executables. Using strings with grep to find domains or URLs from reader\_sl.exe's memory dump: 

<pre>
strings proc-mem-dumps/1640.dmp | grep -i "\.com\|\.net\|\.org\|http"
[SNIP]
*ubs.com*
*acbtz.com*
*dtbafrica.com*
*nab.com.au*
*us.hsbc.com*
*online.citibank.com/*
*ktt.key.com*
*cm.netteller.com*
http://188.40.0.138:8080/zb/v_01_a/in/cp.php
*account.authorize.net/*
[SNIP]
strings -a -e l proc-mem-dumps/1484.dmp | grep -i "\.com\|\.net\|\.org\|http"
[SNIP]
http://155.98.65.40:8080/zb/v_01_a/in/
http://184.106.189.124:8080/zb/v_01_a/in/
http://91.228.154.199:8080/zb/v_01_a/in/
http://110.234.150.163:8080/zb/v_01_a/in/
http://164.15.21.2:8080/zb/v_01_a/in/
http://91.121.103.143:8080/zb/v_01_a/in/
http://213.17.171.186:8080/zb/v_01_a/in/
http://59.90.221.6:8080/zb/v_01_a/in/
http://188.40.0.138:8080/zb/v_01_a/in/
http://216.24.197.66:8080/zb/v_01_a/in/
http://41.168.5.140:8080/zb/v_01_a/in/
http://125.19.103.198:8080/zb/v_01_a/in/
http://190.81.107.70:8080/zb/v_01_a/in/
http://211.44.250.173:8080/zb/v_01_a/in/
http://210.56.23.100:8080/zb/v_01_a/in/
http://85.214.204.32:8080/zb/v_01_a/in/
[SNIP]
</pre>

The first command output contained several bank domains, HTML, HTTP request headers and some URLs.  The second command that included some changes to encoding displayed even more URLs that the malware likely communicates with. Explorer.exe's memory dump also seems to contain the same IoCs.

Since this particular Cridex malware should not contain malicious kernel modules, there is no need to dump modules from the memory. If that was necessary, **moddump** plugin could be used to dump modules from memory for further analysis. Moddump requires *-D* flag to indicate where to dump the modules. Optional *-b* flag requires base address of a module to only dump that specific module. Dumping ntoskrnl.exe with Volatility 2 by specifying its base address with *-b* flag:

<pre>
python2 vol.py -f ~/Documents/malware-samples/cridex.vmem --profile=WinXPSP2x86 moddump -b 0x804d7000 -D kernel-modules
Volatility Foundation Volatility Framework 2.6.1
Module Base Module Name          Result
----------- -------------------- ------
0x0804d7000 ntoskrnl.exe         OK: driver.804d7000.sys
</pre>

### References

<ul>
    <li>Ligh, M.H., Case, A., Levy, J. & Walters, A. 2014. The Art of Memory Forensics. Indianapolis: John Wiley & Sons. (Must have book for anyone interested in memory forensics)</li>
    <li>https://github.com/volatilityfoundation/volatility/wiki/Command-Reference</li>
    <li>https://volatility3.readthedocs.io/en/v1.0.1/</li>
    <li>https://www.bleepingcomputer.com/startups/reader_sl.exe-175.html</li>
    <li>https://studylib.net/doc/8737790/blackhole-exploit-kit--banking-trojans-and-ach</li>
    <li>https://www.howtogeek.com/401365/what-is-the-ntuser.dat-file/</li>
    <li>https://github.com/volatilityfoundation/volatility/wiki/Command-Reference-Mal</li>
    <li>https://en.wikipedia.org/wiki/Strings_(Unix)</li>
</ul>
