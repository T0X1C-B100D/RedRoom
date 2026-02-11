# Import Modules and Libraries
# =======================================
import os; import subprocess;
import time; import requests;
import termcolor; import colorama;
from termcolor import colored, cprint;
colorama.init();
# =======================================


# Main Client Architecture
# ====================================
class client():
    def __init__(self):
        self.bufferRate=0; self.host="";
        self.password=''; self.key='';
        self.keyB='SUPREMEULTRALORD';
        self.XORkey='0101010101000';
        self.chatting=True; self.toggle=False;
        self.timeout=0; self.clearDisplay();
        self.banner(); self.join(); self.displayRules();
        print(colored("CONNECTING ...","red","on_black"));
        try:
            if (self.send("PING","")!=''):pass;
            else:
                print(colored("ERROR : SERVER OFFLINE OR BAD URL","red","on_black"));
                time.sleep(3); exit();
        except Exception as e:
            print(colored(f"ERROR : SERVER OFFLINE OR BAD URL {e}","red","on_black"));
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
        print(colored(f'.......................................','red','on_black'));
        print(colored(f'.......................................','red','on_black'));
        print(colored(f'..................:+=..................','red','on_black'));
        print(colored(f'..................=##-.................','red','on_black'));
        print(colored(f'.................===%*:................','red','on_black'));
        print(colored(f'................==.=%%+:...............','red','on_black'));
        print(colored(f'...............=+..=%%%+...............','red','on_black'));
        print(colored(f'.........:::-*#+...=%%%%+-:............','red','on_black'));
        print(colored(f'....+%%%%%%%%%%#-..=%%%%%%%%%%##***-...','red','on_black'));
        print(colored(f'.....=%%%%%%%%%%#-.=%%%%%%%%*==-==:....','red','on_black'));
        print(colored(f'.......+%%%%%%%%%%+=%#++=:....-+:......','red','on_black'));
        print(colored(f'........:*%%%%%#***+==:.....-+-........','red','on_black'));
        print(colored(f'..........-#*-..:+%+=#%%#=-+-..........','red','on_black'));
        print(colored(f'..........:+...:+%%+.:*%%%%=...........','red','on_black'));
        print(colored(f'..........-+..-%%%%+...+%%%+:..........','red','on_black'));
        print(colored(f'..........-=.=%%%%%+....+%%%-..........','red','on_black'));
        print(colored(f'.........:+:+%%%%*::-+-..-#%=..........','red','on_black'));
        print(colored(f'.........:##%#=:......:-++-*+..........','red','on_black'));
        print(colored(f'.........=*=:............:-+*:.........','red','on_black'));
        print(colored(f'.......................................','red','on_black'));
        print(colored("\n Red-Room Messenging Application   \n (CLIENTSIDE)    \n Version 1.0 (02/11/2026 REL)","red","on_black"));
        print(colored("\n >> Press Enter to Join Server or CTRL+C to Quit","red","on_black")); print("");
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

    def convertToBinary(self,DATA):
        return ''.join(format(ord(c), '08b') for c in DATA);
        
    def XORCipher(self,DATA):
        D=DATA; COUNTER=0;
        RESULT=''; K=self.XORkey;
        D=self.convertToBinary(D); D=[*D];
        K=[*K];
        for x, _ in enumerate(D):
            if (D[x]!=K[COUNTER]):RESULT+='0';
            else:RESULT+='1';
            if (COUNTER>=(len(K)-1)):COUNTER=0;
            else:COUNTER+=1;         
        return RESULT;
        
    def decrypt(self,DATA):
        d=DATA[::-1]; d=d.split(' ');
        for x, _ in enumerate(d):d[x]=chr(int(d[x])-3);
        return ''.join(d);
        
    def join(self):
        print(colored("=============JOIN============","white","on_black"));
        url=input("URL (REV.ASCII FORMAT) : "); passwd=input("PASSWORD : ");
        enkey=input("KEY : "); revurl=url[::-1]; revurl=revurl.split(' ');
        for x, _ in enumerate(revurl):revurl[x]=chr(int(revurl[x]));
        revurl=''.join(revurl); print(revurl); self.host=revurl;
        self.password=passwd; self.key=enkey;
        
        
    def send(self,COMMAND,DATA):
        url=self.host;
        data={
            'pubswtoxndmf': COMMAND,
            'xkapejxzm': DATA,
            'safsadjqbxa': self.XORCipher(self.password),
            'spiwnam': self.XORCipher(self.key), 
            'oaannw': self.XORCipher(self.keyB)
        };

        try:
            response=requests.post(url,json=data); print("");
            content=str(response.json());
            print(colored(f"\n {self.decrypt(content)}","red","on_black"));
        except:print(colored("ERROR","white","on_red"));
    
    def main(self):
        while (self.chatting==True):
            message="";
            self.clearDisplay(); print(colored(">> CONNECTED TO CHATROOM #01 (TYPE 'BYE' TO LEAVE | PRESS ENTER TO REFRESH )","red","on_black"));
            print(colored("===============================================================================","red","on_black"));
            self.send('FETCH',"");
            print(colored("===============================================================================","red","on_black"));
            if (self.timeout>=10):
                self.toggle=False;
                self.timeout=0;
            else:pass;
            
            if (self.toggle==True):
                print(colored(f"PLEASE WAIT {10-self.timeout} SECONDS | THIS IS TO PREVENT OVERWHELMING OF THE SERVER","yellow","on_black"));
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
