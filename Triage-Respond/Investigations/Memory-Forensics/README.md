# Memory Forensics

Memory forensics is a sub category of digital forensics. In memory forensics, volatile memory like RAM is analysed. Volatile memory can be analysed by taking memory dump of a system's RAM while the system is active. Memory dump is a static capture of the RAM at that moment when the dump was taken. The dump contains data kept in RAM like processes, internet connections, kernel drivers, Windows registry data etc. The data in dump can be analysed by using different tools like Volatility Framework, which is introduced later in this documentation.

### Random Access Memory (RAM) 

RAM is fast memory, which contains all the programs running in the system like operating system and its data. RAM is a volatile memory, which means that when the system loses power, all the data in RAM is lost. This is why RAM is not used as permanent storage for data, but rather for information that is not needed after system is rebooted.

### Dumping memory

Because RAM is continuously changing volatile memory, it has to be saved to hard disk before it can be analysed. There are many different tools for capturing RAM and the tool used should be decided based on the targeted system. Some of the tools may only support certain versions of operating system. If you are going to capture an actual evidence, it is important to choose right tools and use them correctly or the evidence may end up corrupted.

Data in RAM may also be saved in hard drive as hibernation or paging file. System crashes may also create crash dumps, which contain data from RAM. Before system goes into hibernation state, data in RAM is saved into hibernation file. When system returns from hibernation state, the data in hibernation file is copied back to RAM, so the system will return to the same state as it was before going to hibernation state. In Windows systems hibernation file is called Hiberfil.sys and the system cannot go into hibernation state if the file does not exist.

## Volatility Framework

