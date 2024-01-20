'''
move_downloads.py - This program will search in the Downloads folder of the
current user (/home/user/Downloads) and send specific file types to various
standard directories of a typical user file system. These directories include
Documents, Music, Pictures, and Videos. The file extension lists for the various
documents can be modified to include additional file extensions for a specific
directory or to have a current file extension moved to a different directory
(e.g. adding '.txt' to the Pictures directory).
'''


import os
import shutil


# Set username, directory, and file extension list variables
USER = os.getlogin()
DOWNLOADS = os.path.abspath(f'/home/{USER}/Downloads')
DOCUMENTS = os.path.abspath(f'/home/{USER}/Documents')
MUSIC = os.path.abspath(f'/home/{USER}/Music')
PICTURES = os.path.abspath(f'/home/{USER}/Pictures')
VIDEOS = os.path.abspath(f'/home/{USER}/Videos')

DOCUMENTS_EXT = ['.txt', '.doc', '.docx', '.pdf', '.html',
                       '.ppt', '.pptx', '.xlsx', '.odt', '.odf']
MUSIC_EXT = ['.mp3', '.wav', '.aiff', '.pcm', '.flac',
                   '.alac', '.wma', '.ogg', '.aac']
PICTURES_EXT = ['.png', '.jpg', '.jpeg', '.gif', '.bmp',
                      '.raw', '.tiff', '.psd', '.cr2']
VIDEOS_EXT = ['.mp4', '.mov', '.avi', '.flv', '.mkv',
                    '.wmv', '.avchd', '.webm', '.mpeg-4']

# Keep a list of files moved and not moved.
files_moved = []
files_not_moved = []
sub_folders = []


def existing_files(folder):
    """existing_files Search for files that already exist in a specified directory.

    Args:
        folder (str): Absolute path to a directory to search through.
    """
    file_list = []

    folder_files = os.listdir(folder)   # List the files already in the folder.
    for filename in folder_files:
        file_list.append(filename)      # Add existing files to a list.

    return file_list


def move_files (dest_folder, ext_list, file_list):
    """move_files Search for files in the Downloads directory and move them to
    the appropriate directory.

    Args:
        dest_folder (str): Absolute path to a directory to place the files.
        ext_list (list): List of acceptable files extensions to move to dest_folder.
        file_list (list): List of existing files in dest_folder.
    """
    downloads_files = os.listdir(DOWNLOADS)

    for filename in downloads_files:
        if os.path.isdir(os.path.join(DOWNLOADS, filename)) is True:
            if filename not in sub_folders:
                sub_folders.append(filename)
            continue
        else:
            file = os.path.splitext(filename)
            if file[1] in ext_list:
                if filename in file_list:
                    print(f'\nFile \'{filename}\' already in {dest_folder}')
                    files_not_moved.append(filename)
                else:
                    shutil.move(os.path.join(DOWNLOADS, filename),
                                os.path.join(dest_folder, filename))
            else:
                continue


def main():
    """main Main function to run the program.
    """
    print(f'\nSearching through {DOWNLOADS} for files...\n')

    documents_files = existing_files(DOCUMENTS)
    music_files = existing_files(MUSIC)
    pictures_files = existing_files(PICTURES)
    videos_files = existing_files(VIDEOS)

    move_files(DOCUMENTS, DOCUMENTS_EXT, documents_files)
    move_files(MUSIC, MUSIC_EXT, music_files)
    move_files(PICTURES, PICTURES_EXT, pictures_files)
    move_files(VIDEOS, VIDEOS_EXT, videos_files)

    # Print results such as any subfolders, files moved, and files not moved.
    print(f'\n {len(sub_folders)} subfolder(s) in Downloads not moved:')
    for name in sub_folders:
        print(name)

    print(f'\n {len(files_moved)} file(s) moved from Downloads.')
    print(f'\n {len(files_not_moved)} file(s) not moved from Downloads.')        
    print('\nExiting...\n')


if __name__ == "__main__":
    main()
