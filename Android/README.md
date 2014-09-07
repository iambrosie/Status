books
=====
* [android's hacker handbook] (http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111860864X.html)
  * [authors reddit AMA] (http://www.reddit.com/r/netsec/comments/27zdxc/android_hackers_handbook_ama)

additional online resources
===========================
* [vogella android development tutorials] (http://www.vogella.com/tutorials/android.html)

static analysis tools
=====================
* dexdump (from the android SDK): disassembles classes.dex
* [apktool] (https://code.google.com/p/android-apktool): decode APK's contents
* grep
* [androguard] (https://code.google.com/p/androguard/): __the android reverse engineering tool__

dynamic analysis tools
======================
* fire up [logcat] (http://forum.xda-developers.com/showthread.php?t=1726238) while launching the app
* use a debugger, e.g. [andbug] (https://github.com/swdunlop/AndBug)

abbreviations
=============
* OHA: [Open Handset Alliance] (url: http://www.openhandsetalliance.com/oha_members.html)
* AOSP: Android Open Source Project
* [Explanation of Code Names, Tags, and Build Numbers] (http://source.android.com/source/build-numbers.html)
* [Release adoption] (http://developer.android.com/about/dashboards/)
* OEM: Original Equipment Manufacturer
* CDD: [Compatibility Definition Document] (http://source.android.com/compatibility/)
* CTS: Android Compatibility Test Suite
* OTA: Over The Air
* AIDs: Android IDs
* JNI: Java Native Interface
* ADB: Android Debugging Bridge
* ASEC: Android Secure Container
* OBB: Opaque Binary Blobs
* AIDL: Android Interface Definition Language
* JDWP: Java Debug Wire Protocol

major application components
============================
* *AndroidManifest.xml*: contains a smorgasbord of information about the application, including the following: Unique package name, Activities, Services, BroadcastReceivers, Instrumentation definitions, Permission definitions, Information on external libraries packaged with and used by the application, Additional supporting directives, such as shared UID information, preferred installation location and UI info (such as the launcher icon for the application).
* *Intents*: A key part of inter-app communication. These are message objects that contain information about an operation to be performed, the optional target component on which to act, and additional flags or other supporting information (which may be significant to the recipient).
* *Activities*: an Activity is a user-facing application component, or UI. Built on the base Activity class, activities consist of a window, along with pertinent UI elements. These Activities are defined within the application’s manifest.
* *Broadcast Receivers*: Another type of IPC endpoint. These are commonly found where applications want to receive an implicit Intent matching certain other criteria (e.g. an application that wants to receive the Intent associated with an SMS message would register a receiver in its manifest with an intent filter matching the android.provider.Telephony.SMS_RECEIVED action.
* *Services*: application components without a UI that run in the background, even if the user is not interacting directly with the Service’s application. Services must also be declared in the application’s manifest.
* *[Content Providers] (https://developer.android.com/guide/topics/providers/content-providers.html)*: act as a structured interface to common, shared data stores. For example, the Contacts provider and Calendar provider manage centralized repositories of contact entries and calendar entries, respectively, which can be accessed by other applications (with appropriate permissions).