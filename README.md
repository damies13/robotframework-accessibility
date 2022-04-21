# robotframework-accessibility
Automate desktop applications via the OS accessibility layer 

This library aims to be a full cross platform (Windows/MacOS/Linux) desktop automation library that enables you to test your application at the object level by using the operating systems builtin accessability layer.

The accessability layer of an operating system's desktop is provided for screen readers and similar tools to help visually impared people access an application, so if this library is not able to access a component of your application then it's possible that your application doesn't have support for the operating system accessability features, depending on your system requirements this may be a bug.

## Why create this library?

There are already libraries such as FLAUI, Sikuli and ImageHorizon, that can automate desktop applications, why is this library needed?
- Libraries such as Sikuli and ImageHorizon only do image matching, while this often works it can be unreliable and provides limited functionality especially when trying to check feild values
- Libraries like FLAUI and whitelibrary before it are windows only, and there doesn't appear to be equivelents for MacOS or Linux
- Some people might have a requirement to test that their application can be fully accessed via the operating systems accessability layer

Primarily I am developing a desktop application and I wanted to be able to fully test the GUI on Windows, MacOS and Linux, I couldn't find any libraries that gave me good coverage of MacOS and Linux and so as I would need to create libraries for MacOS and Linux I figured haveing 1 library for all desktop platforms would be a nice rather than useing different libraries for each platform and maintaing 3 sets of tests.

## How does it work

The accessability layer of an operating system's desktop is provided for screen readers and similar tools to help visually impared people access an application. This library will use the operating system api's to instruct the accessability layer to interact with the application, similar to how a screen reader would.

The python module used to do this are:
|Operating System|Python Module|
|---|---|
|Windows|[UIAutomation](https://github.com/yinkaisheng/Python-UIAutomation-for-Windows)|
|MacOS|[applescript](https://github.com/andrewp-as-is/applescript.py)|
|Linux|[dogtail](https://gitlab.com/dogtail/dogtail)|

## Documentation

## Other


