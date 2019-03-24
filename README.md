#Overview
---
We all use websites in our day to day life, to host our portfolio(CV), college websites, personal website etc.
Around 140,000 new websites launched per day and in order to host our websites on the internet we need to use hosting websites like godaddy, digital-ocean, etc. and these hosting charges fees on the yearly basis for their service. As we know these change are around (3k to 75k) rupees for just hosting a simple website like a simple student portfolio or a personal websites and for a normal students or an average developer it's hard to pay these hosting fees.
---
###Let's assume a situation to understand with an example.
---

suppose Ram is a college student and he designed a website to host their portfolio(CV) also designed many websites for college fest and he want to host these sites on the internet but due to lack of money he is not able to do because hosting sites charges lot's of money.
Hence, to solve these type of problems, i have programmed a device(Pocket server) which can host website on the internet with free of cost only we need to pay for Pocket Server (Rs.2500).
---
###Let's see how this device work.
---

Just transfer your website to Pocket Server using 
"USB data cable" and connect "Pocket Server" to your phone hotspot network for internet connection and voila your website is now live on internet and anybody from anywhere can access your website and there can all can be done without any service changes to hosting website because server is hosting your website by using your mobile data bandwidth.
Let's get's deep into how this device work "Pocket Server".
---
##Working Principle
---

whenever we are try to host our website are mostly require these things.
1. A static IP/Public IP
2. Bandwidth
3. Server

This device create tunnel b/w your local IP address to public IP in order to host your websites.
In order to forward localhost traffic to Internet here, i am using Serveo tunneling.
###Let's gets an overview how serveo works.
---

There are three pieces involved: your local target server, your ssh client, and Serveo (which is an SSH server + an HTTP server). When you include -R qualis:80:localhost:3000 in your ssh command, your ssh client sends a "tcpip-forward" request to the ssh server that looks kind of like this:

{ "request": "tcpip-forward", "host": "qualis", "port": 80 }

When Serveo gets this request, it adds an entry to a dictionary that maps hosts ("qualis.serveo.net" in this case) to SSH connections.

Then when a web request comes in, it uses the hostname to find a corresponding SSH connection. If one is found, Serveo sends a request over that connection to your SSH client:

{ "request": "forwarded-tcpip", "host": "qualis", "port": 80 }

When your ssh client gets this request, a two-way channel is established between the ssh client and Serveo, and your client opens a connection on localhost port 3000. Serveo then copies all data that's sent to it by the web visitor to your ssh client over that channel, and your ssh client in turn copies the data to the server it connected to on localhost:3000. Here's how the data flows:

Request
=========
Web visitor -> Serveo HTTP server -> Serveo SSH server -> SSH client -> localhost:5000

Response
=========
Web visitor <- Serveo HTTP server <- Serveo SSH server <- SSH client <- localhost:5000

Second to handle bandwidth data it uses your mobile data connection to host your websitess. 
and at last to handle all the traffic it require a server which run on 1.2 GHz CPU and 1GB SDRAM, Which can handle upto 40 requests per second.

####Let's come to most interesting part how to setup and configure our RPI in order to host a website :)
---
##Setup and configuration RPI
---
Burn Rasbian image into memory card and boot up your rpi.
Now we need to update rpi and install some required dependencies, to install dependencies run "Dependencies python file"
-python3 Dependencies.py

 now to got "/var/www/html"
and paste your respective website.

after that we need to configure our server.
-service apache2 start

Now we need to configure WPA supplicant file in order to connect with mobile data connection.
To make our task easy i already make a python script to do so.
Change your wifi name and password in "Network.py" programe to work with your mobile data.

And at last we need to make a tunnel between public ip and your local host site.
This can be easily handled by "SERVEO"

-ssh -R your_domain_name:80:localhost:80 serveo.net

Viola 
Now Our website is live on internet without paying any fee.


#Advantage of Pocket Server
---
1. Easy to carry(Portable size), size is equal to a credit 	    card.
2. Easy to step (Plug and play)

3. Low power consumption (230 mA (1.2W))

4. First of it's kind.

5. User friendly interface 

6. Low budget(Rs 2500) only.

7. Wide variety of applications.

#Disadvantage
---
1. Not suitable for large scale website eg(irctc, flipkart etc).

2. Bandwidth of pocket server depend on our mobile data.

I am currently trying to increase it's efficiency so that it can handle more request per second.