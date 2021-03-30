# Setup Tutorial
Hello would be Canadian user. All credit goes to TreborNamor, all original code and framework can be found here:
https://github.com/TreborNamor/Agressive-Bestbuy-Bot
### Testing
**You can test bot with this URL.**

`https://www.bestbuy.ca/en-ca/search?path=soldandshippedby0enrchstring%253ABest%2BBuy&search=hdmi&sort=priceLowToHigh`

**Do Not Use a URL like this. If you compare both URL's you'll see the difference. Make sure URL looks like the page above. Otherwise bot will not work.**

`https://www.bestbuy.ca/en-ca/product/dynex-0-91m-3-ft-1080p-hdmi-cable-only-at-best-buy/14495335`

### Instructions

**1. Download Pycharm Community Edition & Firefox.**

[PyCharm](https://www.jetbrains.com/pycharm/download)

[Firefox](https://www.mozilla.org/en-US/firefox/new/)

**2. Create a new project called bestbuybot and select create.**

![Image of create-project](https://raw.githubusercontent.com/Notarealprogrammer/bestbuybotca/main/images/create-project.png)

**3. Go to terminal and type:**
  1. `pip install beautifulsoup4`
  2. `pip install selenium`
  3. `pip install webdriver-manager`
  4. `pip install twilio`

![Image of terminal](https://raw.githubusercontent.com/Notarealprogrammer/bestbuybotca/main/images/terminal.png)

**4. Right click bestbuybot folder, and create new python file.**

![Image of create-python](https://raw.githubusercontent.com/Notarealprogrammer/bestbuybotca/main/images/create-python.png)

**5. Copy and paste bestbuy aggressive bot script in that python file you just created.**

![Image of Autofill](https://raw.githubusercontent.com/Notarealprogrammer/bestbuybotca/main/images/copy-paste.png)

**6. Fill out the script with your personal information.**

```
* Twilio Information(optional)

* CVV number

* Add your Firefox profile.
```

To find Firefox profile type "about:profiles" in firefox. It is the Root Directory path

![Image of firefox-profile](https://raw.githubusercontent.com/Notarealprogrammer/bestbuybotca/main/images/firefox-profile.png)

**7. Prepping the account**
Launch Firefox, and make sure to sign-in on a verified google account (any personal one will do). 

   *To get this to stick you will need to use a third-party website such as:
   
   `https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f`
   
![image of Stackoverflow-login](https://raw.githubusercontent.com/Notarealprogrammer/bestbuybotca/main/images/stackoverflow-login.png)

Trust me its worth it just to sign up

Remember to Sign into Bestbuy.ca and save your credentials, Credit Card information, Billing Address etc. 

**8. To run bot, click run then select bestbuybot.**

![Image of run-bot](https://raw.githubusercontent.com/Notarealprogrammer/bestbuybotca/main/images/run-bot.png)

**9. Finalizing the bot**

In the same window that your bot opened, create a new tab and go to firefox options. Under Privacy & Security toggle on both save and autofill logins & passwords. (This must be done in this step because these settings will reset each time you run the bot).

placeholder

![Image of Autofill](https://raw.githubusercontent.com/Notarealprogrammer/bestbuybotca/main/images/autofill.png)

In the extra tab go to bestbuy.ca and log-on to your account (everything should be autofilled if you've done this correctly).

**10. Enjoy!**
