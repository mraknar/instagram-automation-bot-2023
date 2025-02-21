# Instagram Automation Bot (December 2023)

## Overview

This is an Instagram automation bot developed in Python, designed to save time and increase efficiency for users who want to manage their Instagram accounts more effectively. The bot includes features such as automatic following, unfollowing, and liking posts, allowing users to reach their target audience more efficiently.

## Features

### 1. **Automated Actions**

- **Follow Automation**: Automatically follows followers of specified users.
- **Unfollow Automation**: Unfollows users who do not follow back.
- **Like Automation**: Likes posts of specified users.

### 2. **Settings Panel**

- Configure execution intervals by specifying a range, such as 25 to 45 seconds, within which the program selects a random value for each action.
- Set a delay, for example, to pause for 900 seconds after 25 follow actions.
- Additionally, define a limit on the maximum number of followers to be followed from specific user lists.

### 3. **User Interface**

- Simple, user-friendly, and visually comfortable interface.
- Separate windows for each feature.
- Individual buttons to start/stop each function.
- Process summary section displaying executed actions.
- Whitelist feature: Prevents specific users from being unfollowed.

### 4. **Spam Detection and Prevention**

- Detects various types of spam and pauses the bot automatically if spam is detected.
- Uses Selenium to simulate human-like interactions.
- Randomized execution intervals to mimic real user behavior.
- Uses `random` to execute actions at varying time intervals.
- Configurable time settings in the settings panel.
- Automatically stops and resumes operation if spam is detected.

### 5. **License System**

- A simple license system that locks the program if the date has expired.

## Technologies & Libraries Used

- `PIL` (Image Processing)
- `customtkinter` (Modern GUI Design)
- `datetime` (Time Management)
- `selenium` (Web Automation)
- `time`, `random`, `threading` (Execution Control)
- `ensta` (Custom Module with `Guest` and `Host` Classes for Instagram Data Retrieval)

## Project Status
As this project was developed in **December 2023**, it is no longer actively maintained. However, feel free to fork and modify it for your own use!

## Disclaimer

This project is for educational purposes only. Automating actions on Instagram may violate its terms of service. Use at your own risk.

---

**Author**: Muhammed Remzi Aknar\
**License**: MIT