Volatility Framework contains several different tools for investigating memory dumps. Tools are written with Python language and they are open source. Source code is maintained by [Volatility Foundation](https://www.volatilityfoundation.org/). Volatility is a command line tool and it can be used to analyse 32- and 64-bit memory dumps taken from Windows, Linux and Mac systems.

### Volatility 2

Latest Volatility tool version is 3. It does not yet atleast contain all the plugins that [Volatility 2](https://github.com/volatilityfoundation/volatility) has. Volatility 2 requires user to give appropriate kernel symbol profile matching system where the dump was taken from. This way Volatility 2 knows the data structures, algorithms and symbols to use when handling the dump file. Volatility 2 contains plugin called imageinfo, which can be used to determine right profile for dump. Here is an example of using it to find out appropriate profile for dump:

```
python2 vol.py -f mem.dmp imageinfo

Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_24000, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_24000, Win7SP1x64_23418
                     AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/user/volatility/mem.dmp)
                      PAE type : No PAE
                           DTB : 0x187000L
                          KDBG : 0xf80002a03110L
          Number of Processors : 4
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0xfffff80002a04d00L
                KPCR for CPU 1 : 0xfffff880009ee000L
                KPCR for CPU 2 : 0xfffff88002f69000L
                KPCR for CPU 3 : 0xfffff88002fdf000L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2019-12-20 06:35:42 UTC+0000
     Image local date and time : 2019-12-19 22:35:42 -0800
```

Program output shows that the plugin suggested 8 different profiles for the dump. As you can see, each profile is named to describe the operating system version. Now that we know profiles that may match the dump system, other plugins can be ran to the dump. To find out processes that ran on the system when the dump was taken, pslist plugin can be used:

```
python2 vol.py -f mem.dmp --profile=Win7SP1x64 pslist

Volatility Foundation Volatility Framework 2.6.1
Offset(V)          Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit                          
------------------ -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ ------------------------------
0xfffffa8000c3bb10 System                    4      0     93      366 ------      0 2018-12-20 05:28:24 UTC+0000                                 
0xfffffa8001692b10 smss.exe                236      4      2       32 ------      0 2018-12-20 05:28:24 UTC+0000                                 
0xfffffa80021c2930 csrss.exe               320    304     10      535      0      0 2018-12-20 05:28:25 UTC+0000                                 
0xfffffa8002426060 wininit.exe             372    304      3       85      0      0 2018-12-20 05:28:25 UTC+0000                                 
0xfffffa80024255d0 csrss.exe               384    364     10      268      1      0 2018-12-20 05:28:25 UTC+0000                                 
0xfffffa800248a790 services.exe            428    372      9      247      0      0 2018-12-20 05:28:25 UTC+0000                                 
0xfffffa80024a3b10 lsass.exe               444    372     10      592      0      0 2018-12-20 05:28:26 UTC+0000                                 
0xfffffa80024a56f0 lsm.exe                 452    372      9      144      0      0 2018-12-20 05:28:26 UTC+0000                                 
0xfffffa80024867d0 winlogon.exe            512    364      4      120      1      0 2018-12-20 05:28:26 UTC+0000 
...
```

The output contains lot of information about the processes like their names, virtual offsets, PIDs, PPIDs, start times etc. Volatility 2 contains many other plugins. Entire list of them and their description can be found from Volatility 2 GitHub [repo](https://github.com/volatilityfoundation/volatility).

### Volatility 3

[Volatility 3](https://github.com/volatilityfoundation/volatility3) contains improvements compared to Volatility 2. E.g. Volatility 2 profiles are called SymbolSpace and the 3rd version is also faster compared to 2nd. Users no longer need to indicate profile file when running Volatility 3. When analyzing Windows dumps, Volatility automaticly gets necessary symbol file from Microsoft symbol server. This requires internet connection. Mac and Linux symbol files have to be created manually using tool called [dwarf2json](https://github.com/volatilityfoundation/dwarf2json). Otherwise Volatility 3 usage is very similar to Volatility 2. E.g. running pslist plugin:

```
python3 vol.py -f mem.dmp windows.pslist.PsList

PID	PPID	ImageFileName	Offset(V)	Threads	Handles	SessionId	Wow64	CreateTime	ExitTime	File output

4	0	System	0xfa8000c3bb10	93	366	N/A	False	2018-12-20 05:28:24.000000 	N/A	Disabled
236	4	smss.exe	0xfa8001692b10	2	32	N/A	False	2018-12-20 05:28:24.000000 	N/A	Disabled
320	304	csrss.exe	0xfa80021c2930	10	535	0	False	2018-12-20 05:28:25.000000 	N/A	Disabled
372	304	wininit.exe	0xfa8002426060	3	85	0	False	2018-12-20 05:28:25.000000 	N/A	Disabled
384	364	csrss.exe	0xfa80024255d0	10	268	1	False	2018-12-20 05:28:25.000000 	N/A	Disabled
428	372	services.exe	0xfa800248a790	9	247	0	False	2018-12-20 05:28:25.000000 	N/A	Disabled
444	372	lsass.exe	0xfa80024a3b10	10	592	0	False	2018-12-20 05:28:26.000000 	N/A	Disabled
452	372	lsm.exe	0xfa80024a56f0	9	144	0	False	2018-12-20 05:28:26.000000 	N/A	Disabled
512	364	winlogon.exe	0xfa80024867d0	4	120	1	False	2018-12-20 05:28:26.000000 	N/A	Disabled
```

From the command we can see that plugin naming convention is a bit different in Volatility 3. There is a difference atleast in column names and their order in plugin output compared to pslist in Volatility 2, but the plugin output is still mostly same as in Volatility 2.

More information about memory analysis and Volatility plugins can be found from [this documentation](https://github.com/JYVSECTEC/PHR-model/blob/master/Triage-Respond/Investigations/Memory-Forensics/Analyzing-memory-dump.md).

### References

<ul>
    <li>https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6113291</li>
    <li>https://docs.microsoft.com/en-us/troubleshoot/windows-client/deployment/disable-and-re-enable-hibernation</li>
    <li>http://homepage.cem.itesm.mx/carbajal/Microcontrollers/ASSIGNMENTS/readings/ARTICLES/barr01_memory_types.pdf</li>
    <li>https://volatility3.readthedocs.io/_/downloads/en/latest/pdf/</li>
</ul>
