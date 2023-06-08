# <p align="center"><img src="Images/ReadmeHeader.gif" alt="JARVIS" width="100%"/></a></p>

<p align="center"> 
  <img src="https://img.shields.io/github/stars/BolisettySujith/J.A.R.V.I.S.svg" alt="BolisettySujith" /> 
  <img src="https://img.shields.io/github/forks/BolisettySujith/J.A.R.V.I.S.svg" alt="BolisettySujith" /> 
</p>


<p align="center"> 
  <img src="https://img.shields.io/github/issues/BolisettySujith/J.A.R.V.I.S.svg" alt="BolisettySujith" /> 
  <img src="https://img.shields.io/github/contributors/BolisettySujith/J.A.R.V.I.S.svg" alt="Contrinutors" /> 
  <img src="https://img.shields.io/github/license/BolisettySujith/J.A.R.V.I.S.svg" alt="License" /> 
</p>

## Introduction 👨‍💻
It is a voice assistant which can be used to interact with your computer and also you have been seeing it in Iron man movies, but this JARVIS is not that much advanced as shown in movies. 

### Built with: Python<img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" alt="Python" height="40" style="vertical-align:top">

- Demo video for ***JARVIS*** is available [here](https://docs.google.com/presentation/d/14w4dQUpqVOmGvAXEn8vYkHQUmMYU72wIb-AK0SWCWYk/edit?usp=sharing)

## Cool functionalities of JARVIS 😎 :)

I have wrote code which you can use JARVIS in the following ways :

- It can tell **count of Covid-19 cases for each state in India**
- It can do **Screen Recording with voice recording** stuff.
- It can also do **voice recording**
- It can access your **mobile camera**
- It can access your **web camera**

- <details>
  <summary>It can find the location of a phone number</summary>
  <br>
  
    Unfortunately there is no such thing as magic, and neither we, nor anyone else, have the ability to derive a phone’s location from an input string.
    
    <b>Here is what is actually happening:</b>

    The phone number is entered and a library is used to turn the country calling code into the name of the country. For example numbers starting with +91 becomes India, +880 is Bangladesh, +34 is Spain, etc.

    The country name is then sent to our geocoding API as a forward geocoding request (placename to coordinates). We then return the coordinates of the center of the country. For example we turn India into 22.3511148, 78.6677428, roughly in the middle of Uttar Pradesh.

    People get confused and angry as to why the coordinates are not actually where the phone is physically located.

    Reference: [We can NOT convert a phone number into a location. Sorry.](https://blog.opencagedata.com/post/we-can-not-convert-a-phone-number-into-a-location-sorry)
  </details>

- It can read **pdf's**
- It can work as a **telephone dictionary**(Add contacts, search contacts)
- It can **generate qr codes** for Links/anyText.
- It can check/find your **Internet speed**
- It can tell your **IP address**
- It can tell the **latest news**
- It can check the **system condition**
- It can send **gmails**
- It can send **whatsapp messages to Individual & group chats**
- It can play **youtube songs**
- It can **download youtube songs** 
- It can **download instagram profiles**
- It can find/tell your **current location** where ever you are
- It can take **screenshots** with a custom filename 
- It can tell **current time**
- It can tell **current day**
- It can tell random **progrmamming jokes**
- It can also tell your **schedule** for each day
- It can be **silent** for a certain number of time if we mention how much time we want it to be silent
- It can **search in wikipedia** and tell about it in 5 lines
- It can tell **procedure/instructions** how to make something(Eg:How to make a cake)
- It can **search for information** in browser which we want
- It can **control system volumes**
- It can **control system power activities**(Eg: shutdown, restart, sleep)
- It can **play music file** in a particular directory where the songs are present
- It can open your **social media and open-source accounts**
- It can open your **college meeting accounts**
- It can open your **OTT platforms accounts**
- It can open your **all google apps**
- It can open presentation tools like **canva, google slide**
- It can open **shopping websites**
- It can open **all the URL links**
- It can open/close **all the pc applications**(*NOTE*: give correct path based on your OS)
- It can **sleep until you say wake up**
- Finally It **can interact with you** and you can also add more commands if you want😎

> **NOTE:** Before running the code you must make sure you have all the modules installed in your python version(***NOTE:*** python version can be >=3.6).

## These are the following modules used in JARVIS📚 :

[SpeechRecognisation](https://pypi.org/project/SpeechRecognition/) | [PyAudio](https://pypi.org/project/PyAudio/) | [pyttsx3](https://pypi.org/project/pyttsx3/) | [pywhatkit](https://pypi.org/project/pywhatkit/) | [datetime](https://pypi.org/project/DateTime/) | [wikipedia](https://pypi.org/project/wikipedia/) | [pyjokes](https://pypi.org/project/pyjokes/) | [cv2](https://pypi.org/project/opencv-python/) | [cv2 tools](https://pypi.org/project/cv2-tools/) | [requests](https://pypi.org/project/requests/) | [smtplib](https://pypi.org/project/secure-smtplib/) | [psutil](https://pypi.org/project/psutil/) | [random](https://pypi.org/project/random2/) | [instaloader](https://pypi.org/project/instaloader/) | [PyAutoGUI](https://pypi.org/project/PyAutoGUI/) | [PyPDF2](https://pypi.org/project/PyPDF2/) | [bs4](https://pypi.org/project/bs4/) | [PyQt5](https://pypi.org/project/PyQt5-Qt5/) | [pywikihow](https://pypi.org/project/pywikihow/) | [speed test](https://pypi.org/project/speedtest-cli/) | [pytube](https://pypi.org/project/pytube/) | [numpy](https://pypi.org/project/numpy/) | [urllib](https://pypi.org/project/urllib3/) | [covid](https://pypi.org/project/covid-india/) | [phonenumbers](https://pypi.org/project/phonenumbers/) | [folium](https://pypi.org/project/folium/) | [opencage](https://pypi.org/project/opencage/) | [pillow](https://pypi.org/project/Pillow/) | [Pywave](https://pypi.org/project/PyWave/) | [win32api](https://pypi.org/project/pywin32/) | [mscvrt](https://docs.python.org/dev/library/msvcrt.html#msvcrt.kbhit)

## API keys 🔑
To run this project you should need some API key's for reading news, for finding phone number location. Register for your API key by clicking the following
- [NewsAPI](https://newsapi.org/) : used for fetching news
- [Open cage](https://opencagedata.com/) : to locate a place in maps

> *Note* : supported OS : **Windows**, working on the making the JARVIS for Linux, but it many take some time.

## Installation 💻
- You need to first ```fork``` this repository and ```clone``` the repository to your local system 

    ```
    $ git clone https://github.com/<your-github-username>/J.A.R.V.I.S.git
    ```
- Make sure to install all the required python modules mentioned above or you can simply install them by 

    ```
    $ pip install -r requirements.txt
    ```

    > Note: For any errors while installing the python modules refer [**```ERRORS.md```**](https://github.com/BolisettySujith/J.A.R.V.I.S/blob/main/ERRORS/ERRORS.md) because I got some errors while installing and using them.
- Add the correct **system** paths in ```JARVIS.py``` to open the **system applications**
- Add your **gmail id** and **password** to send emails(line:797,798)
- Make sure you have registerd in [NewsAPI](https://newsapi.org/) and replace the ```apiKey=```**```YOUR_NEWS_API_KEY```** with your API key(Line: 852) and in [Open cage](https://opencagedata.com/) and replace the ```API_key =``` "**```_OPEN_CAGE_GEOCODE_API_KEY_```**" with your API key(PhoneNumber.py(lineNo: 13))
- For using mobile camera you need to first install an app in mobile called [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_US&gl=US) after installing go to **START SERVER** it will open your mobile camara at the bottom of the screen you can see **IPv4** there you can find the IP address and replace ```_IP_Webcam_IP_address_``` with the IP address in ```JARVIS.py``` MobileCamera function(line: 332)
- Add the correct system paths to gifs or for background images in **```JarvisUi.py```** and **```JARVIS.py```**. If you got any elements missing(RED SCREEN) refer [**```ERRORS.md```**](https://github.com/BolisettySujith/J.A.R.V.I.S/blob/main/ERRORS/ERRORS.md) file.
- Finally to launch Jarvis, use the following commands:
  > **GUI Version of Jarvis**
   ```
   $ python Jarvis.py
   ```
  > **Terminal Version of Jarvis**
   ```
   $ python JarvisWithoutGUI.py
   ```

That's it **#Enjoy** speaking with your computer friend 😁

Demo video for ***JARVIS*** is available [here](https://docs.google.com/presentation/d/14w4dQUpqVOmGvAXEn8vYkHQUmMYU72wIb-AK0SWCWYk/edit?usp=sharing)

## FINAL GUI of JARVIS😎
<p align="center"><img src="Images/JAR.gif" alt="JARVIS" width="75%"/></a></p>

> Note: For any errors while installing the python modules refer [**```ERRORS.md```**](https://github.com/BolisettySujith/J.A.R.V.I.S/blob/main/ERRORS/ERRORS.md) because I got some errors while installing and using them.

## Motivation for this project🙃
Due to covid19 in my house I'm in a seperate room, without talking with anyone, so thought to talk with my laptop which I will use everyday, and came up with this project.

## How to Contribute 🤔

To contribute to this project please read the [CONTRITUTING.md](https://github.com/BolisettySujith/J.A.R.V.I.S/blob/main/CONTRIBUTING.md) file.

## Want to run JARVIS as an Application?
Read [this](https://github.com/BolisettySujith/J.A.R.V.I.S/blob/main/py2exe.md), to convert a .`py` file to `.exe` file. 

## Future plans😇

In the present JARVIS GUI we cannot see the commands running but they are visible on the terminal, so plan to bring up the commands to display on the GUI.

If you like the repository **```FORK && clone```** 🍴 the repository, start using JARVIS, and don't forget to **⭐** the repository.
