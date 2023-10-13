#!/usr/bin/python3

import sys
import os
import subprocess
import shutil

#
#  DEPENDENCIES:
#     - spotdl
#


def download_spotify_playlist(link, path):
    try:
        subprocess.run(["spotdl", link, "--output", path], check=True)
        print("Playlist download completed successfully.")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


def get_valid_folder_name():
    while True:
        folder_name = input("Enter the name of the folder: ").strip()
        if not any(char in folder_name for char in "/\\") and folder_name:
            return folder_name
        else:
            print("Invalid folder name. Please avoid using '/' and '\\'.")


def main():
    if len(sys.argv) != 3 or \
            not sys.argv[1].startswith('https://open.spotify.com/playlist/'):
        print('Usage: musicorg <Spotify playlist URL> <output path>')
        print('Provide a valid Spotify playlist URL and an output path.')
        sys.exit(1)

    playlist_url = sys.argv[1]
    output_path = sys.argv[2]

    if output_path.endswith('/'):
        output_path = output_path[:-1]

    folder_name = get_valid_folder_name()
    target_directory = os.path.join(output_path, folder_name)

    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    temp_directory = os.path.join(target_directory, 'temp_music')
    os.makedirs(temp_directory)

    download_spotify_playlist(playlist_url, temp_directory)

    os.system('clear')

    print('Music downloaded succesfully')

    for song in os.listdir(temp_directory):
        artist = song.split(' -')[0].replace(' ', '_')

        artist_path = os.path.join(target_directory, artist)

        if not os.path.exists(artist_path):
            os.makedirs(artist_path)

        source_file = os.path.join(temp_directory, song)
        destination_file = os.path.join(artist_path, song)

        shutil.move(source_file, destination_file)

    shutil.rmtree(temp_directory)

    os.system('clear')
    print('Program finished succesfully')


if __name__ == "__main__":
    main()
