# Unit 4 Lecture: Chapter 8

Securing Information Systems

Imagine

What does cybersecurity mean?

As societies become more dependent on computers and information systems, firms and other organizations, especially government agencies, need to make significant investment in their systems in order to make them less vulnerable and more reliable.. The threats are real, but the solutions to date have only been partial at best, and at worse, not up to the task of providing Internet security for individuals or business firms.

 [link: #fragment-1] 8.1

 [link: #fragment-2] 8.2

 [link: #fragment-3] 8.3

 [link: #fragment-4] 8.4

 [link: #fragment-5] 8.5

 [link: #fragment-6] Review Questions

8.1 Why are information systems vulnerable to destruction, error, and abuse?

As firms become more technologically oriented, they must become more aware of security and control issues surrounding their information systems and protect the resources more stringently than ever before. It’s that simple.

8.1.1 Why Systems Are Vulnerable

Information systems are vulnerable to technical, organizational, and environmental threats from internal and external sources. The weakest link in the chain is poor system management. If managers at all levels don’t make security and reliability their number one priority, then the threats to an information system can easily become real. The figure below gives you an idea of some of the threats to each component of a typical network.  

Figure 8.1: Contemporary Security Challenges and Vulnerabilities

Businesses that partner with outside companies are more vulnerable because at least some data may be less controlled. Partnering companies may not protect information as stringently. Hardware and software safeguards may not be as important to outsiders. Employees of the partnering firm may not view security as diligently as the primary business.

In today’s business environment, it’s not enough to protect hardware and software physically located within an organization. Mobile computing devices such as smartphones, cell phones, netbooks, and laptops, add to the vulnerability of information systems by creating new points of entry into information systems. There are more than one million apps for Apple mobile computing devices and 800,000 apps for Droid-based devices. Even though most of these small software programs are well-constructed, some could potentially threaten corporate networks.  

8.1.1.1 Internet Vulnerabilities

“When your hotel automatically emails you your booking information, there's a good chance that you're not the only person with access to those documents.

Symantec, a security company, found flaws on hundreds of hotel websites, which were leaking sensitive information like names, phone numbers, passport numbers and addresses in confirmation emails.

Candid Wueest, a threat researcher at Symantec, said he looked at more than 1,500 hotel websites in 54 countries and found the issues among two-thirds of them.

Hotels are a primary target for cyberattacks, as they hold treasure troves of data on guests during vacation season. They are frequently hacked, as cyberattacks on Sheraton, Westin,  [link: https://www.cnet.com/news/starwood-marriott-and-hyatt-hotels-hit-by-malware-leaving-customer-card-data-exposed/] Starwood, Marriott and  [link: https://www.cnet.com/news/ftc-sues-wyndham-hotels-over-data-breaches/] Wyndham hotels over the last few years show. Last November, Marriott disclosed that hackers had stolen records from up to 383 million guests in one of the  [link: https://www.cnet.com/news/marriott-says-hackers-stole-more-than-5-million-passport-numbers/] largest personal data breaches in history.

Hotels have a hotbed of data, and their websites have been leaking out that information, Wueest said. One major issue stems from the URL that they send to guests in emails. About 850 hotel websites don't require authentication to see those details, allowing anyone with the link to view your personal information. Nearly one-third of those pages have the booking number in the URL itself, Wueest found.

If the guest were the only person who could view that URL, it wouldn't be much of an issue, but these websites have advertisers and third-party analytics tools embedded on the pages.

Those third parties get that URL too, and a potential attacker could gather that information for malicious purposes, researchers found. Wueest said he found a Google Analytics request for a hotel booking confirmation page contained a URL with the reservation number in plain sight.

All an attacker would have to do with that is enter the reservation number and find out all the sensitive information tied to it.” (Your hotel check-in confirmation could be putting you at risk,  [link: http://www.cnet.com] www.cnet.com, Ng, Alfred, April 10, 2019)

As this article shows, every  point of entry into the Internet network is a point of vulnerability. It takes a combination of businesses, users, and Internet Service Providers to increase security and together, work to prevent problems.

If you connect to the Internet with a cable modem or DSL you are much more vulnerable to hackers on your home PC than if you connect with a dial-up modem. That’s because you are always connected, with a permanent IP address, which makes it easier for hackers to find you. The only smart thing to do is keep your software up-to-date and include firewall protection.

Because distributed computing is used extensively in network systems, you have more points of entry, which can make attacking the system easier. The more people you have using the system, the more potential for fraud and abuse of the information maintained in that system. That’s why you have to make it everybody’s business to protect the system. It’s easy for people to say that they are only one person and therefore they won’t make much difference. But it only takes one person to let down the necessary safeguards in order for one other person to disable a system or destroy data.

8.1.1.2 Wireless Security Challenges

It’s a difficult balancing act when it comes to making wireless systems easy to access and yet difficult to penetrate. Internet cafes, airports, hotels, and other hotspot access points need to make it easy for users to use WiFi systems, generally by providing encryption free, no-password connections.  This allows hackers to access unsuspecting users’ systems and steal data or use the entry point as a way to spread malicious programs. The hackers can use war driving techniques to gain access to wireless networks not only in hotels and airports, but private businesses and government centers.

Wireless networks are vulnerable in the following ways:

Radio frequency bands are easy to scan.

Signals are spread over a wide range of frequencies.

Service set identifiers (SSID) are broadcast multiple times and are easily picked up.

Rogue access points can be established on different radio channels and divert signals from authentic points.

Wired equivalent privacy (WEP) isn’t very effective because it relies on user input.

 

8.1.2 Malicious Software: Viruses, Worms, Trojan Horses, and Spyware

Web-enabled and e-mail-enabled cell phones are now being targeted as a way to spread viruses, or more accurately, malware as the article below explains.

“A common question posed by IT managers is whether or not they should be installing anti-virus software on enterprise smartphones. Like almost all security questions, the answer is a clear-cut “it depends.”

First and foremost, it’s important to define the scope of protection. Anti-virus is a misnomer. Anti-malware gets closer, but the best way to think of these tools is as endpoint security suites, which are very similar to the endpoint security installed on corporate laptop and desktop systems. The leading products do not just protect against viruses — they are full mobile device security suites. If you find a tool that is nothing but anti-virus protection, that’s definitely not state of the art and it’s also not very useful; in today’s security landscape, organizations need to outfit their hardware with software that does more.

Enterprise-class anti-malware tools have another characteristic: centralized management consoles. This creates some overlap with common MDM and EMM solutions, but each software system still has its differences.” (Is Installing Anti-Virus Software on Mobile Devices Necessary?, https://insights.samsung.com, Snyder, Jan. 22, 2018)

A different type of malware called worms can also destroy data on computers or clog network systems with software-generated electronic transmissions. Worms are similar to viruses in that they can create additional file copies on a computer and generate e-mails to other computers with the infected file attached. Worms differ from viruses because they don’t need human intervention to spread from one computer to another. That helps explain why computer worms spread much more rapidly than computer viruses.

Drive-by downloads are malware stored in a downloaded file that you intentionally or unintentionally request from a web source.

Trojan horses cause problems because they force a computer system to perform unexpected operations, often to the detriment of the system and the user. This type of malware is usually masked in e-mail messages although it can be stored on web sites.

This table gives you examples of malicious code that are spread through vulnerable Internet-connected systems.

Table 8.1 Examples of Malicious Code 

NAME
TYPE
DESCRIPTION 

Cryptolocker
Ransomeware/Trojan
Hijacks users' photos, videos, and text documents; encrypts them with virtually unbreakable asymmetric encryption; and demands ransom payment for them. 

Conficker
Worm
First detected in November 2008 and still a problem. uses flaws in Windows software to take over machines and link them int a virtual computer that can be commanded remotely. Had more than 5 million computers worldwide under its control. Difficult to eradicate.

Sasser.ftp
Worm
First appeared in May 2004. Spread over the Internet by attaching random IP addresses. Causes computers to continually crash and reboot and infected computers to search for more victims. Affected millions of computers worldwide and caused an estimated $14.8 billion to $18.6 billion in damages. 

ILOVEYOU
Virus
First detected on May 3, 2000. Script virus written in Visual Basic script and transmitted as an attachment to email with the subject line ILOVEYOU. Overwrites music, image, and other files with a copy of itself and did an estimated 10 billion to $15 billion in damage. 

We previously mentioned that mobile computing devices such as smartphones and tablet computers increase the vulnerability of corporate networks because they create new points of entry. Social networking web sites such as Facebook also pose security threats. Users assume that every message they get from “friends” or every well-constructed web site is authentic. Unfortunately, that’s a wrong assumption. Facebook has become an easy target for unauthorized users to infiltrate networks and spread malware. Web site applications are becoming a magnet for hackers to gain access to users’ computers. It’s imperative that web site programmers and authors create underlying code that properly validates and filters data entered by site users. That will help prevent SQL injection attacks that target databases and unleash malicious code.

As the article below points out, a real threat to computers and mobile devices, called ransomware, requires users to pay a certain amount of money to unlock their files or remove annoying pop-up messages.

“Malware that holds data for ransom has been around for years. In 1991, a biologist spread PC Cyborg, the first ever ransomware, by sending floppy disks via surface mail to other AIDS researchers, for instance. In the mid '00s Archiveus was the first ransomware to use encryption, though it's long ago been defeated and you can find its password on its Wikipedia page. In the early '10s, a series of "police" ransomware packages appeared, so called because they purported to be warnings from law enforcement about the victims' illicit activities and demanded payment of "fines"; they began to exploit the new generation of anonymous payment services to better harvest payments without getting caught.

In the late '10s, a new ransomware trend emerged: the use of cryptocurrencies as the ransom payment method of choice by cybercriminals. The appeal to the extortionists is obvious, as cryptocurrencies are specifically designed to provide an untraceable, anonymous payment method. Most ransomware gangs demanded payment in bitcoin, the most high-profile cryptocurrency, although some began shifting their demands to other currencies as bitcoin's popularity made its value more volatile.

Over the years, ransomware has grown from a curiosity and an annoyance to a major crisis deeply entwined with top-secret spy agencies and international intrigue.

Despite these very real threats, ransomware has actually been in decline over 2018 and 2019. The drop was steep: ransomware affected about 48 percent of organizations in 2017, but only 4 percent in 2018. There are a couple of reasons for the drop. One is that ransomware attacks are increasingly tailored for specific targets and run by sophisticated controllers in real time, like SamSam and Ryuk. That 48 percent figure for 2017 may sound shockingly high, but much of the "affected" organizations are just companies that received generic phishing emails with ransomware payloads that are simple for IT security to detect and deflect. Targeted attacks affect fewer organizations but have a much higher success rate; the decline in infections has not matched a decline in revenue for attackers.” (The 6 biggest ransomware attacks of the last 5 years,  [link: http://www.csoonline.com] www.csoonline.com, Fruhlinger, Josh, April 5, 2019)

Not all spyware is damaging to a computer system. It is a popular method for some web sites to monitor how users navigate through a site, providing critical information that the web designers and developers can use to improve the site. Unfortunately, some spyware is becoming a preferred method for hackers to install malicious code on computers and allow them to infiltrate an unsuspecting computer. Key loggers are an example of how spyware programs are used to capture personal or business information from unsuspecting users.

8.1.3 Hackers and Computer Crime

Hackers and crackers, those who intentionally create havoc or do damage to a computer system, have been around for a long time. Many companies don’t report hackers’ attempts to enter their systems because they don’t want people to know their systems are vulnerable. That makes it hard to gather real statistics about the extent of hacking attempts and successes. Unauthorized access is a huge problem, though.

In a typical game of cat-and-mouse, hackers constantly develop new ways to get around security software. Unfortunately, they usually have the upper hand because they can create hacking methods faster than security software companies can create, update, and distribute software that blocks them. Users who fail to keep their software updated inadvertently help hackers continue to ply their trade.

Some hackers penetrate systems just to see if they can. They use special computer systems that continually check for password files that can be copied. Or they look for areas of the system that have been “left open,” so to speak, where they can enter the system. Sometimes they don’t do any damage, but far too often they destroy files, erase data, or steal data for their own use through cybervandalism. Other hackers attack systems because they don’t like the company. As the article below points out, the end result is always system disruption.

“Cyber vandals are individuals who damage information infrastructures purely for their own enjoyment and pleasure. Their primary motivation is not financial; it is the desire to prove that the feat could be accomplished. Once inside they leave their mark so there is no denying their presence. At first brush this may seem more of a prank than an attack aimed at destruction. The effect on business, however, is undeniable. These types of attacks fall into the category of DOS or Denial of Service attack. The affected site must be shut down and repaired before it can be returned to normal operation. The massages left behind vary in tone: sometimes racial, sometimes profane, and sometimes political. Whatever the message, the effect is always disruptive.” (What is Cybervandalism?, www.quora.com, Gadhavi, Sandeep, April 11, 2018)

8.1.3.1 Spoofing and Sniffing

These are two other methods hackers and criminals use to gain improper or illegal access to computer systems. Spoofing is becoming a common way to steal financial information through fake web sites. The spoofed site is almost a mirror image of the real site and unless the unsuspecting users examine the spoof closely, they may inadvertently give out important personal and financial information.

Using a sniffer program is a popular way to “grab” information as it passes over transmission lines regardless of whether they are hard-wired or wireless. It is almost impossible to detect, and encryption is about the only way to safeguard against it.

8.1.3.2 Denial of Service Attacks

As companies and organizations expand their business to web sites, they are opening another point of vulnerability through denial of service attacks. Using botnets to launch distributed denial of service attacks is becoming all too common. The hackers seem to enjoy attacking the most popular web sites such as Facebook and Twitter. As the article points below points out, only aggressive monitoring and coordination among businesses and law enforcement will slow the onslaught of DDoS attacks.

“Distributed Denial of Service (DDoS) attacks can cripple a business and cause significant losses. The financial costs can easily climb into the hundreds of thousands of dollars. It's encouraging, however, to see that a global crackdown on DDoS services is making an impact.

Late last year, the FBI teamed up with law enforcement agencies from around the world to crack down on DDoS-for-hire (also known as "stesser" or "booter") services. More than a dozen providers were targeted in a coordinated effort that lasted several months.

When the dust cleared 15 DDoS services had been shut down. The Bureau estimated that they had been responsible for launching more than 200,000 attacks since 2014. It shouldn't come as a complete shock, then, that there was a substantial drop following the 2018 crackdown.

How substantial? Year-over-year DDoS attacks dropped by more than 50%. In addition to fewer attacks being launched DDoS incidents caused shorter disruptions, too. A typical DDoS outage lasted 7.5 hours. The strength of the attacks (generally measured by the network bandwidth being directed at a victim) also plummeted by 85%.

We shouldn't expect DDoS attacks to become a thing of the past. Though the FBI-led efforts have made a significant difference, security researchers tracked nearly 1,500 separate attacks in December of 2018 alone.” (FBI Crackdown Leads To Massive Drop In DDoS Attacks, www.forbes.com, Matthews, Lee, March 19, 2019)

Denial of service attacks are at the core of some of the most serious forms of cyberwarfare being played out across the world between countries and governments. The use of botnets makes it very difficult to determine the origin of the attacks and pinpoint responsibility.

8.1.3.3 Computer Crime

Some of the crimes we have just described are the most popular. Computer crime is a growing national and international threat to the continued development of e-business and e-commerce. When the Internet was first created in the late 1960s, the designers intentionally built it to be open and easily accessible. Little did they know 40 years later, that structure would be the very cause of so much crime and vandalism. Table 8.2 lists the best known examples of computer crime.

Table 8-2 Examples of Computer Crime. 

Computers as Targets of Crime 

Breaching the confidentiality of protected computerized data

Accessing a computer system without authority 

Knowingly accessing a protected computer to commit fraud

Intentionally accessing a protected computer and causing damage, negligently or deliberately 

Knowingly transmitting a program, program code, or command that intentionally causes damage to a protected computer 

Threatening to cause damage to a protected computer 

Computer as Instruments of Crime 

Theft of trade secrets

Unauthorized copying of software ore copyrighted intellectual property, such as articles, books, music, and video. 

Schemes to defraud

Using email for threats or harassment

Intentionally attempting to intercept electronic communication 

Illegally accessing stored electronic communications, including e-mail and voice mail

Transmitting or possessing child pornography using a computer 

It’s very difficult for our society and our governments to keep up with the rapid changes in the types of computer crime being committed. Many laws have to be rewritten and many new laws must be implemented to accommodate the changes.

8.1.3.4 Identity Theft

The fastest growing crime off or on the Internet is identity theft. Even though identity theft is most likely to occur in an offline environment, once your personal information has been stolen it’s easy to use it in an online environment.

Several government web sites provide extensive information about how to prevent identity theft. The Federal Trade Commission at  [link: http://www.ftc.gov/] www.ftc.gov gives you information about what to do if you think your identity has been stolen. Another government-sponsored site is OnGuardOnline.gov: “OnGuardOnline.gov provides practical tips from the federal government and the technology industry to help you be on guard against Internet fraud, secure your computer, and protect your personal information.”

There are many precautions people can take to help prevent identity theft. One way is to scrutinize e-mails or phone calls that ask for your personal information or financial account information. No legitimate financial institution will ever send an e-mail requesting you to supply your account information. That is the number one indicator that the e-mail is a phishing e-mail. You should ignore and delete the e-mail immediately. You can also access  [link: http://www.annualcreditreport.com/] www.annualcreditreport.com and receive free copies of your credit reports from the three major credit reporting bureaus to monitor the information about your credit card and financial activities.

“A recent phishing scam is targeting businesses and consumers who use Office 365 email services. Fraudsters are gaining access to Office 365 accounts by stealing login credentials obtained using convincing fake login screens.

Fraudster email attacks are becoming increasingly sophisticated – often appearing to be sent from a business, organization, or individual the victim normally emails or does business with. The fictitious emails contain malicious links or attachments that redirect the victim to a fake login page asking for their email username and password. Once the information is entered, fraudsters then use the stolen credentials to log into Office 365 and send fraudulent emails to the victim’s contact list, perpetuating the scam.

While Office 365 is the most recent phishing target, these types of scams regularly impact other email applications and platforms as well. Always be cautious when opening any emails that were not expected, are coming from someone you do not know, and contain links or attachments you were not expecting. Take advantage of added security measures that your email provider offers.” (Latest Email Phishing Scam Targets Office 365 Users,    [link: http://www.themerrimack.com] www.themerrimack.com, posted May 1, 2018)

Other ways your identity can be stolen is through evil twins based on wireless network intrusions and pharming, the use of bogus web sites. All of these are classified as computer crimes for which our government is continually passing new laws.

8.1.3.5 Click Fraud

All those ads you see on web sites cost the sponsor money. Every time someone clicks on an ad, the sponsor is charged a pay-per-click fee. The fee is based on the popularity of the search words that generated the ad. What if your company is paying for an ad with little or no resultant traffic to your web site? That’s what happens in the case of click fraud. A person or a software program continually hits on the ad, driving up the advertising fees, without any intention of actually visiting the site. The article below describes two types of click fraud.

“Click fraud is the act of illegally clicking on pay-per-click (PPC) ads to increase site revenue or to exhaust advertisers’ budgets. Click fraud is different from invalid clicks (those that are repeated or made by the ad's publisher) in that it is intentional, malicious and has no potential for the ad to result in a sale. Click fraud happens with pay-per-click advertising and may involve either humans, a computer program or an automated script pretending to be a legitimate user and clicking on paid search advertising with no intention of purchasing something.

Click fraud is committed for two reasons, either to reduce competition among advertisers or to generate revenue by gaming the PPC advertising system. For example, Advertiser A can engage in click fraud to use up Advertiser B’s ad budget and space on irrelevant clicks, leaving Advertiser A as the sole advertiser. This is an example of non-contracting party click fraud.

Another example is maliciously attempting to make it look like a publisher is clicking on its own ads, which may cause an advertising network to end its relationship with that publisher. Since PPC advertising revenue is the primary source of income for some publishers, this practice can put a publisher out of business. Click fraud may also be committed to vandalize a publisher without a financial motive or when friends, family or fans of a publisher click on ads on a website to generate revenue. Both can be difficult to detect.” (Click Fraud, www.investopedia.com, Kenton, Will, May 29, 2018)

8.1.3.6 Global Threats: Cyberterrorism and Cyberwarfare

As terrorism continues to increase the possibility of physical attacks anywhere in the world, computer systems can be targeted as often as buildings, cars, or trains. Governments realize this and are investigating ways of preventing cyberattacks or minimizing the damage caused to the vast number of networks that are vulnerable. The U.S. government and many of its allies and enemies are working to prevent their systems from cyberwarfare attacks. As the article below points out, cyberwarfare threats will only increase as our world becomes more reliant on digital systems. 

“It’s time we got serious about defending the country against cyberwarfare.

The nature of warfare inevitably evolves, and the best-defended and economically dominant countries of the world need to evolve with it. We didn’t see a problem beefing up our air force when aviation ruled the battlefield, and we’re still dealing with a nuclear stockpile meant to deter our enemies from attacking us with these enormously destructive weapons. So why are we so far behind on defending ourselves from a cyberattack?

The future of war is digital, and if we’re going to survive the assault, we need to be ready.

Cyberwarfare is threatening for several reasons. For starters, even a large-scale, devastating attack could be launched by a single, motivated person. When you don’t need to get government approval, or mobilize an army of tens of thousands, the stakes become much higher and the threat becomes more immediate.

It’s also threatening because the stakes are higher than ever. Most of our daily lives, careers, habits, needs, and entertainment are tied to digital systems. Take out the wrong one and millions could be without access to the resources they need to survive.” (The Future of Cyberwarfare, www.americanthinker.com, Alton, Larry, December 5, 2018)

8.1.4 Internal Threats: Employees

It is surprising to learn that most computer crime against companies is committed by current or former employees. They know the system best, are entrusted with huge amounts of data, and have the easiest access. Managers and executives need to be aware of potential internal threats to their systems and put special measures in place to safeguard systems and data. They also need to impress upon all employees how important security is throughout the system right down to the last person.

 [link: #tab-1] Leader of Hacker Gang Sentenced to 9 Years For Hospital Malware

 [link: #tab-2] Goldman Sachs Programmer Sentenced To 8 Years in Prison for Code Theft

 [link: #tab-3] Former Dow Research Scientist Sentenced to 60 Months in Prison for Stealing Trade Secrets and Perjury 

Jesse William McGraw worked as a night security guard at Northern Central Medical Plaza in Dallas where he essentially had free run of the building. While working, McGraw gained physical access to more than ten of the hospital’s computers, including those located in a nurses’ station and controlling the heating, ventilation and air conditioning (HVAC) systems. He enabled the computers to be accessed remotely and removed certain security features (for example, by uninstalling anti-virus programs), which made the entire network more vulnerable to attack. McGraw also installed malicious codes, or “bots,” on several computers. In March 2011, he was sentenced to nine years in prison for installing malware on the facilities’ computers.

Reference
Poulsen, K. (2011, March 18). Leader of Hacker Gang Sentenced to 9 Years For Hospital Malware. Retrieved December 04, 2017, from https://www.wired.com/2011/03/ghostexodus-2/

A former computer programmer at Goldman Sachs & Co., was sentenced in March 2011 to 97 months in prison for theft of trade secrets and interstate transportation of stolen property. For just over two years, Sergey Aleynikov was employed at Goldman Sachs as a computer programmer responsible for developing computer programs supporting the firm’s high-frequency trading on various commodities and equities markets. Shortly after 5 p.m. on his last day of employment, Aleynikov transferred substantial portions of the Goldman Sachs’ proprietary computer code for its trading platform to an outside computer server in Germany. He encrypted the files and transferred them over the Internet without informing Goldman Sachs. During the sentencing proceeding, U.S. District Court Judge Denise L. Cote said Aleynikov’s conduct deserved “a significant sentence because the scope of his theft was audacious—motivated solely by greed, and it was characterized by supreme disloyalty to his employer.”

Reference
Zetter, K. (2011, March 18). Goldman Sachs Programmer Sentenced to 8 Years in Prison for Code Theft. Retrieved December 04, 2017, from  [link: https://www.wired.com/2011/03/aleynikov-sentencing/] https://www.wired.com/2011/03/aleynikov-sentencing/ 

A federal jury convicted a former Dow Chemical Company employee of stealing trade secrets and selling them to companies in China, as well as committing perjury. According to the evidence presented in court in early 2011, Wen Chyu Liu (also known as David Liou) came to the United States from China for graduate work. He began working for Dow in 1965 and retired in 1992. Liu traveled throughout China to market the stolen information, and court evidence showed that he paid current and former Dow employees for material and information. In one instance, Liu bribed a then-employee with $50,000 in cash to provide Dow's process manual and other CPE-related information.

Reference
Former Dow Research Scientist Sentenced to 60 Months in Prison for Stealing Trade Secrets and Perjury. (2012, January 13). Retrieved December 06, 2017, from  [link: https://archives.fbi.gov/archives/neworleans/press-releases/2012/former-dow-research-scientist-sentenced-to-60-months-in-prison-for-stealing-trade-secrets-and-perjury] https://archives.fbi.gov/archives/neworleans/press-releases/2012/former-dow-research-scientist-sentenced-to-60-months-in-prison-for-stealing-trade-secrets-and-perjury 

Password theft is the easiest way for hackers to gain access to a system. They generally use specially written software programs that can build various passwords to see if any of them will work. That’s why you should use odd combinations of letters and numbers not easily associated with your name to create your password. The longer the password, the harder it is to replicate. The same password should not be used for more than one access point. Using multiple passwords limits the damage done if a hacker does manage to obtain a single password.

Safeguarding individual passwords from social engineering maliciousness is the responsibility of everyone in the organization. An effective way of limiting access to data is to establish computer-generated logs that show every employee who logged on, what they did, what part of the system they accessed, and whether any data were used or updated. Logs are easily created by system software programs and should be periodically reviewed by the information technology staff and department managers. If nothing else, it gives them an idea of what their employees are doing.

8.1.5 Software Vulnerability

You too can be a millionaire! On the ABC television show Who Wants to be a Millionaire, one contestant won the top prize of $1 million by knowing which insect represented a computer “bug.” The term bug, used to describe a defect in a software program, has been around since the 1940s and 1950s. Back then, computers were powered by vacuum tubes—hundreds and thousands of them. Grace Hopper, an early computer pioneer, was troubleshooting a computer that had quit running. When her team opened the back of the computer to see what was wrong, they found a moth had landed on one of the tubes and burnt it out. She coined the term “bug” to describe a problem with computers.

Zero-day vulnerabilities are security holes in software code unknown to its creator but through which hackers can enter a system and wreak havoc. It’s called zero day because the software creator has zero days after learning about the hole in which to fix the code.

With millions of lines of code, it’s impossible to have a completely error-free program. Most software manufacturers know their products contain bugs when they release them to the marketplace. They provide free updates, patches, and fixes on their web sites. That’s why it’s a good idea not to buy the original version of a new software program but to wait until some of the major bugs have been found and corrected.

Because bugs are so easy to create, most unintentionally, you can reduce the number of them in your programs by using the tools discussed in other chapters of the Laudon text to design good programs. Many bugs originate in poorly defined and designed programs and keep infiltrating all parts of the program.

Bottom Line

Information systems security is everyone’s business. Understanding the vulnerabilities present in hardware, software, data, and networks, is the first step to good security. The “it won’t happen to me” attitude is trouble. Instituting measures to decrease the bugs and defects in software and data entry can solve many system quality problems.

 

8.1.5.1 Newly Discovered Vulnerabilities in Microprocessor Design

Most malware affecting computer users has been in the form of software programs. Unfortunately, malware has now been discovered in computer hardware components. It’s a much harder problem to fix.

 [link: #top] 

Interactive Session 

Technology: Meltdown and Spectre Haunt the World’s Computers (see page 309 of the text) describes how malware programs have been built into computer chips. The vulnerability enables a malicious program to gain access to data it should never be able to see.

 [link: #top] 

 

8.2 What is the business value of security and control?

Transactions worth billions and trillions of dollars are carried out on networks every day. Think of the impact if the networks experience downtime for even a few minutes. The lack of information systems security and control is only getting more expensive as the article below points out.

“IBM is proud to sponsor the 13th annual Cost of a Data Breach study, the industry’s gold-standard benchmark research, independently conducted by Ponemon Institute. This year’s study reports the global average cost of a data breach is up 6.4 percent over the previous year to $3.86 million. The average cost for each lost or stolen record containing sensitive and confidential information also increased by 4.8 percent year over year to $148.”

(2018 Cost of a Data Breach Study, www.ibm.com, Ponemon Institute, accessed April 15, 2019)

If a business doesn’t adequately protect its systems for any other reason, it should just to avoid expensive and time-consuming legal action. The national retailer T.J. Maxx was forced to spend about $200 million in litigation and damage costs after it experienced a serious security breach in 2008. The money could certainly have been put to better use. Data breaches in other retailers’ systems have cost as much as $1 billion dollars.

 

8.2.1 Legal and Regulatory Requirements for Electronic Records Management

Because so much of our personal and financial information is now maintained electronically, the U.S. government is beginning to pass laws mandating how the data will be protected from unauthorized or illegal misuse. Congress has passed several measures outlining the requirements for electronic records management:

HIPAA: Protects medical and health care data.

Gramm-Leach-Bliley Act: Requires financial institutions to ensure the security and confidentiality of customer data.

Sarbanes-Oxley Act: Requires companies and their management to safeguard the accuracy and integrity of financial information that is used internally and released externally.

All of these laws are in response to computer crimes and abuses that businesses or individuals have committed or experienced. It’s very difficult to pass the laws and costly for businesses who struggle to comply with them.

 

8.2.2 Electronic Evidence and Computer Forensics

Two things are happening in the corporate world that are changing the requirements for how companies handle their electronic documents: 1) Companies are communicating more and more with e-mail and other forms of electronic transmissions, and 2) Courts are allowing all forms of communication to be held as evidence. Therefore, businesses must develop methods of capturing, storing, and presenting any and all electronic communications including e-mail, instant messaging, and e-commerce transactions.

Computer forensics is a growing field because of the increasing digitization of documents and communications. Many people believe that just because they delete a file from a computer file directory that it’s no longer available or recoverable. That’s a false belief. Ambient data remains on hard drives in magnetic form long after it’s apparently been deleted. People trained in computer forensics are able to uncover ambient data and other forms of electronic evidence that can be used in courts of law. Businesses and employees must increase their awareness of the necessity for keeping good records.

Bottom Line

Regardless of where or how electronic transmissions were generated or received, businesses are now responsible for making sure they are monitored, stored, and available for scrutiny. These new requirements significantly change the way businesses view their information resources.

8.3 What are the components of an organizational framework for security and control?

How do you help prevent some of the problems we’ve discussed? One of the best ways is to institute controls into your information system the same way you might in any other system; through methods, policies, and procedures.

8.3.1 Information Systems Controls

Think about what a typical company does when it builds a new office building. From the beginning of the design phase until the building is occupied, the company decides how the physical security of the building and its occupants will be handled. It builds locks into the doors, maybe even designs a single entry control point. It builds a special wing for the executive offices that has extra thick bulletproof glass. There are fences around the perimeter of the building that control the loading docks.

These are just a few examples to get you to think about the fact that the company designs the security into the building from the beginning. It doesn’t wait until everything is built. You should do the same thing with an information system. It’s no different from any other system that requires planning and well-thought-out policies and procedures before construction begins.

The two types of information system controls are:

General controls: Software, physical hardware, computer operations, data security, implementation process, and administrative. Table 8.4 describes each of these.

Application controls: Input, processing, and output.

Table 8.4 General Controls 

Type of General Control
Description 

Software controls 
Monitor the use of system software and prevent unauthorized access of software programs, system software, and computer programs.

Hardware controls 
Ensure that computer hardware is physically secure, and check for equipment malfunction. Organizations that are critically dependent on their computers also must make provisions for backup or continued operation to maintain constant service. 

Computer operations controls 
Oversee the work of the computer department to ensure that programmed procedures are consistently and correctly applied to storage processing of data. They include controls over the setup of computer processing jobs and backup and recovery procedures for processing that ends abnormally. 

Data security controls
Ensure that valuable business data files on either disk or tape are not subject to unauthorized access, change, or destruction while they are in use or in storage. 

Implementation controls
Audit the systems development process at various points to ensure that the process is properly controlled and managed. 

Administrative controls 
Formalized standards, rules, procedures, and control disciplines to ensure that the organization's general and application controls are properly executed and enforced. 

 

8.3.2 Risk Assessment

Companies and government systems constantly use risk assessment to determine weak links in their physical building security. You can use the same methodology to assess the risk in your information system. Use risk assessment to set up cost comparisons for developing and maintaining security against the loss potential. It’s done all the time in other systems, so use it for your information system as well.

 

8.3.3 Security Policy

Companies spend a lot of money on physical security such as locks on doors or fences around supply depots.

Companies spend a lot of money on physical security such as locks on doors or fences around supply depots. They need to do the same thing for their information systems. Because of the increasing liability for security breaches, many companies are now establishing a chief security officer position to help ensure the firm maximizes the protection of information resources. Some tools available to the CSO are:

Security policy: Principle document that determines security goals and how they will be achieved.

Acceptable use policy: Outlines acceptable and unacceptable uses of hardware and telecommunications equipment; specifies consequences for noncompliance.

Figure 8.3 shows how adequate policies would limit access for two different users.

Figure 8.3: Access Rules for a Personnel System

8.3.4 Disaster Recovery Planning and Business Continuity Planning

Floods, fires, hurricanes, even tsunamis, happen without a moment’s notice. Perhaps the most important element of a successful system is a disaster recovery plan. Some firms, not just in New York City and Washington D.C. but around the world, discovered the necessity for a well-written and tested plan on September 11, 2001. Those firms that had completed business continuity planning were able to carry on business, while those that hadn’t spent days and weeks recovering from the terrorist attacks.

It’s important that managers and employees work with information system technicians to develop these plans. Too much is at stake to leave the planning process to one group or the other.

8.3.5 The Role of Auditing

Companies audit their financial data using outside firms to make sure there aren’t any discrepancies in their accounting processes. Perhaps they audit their supply systems on a periodic basis to make sure everything is on the up-and-up. They should also audit their information systems. After all, information is as an important resource as any other in the organization. Information systems audits verify that the system was developed according to specifications, that the input, processing, and output systems are operating according to requirements, and that the data is protected against theft, abuse, and misuse. In essence, an MIS audit checks all the controls we’ve discussed in this chapter.

 

Bottom Line

General and application controls help protect information systems. Risk assessments help determine which assets require protection and how much protection they need. Business continuity and disaster recovery planning are more important than ever for businesses.

8.4 What are the most important tools and technologies for safeguarding information resources?

Let’s look at some of the ways a firm can help protect itself.

8.4.1 Identity Management and Authentication

Identity management software is one of the most important principles of a strong, viable security policy. It includes:

Business processes and software tools for identifying valid system users.

Controlling access to system resources.

Policies for identifying and authorizing different categories of system users.

Specifying what systems or portions of systems each user is allowed to access.

Processes and technologies for authenticating users and protecting their identities

Continuous headlines telling of hackers’ exploits in the past year should be enough to convince every company of the need to install firewalls, identity management systems, and other security measures. With the installation of cable modems or DSL lines, home users must follow the same guidelines. These new connections, which leave your personal computer “always on,” are just as vulnerable to attacks as corporate systems.

If you allow employees to keep certain data on their machines that are not backed up to the mainframe computer, you need to ensure that safeguards are installed on the individual PCs. Make sure you have controls in place for access to individual data, backing it up, and properly protecting it against corruption. Do you even have a policy about whether employees can store data on their individual terminals?

In corporate systems, it’s important to ensure authentication methods are in place so that unauthorized users can’t gain access to the system and its data. Access can be granted in one of three ways: something you know—passwords; something you have—tokens or smart cards; something you are—biometric authentication.

Because most simple password systems are too weak and make the system too vulnerable, security experts are devising new methods to control access. Tokens and smart cards are small, physical devices individuals use to securely access information systems.

Biometric authentication is becoming more popular as a method of protecting systems and data as the technology is refined. While you may have seen the fingerprint or facial recognition techniques only on sci-fi movies, rest assured it may be the next wave of security that’s installed in your organization.

Because it’s quite easy to break through one means of authentication, namely a straightforward password system, two-factor authentication is becoming more popular. It requires two forms of authentication like a bank card (one form) that needs a PIN number (second form) for access.

 

8.4.2 Firewalls, Intrusion Detection Systems, and Antivirus Software

The four types of firewalls described in the text are:

Packet filtering: Data packet header information is examined in isolation.

Stateful inspection: The actual message comes through the firewall but must be identified by the user as passable.

Network address translation (NAT): Conceals IP addresses and makes it more difficult to penetrate systems.

Application proxy filter: Similar to a fence through which a substitute message passes.

 

8.4.2.1 Intrusion Detection Systems

Firewalls can deter, but not completely prevent, network penetration from outsiders and should be viewed as one element in an overall security plan. In addition to firewalls, digital firms relying on networks use intrusion detection systems to help them protect their systems.

In March 2002, Wright Patterson Air Force Base, Ohio, reported more than 250,000 unauthorized attempted entries into its computer systems by hackers in a 24-hour period. The intrusion detection systems it had in place allowed authorities to track the hacker attempts and thwart damage to its critical data and systems.

8.4.2.2 Antivirus and Antispyware Software 

Whether you use a stand-alone PC or your computer is attached to a network, you’re just asking for trouble if you don’t have anti-malware software. This type of software checks every incoming file for viruses, worms, spyware, Trojan horses, and adware. Not if, but when, you receive an infected file, the software alerts you to its presence and usually quarantines it until you decide what to do with it. You can choose to delete the file or “clean” it.

Make sure you update your anti-malware software at least once a week because new viruses are constantly being written and passed around. Some anti-malware software companies now make it very easy to keep your anti-malware software current through online updates. McAfee.com will detect when you are online and notify you when new updates are available. With a few mouse clicks, you download the software to protect against the newest malware.

8.4.2.3 Unified Threat Management Systems

It’s a daunting task to individually manage all the security tools available to business. Unified threat management technologies help organizations by providing all of them in one comprehensive package. It’s a great way for small- and medium-size organizations to ensure they cover all the security vulnerabilities in their systems.

8.4.3 Securing Wireless Networks

It’s important for wi-fi users to protect their data and electronic transmissions as wireless networks and their access points proliferate around the country. Security is easily penetrated because of the very nature of the spectrum transmission used in wi-fi. Unless users take stringent precautions to protect their computers, it’s relatively easy for hackers to obtain access to files. Stronger encryption and authentications systems for wi-fi than the original Wired Equivalent Privacy (WEP) are included in newer computer models. Wi-fi Protected Access (WPA) improves security on wireless networks but individual users still carry the responsibility to make sure passwords are changed from the original and encryption systems are used to help protect data.

 

8.4.4 Encryption and Public Key Infrastructure

Most people are reluctant to buy and sell on the Internet because they’re afraid of theft, fraud, and interception of transactions. To help ease the mind and make transactions secure, many companies are using very sophisticated methods of protecting data as they travel across the various transmission mediums through the use of encryption.

The standard methods of making online transactions more secure are Secure Socket Layers, Transport Layer Security (TLS), and Secure Hypertext Transport Protocol. The next time you’re on an e-commerce or e-business web site, look in the address text box of your browser and notice if the address begins with https. If so, the site incorporates one of these two security measures.

Watch any World War II movie and you’ll see episodes of the good guys intercepting coded messages from the enemy. The messages were scrambled and almost impossible to interpret. But the good guys always won out in the end and unscrambled the message in time to save the world. Now we use sophisticated software programs to encrypt or scramble transmissions before they are sent. The sender and recipient have special software programs they can use to encode and decode the transaction on each end.

Figure 8.6: Public Key Encryption

This figure shows you how public key encryption works using two keys: one public and one private. The keys are created through complicated mathematical formulas. The longer the key, the harder it is to decipher. That’s the whole point of encryption. Encryption software programs incorporate authentication and message integrity in its program to ensure senders and receivers are protected against many of the computer crimes committed on networks and the Internet.

Another way of providing authenticity to network transmissions is by using a digital certificate. Just as your personal signature is connected to you, a digital certificate provides a way of proving you are who you say you are. GlobalSign.com has lots of information about its digital certificate product and other useful information about this technology. You can get a demo certificate, find someone’s certificate, or get more information about how to use your own certificate.

Figure 8.7 Digital Certificates

Public key infrastructure (PKI) is another method for providing secure authentication of online identity and makes users more comfortable transacting business over networks.

8.4.5 Securing Transactions with Blockchain 

One of the best security processes has been created through blockchain technology. As each block in a chain of transactions is created, it’s stored in sequence with all the other blocks. The blockchain is continually updated and kept in sync. That makes it difficult to change or alter a single record because it would become out of sync and therefore, detectable. Blockchains use cryptography to secure all transactions within the chain.

8.4.6 Ensuring System Availability

Many companies create fault-tolerant computer systems that are used as back-ups to help keep operations running if the main system should go out. These back-up systems add to the overall cost of the system—but think about the losses if the system experiences a significant period of downtime. Add the cost of lost productivity by employees to lost transactions and unhappy customers; you do the math. Just imagine what would happen if an airline reservation system (a typical online transaction processing system) went down. Have you ever called a company to place an order for a new dress and it couldn’t take your order because the computer was down? Maybe you called back later, and maybe you didn’t.

8.4.6.1 Controlling Network Traffic: Deep Packet Inspection

Network data traffic takes many different forms, from simple text file transfers to massive audio or video file transmission. Obviously, the small text files take up less bandwidth and can be transmitted faster than the larger files. Deep packet inspection technologies help identify which types of files are being transferred and delay those that hog the network.

“If routing can be compared to the post-mailing system, then Deep Packet Inspection “DPI” should be equal to the Airport Security.

Just like a postman that looks at the package recipient label— the job of a networking device (or router) is only to look at the header of the IP packet, look at the destination address, make a decision, and route as fast as possible. Looking at just one portion of the packet makes routing much more efficient and fast.

But in the post-mailing system, a mail carrier cannot open the package to inspect its contents. You can leave this to the Transportation Security Airport “TSA.” They are the ones with the technology, resources, and permission to check every single passenger, bag, and package.

In the networking space, a router can do a lot more than just checking the destination address. With the DPI  technology, a router can look deep into the contents of the package and make decisions accordingly.

Deep Packet Inspection “DPI” is a sophisticated method to examine the contents of network traffic. It can filter packets based on in-depth analysis at all layers of the OSI model.

As mentioned before, a router would typically only look at the IP header of a packet. In the case of a stateless firewall (also known as an ACL “Access Control List”), it would only check connections based on source and destination IP addresses.

DPI is so important because it can help large corporations improve their security standpoint by shaping its traffic.

But not every router (or firewall) can handle deep packet inspection. The technology requires substantial resources to work, so it is not common in SMBs (Small-to-Medium-Businesses), and if not configured correctly, it can be a real traffic bottleneck.

A router with DPI needs to be powerful to be able to open every packet, inspect it, wrap it, and send it again. Only large enterprises, governments, and telecom service providers have the resources to put this technology to work.” (Deep Packet Inspection – How to Guide and Software & Tools to Analyze Packets,  [link: http://www.ittsystems.com] www.ittsystems.com, Review By  [link: https://www.ittsystems.com/author/root/] Editor, Last Updated: April 8, 2019)

8.4.6.2 Security Outsourcing

If your company lacks the internal resources to adequately plan for disaster, you can use an outside source such as managed security service providers. They may be better at the necessary planning and offering appropriate hardware and software resources because they specialize in such things.

 

8.4.7 Security Issues for Cloud Computing and the Mobile Digital Platform

The concept of cloud computing sounds like nirvana to many companies. Someone else takes the responsibility of building and maintaining very expensive information systems. Someone else spends the money and time to ensure the systems are up-to-date and use the latest technology. You pay only for what you use. Sounds great until you consider the flip side of the coin. Just how secure is your data stored in the clouds?

8.4.7.1 Security in the Cloud

Regardless of where your company stores its data, performs data processing, or how it transmits data, your company is ultimately the only one who is responsible for security as the article below points out.

“More data and applications are moving to the cloud, which creates unique infosecurity challenges.

Cloud computing continues to transform the way organizations use, store, and share data, applications, and workloads. It has also introduced a host of new security threats and challenges. With so much data going into the cloud—and into public cloud services in particular—these resources become natural targets for bad actors.

“The volume of public cloud utilization is growing rapidly, so that inevitably leads to a greater body of sensitive stuff that is potentially at risk,” says Jay Heiser, vice president and cloud security lead at Gartner, Inc.

Contrary to what many might think, the main responsibility for protecting corporate data in the cloud lies not with the service provider but with the cloud customer. “We are in a cloud security transition period in which focus is shifting from the provider to the customer,” Heiser says. “Enterprises are learning that huge amounts of time spent trying to figure out if any particular cloud service provider is ‘secure’ or not has virtually no payback.”” (The dirty dozen: 12 top cloud security threats for 2018, www.csoonline.com, Violino, Bob, Jan. 5, 2018)

 

Interactive Session

Management: How secure is the cloud? (see page 324 of the text) points out security issues managers and users of cloud computing must be concerned with. Using the public cloud disrupts traditional cybersecurity models that many companies have built up over years.

8.4.7.2 Securing Mobile Platforms

Hackers don’t discriminate when it comes to targeting computing devices. They will go after your unprotected smartphone just as gladly as they will your desktop or laptop computer. As the article below points out, mobile device security is here to stay. Now it becomes a matter of protecting yourself from the hackers.

“Mobile spyware has become increasingly more ubiquitous in corporate networks and devices. In a 2017 study, Check Point has found that out of the 850 organizations that they queried, 100% had experienced a mobile malware attack at least once in the past.

To date, most cybersecurity companies have focused either on software-only or built-in hardware solutions as a way of fighting back against these threats. While some of these solutions have proven to be effective, I want to propose that the next generation of mobile security will be primarily based on hardware rather than software solutions.

In a Frost & Sullivan security analysis, Frank Dickson points to the key problem of identifying mobile threats: “Identifying a true threat can be difficult when malicious apps blur the lines between useful features and excessive or exploitative functionality.” Indeed, as more and more applications rely on collecting users’ behavioral information for marketing or design purposes, the line between malicious and aboveboard apps blurs more and more every day.

This trend has been growing in recent months. In August of 2017, the spyware dubbed Pegasus took hold of iOS: the spyware was capable of hacking any iPad or iPhone to harvest data or conduct surveillance on the victim. After Apple fixed these exploits, a spyware version of Pegasus masqueraded itself as an app download on the Android store, secretly gaining root access to millions of devices.

For government officials or enterprises working with sensitive information, Android and iOS no longer provide adequate security solutions for keeping data safe and secure from malware. For these reasons it is more important that ever to go beyond the ineffective software solutions that are populating the mobile marketplace.” (The future of smartphone security: Hardware isolation, www.helpnetsecurity.com, Kreisman Uri, February 2, 2018)

 

8.4.8 Ensuring Software Quality

There are two methods to help improve software programs and ensure better quality of them. The first one, software metrics, allows IS departments and users to measure a system’s performance and identify problems as they occur. You could measure the number of transactions that are processed in a given amount of time or measure your company’s online response time. As with any other type of metric, software metrics must be carefully designed, formal, objective, and used consistently.

Testing software for bugs and the inevitable errors is so important and yet, so often overlooked. The two best methods of testing are walkthroughs and debugging. Walkthroughs are done before the software is written. Obviously, debugging is done after software is written when errors are found.

Bottom Line

Some of the technologies and tools businesses use for security and control include access control, firewalls, intrusion detection systems, antivirus software, and encryption. The tools available for ensuring business continuity include fault-tolerant systems and high-availability computing. Security is everyone’s concern throughout the organization.

8.5 How will MIS help my career?

The chapter’s elements and information can help in securing a good job as an identity access and management support specialist. This position will monitor an identity management system to ensure that the company is meeting its audit and compliance controls. These types of jobs are becoming more popular as information technology becomes more important in the workplace.

Review

Discuss why wireless networks are more susceptible to security problems and how businesses can protect them.

Discuss the security issues associated with cloud computing and what cloud users should do about them.

Discuss the threat employees pose to information system security.

Discuss three laws recently passed by the U.S. government that created electronic records management obligations for businesses.

Discuss the elements of a good security policy that every business should have. 

Compare your answers with  [link: https://canvas.park.edu/courses/57651/pages/unit-4-lecture-chapter-8-answers-to-review-questions] these.

Please select the next tab above to move to the next content tab or the next button below to move to the next topic.
