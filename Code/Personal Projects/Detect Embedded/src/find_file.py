import os, platform, sys
def winlocate_file(filename, start_paths=['A:\\', 'B:\\', 'C:\\', 'D:\\', 'E:\\', 'F:\\', 'G:\\', 'H:\\', 'I:\\', 'J:\\', 'K:\\', 'L:\\', 'M:\\', 'N:\\', 'O:\\', 'P:\\', 'Q:\\', 'R:\\', 'S:\\', 'T:\\', 'U:\\', 'V:\\', 'W:\\', 'X:\\', 'Y:\\', 'Z:\\'], case_sensitive=True):
    """
    Locate a file on specified drives.
    :param filename: The name of the file to search for.
    :param start_paths: List of starting directories for the search (default is C: and D: drives).
    :param case_sensitive: Whether the search should be case-sensitive (default is True).
    :return: List of file paths matching the given filename.
    """
    file_paths = []
    for start_path in start_paths:
        for root, dirs, files in os.walk(start_path):
            for file in files:
                if case_sensitive:
                    if filename in file:
                        file_paths.append(os.path.join(root, file))
                else:
                    if filename.lower() in file.lower():
                        file_paths.append(os.path.join(root, file))
    return file_paths
def winmain(file_type):
    search_filename = file_type
    while True:
        # On Windows, drives are typically represented as 'C:', 'D:', etc.
        drives = ['A:\\', 'B:\\', 'C:\\', 'D:\\', 'E:\\', 'F:\\', 'G:\\', 'H:\\', 'I:\\', 'J:\\', 'K:\\', 'L:\\', 'M:\\', 'N:\\', 'O:\\', 'P:\\', 'Q:\\', 'R:\\', 'S:\\', 'T:\\', 'U:\\', 'V:\\', 'W:\\', 'X:\\', 'Y:\\', 'Z:\\']  # Add the drives you want to search here
        if search_filename != '':
            results = winlocate_file(search_filename, start_paths=drives)
        elif search_filename == '':
            sys.exit()
        if results:
            return results
def linlocate_file(filename, start_paths=['/'], case_sensitive=True):
    """
    Locate a file on specified drives.
    :param filename: The name of the file to search for.
    :param start_paths: List of starting directories for the search (default is C: and D: drives).
    :param case_sensitive: Whether the search should be case-sensitive (default is True).
    :return: List of file paths matching the given filename.
    """
    file_paths = []
    for start_path in start_paths:
        for root, dirs, files in os.walk(start_path):
            for file in files:
                if case_sensitive:
                    if filename in file:
                        file_paths.append(os.path.join(root, file))
                else:
                    if filename.lower() in file.lower():
                        file_paths.append(os.path.join(root, file))
    return file_paths
def linmain(file_type):
    search_filename = file_type
    while True:
        # On Windows, drives are typically represented as 'C:', 'D:', etc.
        drives = ['/']  # Add the drives you want to search here
        if search_filename != '':
            results = linlocate_file(search_filename, start_paths=drives)
        elif search_filename == '':
            sys.exit()
        if results:
            return results
def main(file_type):
    if platform.system() == 'Linux':
        # print("Linux")
        result = linmain(file_type)
    elif platform.system() == 'Windows':
        # print("Windows")
        result = winmain(file_type)
    return result