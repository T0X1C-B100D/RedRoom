# Import Modules and Libraries
# =======================================
import os; import sys; import subprocess;
import time; import datetime as dt;
import socket; import requests;
import termcolor; import colorama;
import base64; from datetime import datetime;
from termcolor import colored, cprint;
colorama.init();
# =======================================


# Main Client Architecture
# ====================================
class client():
    def __init__(self):
        self.bufferRate=0; self.host="";
        self.password=''; self.key='';
        self.chatting=True; self.toggle=False;
        self.timeout=0; self.clearDisplay();
        self.banner(); self.join(); self.displayRules();
        print(colored("CONNECTING ...","magenta","on_black"));
        try:
            if (self.send("PING","")!=''):pass;
            else:
                print(colored("ERROR : SERVER OFFLINE OR BAD URL","red","on_black"));
                time.sleep(3); exit();
        except:
            print(colored("ERROR : SERVER OFFLINE OR BAD URL","red","on_black"));
            time.sleep(3); exit();
        
    def clearDisplay(self):
        try:os.system("cls");
        except:subprocess.run(["cls"],shell=True,text=True);
        try:os.system("clear");
        except:subprocess.run(["clear"],shell=True,text=True);
    
    def displayRules(self):
        print(""); print(colored("===============RULES===============","red","on_black"));
        print(colored("1. Warning, we do not moderate / censor","red","on_black"));
        print(colored("2. Please do not share any personal information within the chatroom","red","on_black"));
        print(colored("3. Please do not spam the chatroom","red","on_black"));
        print(colored("4. We do not log the chat / keep logs","red","on_black"));
        print(colored("5. A V.P.N. / proxy connection is advised \n","red","on_black"));
        print(colored("6. For vendors, please do not openly advertise products, wait until asked","red","on_black"));
        print(colored("7. Do not discuss transaction or product delivery details within the chatroom","red","on_black"));
        print(colored("8. When a user has expressed interest in your wares, respond with a method of contact","red","on_black"));
        print(colored("9. It is your own responsibility to prevent yourself from getting hacked or scammed \n","red","on_black"));
        print(colored("===================================","red","on_black"));
        input(">> Press Enter if You have Read, Understand, and Agree to the above Rule Set");
        
    def banner(self):
        print(""); print(colored("Welcome to The BlackHole Messenging Application","magenta","on_black"));
        print(colored(">> Press Enter to Join a Room or CTRL+C to Quit","magenta","on_black")); print("");
        input("");
        
    def encrypt(self,DATA):
        content=DATA; content=[*content]; COUNTER=0;
        KEY=self.key; KEY=[*KEY];
        for x, _ in enumerate(content):content[x]=int(ord(content[x]));
        for x, _ in enumerate(KEY):KEY[x]=int(ord(KEY[x]));
        for x, _ in enumerate(content):
            content[x]=content[x]+KEY[COUNTER];
            if (COUNTER>=(len(KEY)-1)):COUNTER=0;
            else:COUNTER+=1;
        for x, _ in enumerate(content):content[x]=str(content[x]);
        content=' '.join(content); return str(content[::-1]);
        
    def join(self):
        print(colored("=============JOIN============","green","on_black"));
        url=input("URL (COMPRESSED REV.B64 FORMAT) : "); passwd=input("PASSWORD : ");
        enkey=input("KEY : "); self.host=url; self.password=passwd; self.key=enkey;
     
    def send(self,COMMAND,DATA):
        url=self.host;
        data={
            'signal': COMMAND,
            'value': DATA,
            'password': self.password,
            'key': self.key,
        };

        try:
            response=requests.post(url,json=data); print("");
            content=str(response.json());
            print(colored(f"\n {content}","magenta","on_black"));
        except:print(colored("ERROR","red","on_black"));
    
    def main(self):
        while (self.chatting==True):
            message="";
            self.clearDisplay(); print(colored(">> CONNECTED TO CHATROOM #01 (TYPE 'BYE' TO LEAVE | PRESS ENTER TO REFRESH )","blue","on_black"));
            print(colored("===============================================================================","green","on_black"));
            self.send('FETCH',"");
            print(colored("===============================================================================","green","on_black"));
            if (self.timeout>=5):
                self.toggle=False;
                self.timeout=0;
            else:pass;
            
            if (self.toggle==True):
                print(colored(f"PLEASE WAIT {5-self.timeout} SECONDS | THIS IS TO PREVENT OVERWHELMING OF THE SERVER","yellow","on_black"));
                message=''; time.sleep(1); self.timeout+=1;
            else:message=input("MESSAGE : ");
            
            if (message=="BYE"):
                self.send("BYE",""); self.chatting=False; break;
            elif (message=="" or message==" "):pass;
            else:
                message=self.encrypt(str(message));
                self.send("SEND",message);
                self.toggle=True;
# ====================================

# Instantiate the Client Object
# ================================================
if (__name__=="__main__"):
    clientInstance=client(); clientInstance.main();
    exit();
# ================================================
