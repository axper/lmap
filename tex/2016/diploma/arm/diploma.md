Սերվերային համակարգերում անվտանգությունը գնահատող ծրագրի մշակում
================================================================

Հապավումներ
===========

- Lmap - Լոկալ Nmap
- TCP - Փոխանցման կառավարման հաղորդակարգ
- UDP - Օգտագործողի դատագրամ հաղորդակարգ
- IDS - Ներխուժում հայտնաբերող համակարգ
- psutil - python system and process utilities

Ներածություն
============

Ինչու է տեղեկատվական անվտանգությունը կարևոր
-------------------------------------------

### Ի՞նչ է տեղեկատվական անվտանգությունը

Տեղեկատվական անվտանգությունը տեղեկատվական ռեսուրսների չլիազորված օգտագործման
կանխման և հայտնաբերման պրոցեսն է։ [23]

Կանխումը չարամիտ չլիազորված անձանց (նաև ասում են «հակառակորդներ»,
«հարձակվողներ», «ներխուժողներ», «հաքերներ») կողմից ծրագրային ապահովման կամ
տվյալների որոշ մասի օգտագործման դեմ ուղղված միջոցառումներ համակարգն է։

Հայտնաբերումը չլիազորված մուտքի փորձի առկայության ստուգման պրոցեսն է։ Եթե
նման փորձ առկա է, ապա նաև՝ արդոք այն հաջողվել է, և թե կոնկրետ ինչ է տեղի
ունեցել։ [20]

### Ինչու՞ պետք է հոգալ տեղեկատվական անվտանգության մասին

Այսօր համակարգիչները և էլեկտրոնային տեխնիկան օգտագործվում են
կյանքի գրեթե բոլոր ոլորտներում։ Բանկային համակարգի ու ներդրումների ոլորտից
մինչև գնումների և հեռահաղորդակցության ոլորտ համակարգիչները դարձել են
յուրաքանչյուր բիզնեսի անբաժանելի մասը։ Դժվար է նշել մի ոլորտ, որը
օգուտ չի քաղել տեղեկատվական տեխնոլոգիաների բուռն զարգացումից։

Չնայած ընկերությունների կողմից պահվող ոչ բոլոր տվյալները կարելի է
դասակարգել որպես «հույժ գաղտնի», ցանցային ադմինիստրատորները հավանաբար
չեն ուզենա որ անծանոթ անձինք նայեն իրենց բիզնեսի ներքին հաղորդակցությանը,
իրենց անձնական ինֆորմացիային, և փոփոխություններ կատարեն իրենց վստահված
համակարգերում։

### Ինչու՞ ինչ֊որ մեկը կցանկանա կոտրել որոշակի համակարգ

Attackers often do not care about about a user's or organization's identity.
Having control of a server not only puts the organization at a risk, but also visitors of the website. Attackers can also
use a compromised server to launch attacks on other organizations without discovering their true identity.
Having control over compromised server helps attackers carry out DDoS attacks.
An attacker has several reasons to break into a server:

* Monetary gain - Stealing details of your bank account and credit card
* Business disruption - An organization might pay hackers to cause chaos in their rival's network
* Information leakage - An organization might pay hackers to gain competitive advantage over a rival company by accessing it's secrets
* DDoS - To carry out distributed denial of service (DDoS) attacks on other servers
* SEO - A hacked website might be used to increase SEO of other sites by placing links to that site on the hacked website
* Base for further attacks - A hacked server might be used for broader attacks, having more servers helps them cover their true identity
* Fun - An attacker might do it for fun or amusement

Aspects of server security
--------------------------

Information security remains one of the most important issues businesses have to tackle today.[21]

1. Remove unnecessary services
Default operating system installations and configurations, are not secure. Many default services are installed, but not used,
such as print servers, samba shares etc. These services increase the attack surface by opening more ways for the
malicious user to abuse the system.

Administrators must disable or secure all unnecessary services via firewall.

