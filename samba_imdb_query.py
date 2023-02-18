from imdb import Cinemagoer
import pprint
import os
import re
import time
import sys
from smb.SMBConnection import SMBConnection

"""
pip install cinemagoer
pip install pysmb
"""

SMB_SERVER_IP = "192.168.0.107"
SMB_SERVER_PORT = 139
SMB_USERNAME = ""
SMB_PASSWORD = ""
SMB_CLIENT_NAME = "client"
SMB_SHARE_NAME = 'pihomeopen'
SMB_FOLDER = "/FreeMovies"
IMDB_QUERY_RATE_LIMIT_SECONDS = 5

conn = SMBConnection(SMB_USERNAME, SMB_PASSWORD, SMB_CLIENT_NAME, SMB_SERVER_IP, use_ntlm_v2=True)
conn.connect(SMB_SERVER_IP, SMB_SERVER_PORT)


file_list = conn.listPath(SMB_SHARE_NAME, SMB_FOLDER)
for smbFile in file_list:
    localFileName=smbFile.filename
    try:
        match = re.search(r'^(.+)(\d{4})', localFileName)
        if match:
            localMovieTitle=match.group(1)
            localMovieYear=match.group(2)
            print(localMovieTitle.ljust(30, " ")+" ("+str(localMovieYear),end =") # ")
        else:
            print("CAN'T BE ANALYZED: "+localFileName)
            continue
        ia = Cinemagoer()
        # We are searching for IMDB movies by local movie name and year
        imdbFoundMovies = ia.search_movie(localMovieTitle)
        """
        We get an array like this:
        [<Movie id:1571222[http] title:movie_title (year)_>,
        <Movie id:1571222[http] title:movie_title (year)_>,
        <Movie id:1571222[http] title:movie_title (year)_>],
        """
        # go through the results
        if len(imdbFoundMovies) > 0:
            for imdbFoundMovie in imdbFoundMovies:
                id=imdbFoundMovie.getID()
                foundTitle=imdbFoundMovie["title"]
                imdbMovie=ia.get_movie(id)          
                imdbMovieYear=str(imdbMovie.get('year'))
                if(imdbMovieYear==localMovieYear):
                    print(
                        foundTitle.ljust(30, " ")+
                        (" # https://www.imdb.com/title/tt"+id+"/").ljust(45, " "),end =" # ")
                    if 'rating' in imdbMovie.keys():
                        print("RATING # "+str(imdbMovie['rating'])+" # "+(", ".join(imdbMovie['genres'])),end ="")
                    else:
                        print("RATING # N/A",end ="")
                    break
                else:
                    print(".",end ="")
                time.sleep(IMDB_QUERY_RATE_LIMIT_SECONDS)
        else:
            print("no items found",end ="")
        print("")
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print("\nERRROR: "+str(e)+"##############################################")
    time.sleep(IMDB_QUERY_RATE_LIMIT_SECONDS)








