# AllWorkNoPlay
Overview:
AllWorkNoPlay is a program in python that will Block websites from us while we are working and want it to be productive. For some people, focusing while working can be a huge task, with the availability of internet. With disposal of websites like Facebook, Amazon, Netflix, people get distracted while doing important work and end up spending time on these websites instead. 
Although this can be achieved by editing the host file manually but automated work will save time and will be more efficient as well. This code will automatically edit the host file in the system according to user input in the program.

Working:
AllWorkNoPlay will run in the background and will require user to input the time window in which he/she wishes to block those websites as well as a list of websites he/she wishes to block. A certain timeframe will be set using the library “datetime”. By setting the datetime, we will be telling the program to block access to listed websites from this hour to that hour. When the timeframe is up, the program will automatically delete the list of websites from the host file and the user will be able to access those file again.
So, when the user tries to access the websites which he/she listed to be blocked in that time window, he/she will be redirected to a dead page instead. In this program, I added the IP address ‘127.0.0.1’ as the final redirected page, as listed in the host file.

Applications:
AllWorkNoPlay will let the user be more efficient at work. This can be used for individual purpose or even at workspace, where organizations can run this program mandatorily in thr background of all the systems and block certain websites which they think might distract employees.
There are certain websites like coursehero.com, chegg.com using which students might cheat in an online exam. Running this program in the background of all the student systems will prevent student from accessing those websites for a certain timeframe. 
For people who shop online compulsively, this might be a boon. They can restrict access to online shopping websites for most hours of the day and hence can save on budget.

System Requirements:
I personally prefer running the code in the command prompt but you can run it in any IDE as well.
To set the program to be able to run on a schedule, the program can be added in the task scheduler. For example, I added my time frame as 9-17 (ie 9AM to 5PM) and in the task scheduler, chose the option “run upon startup”. So every time I start my system and it is in the time frame I added in the code, it will run in the background automatically.