2. Remote access
Connecting to the server using an unsecured, public network connection makes it possible for hackers to perform
attacks such as man-in-the-middle and data stealing.

Administrators must make sure that all remote connections to the servers are secured properly using encryption and
security tokens.

5. Permissions and privileges
Proper permissions management has an important role in server security. If a malicious user or process is given more privileges
than he needs to carry out his job, he can use that to compromise the server.

Administrators must make sure that all system users have only access to files and resources which are required to carry out their job.

6. Installing security updates on time
It is important to update the operating system and and the software with latest updates and security patches.
While installing updates can be somewhat dangerous, in means that it might introduce stability issues, administrators
must ensure that they are installed in a timely manner.

7. Monitoring and log audit
Logs are produces by every piece of software - the operating system, web applications, all kinds of services, databases, network, routers, switches etc.

These logs must be monitored and frequently checked, because logs can often indicate an upcoming attack. Even in case
of a successfully compromised system logs server as the only way to perform forensic analysis.

8. User accounts
Unused user accounts, such as of a laid off employee should be disabled along with accounts created by various services.

Every administrator accessing the server needs to have his own account and his own password, and correct privileges. Passwords should not be shared.

9. Remove unused modules and extensions
Applications such as web servers often contain a number of pre-defined default extensions and modules.
These modules can contain vulnerabilities and can increase the possible attack surface for the attacker.

Administrators must ensure that, whenever possible, only modules required by the web application are enabled.

11. Stay informed
Nowadays information about software and operating system, including security can be found freely on the internet.

Administrators must make sure that they and the users are constantly informed about latest news about attacks and vulnerabilities.

12. Use security scanners
Scanners are pieces of software which help automate and ease the process of securing a server and applications.

Software static/dynamic analysis tools such as Sonar for java, Valgrind for C etc help find bugs and vulnerabilities early
in application lifecycle.
Network security scanners help administrators to ensure the security of their servers. These tools are able to find open ports, 
vulnerable services and even viruses.
A list of well known network scanners includes:
    1. Nmap
    2. Nessus
    3. Accunetix

13. Choose proper encryption and hashing algorithms
Use of broken encryption, communication and hashing protocols such as DES, SSL, MD5 should be avoided.

Weaknesses of these algorithms opens an attack vector for an attacker to exploit them.
































## Սերվերային համակարգերում խոցելիությունների հայտնաբերման ներկայիս մոտեցումը
Համակարգերի ադմինիստրատորների առօրյա խնդիրներից է իրենց վստահված համակարգերում պորտ սկանավորման իրականացումը։
Պորտ սկանավորումը օգնում է ադմինիստրատորին հայտնաբերել խոցելիություններ, նախքան դա կարվի հնարավոր հակառակորդի կողմից։
Նման սկանավորման համար ադմինիստրատորները օգտագորում են ծրագրային փաթեթներ ինչպիսիք են՝ nmap, nessus, accunetix և այլն։

Պորտ սկանավորման պրոցեսը սովորաբար անցնում է հետևյալ փուլերով՝

1. Ադմինիստրատորը որոշում է սկանավորելիք հասցեների և պորտերի միջակայքը
2. Նա տալիս է ծրագրին վերոնշյալ տվյալները և գործարկում է ծրագիրը
3. Ծրագիրը փորձարկում է բոլոր հնարավոր IP հասցենե ֊ պորտ համակցությունները
4. Եթե հայտնաբերովում է, որ պորտը բաց է, հատուկ հարցումների շարք է ուղարկվում, որոնց միջոցով ծրագիրը փորձում է գուշակել
թե կոնկրետ ինչ սերվիս է լսում նշված պորտի տակ և նրա մանրամասները (տարբերակ, կոնֆիգուրացիան և այլն)
5. Արդյունքների մասին հաշվետվությունը նեկայացվում է ադմինիստրատորին նախընտրած ֆորմատով (xml, console output, html)

