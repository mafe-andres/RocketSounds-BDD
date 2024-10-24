import os
import json
import random
from data import Data
from player import Player

def search_media(search_input):
    for m in media:
        if search_input == m.title:
            return m
    return None
            

def shuffle(data):
    random.shuffle(media)
    player.play(media)

def playlists():
    pass
    # TODO
    # 1. Llamar método load playlists del usuario
    # 2. Crear menu, opciones: buscar una playlist, crear una playlist
    # 3. Buscar una playlist:   imprimir con numero las playlists del usuario. 
    #                           crear un objeto playlist con el titulo, llamar complete_playlist
    #                           player.play(playlist)
    # 4. Crear una playlist: crear un objeto playlist con el titulo
    #                        crear bucle que pida nombres de canciones, las busque usando search_media
    #                        y las agregue al playlist usando add_media

def search():
    search_input = input("Search: ")
    media = search_media(search_input)
    if media != None:  
        print(media)
        while True:
            print("\n")
            print("1. Play")
            print("2. Go back")
            
            choice = input("Choose an option: ")
            if choice == '1':
                player.play(media)
            elif choice == '2':
                break
            else:
                print("Invalid choice. Please select a valid option.")
    else:
        print("Nothing found.")
        
def login(users_path):
    with open(users_path) as file:
        user_data = json.load(file)
        users = user_data["users"]
        
    while True:
        valid_user = False
        username = input("Username: ")
        password = input("Password: ")
        for user in users:
            if user["username"] == username and user["password"] == password:
                valid_user = True
                break
        if valid_user:
            # TODO 
            # 1. Crear objeto usuario
            return True
        else:
            print('Invalid username or password.')
    
def menu():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
    data_dir = os.path.join(project_root, 'data')
    
    media_dir = os.path.join(project_root, 'media')
    global player
    player = Player(media_dir)
    
    # Login de usuario
    users_path = os.path.join(data_dir, 'users.json')
    if not login(users_path):
        return
    
    # Cargar datos en un objeto
    podcasts_path = os.path.join(data_dir, 'podcast_data.json')
    music_path = os.path.join(data_dir, 'music_data.json')
    data = Data()
    data.load_podcasts(podcasts_path)
    data.load_music(music_path)
    global media
    media = data.songs + data.podcast_episodes
    
    # Menu principal
    while True:
        print("\nMenu:")
        print("1. Shuffle")
        print("2. Playlists")
        print("3. Search")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            shuffle(data)
        elif choice == '2':
            playlists()
        elif choice == '3':
            search()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    menu()