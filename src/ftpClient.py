import ftplib
import matplotlib.pyplot as plt
import csv


serverName = '192.168.1.11'
fileNameData = 'datalog.csv'
def main():
    # Connect to the FTP server
    ftpFH = ftplib.FTP(serverName)

    # Do an anonymous login
    ftpFH.login();

    ftpFH.cwd('\SDDisk\data')  # Change to correct directory
    ftpFH.retrlines('LIST')  # List the directory

    with open('tet', 'wb') as fp:
        ftpFH.retrbinary('RETR ' + fileNameData, fp.write)
        ftpFH.close()
    print(fp)



if __name__ == "__main__":
    main()