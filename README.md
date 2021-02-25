# Twilio Demo for BUILD Spring 2021

## What is Twilio?
* Twilio allows you to programmatically send various forms of communication
* Essentially, write code --> send text/email
* This repository has an extremely basic example to show how easy it is to use Twilio

## Creating a Twilio Account
* Before this code can work for you, you will need a Twilio account
* You can create one at Twilio.com and fill out the requested info
* Your account will come with an account sid and an auth token
* You will also need the phone number that it comes with

## Getting Started/Testing This Demo
* Make sure you have Python and pip (Python package manager) installed on your computer 
    * Install Python at https://www.python.org/downloads/
    * See tutorial at https://www.infoworld.com/article/3530140/how-to-install-python-the-smart-way.html
    * Learn how to install pip at https://www.youtube.com/watch?v=Ko9b_vC6XY0
    
* Clone this repository to your computer and navigate to the repository in terminal or command line
* Create a virtual environment and activate it
  * Official docs are here https://docs.python.org/3/library/venv.html
  * Useful video tutorial: https://realpython.com/lessons/creating-virtual-environment/
* Open your terminal or command line and navigate to this repository
* execute "pip install -r requirements.txt" to install the libraries needed to work with Twilio
* Make a new file called ".env" and copy the contents in .env_defaults over but replace the info with the values that your Twilio account came with
* Make sure to replace the phone numbers in twilio_demo.py with the one's you are testing with
* You can now run twilio_demo.py and see it function!

## Note: This tutorial likely requires some minor amounts of Python knowledge. It is designed for developers with basic experience.
* Twilio is intended for use by developers anyways.
* If you have any questions, feel free to contact me at gutta@usc.edu!
