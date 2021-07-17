import requests

def get_from_popular(id):
    json = requests.get("http://127.0.0.1:5000/popular").json()
    for photos in json["photos"]["photo"]:
        if(int(photos["id"])==id):
            index = json["photos"]["photo"].index(photos)
            return json["photos"]["photo"][index]

    return None


if __name__ =="__main__":
        PORT = 5000

        print(get_from_popular(3840221547))