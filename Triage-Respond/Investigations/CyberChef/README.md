CyberChef is really powerful tool which runs on browser.
At basic level it is just graphic tool for comparing files, defanging urls, doing file comparisons, calculating hashes, sorting data, converting data from one format to other and encoding/decoding etc.
But you can start by combining functions together, and create ready made recipes, you can share these recipes or use those again for same kind of data.

 

 

 

But real power of CyberChef relies on deobfuscation; many malware, scripts etc... are obfuscated so that anti-virus software can't detect those, and to make harder to find out what those malwares does, which is making triage hard... You can easily start deobfuscating files with Cyber Chef to find those really precious IOCs from files, like ip-addresses, file locations, hashes of actual malware, so you know what these malicious files does.

 

 
And you can then re-use your recipes with other files, or with colleques so they can verify your findings.

 


Examples:
During investigation you might find malicious file, with Cyberchef it is easy to pick up URLs from malicious code, if code is plain text.
If code is obfuscated, then we can try to manipulate code with know technics to deobfuscate it. 
Sometimes to get fast results, we just deobfuscate malicious file, then without further investigation, we can calculate hash value for that file, and compare that to know virus hashes. This migth reveal us what this virus is about, even before further code investigation.
It is also useful to be able to defang ULRs when sharing investigation data to others (maybe investigators or even to director?), so that no-one can accidentally go to suspicious URL.
 





Use case: Suspicious file?

In this example lets assume that we have found suspicious file during investigation, which just includes hexadecimals:

 


Example file looks like this (Not actually malicious file, created just for this example):   

  71 6e 76 64 73 72 69 64 6d 6d 21 2c 42 6e 6c 6c 60 6f 65 21 23 29 4f 64 76 2c 4e 63 6b 64 62 75 21 4f 64 75 2f 56 64 63 42 6d 68 64 6f 75 28 2f 45 6e 76 6f 6d 6e 60 65 47 68 6d 64 29 26 69 75 75 71 72 3b 2e 2e 66 68 75 69 74 63 2f 62 6e 6c 2e 4b 58 57 52 44 42 55 44 42 2e 51 49 53 2c 6c 6e 65 64 6d 2e 73 60 76 2e 6c 60 72 75 64 73 2e 51 73 64 71 60 73 64 5e 49 74 6f 75 5e 53 64 72 71 6e 6f 65 5e 51 6e 72 75 64 73 2f 71 65 67 26 2d 21 26 51 73 64 71 60 73 64 5e 49 74 6f 75 5e 53 64 72 71 6e 6f 65 5e 51 6e 72 75 64 73 2f 71 65 67 26 28 23 
 

