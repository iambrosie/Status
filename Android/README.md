books
=====
* [android's hacker handbook] (http://eu.wiley.com/WileyCDA/WileyTitle/productCd-111860864X.html)
  * [authors reddit AMA] (http://www.reddit.com/r/netsec/comments/27zdxc/android_hackers_handbook_ama)

additional resources
====================
* [vogella android development tutorials] (http://www.vogella.com/tutorials/android.html)
* [xda developers android forum] (http://forum.xda-developers.com/)
* attacks:
  * https://jon.oberheide.org/blog/2011/05/28/when-angry-birds-attack-android-edition/
  * https://jon.oberheide.org/blog/2011/03/07/how-i-almost-won-pwn2own-via-xss/

tools
=====
* static analysis
  * dexdump (from the android SDK): disassembles classes.dex
  * [apktool] (https://code.google.com/p/android-apktool): decode APK's contents
  * grep
  * [androguard] (https://code.google.com/p/androguard/): __the android reverse engineering tool__ provides support for static analysis, disassembly and decompilation

* dynamic analysis
  * fire up [logcat] (http://forum.xda-developers.com/showthread.php?t=1726238) while launching the app
  * use a debugger, e.g. [andbug] (https://github.com/swdunlop/AndBug)
  * [drozer] (https://www.mwrinfosecurity.com/products/drozer/) by MWR Labs

* static and dynamic analysis
  * [andrubis] (https://anubis.iseclab.org/)

* file system
  * canhazaxs

abbreviations
=============
* [Explanation of Code Names, Tags, and Build Numbers] (http://source.android.com/source/build-numbers.html)
* [Release adoption] (http://developer.android.com/about/dashboards/)
* ADB: Android Debugging Bridge
* ADT: Android Development Tools
* AIDL: Android Interface Definition Language
* AIDs: Android IDs
* AOSP: Android Open Source Project
* ASEC: Android Secure Container
* AVRCP: Audio/Video Remote Control Profile
* CAPEC: MITRE’s Common Attack Pattern Enumeration and Classification
* CDD: [Compatibility Definition Document] (http://source.android.com/compatibility/)
* CDMA: Code Division Multiple Access
* CTS: Android Compatibility Test Suite
* CVSS: Common Vulnerability Scoring System
* DUN: Dial-up Networking Profile
* FTP: File Transfer Profile
* GPS: Global Positioning System
* GSM: Global System for Mobile communication
* HFP: Hands-Free Profile
* HID: Human Interface Device Profile
* HSP: Headset Profile
* JDWP: Java Debug Wire Protocol
* JNI: Java Native Interface
* L2CAP: Logical Link Control and Adaptation Protocol
* LTE: Long Term Evolution
* NDEF: NFC Data Exchange Format
* NFC: Near Field Communication
* OBB: Opaque Binary Blobs
* OEM: Original Equipment Manufacturer
* OHA: [Open Handset Alliance] (url: http://www.openhandsetalliance.com/oha_members.html)
* Osmocom: Open Source Mobile Communications
* OTA: Over The Air
* PUK: Personal Unblocking Key
* QR: Quick Response Codes
* RFCOMM: Radio Frequency Communications
* RFID: Radio Frequency Identification
* RIL: Radio Interface Layer
* SIP: Session Initiation Protocol
* SOC: System-on-Chip
* SSO: Google’s Single Sign On system
* USRP: Universal Software Radio Peripheral
* USSD: Unstructured Supplementary Service Data
* WAP: Wireless Application Protocol

major application components
============================
* *AndroidManifest.xml*: contains a smorgasbord of information about the application, including the following: Unique package name, Activities, Services, BroadcastReceivers, Instrumentation definitions, Permission definitions, Information on external libraries packaged with and used by the application, Additional supporting directives, such as shared UID information, preferred installation location and UI info (such as the launcher icon for the application).
* *Intents*: A key part of inter-app communication. These are message objects that contain information about an operation to be performed, the optional target component on which to act, and additional flags or other supporting information (which may be significant to the recipient).
* *Activities*: an Activity is a user-facing application component, or UI. Built on the base Activity class, activities consist of a window, along with pertinent UI elements. These Activities are defined within the application’s manifest.
* *Broadcast Receivers*: Another type of IPC endpoint. These are commonly found where applications want to receive an implicit Intent matching certain other criteria (e.g. an application that wants to receive the Intent associated with an SMS message would register a receiver in its manifest with an intent filter matching the android.provider.Telephony.SMS_RECEIVED action.
* *Services*: application components without a UI that run in the background, even if the user is not interacting directly with the Service’s application. Services must also be declared in the application’s manifest.
* *[Content Providers] (https://developer.android.com/guide/topics/providers/content-providers.html)*: act as a structured interface to common, shared data stores. For example, the Contacts provider and Calendar provider manage centralized repositories of contact entries and calendar entries, respectively, which can be accessed by other applications (with appropriate permissions).

attack terminology primer
=========================
* The two most common topics when discussing attacks are *attack vectors* and *attack surfaces*.
* An *attack vector* generally refers to the means by which an attacker makes its move. Attack vectors
can be classified based on several criteria, including authentication, accessibility, and difficulty.
* An *attack surface* is generally understood as a target’s open flanks—that is to say, the characteristics of a target that makes it vulnerable to attack. More technically speaking, an attack surface refers to the code that an attacker can execute and therefore attack. Attack surface properties:
  * Atack vector
  * Priveleges gained
  * Memory safety
  * Complexity
* As a general rule, an attacker seeks to gain as much privilege as possible with as little investment as possible. Thus, especially risky attack surfaces are a logical place to focus.

android attack surfaces
=======================
* Remote attack surfaces (the name comes from the fact that the attacker need not be physically located near her victim).
  * On a live device, the /proc/net directory can be particularly enlightening. More specifically, the ptype entry in that directory provides a list of the protocol types that are supported along with their corresponding receive functions.

  ```
  root@crespo:/ # cat /proc/net/ptype
  cat /proc/net/ptype
  Type Device      Function
  0800          ip_rcv+0x0/0x33c                // IPV4
  00f5          phonet_rcv+0x0/0x4f0            // PhoNet
  0806          arp_rcv+0x0/0x144               // ARP
  890d wlan0    packet_rcv+0x0/0x3b8            
  86dd          ipv6_rcv+0x0/0x404              // IPV6
  888e wlan0    packet_rcv+0x0/0x3b8
  ```

  * Enumerating exposed network services can be done in two ways: by using a port scanner such as Nmap or by listing the listening ports of a test device using shell access:

  ```
  root@crespo:/ # netstat -an | grep LISTEN
  netstat -an | grep LISTEN
   tcp       0      0 127.0.0.1:5037         0.0.0.0:*              LISTEN
  ```

  * Mobile devices expose an additional remote attack surface through cellular communications (SMS and MMS). MMS messages can contain rich multimedia content. Other protocols are built on top of SMS (e.g. WAP). WAP supports push messaging and other protocols. One type of request implemented as a WAP Push message is the Service Loading (SL) request. This request allows the subscriber to cause the handset to request a URL, sometimes without any user interaction.

  * Browser attack surface: up until Android 4.1, devices shipped with only one browser: the Android
  Browser (based on WebKit). With the release of the 2012 Nexus 7 and the Nexus 4, Google started shipping Chrome for Android (based on Chromium) as the default browser. In current versions of vanilla Android, Chrome is the only browser presented to the user. However, the traditional Android browser engine is still present and is used by apps discussed further in the “Web-Powered Apps” section later in this chapter. In Android 4.4, Google switched from using a pure-WebKit-supplied engine (libwebcore.so) to using an engine based on Chromium (libwebview-chromium.so). The primary difference between Chrome for Android and the two other engines is that the Chrome for Android receives updates via Google Play. The WebKit- and Chromium-based engines, which are exposed to apps via the Android Framework, are baked into the firmware and cannot be updated without a firmware upgrade. This drawback leaves these two engines exposed to publicly disclosed vulnerabilities, sometimes for a lengthy period of time. This is the “half-day vulnerability” risk.

android malware
===============
* Android.Troj.mdk - early 2013, infected up to 1 million Chinese Android devices
* Rootstrap Android botnet - infected more than 100,000 Android devices in China
* #malwaremustdie:
  * *Bouncer* - Google's QEMU based Android emulator designed to execute apps in order to determine whether they exhibit malicious behavior
              - Attacks on Bouncer: Charlie Miller and Jon Oberheide, Nicholas Percoco ("Adventures in Bouncerland")

android remote attack surfaces
==============================
* Almost all devices support Wi-Fi and Bluetooth. Many of those also support Global Positioning System (GPS). Devices able to make cellular telephone calls support one or more of the standard cell technologies, such as Global System for Mobile communications (GSM) and Code Division Multiple Access (CDMA). Newer Android devices also support Near Field Communication (NFC).

* *GPS* (often referred to as location data in Android)
  * It works based on signals from satellites that orbit the planet. The GPS receiver chip receives these signals, amplifies them, and determines its location based on the result.
  * Though GPS is a one-way communications mechanism, location data is exposed to Android applications through the Android Framework (android.location API) and Google Play Services (Location Services API).
  * The hardware and software that implements GPS varies from one device to the next. Some devices have a dedicated chip that provides GPS support while others have GPS support integrated into the System-on-Chip (SoC).

* *Baseband* (provides the ability to communicate with mobile networks)
  * At the lowest level, this functionality is provided by a cellular modem. This component, often called the *baseband processor*, might be a separate chip or might be part of the SoC.
  * The software that runs on this chip is referred to as the *baseband firmware* and is one of the software components that comprise the Android telephony stack.
  * An attack against the baseband is a remote attack. However, an attacker must be within a certain proximity to a victim. In typical deployments, the cell modem can be several miles away from the cell tower (an attacker only needs to be close enough to the victim to appear to be the strongest signal).
  * After the victim associates with the attacker’s tower, the attacker can MitM the victim’s traffic or send attack traffic as they desire. This type of attack is called a Rogue Base Station attack.
  * Communicating with the baseband is only possible using sophisticated radio hardware like the Universal Software Radio Peripheral (USRP) from Ettus Research or BladeRF from Nuand. However, the availability of small, portable base stations like Femtocells and Picopops could make this task easier.
  * In Android, the Radio Interface Layer (RIL) communicates with the baseband and exposes cellular functionality to rest of the device.

* *Bluetooth* (originally designed as a wireless alternative to serial communications with relatively low range and power consumption)
  * Most Bluetooth communications are limited to around 9.75 m (32 feet), but the use of antennae and more powerful transmitters can expand the range up to 99.9 m (328 feet).
  * Bluetooth actually includes more than 30 profiles, each of which describes a particular capability of a Bluetooth device (e.g. most Bluetooth headsets use the Hands-Free Profile (HFP) and/or Headset Profile (HSP).
  * These profiles give the connected device control over the device’s speaker, microphone and more. Other commonly used profiles include File Transfer Profile (FTP), Dial-up Networking Profile (DUN), Human Interface Device (HID) Profile, and Audio/Video Remote Control Profile (AVRCP).
  * Much of the functionality of the various Bluetooth profiles requires going through the *pairing* process (usually the process involves entering a numeric code on both devices to confirm that they are indeed talking to each other but some devices have hard-coded codes and therefore are easier to attack).
  * After a pairing is created, it’s possible to hijack the session and abuse it. Possible attacks include Bluejacking, Bluesnarfing and Bluebugging.
  * Android used the Bluez user-space Bluetooth stack until Android 4.2 when Google switched to Bluedroid.
  * More information about the Bluetooth subsystem in Android is available [here] (https://source.android.com/devices/bluetooth.html).

* *Wi-Fi* (primarily used to connect to LANs but it can also be used to connect directly to other computer systems using Ad-Hoc or Wi-Fi Direct features)
  * The maximum range of a typical Wi-Fi network is about 36.5 m (120 feet), but can easily be extended through the use of repeaters or directional antennae.
  * The Wi-Fi stack on Android is much like the Bluetooth stack. In fact, some devices include a single chip that implements both technologies. Like Bluetooth, the source code for the Wi-Fi stack is open source.
  * In user-space, wpa_supplicant implements authentication protocols and the Android operating system manages memorized connections.

* *NFC* (wireless communications technology that builds upon RFID)
  * The range is typically limited to less than 20 cm (8 inches).
  * Typical use cases for NFC on Android devices: 
    * Tags (prominently displayed in public places as part of interactive advertising posters) in the form of stickers
    * Two users touch their Android devices together to *beam* data, such as a photo.
    * For contactless payments
  * Kernel drivers (libpn544_fs.so) speak to the NFC hardware. Then, the driver passes the data to the NFC Service (com.android.nfc composed out of libnfc_jni.so, libnfc.so and libnfc_ndef.so) within the Android Framework. In turn, the NFC Service delivers the NFC tag data to Android apps that have registered to be the recipient of NFC messages.
  * The most popular message format for NFC is NDEF. These can contain any data, but are typically used to transmit text, phone numbers, contact information, URLs, and images. Parsing these types of messages often results in performing actions such as pairing Bluetooth devices, launching the web browser, dialer, YouTube, or Maps applications, and more. And in some cases these operations are performed without any user interaction.
  * Succesful past attacks on NFC:
    * Charlie Miller - used NFC to automatically set up connections using other wireless technologies such as Bluetooth and Wi-Fi Direct.
    * Georg Wicherski and Joshua J. Drake - used NFC to launch a successful browser attack at BlackHat USA in 2012.
    * MWR Labs - exploited a file format parsing vulnerability in the Polaris Office document suite at the 2012 Mobile Pwn2Own.
  * More information about NFC on Android can be found [here] (http://developer.android.com/guide/topics/connectivity/nfc/index.html).

android local attack surfaces
=============================
* In this section, we'll take a closer look at the various attack surfaces exposed to code that’s already executing on a device, whether it be an Android app, a shell via ADB, or otherwise.

* *The file system*
  * You can enumerate file system entries easily using the *opendir* and *stat* system calls. However, some directories do not allow lesser privileged users to list their contents (those lacking the read bit).
  * To make it easier to determine file system entries that could be interesting, Joshua J. Drake developed a tool called *canhazaxs*.

* *System Calls*
  * The Linux kernel also processes potentially malicious data when it executes system calls. As such, system call handler functions inside the kernel represent an interesting attack surface.
  * Finding such functions is easily accomplished by searching for the SYSCALL_DEFINE string within the kernel source code.

* *Sockets* (created using the socket system call)
  * socket system call's function prototype:

    ```
    int socket(int domain, int type, int protocol);
    ```

    * The domain parameter is most important as its value determines how the  protocol parameter is interpreted.
  * It's possible to determine which protocols are supported by an Android device by inspecting the /proc/net/protocols.
  * The source code that implements each protocol can be found within the Linux kernel source in the net subdirectory.
  * Most Android devices make extensive use of sockets in the PF_UNIX, PF_INET and PF_NETLINK domains. Detailed information about the status of instances of each type of socket can be obtained via entries in the /proc/net directory
  * The first, and most commonly used, socket domain is the PF_UNIX domain. Many services expose IPC functionality via sockets in this domain, which expose endpoints in the file system that can be secured using traditional user, group, and permissions.
  * In addition to traditional PF_UNIX domain sockets, Android implements a special type of socket called an Abstract Namespace Socket. Several core system services use sockets in this domain to expose IPC functionality. 
  * Any application that wants to talk to hosts on the Internet uses PF_INET sockets. On rare occasions, services and apps use PF_INET sockets to facilitate IPC.
  * The final common type of socket in Android is the PF_NETLINK socket. These types of sockets are usually used to communicate between kernel-space and user-space.
  * On typical Linux systems, you can match processes to sockets using the *lsof* command or the  netstat command with the -p option. Unfortunately, this doesn’t work out of the box on Android devices. Using a properly built BusyBox binary on a rooted device may allow you tu achieve this task.

* *Binder* (the basis of Intents that are used to communicate between app-level Android components)
  * The driver itself is implemented in kernel-space and exposes an attack surface via the /dev/binder character device (then, Dalvik applications communicate with one another through several levels of abstraction built on top).

* *Shared Memory* (Android devices do not use traditional POSIX shared memory but they do contain several shared memory facilities)
  * Android implements a custom shared memory mechanism called Anonymous Shared Memory, or ashmem for short.
  * You can find out which processes are communicating using ashmem by looking at the open file descriptors in the /proc file system:

  ```
  root@crespo:/ # busybox ls -ld /proc/[0-9]*/fd/* | grep /dev/ashmem | busybox awk -F/ ‘{print $3}’ | busybox sort -u
  * | grep /dev/ashmem | busybox awk -F/ '{print $3}' | busybox sort -u         <
  [...]
  17704
  17921
  18115
  18139
  18218
  18232
  ```

  * In addition to ashmem, other shared memory facilities—for example, Google’s pmem, Nvidia’s NvMap, and ION—exist on only a subset of Android devices.

android physical attack surfaces
================================