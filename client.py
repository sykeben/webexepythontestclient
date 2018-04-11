import requests
import os
import urllib.request
import zipfile
import subprocess
import shutil

quitnow = False
serverok = False
quicall = 0

tempdir = "C:\webexetemp"
pkgdir = tempdir + "\package"
zipdir = tempdir + "\package.zip"
exedir = pkgdir + "\webexe.boot.exe"

print("WELCOME!")
print("(C)2018 - Ben Sykes")

while (serverok == False):

    print("")
    print("Enter a server URL (e.g. https://web.site.com/subdir):")
    serverurl = input(">>> ")

    print("")
    print("Checking server . . .")
    specialerror = False
    try:
        specialfile = requests.get(serverurl+"/this.is.a.web.exe.server")
    except:
        print("- An error occured.")
        specialerror = True
    if (specialerror == False):
        if (specialfile.text == "this_is_a_web_exe_server"):
            print("- Correct and valid.")
            serverok = True
        else:
            print("- Incorrect and/or invalid.")

while (quitnow == False):

    appvalid = False
    while (appvalid == False):

        print("")
        print("Downloading list . . .")
        listfile = requests.get(serverurl+"/list")
        print("- Done.")

        print("")
        print("Splitting list . . .")
        splitlist = listfile.text.split("|")
        print("- Done.")

        print("")
        print("")
        print("")
        print("AVAILABLE APPLICATIONS:")
        print("[AppID]:[ReadableName]")
        print("")
        for i in splitlist:
            print(i)
        print("")
        print("Enter an AppID (or \"/quit\" to exit):")
        app2launch = input(">>> ")

        if (app2launch == "/quit"):
            quitnow = True
            quicall = 1
            appvalid = True
        else:
            print("")
            print("")
            print("")
            print("Verifying the app exists . . .")
            for i in splitlist:
                testtxt = i.split(":")
                if (testtxt[0] == app2launch):
                    appvalid = True
            if (appvalid == True):
                print("- App exists.")
            else:
                print("- App does not exist.")

    if (quicall == 0):

        print("")
        print("Prepping temp folder . . .")
        if not os.path.exists(tempdir):
            os.makedirs(tempdir)
            os.makedirs(pkgdir)
        else:
            shutil.rmtree(tempdir, ignore_errors=True)
            os.makedirs(tempdir)
            os.makedirs(pkgdir)
        print("- Done.")

        print("")
        print("Downloading app package . . .")
        urllib.request.urlretrieve(serverurl+"/app/"+app2launch+".zip", zipdir)
        print("- Done.")

        print("")
        print("Extracting app package . . .")
        with zipfile.ZipFile(zipdir,"r") as zipref:
            zipref.extractall(pkgdir)
        print("- Done.")

        print("")
        print("Executing application . . .")
        subprocess.run(exedir)
        print("- Completed.")

print("")
print("")
print("")
print("Cleaning up . . .")
if not os.path.exists(tempdir):
    os.makedirs(tempdir)
    os.makedirs(pkgdir)
else:
    shutil.rmtree(tempdir, ignore_errors=True)
    os.makedirs(tempdir)
    os.makedirs(pkgdir)
print("- Done.")

print("")
print("Quitting . . .")
quit()