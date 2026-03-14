# Appium with Python — A to Z Guide

## Table of Contents

1. [What is Appium](#1-what-is-appium)  
2. [Appium Architecture](#2-appium-architecture)  
3. [Install Appium](#3-install-appium)  
4. [Install Python Client](#4-install-python-client)  
5. [Android Setup](#5-android-setup)  
6. [Start Appium Server](#6-start-appium-server)  
7. [Driver Initialization](#7-first-driver-code-python)  
8. [Appium Options / Capabilities](#8-driver-initialization-modern-appium-options)  
9. [Options Explained](#9-appium-options--capabilities-explained)  
10. [Locators](#10-locators-in-appium-python)  
11. [Waits](#11-waits-in-appium-python)  
12. [Actions](#12-appium-actions-and-element-functions)  
13. [Gestures](#13-gestures-in-appium-tap-swipe-scroll-drag)  
14. [Appium Inspector](#14-appium-inspector-find-locators)  
15. [Page Object Model](#15-page-object-model-pom-in-appium)  
16. [Real Device / Emulator / ADB](#16-real-device-vs-emulator--adb--troubleshooting)  
17. [Framework Best Practices](#17-appium-framework-best-practices)  
18. [Advanced Appium Commands](#18-advanced-appium-commands)  
19. [Parallel Testing](#19-parallel-testing-with-appium-pytest)  
20. [CI/CD with GitHub Actions](#20-cicd-with-github-actions-appium--pytest)  
21. [Interview Questions](#21-appium-interview-questions)

---
This repository documents Appium automation using Python from beginner to advanced level.

The goal of this project is to cover everything required for mobile automation:

- Appium setup
- Python client
- Desired capabilities
- Locators
- Actions & gestures
- Waits
- Android concepts
- Page Object Model
- Real device testing
- Emulator testing
- Automation framework design
- Troubleshooting

This repository works as both:

- Learning guide
- Code examples
- Reference documentation

---

# 1. What is Appium

Appium is an open-source automation framework used for testing mobile applications.

It supports:

- Android
- iOS
- Windows apps

Appium allows automation using standard WebDriver protocol.

Supported languages:

- Python
- Java
- JavaScript
- C#
- Ruby

In this project we use:

Python + Appium + Pytest

---

# 2. Appium Architecture

Appium works in client-server architecture.

Python Test Code  
↓  
Appium Python Client  
↓  
Appium Server  
↓  
UIAutomator2 (Android driver)  
↓  
Android device / emulator  

Flow:

Test → Appium Client → Appium Server → Driver → Device

---

# 3. Install Appium

Install Node.js first:

https://nodejs.org

Check:

```
node -v
npm -v
```

Install Appium:

```
npm install -g appium
```

Check:

```
appium -v
```

Install doctor:

```
npm install -g @appium/doctor
```

Check:

```
appium-doctor
```

Fix all errors before continuing.

---

# 4. Install Python client

Create project:

```
mkdir appium-python-a-to-z
cd appium-python-a-to-z
```

Create virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

Install packages:

```
pip install Appium-Python-Client pytest selenium
```

Save requirements:

```
pip freeze > requirements.txt
```

---

# 5. Android Setup

Install Android Studio

Install:

- SDK
- platform-tools
- emulator
- system image

Check SDK:

```
ls ~/Library/Android/sdk
```

Set variables:

```
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:$ANDROID_HOME/emulator
```

Check:

```
adb devices
```

---

# 6. Start Appium server

Start server:

```
appium
```

Default URL:

```
http://127.0.0.1:4723
```

---

# 7. First Driver Code (Python)

Create file:

tests/test_driver.py
# 8. Driver Initialization (Modern Appium Options)

New Appium versions use Options instead of desired capabilities dictionary.

Python client uses:

UiAutomator2Options

Example:

```
from appium import webdriver
from appium.options.android import UiAutomator2Options


def test_open_app():

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    driver.quit()
```

Important:

Old way (deprecated):

```
caps = {}
webdriver.Remote(url, caps)
```

New way:

```
options = UiAutomator2Options()
webdriver.Remote(url, options=options)
```

Always use Options with new Appium.

# 9. Appium Options / Capabilities Explained

In modern Appium Python client we use Options instead of desired capabilities.

For Android automation we use:

UiAutomator2Options

Import:

```
from appium.options.android import UiAutomator2Options
```

Example:

```
options = UiAutomator2Options()

options.platform_name = "Android"
options.device_name = "emulator-5554"
options.automation_name = "UiAutomator2"
```

---

## 9.1 platform_name

Specifies OS.

```
options.platform_name = "Android"
```

Possible values:

- Android
- iOS

---

## 9.2 device_name

Name of device or emulator.

```
options.device_name = "emulator-5554"
```

Check devices:

```
adb devices
```

Example output:

```
emulator-5554
320105025759
```

Use one of these.

---

## 9.3 udid (Real device)

Required for real device.

```
options.udid = "320105025759"
```

Check:

```
adb devices
```

---

## 9.4 automation_name

Driver used by Appium.

```
options.automation_name = "UiAutomator2"
```

Android → UiAutomator2  
iOS → XCUITest

Always use UiAutomator2 for Android.

---

## 9.5 app (install APK)

If you want Appium to install app.

```
options.app = "/Users/abu/app.apk"
```

Example:

```
options.app = "app/Android-MyDemoAppRN.apk"
```

Use when:

- new app
- reinstall needed
- testing APK file

---

## 9.6 appPackage

Start already installed app.

```
options.app_package = "com.saucelabs.mydemoapp.rn"
```

---

## 9.7 appActivity

Main activity of app.

```
options.app_activity = "com.saucelabs.mydemoapp.rn.MainActivity"
```

Find activity:

```
adb shell dumpsys window | grep mCurrentFocus
```

---

## 9.8 noReset

Do not reset app state.

```
options.no_reset = True
```

Use when:

- keep login
- faster tests

---

## 9.9 fullReset

Uninstall app before test.

```
options.full_reset = True
```

Use when:

- clean install needed
- testing first launch

---

## 9.10 newCommandTimeout

Time before session closes.

```
options.new_command_timeout = 300
```

Good for long tests.

---

## 9.11 adbExecTimeout

Fix emulator slow errors.

```
options.adb_exec_timeout = 60000
```

Useful for:

- emulator slow
- install timeout
- socket hangup

---

## 9.12 autoGrantPermissions

Auto allow permissions.

```
options.auto_grant_permissions = True
```

Useful for:

- camera
- storage
- location

---

## 9.13 Example full options

```
from appium import webdriver
from appium.options.android import UiAutomator2Options


options = UiAutomator2Options()

options.platform_name = "Android"
options.device_name = "emulator-5554"
options.automation_name = "UiAutomator2"

options.app_package = "com.saucelabs.mydemoapp.rn"
options.app_activity = "com.saucelabs.mydemoapp.rn.MainActivity"

options.no_reset = True
options.new_command_timeout = 300
options.auto_grant_permissions = True


driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)
```
# 10. Locators in Appium (Python)

Locators are used to find elements in mobile UI.

In Appium Python we use:

```
from appium.webdriver.common.appiumby import AppiumBy
```

Example:

```
driver.find_element(AppiumBy.XPATH, "//android.widget.TextView")
```

Appium supports multiple locator strategies.

---

## 10.1 Accessibility ID (Best locator)

Fastest and most stable.

Uses content-desc in Android.

Example:

```
driver.find_element(
    AppiumBy.ACCESSIBILITY_ID,
    "Login button"
)
```

Example XML:

```
content-desc="Login button"
```

Use this whenever possible.

Best choice.

---

## 10.2 ID locator

Uses resource-id.

Example:

```
driver.find_element(
    AppiumBy.ID,
    "com.app:id/login"
)
```

Example XML:

```
resource-id="com.app:id/login"
```

Very fast.

Good locator.

---

## 10.3 XPath locator

Most flexible but slower.

Example:

```
driver.find_element(
    AppiumBy.XPATH,
    "//android.widget.TextView[@text='Login']"
)
```

Example XML:

```
android.widget.TextView
text="Login"
```

Use when ID not available.

Avoid very long XPath.

Bad:

```
/hierarchy/android/.../android...
```

Good:

```
"//android.widget.TextView[@text='Login']"
```

---

## 10.4 Class name

Find by class.

```
driver.find_element(
    AppiumBy.CLASS_NAME,
    "android.widget.TextView"
)
```

Not very stable.

Use only when needed.

---

## 10.5 Android UIAutomator (Powerful)

Android only.

Example:

```
driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().text("Login")'
)
```

Example:

```
driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().description("Login button")'
)
```

Very powerful.

Used in advanced automation.

---

## 10.6 Multiple elements

```
elements = driver.find_elements(
    AppiumBy.CLASS_NAME,
    "android.widget.TextView"
)
```

Example:

```
for el in elements:
    print(el.text)
```

---

## 10.7 Best locator priority

Use in this order:

1. Accessibility ID
2. ID
3. UIAutomator
4. XPath
5. Class name

Never start with XPath if ID exists.

---

## 10.8 Example test

```
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


def test_locator():

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    login = driver.find_element(
        AppiumBy.ACCESSIBILITY_ID,
        "Login button"
    )

    login.click()

    driver.quit()
```

---

## 10.9 How to find locators

Use:

Appium Inspector

Steps:

1. Start Appium
2. Open Inspector
3. Start session
4. Click element
5. Copy locator

Recommended locator:

Accessibility ID
ID
Short XPath
# 11. Waits in Appium (Python)

Mobile apps are slow and dynamic.

Elements may not appear immediately.

If we try to find element too early → test fails.

To fix this we use waits.

Appium supports:

- Implicit wait
- Explicit wait (recommended)
- Fluent wait (advanced)

---

## 11.1 Implicit wait

Waits for element globally.

Example:

```
driver.implicitly_wait(10)
```

Appium will wait up to 10 seconds.

Example:

```
driver = webdriver.Remote(url, options=options)

driver.implicitly_wait(10)

driver.find_element(AppiumBy.ID, "login")
```

Not recommended for large frameworks.

Use explicit wait instead.

---

## 11.2 Explicit wait (Best practice)

Wait for specific element.

Import:

```
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```

Example:

```
wait = WebDriverWait(driver, 10)

element = wait.until(
    EC.presence_of_element_located(
        (AppiumBy.XPATH, "//android.widget.TextView")
    )
)
```

Best method for automation.

---

## 11.3 visibility_of_element_located

Wait until visible.

Recommended for mobile.

```
wait.until(
    EC.visibility_of_element_located(locator)
)
```

Example:

```
locator = (
    AppiumBy.ACCESSIBILITY_ID,
    "Login button"
)

el = wait.until(
    EC.visibility_of_element_located(locator)
)
```

Use this most of the time.

---

## 11.4 presence_of_element_located

Wait until element exists.

Not always visible.

```
EC.presence_of_element_located
```

Use when:

- element hidden
- element loading
- checking existence

---

## 11.5 clickable wait

Wait until clickable.

```
EC.element_to_be_clickable(locator)
```

Example:

```
wait.until(
    EC.element_to_be_clickable(locator)
).click()
```

Good for buttons.

---

## 11.6 Create reusable wait function (Best practice)

Used in frameworks.

Example:

```
def wait(driver, locator, timeout=10):

    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )
```

Use:

```
wait(driver, locator).click()
```

This is used in Page Object Model.

---

## 11.7 Example with wait

```
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_wait():

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    wait = WebDriverWait(driver, 10)

    login = wait.until(
        EC.visibility_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "Login button")
        )
    )

    login.click()

    driver.quit()
```

---

## 11.8 Best practices

✔ Use explicit wait  
✔ Avoid long implicit wait  
✔ Always wait before click  
✔ Always wait before send_keys  
✔ Use reusable wait method  
✔ Use visibility wait for mobile  

Bad:

```
driver.find_element(...)
```

Good:

```
wait.until(...)
```
# 12. Appium Actions and Element Functions

After locating elements, we perform actions on them.

Common actions:

- click()
- send_keys()
- clear()
- text
- get_attribute()
- is_displayed()
- find_element()
- find_elements()
- back()
- hide_keyboard()

These functions are part of WebDriver API.

---

## 12.1 click()

Click on element.

```
element.click()
```

Example:

```
login = driver.find_element(
    AppiumBy.ACCESSIBILITY_ID,
    "Login button"
)

login.click()
```

---

## 12.2 send_keys()

Type text.

```
element.send_keys("text")
```

Example:

```
username = driver.find_element(
    AppiumBy.XPATH,
    "//android.widget.EditText"
)

username.send_keys("user1")
```

Used for:

- input fields
- password fields
- search

---

## 12.3 clear()

Clear text field.

```
element.clear()
```

Example:

```
field.clear()
field.send_keys("new text")
```

Important for forms.

---

## 12.4 element.text

Get visible text.

```
print(element.text)
```

Example:

```
title = driver.find_element(
    AppiumBy.XPATH,
    "//android.widget.TextView"
)

print(title.text)
```

Used for assertions.

---

## 12.5 get_attribute()

Get attribute value.

```
element.get_attribute("text")
```

Example:

```
value = element.get_attribute("content-desc")
```

Common attributes:

```
text
content-desc
resource-id
checked
enabled
displayed
```

---

## 12.6 is_displayed()

Check if element visible.

```
element.is_displayed()
```

Example:

```
assert element.is_displayed()
```

Used in tests.

---

## 12.7 find_element()

Find one element.

```
driver.find_element(
    AppiumBy.XPATH,
    "//android.widget.TextView"
)
```

Returns single element.

---

## 12.8 find_elements()

Find multiple elements.

```
elements = driver.find_elements(
    AppiumBy.CLASS_NAME,
    "android.widget.TextView"
)
```

Example:

```
for el in elements:
    print(el.text)
```

Used for lists.

---

## 12.9 driver.back()

Press back button.

```
driver.back()
```

Useful for Android navigation.

---

## 12.10 hide_keyboard()

Hide mobile keyboard.

```
driver.hide_keyboard()
```

Needed when keyboard blocks element.

Example:

```
field.send_keys("text")

driver.hide_keyboard()
```

---

## 12.11 press key (Android)

Press hardware key.

Example BACK:

```
driver.press_keycode(4)
```

Common codes:

```
4 = back
3 = home
66 = enter
```

---

## 12.12 Example test

```
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


def test_actions():

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    el = driver.find_element(
        AppiumBy.ACCESSIBILITY_ID,
        "Login button"
    )

    el.click()

    driver.back()

    driver.quit()
```

---

## 12.13 Best practices

✔ Always wait before click  
✔ Always clear before send_keys  
✔ Use is_displayed for assert  
✔ Use find_elements for lists  
✔ Hide keyboard if needed  

# 13. Gestures in Appium (Tap, Swipe, Scroll, Drag)

Mobile automation requires gestures.

Common gestures:

- tap
- long press
- swipe
- scroll
- drag and drop
- press coordinates

In modern Appium we use:

W3C Actions  
mobile commands

Old TouchAction is deprecated.

---

## 13.1 Tap on element

Normal tap = click()

```
element.click()
```

Example:

```
driver.find_element(
    AppiumBy.ACCESSIBILITY_ID,
    "Login button"
).click()
```

---

## 13.2 Tap by coordinates

Sometimes element not clickable.

Use pointer action.

```
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


actions = ActionBuilder(driver)

finger = PointerInput("touch", "finger")

actions.add_action(finger)

actions.pointer_action.move_to_location(500, 1200)

actions.pointer_action.pointer_down()

actions.pointer_action.pointer_up()

actions.perform()
```

Used when:

- custom UI
- canvas
- game
- map

---

## 13.3 Swipe

Swipe screen.

Example:

```
driver.swipe(500, 1500, 500, 500, 500)
```

Arguments:

```
start_x
start_y
end_x
end_y
duration
```

Example:

```
driver.swipe(500, 1600, 500, 400, 800)
```

Swipe up.

---

## 13.4 Scroll using mobile command (recommended)

Best way in modern Appium.

```
driver.execute_script(
    "mobile: scroll",
    {"direction": "down"}
)
```

Example:

```
driver.execute_script(
    "mobile: scroll",
    {"direction": "up"}
)
```

Possible values:

```
up
down
left
right
```

---

## 13.5 Scroll to element (Android UIAutomator)

Very useful.

```
driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(text("Login"))'
)
```

Example:

```
driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(description("Login button"))'
)
```

Best method for Android.

---

## 13.6 Long press

Use pointer action.

Example:

```
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder

actions = ActionBuilder(driver)

finger = PointerInput("touch", "finger")

actions.add_action(finger)

actions.pointer_action.move_to(element)

actions.pointer_action.pointer_down()

actions.pointer_action.pause(2)

actions.pointer_action.pointer_up()

actions.perform()
```

Used for:

- context menu
- drag
- hold buttons

---

## 13.7 Drag and drop

Example:

```
actions.pointer_action.move_to(source)

actions.pointer_action.pointer_down()

actions.pointer_action.move_to(target)

actions.pointer_action.pointer_up()

actions.perform()
```

Used for:

- sliders
- drag items
- games

---

## 13.8 Hide keyboard

```
driver.hide_keyboard()
```

Needed when keyboard blocks UI.

---

## 13.9 Press Android key

```
driver.press_keycode(4)
```

Common:

```
4 = back
3 = home
66 = enter
82 = menu
```

---

## 13.10 Example gesture test

```
def test_scroll(driver):

    driver.execute_script(
        "mobile: scroll",
        {"direction": "down"}
    )
```

---

## 13.11 Best practices

✔ Use click() when possible  
✔ Use UIAutomator scroll for Android  
✔ Avoid swipe unless needed  
✔ Use execute_script for gestures  
✔ Avoid deprecated TouchAction  

# 14. Appium Inspector (Find Locators)

Appium Inspector is used to inspect mobile UI and get locators.

It shows:

- XML hierarchy
- attributes
- content-desc
- resource-id
- text
- class
- xpath

Inspector is required for automation.

---

## 14.1 Start Appium server

Start Appium:

```
appium
```

Default:

```
http://127.0.0.1:4723
```

---

## 14.2 Open Appium Inspector

Open:

Appium Inspector app

Click:

New Session

Enter capabilities.

Example:

```
{
  "platformName": "Android",
  "deviceName": "emulator-5554",
  "automationName": "UiAutomator2",
  "appPackage": "com.saucelabs.mydemoapp.rn",
  "appActivity": "com.saucelabs.mydemoapp.rn.MainActivity",
  "noReset": true
}
```

Click Start Session.

---

## 14.3 Inspector UI

Inspector shows:

Left → app screen  
Right → element properties  
Bottom → XML tree  

Example properties:

```
text
content-desc
resource-id
class
clickable
enabled
displayed
bounds
```

---

## 14.4 Best locator choice

Use this priority:

1. Accessibility ID
2. resource-id
3. Android UIAutomator
4. Short XPath
5. Class name

Bad:

```
/hierarchy/android/.../android...
```

Good:

```
"//android.widget.TextView[@text='Login']"
```

---

## 14.5 Accessibility ID example

```
content-desc="Login button"
```

Use:

```
AppiumBy.ACCESSIBILITY_ID
```

Example:

```
driver.find_element(
    AppiumBy.ACCESSIBILITY_ID,
    "Login button"
)
```

Best locator.

---

## 14.6 ID example

```
resource-id="com.app:id/login"
```

Use:

```
AppiumBy.ID
```

Example:

```
driver.find_element(
    AppiumBy.ID,
    "com.app:id/login"
)
```

Fast locator.

---

## 14.7 XPath example

```
text="Login"
```

Use:

```
AppiumBy.XPATH
```

Example:

```
driver.find_element(
    AppiumBy.XPATH,
    "//android.widget.TextView[@text='Login']"
)
```

Use only when needed.

---

## 14.8 Android UIAutomator example

```
driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiSelector().text("Login")'
)
```

Powerful locator.

Android only.

---

## 14.9 Common mistakes

Wrong:

```
full xpath
```

Wrong:

```
index only
```

Wrong:

```
class only
```

Correct:

```
accessibility id
id
short xpath
```

---

## 14.10 Tips

✔ Always inspect real device  
✔ Always inspect emulator  
✔ Check content-desc first  
✔ Avoid long XPath  
✔ Use scrollable locator when needed  

# 15. Page Object Model (POM) in Appium

Page Object Model is a design pattern used in automation frameworks.

It separates:

Tests  
Page logic  
Driver setup  

Benefits:

- reusable code
- clean tests
- easy maintenance
- scalable framework

Used in real projects.

---

## 15.1 Project structure

Example:

```
appium-python/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── product_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│
├── conftest.py
├── requirements.txt
```

---

## 15.2 BasePage

Contains common functions.

Example:

```
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait(self, locator, timeout=10):

        return WebDriverWait(
            self.driver,
            timeout
        ).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):

        self.wait(locator).click()

    def type(self, locator, text):

        el = self.wait(locator)

        el.clear()

        el.send_keys(text)
```

---

## 15.3 LoginPage example

```
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME = (
        AppiumBy.ACCESSIBILITY_ID,
        "Username input field"
    )

    PASSWORD = (
        AppiumBy.ACCESSIBILITY_ID,
        "Password input field"
    )

    LOGIN_BTN = (
        AppiumBy.ACCESSIBILITY_ID,
        "Login button"
    )

    def login(self, user, pwd):

        self.type(self.USERNAME, user)

        self.type(self.PASSWORD, pwd)

        self.click(self.LOGIN_BTN)
```

---

## 15.4 Test file

```
from pages.login_page import LoginPage


def test_login(driver):

    login = LoginPage(driver)

    login.login(
        "bob@example.com",
        "10203040"
    )
```

Tests stay clean.

---

## 15.5 Driver fixture (conftest.py)

```
import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture
def driver():

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    yield driver

    driver.quit()
```

---

## 15.6 Why POM is important

Without POM:

```
test file big
duplicate code
hard to maintain
```

With POM:

```
clean
reusable
scalable
professional
```

All real frameworks use POM.

---

## 15.7 Best practices

✔ Use BasePage  
✔ Use page classes  
✔ Keep tests clean  
✔ Use fixtures  
✔ Use waits inside pages  
✔ Avoid driver.find_element in tests  

Good:

```
login.login()
```

Bad:

```
driver.find_element(...)
```
# 16. Real Device vs Emulator / ADB / Troubleshooting

Appium can run tests on:

- Android emulator
- Real Android device

Both are used in real projects.

---

## 16.1 Check connected devices

Use adb:

```
adb devices
```

Example:

```
List of devices attached
emulator-5554
320105025759
```

Use one of these as:

```
options.device_name
options.udid
```

---

## 16.2 Emulator setup

Start emulator:

```
emulator -list-avds
```

Start:

```
emulator -avd Pixel_6
```

Check:

```
adb devices
```

Use:

```
options.device_name = "emulator-5554"
```

---

## 16.3 Real device setup

Enable:

- Developer mode
- USB debugging

Connect USB.

Check:

```
adb devices
```

Use:

```
options.udid = "320105025759"
options.device_name = "Android"
```

Real device is more stable.

---

## 16.4 ANDROID_HOME

Required for Appium.

Set:

```
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:$ANDROID_HOME/emulator
```

Check:

```
echo $ANDROID_HOME
```

Fix error:

```
ANDROID_HOME not set
```

---

## 16.5 Common Appium errors

### ANDROID_HOME not exported

Error:

```
Neither ANDROID_HOME nor ANDROID_SDK_ROOT
```

Fix:

```
export ANDROID_HOME=...
```

---

### adb timeout

Error:

```
adbExecTimeout
```

Fix:

```
options.adb_exec_timeout = 60000
```

---

### socket hang up

Error:

```
Could not proxy command
socket hang up
```

Fix:

- restart emulator
- restart Appium
- restart adb

```
adb kill-server
adb start-server
```

---

### app not installed

Error:

```
app does not exist
```

Fix path:

```
options.app = "/full/path/app.apk"
```

---

### session not created

Error:

```
session not started
```

Fix:

- check device
- check appium running
- check capabilities

---

### stale element

Error:

```
StaleElementReferenceException
```

Fix:

- use explicit wait
- wait for screen
- refind element

---

## 16.6 Useful ADB commands

List devices:

```
adb devices
```

Install apk:

```
adb install app.apk
```

Uninstall:

```
adb uninstall package
```

Find package:

```
adb shell pm list packages
```

Find activity:

```
adb shell dumpsys window | grep mCurrentFocus
```

Restart adb:

```
adb kill-server
adb start-server
```

Logcat:

```
adb logcat
```

---

## 16.7 Emulator slow fix

Use:

```
options.adb_exec_timeout = 60000
options.new_command_timeout = 300
```

Close apps.

Use cold boot.

Use real device if possible.

---

## 16.8 Best practice

✔ Use real device for stability  
✔ Use emulator for development  
✔ Always check adb devices  
✔ Always set ANDROID_HOME  
✔ Always wait for screen  
✔ Increase timeout for emulator  

# 17. Appium Framework Best Practices

This section describes best practices used in real automation projects.

Following these rules makes your framework:

- stable
- maintainable
- scalable
- professional

All real QA / SDET frameworks follow these rules.

---

## 17.1 Recommended project structure

```
appium-python-framework/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│
├── conftest.py
├── requirements.txt
├── README.md
├── pytest.ini
```

Keep pages and tests separate.

---

## 17.2 Use Page Object Model

Never write locators in test files.

Bad:

```
driver.find_element(...)
```

Good:

```
login_page.login()
```

Page files contain:

- locators
- actions
- waits

Tests contain:

- steps
- assertions

---

## 17.3 Use BasePage

Common functions should be reused.

Example:

```
click()
type()
wait()
get_text()
```

Do not repeat code.

---

## 17.4 Locator strategy best practice

Use locator priority:

1. Accessibility ID
2. resource-id
3. UIAutomator
4. Short XPath
5. Class name

Avoid:

- full xpath
- index only
- long hierarchy

Good:

```
AppiumBy.ACCESSIBILITY_ID
```

Bad:

```
/hierarchy/android/...
```

---

## 17.5 Wait strategy best practice

Always use explicit wait.

Bad:

```
driver.find_element(...)
```

Good:

```
wait(locator)
```

Best:

```
visibility_of_element_located
```

Avoid long implicit wait.

---

## 17.6 Keep tests clean

Bad test:

```
driver.find_element
driver.find_element
driver.find_element
```

Good test:

```
login.login()
product.add_to_cart()
cart.checkout()
```

Tests should read like steps.

---

## 17.7 Use fixtures

Driver should be in fixture.

Example:

```
@pytest.fixture
def driver():
```

Do not create driver in every test.

---

## 17.8 Use constants for locators

Good:

```
LOGIN_BTN = (...)
```

Bad:

```
"//android.widget..."
```

---

## 17.9 Use reusable functions

Good:

```
def login():
```

Bad:

repeat login in every test.

---

## 17.10 Use config file

Store data in config.

Example:

```
username
password
app path
device id
```

Do not hardcode.

---

## 17.11 Make framework CI ready

Framework should run with:

```
pytest -v
```

No manual steps.

Good framework:

- no UI needed
- no manual input
- no hardcoded paths

---

## 17.12 Logging and reports

Use:

- pytest-html
- logs
- screenshots

Example:

```
pytest --html=report.html
```

---

## 17.13 Real project rules

✔ Use POM  
✔ Use fixtures  
✔ Use waits  
✔ Use good locators  
✔ Keep tests clean  
✔ Separate pages/tests  
✔ Use config  
✔ Make CI ready  
✔ Use git  
✔ Use README  

This is how real Appium frameworks are built.
# 18. Advanced Appium Commands

Appium provides advanced commands for controlling the device, app, and OS.

These commands are used in real automation frameworks.

Examples:

- execute_script
- mobile commands
- install / remove app
- start activity
- background app
- lock / unlock
- current activity
- current package

---

## 18.1 execute_script

Used for mobile commands.

Example:

```
driver.execute_script(
    "mobile: scroll",
    {"direction": "down"}
)
```

execute_script is required for gestures.

---

## 18.2 Get current activity

Android only.

```
driver.current_activity
```

Example:

```
print(driver.current_activity)
```

Useful for:

- navigation validation
- debugging

---

## 18.3 Get current package

```
driver.current_package
```

Example:

```
print(driver.current_package)
```

Used to check correct app.

---

## 18.4 Start activity

Start screen manually.

```
driver.start_activity(
    "com.app.package",
    "MainActivity"
)
```

Example:

```
driver.start_activity(
    "com.saucelabs.mydemoapp.rn",
    "com.saucelabs.mydemoapp.rn.MainActivity"
)
```

Useful for:

- deep link testing
- skip login
- navigation tests

---

## 18.5 Install app

```
driver.install_app("/path/app.apk")
```

Example:

```
driver.install_app("app.apk")
```

Used in automation setup.

---

## 18.6 Remove app

```
driver.remove_app("package.name")
```

Example:

```
driver.remove_app(
    "com.saucelabs.mydemoapp.rn"
)
```

Used for clean install tests.

---

## 18.7 Check if app installed

```
driver.is_app_installed("package")
```

Example:

```
driver.is_app_installed(
    "com.saucelabs.mydemoapp.rn"
)
```

---

## 18.8 Background app

Send app to background.

```
driver.background_app(5)
```

Example:

```
driver.background_app(10)
```

App returns after seconds.

Used for:

- interruption tests
- resume tests

---

## 18.9 Lock / unlock device

Lock:

```
driver.lock()
```

Unlock:

```
driver.unlock()
```

Used for:

- security tests
- resume tests

---

## 18.10 Press keycode

Android hardware key.

```
driver.press_keycode(4)
```

Common:

```
4 = back
3 = home
66 = enter
82 = menu
24 = volume up
25 = volume down
```

---

## 18.11 Open notifications

```
driver.open_notifications()
```

Used for:

- notification testing
- push testing

---

## 18.12 Get page source

```
driver.page_source
```

Example:

```
print(driver.page_source)
```

Used for debugging.

---

## 18.13 Take screenshot

```
driver.save_screenshot("screen.png")
```

Used for:

- failure reports
- debugging
- CI

---

## 18.14 Reset app

```
driver.reset()
```

App restarts.

Used for:

- clean state
- login reset

---

## 18.15 Close / launch app

Close:

```
driver.close_app()
```

Launch:

```
driver.launch_app()
```

Used for:

- restart tests
- crash tests

---

## 18.16 Best practices

✔ Use execute_script for gestures  
✔ Use start_activity for navigation  
✔ Use install/remove for clean tests  
✔ Use screenshot for failures  
✔ Use background for resume tests  
✔ Use current_activity for validation  

Advanced commands are used in real frameworks.

# 19. Parallel Testing with Appium (Pytest)

Parallel testing allows running multiple tests at the same time.

Used for:

- faster execution
- multiple devices
- CI pipelines
- real projects

In Python we use:

pytest-xdist

---

## 19.1 Install pytest-xdist

```
pip install pytest-xdist
```

Run tests in parallel:

```
pytest -n 2
```

Example:

```
pytest -n 4
```

Runs 4 tests at the same time.

---

## 19.2 Problem with Appium parallel

Appium needs:

- different device
- different port
- different systemPort
- different udid

Otherwise tests crash.

---

## 19.3 Example for multiple devices

Device 1:

```
options.udid = "320105025759"
options.system_port = 8201
```

Device 2:

```
options.udid = "emulator-5554"
options.system_port = 8202
```

system_port must be different.

---

## 19.4 Example fixture for parallel

```
import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture
def driver(request):

    device = request.param

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"

    options.udid = device["udid"]

    options.system_port = device["port"]

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    yield driver

    driver.quit()
```

---

## 19.5 Example test

```
devices = [
    {"udid": "320105025759", "port": 8201},
    {"udid": "emulator-5554", "port": 8202},
]


@pytest.mark.parametrize("driver", devices, indirect=True)
def test_parallel(driver):

    assert driver is not None
```

Run:

```
pytest -n 2
```

---

## 19.6 Parallel with multiple Appium servers

Better approach.

Start Appium on different ports:

```
appium -p 4723
appium -p 4725
```

Driver:

```
webdriver.Remote(
    "http://127.0.0.1:4725",
    options=options
)
```

Used in real labs.

---

## 19.7 Best practices

✔ Use different systemPort  
✔ Use different udid  
✔ Use different Appium ports  
✔ Use pytest-xdist  
✔ Use real device lab  

Parallel testing is required in real projects.

# 20. CI/CD with GitHub Actions (Appium + Pytest)

Continuous Integration allows tests to run automatically when code changes.

In real projects automation runs in:

- GitHub Actions
- Jenkins
- GitLab CI
- Azure DevOps

In this project we use GitHub Actions.

---

## 20.1 Create workflow folder

Create:

```
.github/workflows
```

Create file:

```
.github/workflows/tests.yml
```

---

## 20.2 Example workflow

```
name: Appium Tests

on:
  push:
    branches: [ main ]

  pull_request:
    branches: [ main ]


jobs:

  test:

    runs-on: ubuntu-latest

    steps:

      - name: Checkout code
        uses: actions/checkout@v3


      - name: Setup Python
        uses: actions/setup-python@v4

        with:
          python-version: 3.11


      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt


      - name: Run tests
        run: |
          pytest -v
```

This will run tests automatically.

---

## 20.3 Mobile tests in CI

Mobile tests require:

- emulator
- real device
- cloud device farm

Examples:

- BrowserStack
- SauceLabs
- Firebase Test Lab
- AWS Device Farm

CI usually runs:

unit tests  
API tests  
framework checks  

Mobile tests run in device lab.

---

## 20.4 Example with Appium server in CI

Example step:

```
- name: Start Appium
  run: |
    npm install -g appium
    appium &
```

Then run tests.

---

## 20.5 Best practice for CI

✔ Do not hardcode paths  
✔ Use requirements.txt  
✔ Use pytest  
✔ Use config file  
✔ Use environment variables  
✔ Keep tests independent  

Good framework should run with:

```
pytest -v
```

No manual steps.

---

## 20.6 CI ready checklist

✔ requirements.txt  
✔ pytest works  
✔ no manual input  
✔ driver in fixture  
✔ config file  
✔ README  
✔ git repo  

This is required for real automation projects.
# 21. Appium Interview Questions

This section contains common Appium interview questions and answers.

These questions are frequently asked in QA / SDET / Automation interviews.

---

## 21.1 What is Appium?

Appium is an open-source automation framework used for testing mobile applications.

Supports:

- Android
- iOS
- Windows

Uses WebDriver protocol.

Supports multiple languages:

- Python
- Java
- JavaScript
- C#
- Ruby

---

## 21.2 Appium architecture

Client → Appium Server → Driver → Device

Example:

Python test  
↓  
Appium Python client  
↓  
Appium server  
↓  
UIAutomator2 / XCUITest  
↓  
Mobile device

---

## 21.3 Difference between Appium 1 and Appium 2

Appium 1:

- drivers built-in
- old capabilities style

Appium 2:

- drivers installed separately
- uses options
- modular architecture

Example:

```
UiAutomator2Options
```

---

## 21.4 What is UiAutomator2?

Android automation driver.

Used for:

- Android 6+
- real device
- emulator

Set:

```
options.automation_name = "UiAutomator2"
```

---

## 21.5 What is desired capabilities / options?

Configuration used to start session.

Example:

```
options.platform_name = "Android"
options.device_name = "emulator-5554"
options.app_package = "com.app"
```

Used to tell Appium:

- device
- app
- driver
- settings

---

## 21.6 What locator strategies exist in Appium?

- Accessibility ID
- ID
- XPath
- Class name
- Android UIAutomator

Best order:

1 Accessibility ID  
2 ID  
3 UIAutomator  
4 XPath  
5 Class

---

## 21.7 Difference between implicit and explicit wait

Implicit wait:

```
driver.implicitly_wait(10)
```

Global.

Explicit wait:

```
WebDriverWait
```

Better.

Use explicit wait in frameworks.

---

## 21.8 What is Page Object Model?

Design pattern.

Separates:

- tests
- pages
- driver

Benefits:

- reusable
- clean
- maintainable
- scalable

Used in real projects.

---

## 21.9 How to scroll in Appium?

Android UIAutomator:

```
new UiScrollable(...)
```

mobile command:

```
driver.execute_script("mobile: scroll")
```

---

## 21.10 How to run tests on real device?

Enable:

- developer mode
- USB debugging

Check:

```
adb devices
```

Set:

```
options.udid
```

---

## 21.11 What is systemPort?

Used for parallel testing.

Each device needs different port.

```
options.system_port = 8201
```

---

## 21.12 How to debug Appium tests?

Use:

- Appium Inspector
- adb logcat
- page_source
- screenshots

Example:

```
driver.page_source
```

---

## 21.13 How to handle keyboard?

```
driver.hide_keyboard()
```

---

## 21.14 How to restart app?

```
driver.close_app()
driver.launch_app()
```

or

```
driver.reset()
```

---

## 21.15 How to run parallel tests?

Use:

```
pytest-xdist
```

Need:

- different device
- different systemPort
- different Appium port

---

## 21.16 How to make framework stable?

✔ use explicit waits  
✔ use good locators  
✔ use POM  
✔ use fixtures  
✔ use config  
✔ avoid sleep  
✔ avoid long xpath  

---

## 21.17 How to run Appium in CI?

Use:

- GitHub Actions
- Jenkins
- BrowserStack
- SauceLabs

CI runs:

```
pytest
```

Device farm runs mobile tests.

---

## 21.18 Most important Appium topics

✔ Options / capabilities  
✔ Locators  
✔ Waits  
✔ Gestures  
✔ POM  
✔ Parallel  
✔ CI/CD  
✔ ADB  
✔ Inspector  
✔ Troubleshooting  

These are required for real automation jobs.
