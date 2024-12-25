# YouTube Manager Application

## Overview

The YouTube Manager Application is a simple command-line tool to manage a list of YouTube videos. It allows users to add, update, delete, and print videos stored in a SQLite database.

## Features

- **Print Videos**: Display a list of all videos in the database.
- **Add Video**: Add a new video to the database.
- **Update Video**: Update the details of an existing video.
- **Delete Video**: Remove a video from the database.

## Requirements

- Python 3.x
- SQLite3

## Installation

1. Clone the repository or download the `index.py` file.
2. Ensure you have Python 3.x installed on your machine.
3. Install SQLite3 if not already installed.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing `index.py`.
3. Run the script using the command:
    ```sh
    python index.py
    ```
4. Follow the on-screen prompts to manage your YouTube videos.

## Code Overview

The main functions in the script are:

- `print_videos()`: Prints all videos in the database.
- `add_video()`: Adds a new video to the database.
- `update_video()`: Updates an existing video in the database.
- `delete_video()`: Deletes a video from the database.
- `main()`: The main loop that provides the user interface.

## Database Schema

The application uses a SQLite database with a single table `youtube_manager`:

- `id`: INTEGER PRIMARY KEY AUTOINCREMENT
- `video`: TEXT NOT NULL
- `time`: TEXT NOT NULL

## License

This project is licensed under the MIT License.

## Acknowledgements

- SQLite3 documentation: https://www.sqlite.org/docs.html
- Python SQLite3 module documentation: https://docs.python.org/3/library/sqlite3.html