Սակայն նման մոտեցումը ունի որոշակի թերություններ՝

- Յուրաքանչյուր IP հասցոի յուրաքանչյուր TCP և UDP պորտ սկանավորելը պահանջում է երկար ժամանակ
- Սկանավորումը գրավում է ցանցային ռեսուրսները և հնարավոր է որոշ համակարգեր անօգտագործելի դառնան սկանավորման ընթացքում
- Որոշ իրավիճակներում սկանավորումը կարող է անտեղի տագնապի ազդանշան առաջացնել ներխուժում հայտնաբերող համակարգերում։
- Հնարավոր են կեղծ դրական արդյունքներ և սխալ սերվիսների նույնականցումներ
- Եթե սերվիսը աշխատում է անսովոր պորտի տակ, ապա այն հնարավոր է չհայտնաբեվի թռուցիկ սկանավորման եղանակով։

## Այլընտրանք
Այս աշխատությունում մենք ներկայացնում ենք սերվերների խոցելիությունների գնահատման այլընտրանքային եղանակ։ Այն սկանավորում է
համակարգերը ներսից։

Այս ծրագրի գործունեության եղանակը որոշ չափով նման է Microsoft Baseline Security Analyzer ծրագրին:

Ծրագիրը մտածելու տեղ է տալիս օգտագործողին, պարզապես նրան ներկայացնելով նրան փաստեր համակարգի մասին։

Ծրագիրը ավտոմատ եղանակով սկանավորում է համակարգում աշխատող սերվիսները բազմաթիվ հայտնի խոցելիությունների հետ համեմատելով
դրանց կոնֆիգուրացիոն ֆայլեը։

# Ինչպես է այն աշխատում
Սկզբում ծրագիրը հայտնաբերում է համակարգում բոլոր բաց TCP և UDP պորտերը: Հետո յուրաքանչյուր բաց պորտի համար ծրագիրը
սկանավորում է նրա կոնֆիգուրացիոն ֆայլը հայտնի սխալ կարգաբերումների, դատարկ/թույլ գաղտնաբառերի և այլ խոցելիությունների
առկայության համար և հաշվետվություն է ներկայացնում օգտագործողին։

Բացի հայտնաբերելուց թե որոշակի պորտ բաց է թե ոչ, ծրագիրը ստուգում է թե արդյոք այն կասեցված է firewall-ով։

# Տարածվակ կարգաբերման սխալներ
- Դատարկ գաղտնաբառեր
- Սխալ կարգաբերումներ, որոնք կարող են առաջացնել օրինակ՝ path traversal գրոհներ
- Հին/կոտրված հեշերի և գաղտնագրման ալգորիթմների օգտագործում

# Թարմացումներ
Ծրագրի այս հատվածը ստուգում է թե արդյոք համակարգը վերջերս թարմացվել է։ Եթե վերջին թարմացման ժամանակը ուշ է քան նախատեսված է
այս ծրագրի կարգաբերման ֆայլում, օգտագործողը ստանում է նկատողություն։

## Debian/APT-ի վրա հիմնված համակարգեր
[8] Ծրագիրը ստուգում է `/var/cache/apt/` պանակի մեջ վերջին գրման ժամանակը, որպեսզի հայտնաբերի `sudo apt-get update`
հրահանգի վերջին կատարման ժամնակը։

## Red Hat/YUM-ի վրա հիմնված համակարգեր
[9] Ծրագիրը ստուգում է `sudo yum update` հրահանգի կատարման վերջին ժամկետը, վերլուծելով `yum history` հրահանգի
արդյունքը։

## Arch/Pacman֊ի վրա հիմնված համակարգեր
[10] Ծրագիրը ստուգում է `sudo pacman -Syu` հրահանգի վերջին կատարման ժամանակը, վերլուծելով `/var/lob/pacman.log` ֆայլը։

