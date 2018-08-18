"""
This module downloads the test cases from the file provided
and saves using the string as starting name for all files
makes it easy for executor to run.
"""
import sys
import urllib.request


def download_tests(link_file='links.txt', sve_name='test'):
    """
    Downloads the test cases from the link file and saves it using the sve_name as the
    starting of the test case files
    :param link_file:links file to download test cases, default file "links.txt"
    :param sve_name: downloaded test cases starting name to save , default "test"
    :return: None
    """
    f = open(link_file)
    for num, line in enumerate(f):
        try:
            opener = urllib.request.urlopen(line)
            fil = open(sve_name+str(num)+".txt", "w")
            wr=str(opener.read())[2:-1]
            fil.writelines(wr)
            fil.close()
        except ValueError:
            pass


if __name__ == '__main__':
    if len(sys.argv) > 1:
        save_name = sys.argv[1]
        if len(sys.argv) > 2:
            links = sys.argv[2]
        else:
            links = "links.txt"
        download_tests(links, save_name)
    else:
        download_tests()