If we put it on cybechef, it actually detect that if you use "From hex" function it will produce somethign readable, so lets try that:  
```
qnvdsridmm!,Bnll`oe!#)Odv,Nckdbu!Odu/VdcBmhdou(/Envomn`eGhmd)&iuuqr;..fhuitc/bnl.KXWRDBUDB.QIS,lnedm.s`v.l`ruds.Qsdq`sd^Itou^Sdrqnoe^Qnruds/qeg&-!&Qsdq`sd^Itou^Sdrqnoe^Qnruds/qeg&(#
```

 

hmm... not too helpful... lets try XOR brute forcing to see if we get anything out of that:  
```
Key = 01: powershell -Command "(New-Object Net.WebClient).DownloadFile('https://github.com/JYVSECTEC/PHR-model
Key = 02: sltfqpkfoo#.@lnnbmg#!+Mft.Laif`w#Mfw-Tfa@ojfmw*-GltmolbgEjof+$kwwsp9,,djwkva-`ln,IZUPF@WF@,SKQ.nlgfo
Key = 03: rmugpqjgnn"/Amooclf" *Lgu/M`hgav"Lgv,Ug`Ankglv+,FmulnmcfDkng*%jvvrq8--ekvjw`,amo-H[TQGAVGA-RJP/omfgn
Key = 04: ujr`wvm`ii%(Fjhhdka%'-K`r(Jgo`fq%K`q+R`gFil`kq,+AjrkijdaCli`-"mqquv?**blqmpg+fjh*O\SV@FQ@F*UMW(hja`i
Key = 05: tksavwlahh$)Gkiiej`$&,Jas)Kfnagp$Jap*SafGhmajp-*@ksjhke`Bmha,#lpptw>++cmplqf*gki+N]RWAGPAG+TLV)ik`ah
Key = 06: whpbutobkk'*Dhjjfic'%/Ibp*Hembds'Ibs)PbeDknbis.)ChpikhfcAnkb/ osswt=((`nsore)dhj(M^QTBDSBD(WOU*jhcbk
Key = 07: viqctuncjj&+Eikkghb&$.Hcq+Idlcer&Hcr(QcdEjochr/(Biqhjigb@ojc.!nrrvu<))aornsd(eik)L_PUCERCE)VNT+kibcj
Key = 08: yf~l{zalee)$Jfddhgm)+!Gl~$Fkclj})Gl}'^lkJe`lg} 'Mf~gefhmO`el!.a}}yz3&&n`}a|k'jfd&CP_ZLJ]LJ&YA[$dfmle
Key = 09: xg.mz{`mdd(%Kgeeifl(* Fm.%Gjbmk|(Fm|&_mjKdamf|!&Lg.fdgilNadm /`||x{2''oa|`}j&kge'BQ^[MK\MK'X@Z%eglmd
Key = 0a: {d|nyxcngg+&Hdffjeo+)#En|&Dianh.+En.%\niHgbne."%Od|egdjoMbgn#,c..{x1$$lb.c~i%hdf$AR]XNH_NH$[CY&fdong
```

 

Ok it seems that with key = 01 it is plain text and ity runs powershell

 

So lets XOR it with 01:
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://github.com/JYVSECTEC/PHR-model/raw/master/Prepare_Hunt_Respond_Poster.pdf', 'Prepare_Hunt_Respond_Poster.pdf')"

 

Lets extract urls:   
'https://github.com/JYVSECTEC/PHR-model/raw/master/Prepare_Hunt_Respond_Poster.pdf'

 

now if we would want to report this url so that reader cant accidentally click it, we would use use defanging:  
hxxps[://]github[.]com/JYVSECTEC/PHR-model/raw/master/Prepare_Hunt_Respond_Poster[.]pdf'

 

defanging is really useful, specially if we use instant message applications, where there is "preview-mode" for websites... Because if you change IOC information with other investigators from there, without defanging, attackers can see that instant message application is connecting to that URL 

 

Recipe: 
```  
From_Hex('Auto')
XOR_Brute_Force(1,100,0,'Standard',false,true,false,''/disabled)
XOR({'option':'Hex','string':'1'},'Standard',false)
Extract_URLs(false)
Defang_URL(true,true,true,'Valid domains and full URLs')
``` 
You can try this by yourself:



	
go to https://gchq.github.io/CyberChef/
	copy this to input data  
	71 6e 76 64 73 72 69 64 6d 6d 21 2c 42 6e 6c 6c 60 6f 65 21 23 29 4f 64 76 2c 4e 63 6b 64 62 75 21 4f 64 75 2f 56 64 63 42 6d 68 64 6f 75 28 2f 45 6e 76 6f 6d 6e 60 65 47 68 6d 64 29 26 69 75 75 71 72 3b 2e 2e 66 68 75 69 74 63 2f 62 6e 6c 2e 4b 58 57 52 44 42 55 44 42 2e 51 49 53 2c 6c 6e 65 64 6d 2e 73 60 76 2e 6c 60 72 75 64 73 2e 51 73 64 71 60 73 64 5e 49 74 6f 75 5e 53 64 72 71 6e 6f 65 5e 51 6e 72 75 64 73 2f 71 65 67 26 2d 21 26 51 73 64 71 60 73 64 5e 49 74 6f 75 5e 53 64 72 71 6e 6f 65 5e 51 6e 72 75 64 73 2f 71 65 67 26 28 23  
	
Load this recipe:
```
From_Hex('Auto')
XOR_Brute_Force(1,100,0,'Standard',false,true,false,''/disabled)
XOR({'option':'Hex','string':'1'},'Standard',false)
Extract_URLs(false)
Defang_URL(true,true,true,'Valid domains and full URLs')
```
