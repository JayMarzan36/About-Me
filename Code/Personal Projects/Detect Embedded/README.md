# Overview
At the time that I was working on this project, I was watching a lot of Cyber documentaries. And one thing that was in the back of my mind was how bad actors can hide exe's in images.

So I wanted to see if I could make a program that can detect if an image has an embedded .exe.

It's built off of one of my other projects which is a "file search engine". Which searches a system for and returns a list of a specified file or files with a specific file extension.

It also has a GUI interface, I first started using TKinter but soon found that it was not able to handle displaying the amount of image paths I need it to.

So I did a search and found wxPython and decided to give it a try. And that is what I decided on as the new GUI. 
## How it works

![image](https://github.com/JayMarzan36/About-Me/assets/162857361/910a5765-da1f-401a-a365-70a0536dcdef)

### Browse Images
The user can click "Browse Images" to select one image file to detect if there is an embedded .exe, which after searching will create a pop-up with a report on what was found.

### System Search
If the user clicks System Search, it will do a system search for all .png and .jpg files using the aforementioned "file search engine".

After the search, the program will display the image path with the reason why it was flagged as having an embedded .exe.

### Show OverSized
If the user clicks on Show OverSized, it will clear the output and display all the paths of images that were found to have a larger file size than the average

### Show Sig
If the user clicks on Show Sig, it will also clear the output and display the paths of the images that were found to have a .exe header signature.

### Show Safe
If the user clicks the last option, Show Safe, it will do as it sounds and display all the image paths that were found to be safe. 

## How does it detect the .exe?
The way the program determines if an image has an embedded exe depends on many factors.

In what I have developed, for each image file
*  The image file is converted to bytes
* The bytes are then searched for .exe header signatures
  * Currently the program looks for
     * "MZ"
     * "\\x7fELF"
     * "\\xFF\xD8"
* While the program does a system search, the average size of the images is calculated as KiloBytes. Some images when embedded can have large sizes.
   * The default size for using "Browse Images" is 150 KB

