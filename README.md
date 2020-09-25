# whats_annoying
Script to send messages to Whatsapp and annoy groups you want to quit but they continue adding you when you attempt to leave.

# First install a browser driver

First of all, you will need to download a chrome driver. I don't know how to make 
this work with another browser, but probably it's the same method: install the 
browser and get the driver of the version you have. In the case of Chrome, you can install
the driver based on this [stackoverflow answer](https://stackoverflow.com/questions/41133391/which-chromedriver-version-is-compatible-with-which-chrome-browser-version).

# Now understand the script

After getting a browser, you must edit the script. There are just three variables you must edit:

    driver_path='path/to/your/driver.exe'
    name_victim="Your victim's name as registered in your Whatsapp"
    looping=False

* The `name_victim` variable must have the exact name of the victim you want to apply this script.

* The looping boolean is if you don't have more content to send, then the file will be repeated when
it ends. That way you avoid having to send a lot of repetitions. 


# Time to run the script

First of all, understand that this script needs a very small piece of help from you because we're 
not using Whatsapp Business, so we can't automate certain important things. When you run the 
script, you will need to process the QR code to enter your Whatsapp chat in the PC. After you entertwi

to the website where appear your chats, return to the screen where you're running this script and
press `ENTER` in order to make the code know you have already registered, and it's all you need to 
do. The rest is by the script. Enjoy! :)

## One more thing...

If you use this script, I will be glad to see how you annoy people, so if it's possible, tag me in
 Twitter to watch the show :-) ([@iam-agf](https://twitter.com/iam-agf) )
