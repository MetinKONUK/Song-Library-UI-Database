from a import *
import time
print("""
******WELCOME*****
1.Add Song
2.Delete Song
3.Query Total Duration
Q to Exit
******************
""")
while True:
    p = input("Select Operation Number: ")
    if p.lower() == "q":
        single_library.connection.close()
        break
    elif p == "1":
        a,b,c,d,e = input("Name: "),input("Singer: "),input("Albume: "),input("Production Company: "),int(input("Duration(in seconds): "))
        print("Song is being added to the library...")
        single_library.add_song(a,b,c,d,e)
        time.sleep(3)
        print("Song is in library for current.Thanks a lot for contributing this song!")
    elif p == "2":
        name = input("Please determine the name of the song: ")
        if name:
            print("{} song is being deleted...".format(name))
            single_library.delete_song(name)
            time.sleep(3)
            print("Deletion complete successfully!")
    elif p == "3":
        print("Retrieving duration datas please wait for a second...")
        single_library.calc_total_am()
        
    else:
        print("Please select a valid operation")
