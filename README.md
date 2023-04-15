# PhotoPro Editing Bot
A Telegram bot for photo editing using various filters and effects.

# Features

- /removebackground - To remove background of photo.
- /facecut - To cut the face from photo.
- /enhancephoto - To enhance photo.
- /colorizephoto - To colorize photo.
- /cartoonifyphoto - To make cartoon of photo.
- /colorcorrection - To correct color of photo

# Requirements

- Python 3.6 or higher
- Pyrogram
- requests
- configparser

# Usage

1. Clone the repository to your local machine. 

2. Install the dependencies by running `pip install -r requirements.txt`.

Create a `config.ini` file in the same directory as the Python file with the following contents:

```ini
[@Vilas_Photography]
api_id = your-api-id
api_hash = your-api-hash
token = your-bot-token
cotout_key = your-cutout-api-key
