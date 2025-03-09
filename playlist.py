

# Make a dictionary called 'library'
# The Keys are the playlist and the values will be a list of songs
# Make a function to add a playlist to the library or add a song to a playlist

library = {}

def addPlaylist(playlist):

    if playlist not in library:

        library.setdefault( playlist , [])
    
    else:

        print( "Already have a playlist named "+ playlist )

def addSong(playlist, song):

    if playlist in library:

        library[playlist].append(song)
    
    else:

        print(playlist + " does not exist.")

try:
    print("Welcome to your music library")

    choice = 0

    while choice != 6:

        print("\n1) Create a Playlist"+
              "\n2) Add a Song to a Playlist"+
              "\n3) Open a Playlist"+
              "\n4) Show all Playlist"+
              "\n5) Show all Songs"+
              "\n6) Close App")

        choice = int(input("\nEnter Choice Here: "))

        #1) Create a Playlist
        if choice == 1:

            playlist = input("Playlist Name: ")
            addPlaylist(playlist)

        #2) Add a Song to a Playlist   
        elif choice == 2:

            playlist = input("What playlist would you like to add to?: ")
            song = input("\nSong Name: ")
            addSong(playlist,song)

        #3) Open a Playlist
        elif choice == 3:

            playlist = input("What playlist would you open?: ")
            print(library[playlist])

        #4) Show all Playlist
        elif choice == 4:
            if library:
                print(list(library.keys()))
            
            else:

                print("You haven't created any playlsit yet!")

        #5) Show all Songs
        elif choice == 5:
            
            if library:

                print(list(library.values()))
            
            else:

                print("You haven't created any playlsit yet!")
            

    
    print("Closing App......")


except ValueError:
    print('Please a valid value.')

except KeyError:
    print("That playlist has not been created yet.")

except:
    print("Something went wrong!")


