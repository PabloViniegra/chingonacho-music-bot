# Discord Music Bot

A simple Discord music bot that allows users to play music in voice channels using YouTube as the source. This bot supports basic commands such as play, pause, resume, join, and leave.

## Features

- Play music from YouTube
- Pause and resume playback
- Join and leave voice channels
- Delete downloaded audio files after playback
- Help command for user instructions

## Requirements

- Python 3.8 or higher
- `discord.py` library
- `yt-dlp` library
- `pytube` library
- FFmpeg (must be installed and accessible in your system's PATH)

## Installation

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```
2. **Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
.\venv\Scripts\activate    # On Windows
```

3. **Install Dependencies**
```bash
pip install discord.py yt-dlp pytube
```

4. **Install FFmpeg**

- Download FFmpeg from the [official website](https://ffmpeg.org/download.html).
- Follow the installation instructions specific to your operating system.
- Ensure that FFmpeg is accessible via your system's PATH.

5. **Set Up Your Discord Bot**

- Go to the *Discord Developer Portal*.
- Create a new application and add a bot to it.
- Copy the bot token from the bot section.
- Invite your bot to your server using the OAuth2 URL with the necessary permissions (e.g., ```CONNECT```, ```SPEAK```, ```USE_VAD```).

6. **Create a ```.env``` File**

- In the root directory of your project, create a file named ```.env```.
- Add your Discord bot token to this file:
```
DISCORD_TOKEN=your_bot_token_here
```

## Usage

1. **Run the Bot**

```bash
python musicbotcode.py
```

2. **Bot Commands**

- ```!join```: Connects the bot to the voice channel you're in.
- ```!leave```: Disconnects the bot from the voice channel and removes downloaded files.
- ```!play [title]```: Plays the specified song by title. Example: ```!play Enter Sandman```.
- ```!pause```: Pauses the current playback.
- ```!resume```: Resumes playback if paused.
- ```!help```: Shows this list of commands.