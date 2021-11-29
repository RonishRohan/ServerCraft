import multiprocessing
import platform
import os
import time
import ngrok_info

sdir = ""
globalIP = ""

def findLine(word, lines):
    index = ""
    for line in lines:
        words = str(line).split("=")
        if(words[0]==word):
            index = lines.index(line)
            break
    return index

def downloadServerJar(version, systype):
    if systype=="Linux":
        #print("Enter your terminals launch command(eg:konsole, gnome-terminal, kitty...)")
        term = "st"
        #input("Terminal:")
        os.chmod("./Resources/setup.sh", 436)
        p = os.popen(f"sh ./Resources/setup.sh {ver} {term}")
        while True:
        
            if(os.path.exists(f"./Servers/Versions/{version}/server.properties")):
               
                
                os.popen(f"sleep 5 && killall {term}")
                p.close()
                break
                pass
            time.sleep(5)
                
        pass
    
        
    print("Config generated succesfully!")
    
        
    pass

def editProperties(version):
    file = open(f"./Servers/Versions/{version}/server.properties", "r")
    lines = file.readlines()
    while True:
        ans = input("Do you want advanced configuration?(y/n)")
        if(str(ans)=="y"):
            break
            pass
        elif(str(ans)=="n"):
            print("Enter server details:")
            name = input("Server Name(visible in public):")
            lines[lines.index("motd=A Minecraft Server\n")] = f"motd={str(name).lower()}\n"
            gamemode = input("Default Gamemode(can be changed ingame later, Survival/Creative/Spectator):")
            lines[lines.index("gamemode=survival\n")] = f"gamemode={str(gamemode).lower()}\n"
            diff=input("Difficulty(Easy/Hard):")
            lines[lines.index("difficulty=easy\n")] = f"difficulty={str(diff).lower()}\n"
            pre=input("Premium(false for cracked players, true/false):")
            lines[lines.index("online-mode=true\n")] = f"difficulty=({str(pre).lower()})\n"
            ipconf=input("Do you want to play locally on your wifi or globally over the internet?(local/global):")
            if(ipconf=="local"):
                lines[lines.index("server-ip=\n")] = f"server-ip=0.0.0.0\n"
                print("Now your friends can connect to your server with your by joining 'localhost' in direct connection in minecraft")
                pass
            elif(ipconf=="global"):
                os.popen('st -T "Ngrok" sh -c "ngrok tcp 25565"')
                time.sleep(5)
                print("DONT close the terminal that just started(until you closed the server)")
                ngrok_info.get()
                globalIP = f"{ngrok_info.adress}:{ngrok_info.port}"
                print(f"Done! Global Ip : {ngrok_info.adress}:{ngrok_info.port}")
                
            break
            pass
        else:
            print("Invalid choice!")
    
    file2 = open(f"./Servers/Versions/{version}/server.properties", "w+")
    file2.writelines(lines)

def startServer(version):
    os.popen(f"st -T 'Minecraft Server' sh -c 'cd ./Servers/Versions/{version}/ && java -jar server.jar nogui'")
    pass

if __name__ == "__main__":
    
  
    systype = platform.system()
    print(f"Running on {systype}")
    print("Enter the minecraft version you want to play on(eg:1.16.5); You will need to have the same version on your launcher to be able to play")
    ver = input("Version:")
    print("Downloading and generating files, please wait...")
    downloadServerJar(ver, systype)
    time.sleep(25)
    editProperties(ver)
    print("Configuration done... starting server now")
    startServer(ver)
    print(f"Server will start now and you can connect to it with the address:{globalIP}")
    
    pass

