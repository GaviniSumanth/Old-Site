> **Note**:This project is no longer maintained.

# **CBIT Students' Page (Unofficial)**
This is a repository for the Cbit students' page.

## Installation instructions for scraper
**Note:** The installation has been tested only on linux.Please report any issues so that we can fix them.  
**Step-1:** Install dependencies:  
**For Fedora/RHEL based distros**  
```
sudo dnf install python3-pip python3-tkinter && sudo -v && wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sudo sh /dev/stdin
```
**For Debian/Ubuntu based distros (i.e,linux mint, pop_os etc.,)**  
```
sudo apt install python3-pip python3-tk && sudo -v && wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sudo sh /dev/stdin
```
**For Arch/Arch based distros (i.e,endeavour, manjaro etc.,)**  
```
sudo pacman -S python-pip tk && sudo -v && wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sudo sh /dev/stdin
```
  
**Step-2:** Download scrape.py    
```
wget  https://raw.githubusercontent.com/GaviniSumanth/gavinisumanth.github.io/main/scrape.py
```
**Step-3:** Execute it
Execute the script to download the content of the webpage in a kindle e-reader supporeted format.
  
  
## **Troubleshooting:**  
1)I am unable to execute it.  
A)Check if your linux distribution allows user to execute scripts.If it is disabled then you can modify it by right clicking on scape.py and  changing it in the properties (Assuming that you are using a file manager with a gui).  
  
If you are on a terminal session, execute the below command in the same directory where the scrape.py file is located to make it executable.
```
sudo chmod +x scrape.py
```
2)The program takes a long time to start.  
A)The program requires an active internet connection to download some neccessary python packages during first startup so it may take some time for the first launch.There will be no delays in the future once it completes the installation. 