# Root օգտագործողի անմիջական օգտագործում
Եթե օգտագործողը համակարգ է մտել որպես root, կամ ունի ադմինիստրատորի իրավասություններ, ապա ծրագիրը զգուշացնում է օգտագործողին։

Ծրագիրը հաշվի է առնում այն դեպքը, երբ ինքը գործարկվել է `sudo` հրահանգի օգտագործմամբ, և այդ դեպքւմ զգուշացում չի կատարվում։

# Դատարկ գաղնտաբառեր
Այն պարագայւմ երբ համակարգը արտաքինից հասանելի է այնպիսի սերվիսների կողմից, որոնք օգտագործում են տեղային Linux օգտագործողներին
վավերականցման համար, ապա ծրագիրը ստուգում թե արդյոք բոլոր առկա Linux օգտագործողները ունեն ոչ դատարկ գաղնտաբառ։ Սա կատարվում է
հետևյալ հրամանաի օգնությամբ՝

    awk -F: '($2=="") {print}' /etc/shadow

## Ստուգում որ բոլոր ոչ root օգտագործողների UID-n 0 է

[15]

   awk -F: '($3 == "0") {print}' /etc/passwd

# Սերվիսներ

## SSHd
SSH սերվերի կոնֆիգուրացիոն ֆայլը տեղակայված է՝

- /etc/ssh/sshd_config

1. Ամենավտանգավոր կարգաբերման սխալներից է SSH v1 տարբերակի արձանագրության օգատգործումը։ Այս խոցելիութունը նախկինուոմ
խոցվել է WOOT պրոյեկտ կոչվող հաքերային խմբի կողմից։
2. Ստուգում որ գաղտնաբառով մուտք չի թույլատրվում։ Այս ստուգումը կատարվում է սկանավորելով SSH կարգաբերման ֆայլը հետևյալ
տողի առկայության համար՝

    PasswordAuthentication no

## MySQL
MySQL-ը ամենատարածված ռելացիոն բազաներից է աշխարհում[4]
Ծրագիրը սկանավորում է հետևյալ կոնֆիգուրացիոն ֆայլերը սխալների համար՝

- /etc/my.cnf
- /etc/mysql/my.cnf
- ~/.my.cnf

## Telnet
Եթե հայտնաբերվում է աշխատող telnet սերվեր, ապա օգտագործողը զգուշացվում է։

## FTP
Եթե FTP սերվիս է աշխատում, որը անանուն և միայն կարդացվող չե, ապա օգտագործողը զգուշացվում է FTP արձանագրության օգտագործման
դեմ։ FTP արձանագրությունը ապահով չէ, քանի որ գաղտնաբառը ուղարկվում է բացիեբաց։
If running FTP daemon is not:

# Apache HTTPD

# Requirements
Ծրագրի աշխատանքի համար անհրաժեշտ է՝

- Python 3.5.1
- psutil library

# Sources:
[1]http://sectools.org/
[2]https://docs.python.org/2/library/socket.html
[3]https://pythonhosted.org/psutil/
[4]http://db-engines.com/en/ranking
[5]http://www.yolinux.com/TUTORIALS/LinuxTutorialInternetSecurity.html
[6]http://www.yolinux.com/TUTORIALS/LinuxTutorial-woot-project.html
[7]http://www.iss.net/threats/advise100.html
[8]http://serverfault.com/questions/20747/find-last-time-update-was-performed-with-apt-get
[9]http://serverfault.com/questions/389650/how-to-check-when-yum-update-was-last-run
[10]https://bbs.archlinux.org/viewtopic.php?id=150428
[11]https://www.digitalocean.com/community/tutorials/7-security-measures-to-protect-your-servers
[12]http://askubuntu.com/questions/16178/why-is-it-bad-to-login-as-root
[13]http://www.tecmint.com/linux-server-hardening-security-tips/
[14]https://www.digitalocean.com/community/tutorials/an-introduction-to-securing-your-linux-vps
[15]http://www.cyberciti.biz/tips/linux-security.html
