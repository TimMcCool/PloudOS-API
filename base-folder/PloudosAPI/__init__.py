import requests
import http
from http.cookies import SimpleCookie
import json

class ProxyError(Exception):
    pass

class PloudosServer:
    def __init__(self, session, id, **entries):
        self.serverName = None
        self.serverIP = None
        self.id = id
        self.session = session
        self.__dict__.update(entries)

    def start(self, *, keep_traffic = True):

        print('\033[93m' + "[PLOUDOS] Starting server ..." + '\033[0m')

        requests.get(
        f"https://ploudos.com/manage/{self.id}/ajax2/queue/1",
        cookies = {
            "__qca" : "P0-156255044-1638389337089",
            "PLOUDOS_SESSION_1" : self.session.cookie['PLOUDOS_SESSION_1'],
            "PLOUDOS_SESSION_2" : self.session.cookie['PLOUDOS_SESSION_2'],
            "PLOUDOS_SESSION_3" : self.session.cookie['PLOUDOS_SESSION_3'],
            "PLOUDOS_SESSION_4" : self.session.cookie['PLOUDOS_SESSION_4'],
        },
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        }
        )



        if keep_traffic is True:

            print('\033[93m' + "[PLOUDOS] Keeping up traffic ..." + '\033[0m')


            #now traffic has to be caused to make sure the server will not shut down

            rstatus = ""

            while True:

                response = requests.get(
                    f"https://ploudos.com/manage/{self.id}/ajax2",
                    cookies = {
                        "__qca" : "P0-156255044-1638389337089",
                        "PLOUDOS_SESSION_1" : self.session.cookie['PLOUDOS_SESSION_1'],
                        "PLOUDOS_SESSION_2" : self.session.cookie['PLOUDOS_SESSION_2'],
                        "PLOUDOS_SESSION_3" : self.session.cookie['PLOUDOS_SESSION_3'],
                        "PLOUDOS_SESSION_4" : self.session.cookie['PLOUDOS_SESSION_4'],
                    },
                    headers = {
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.3c6 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
                    }
                )
                response = json.loads(response.text)

                if response["status"] == "WAITING_FOR_ACCEPT":
                    requests.get(
                        f"https://ploudos.com/manage/{self.id}/ajax2/accept",
                        cookies = {
                            "__qca" : "P0-156255044-1638389337089",
                            "PLOUDOS_SESSION_1" : self.session.cookie['PLOUDOS_SESSION_1'],
                            "PLOUDOS_SESSION_2" : self.session.cookie['PLOUDOS_SESSION_2'],
                            "PLOUDOS_SESSION_3" : self.session.cookie['PLOUDOS_SESSION_3'],
                            "PLOUDOS_SESSION_4" : self.session.cookie['PLOUDOS_SESSION_4'],
                        },
                        headers = {
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.3c6 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
                        }
                    )
                    print('\033[93m' + "[PLOUDOS] Automatically accepted." + '\033[0m')

                if not rstatus == response["status"]:
                    print('\033[95m' + "[PLOUDOS] Startup status: " + str(response["status"]) + '\033[0m')
                    rstatus = response["status"]


                try:
                    isRunning = response['isRunning']
                except KeyError:
                    isRunning = False
                if isRunning is True:
                    print('\033[92m' + "[PLOUDOS] Server started successfully." + '\033[0m')
                    break



        else:
            print('\033[93m' + "[PLOUDOS] Start request was sent." + '\033[0m')

        self = self.session.get_server(self.id)

    def stop(self):

        console = requests.get(
        f"https://ploudos.com/manage/{self.id}/ajax2/stop",
        cookies = {
                "__qca" : "P0-156255044-1638389337089",
                "PLOUDOS_SESSION_1" : self.session.cookie['PLOUDOS_SESSION_1'],
                "PLOUDOS_SESSION_2" : self.session.cookie['PLOUDOS_SESSION_2'],
                "PLOUDOS_SESSION_3" : self.session.cookie['PLOUDOS_SESSION_3'],
                "PLOUDOS_SESSION_4" : self.session.cookie['PLOUDOS_SESSION_4'],
            }
        )
        return console.text

    def force_stop(self):

        console = requests.get(
        f"https://ploudos.com/manage/{self.id}/ajax2/killServer",
        cookies = {
                "__qca" : "P0-156255044-1638389337089",
                "PLOUDOS_SESSION_1" : self.session.cookie['PLOUDOS_SESSION_1'],
                "PLOUDOS_SESSION_2" : self.session.cookie['PLOUDOS_SESSION_2'],
                "PLOUDOS_SESSION_3" : self.session.cookie['PLOUDOS_SESSION_3'],
                "PLOUDOS_SESSION_4" : self.session.cookie['PLOUDOS_SESSION_4'],
            }
        )
        return console.text

    def get_console(self):

        console = requests.get(
        f"https://ploudos.com/manage/{self.id}/console/refresh",
        cookies = {
                "__qca" : "P0-156255044-1638389337089",
                "PLOUDOS_SESSION_1" : self.session.cookie['PLOUDOS_SESSION_1'],
                "PLOUDOS_SESSION_2" : self.session.cookie['PLOUDOS_SESSION_2'],
                "PLOUDOS_SESSION_3" : self.session.cookie['PLOUDOS_SESSION_3'],
                "PLOUDOS_SESSION_4" : self.session.cookie['PLOUDOS_SESSION_4'],
            }
        )
        return console.text

    def regenerate_world(self, *, seed="", type="DEFAULT", hardcore=False):

        requests.post(
        f"https://ploudos.com/manage/{self.id}/world",
        cookies = {
                "__qca" : "P0-156255044-1638389337089",
                "PLOUDOS_SESSION_1" : self.session.cookie['PLOUDOS_SESSION_1'],
                "PLOUDOS_SESSION_2" : self.session.cookie['PLOUDOS_SESSION_2'],
                "PLOUDOS_SESSION_3" : self.session.cookie['PLOUDOS_SESSION_3'],
                "PLOUDOS_SESSION_4" : self.session.cookie['PLOUDOS_SESSION_4'],
        },
        data = {
            "seed" : seed,
            "type" : type,
            "hardcore" : hardcore
        }
        )

    def share_add(self, user, *, permissions : list):

        data = {"add_share" : user}
        for permission in permissions:
            data[permission] = ""

        requests.post(
        f"https://ploudos.com/manage/{self.id}/share",
        cookies = {
                "__qca" : "P0-156255044-1638389337089",
                "PLOUDOS_SESSION_1" : self.session.cookie['PLOUDOS_SESSION_1'],
                "PLOUDOS_SESSION_2" : self.session.cookie['PLOUDOS_SESSION_2'],
                "PLOUDOS_SESSION_3" : self.session.cookie['PLOUDOS_SESSION_3'],
                "PLOUDOS_SESSION_4" : self.session.cookie['PLOUDOS_SESSION_4'],
        },
        data = data
        )


    def share_remove(self, user):

        requests.post(
        f"https://ploudos.com/manage/{self.id}/share",
        cookies = {
                "__qca" : "P0-156255044-1638389337089",
                "PLOUDOS_SESSION_1" : self.session.cookie['PLOUDOS_SESSION_1'],
                "PLOUDOS_SESSION_2" : self.session.cookie['PLOUDOS_SESSION_2'],
                "PLOUDOS_SESSION_3" : self.session.cookie['PLOUDOS_SESSION_3'],
                "PLOUDOS_SESSION_4" : self.session.cookie['PLOUDOS_SESSION_4'],
        },
        data = {
            "with_user" : user,
            "remove" : "Delete"
        }
        )

    def ban(self, player):

        requests.post(
        f"https://ploudos.com/manage/{self.id}/player",
        cookies = {
                "__qca" : "P0-156255044-1638389337089",
                "PLOUDOS_SESSION_1" : self.session.cookie['PLOUDOS_SESSION_1'],
                "PLOUDOS_SESSION_2" : self.session.cookie['PLOUDOS_SESSION_2'],
                "PLOUDOS_SESSION_3" : self.session.cookie['PLOUDOS_SESSION_3'],
                "PLOUDOS_SESSION_4" : self.session.cookie['PLOUDOS_SESSION_4'],
        },
        data = {
            "username" : player,
            "add_ban" : ""
        }
        )

    def unban(self, player):

        requests.post(
        f"https://ploudos.com/manage/{self.id}/player",
        cookies = {
                "__qca" : "P0-156255044-1638389337089",
                "PLOUDOS_SESSION_1" : self.session.cookie['PLOUDOS_SESSION_1'],
                "PLOUDOS_SESSION_2" : self.session.cookie['PLOUDOS_SESSION_2'],
                "PLOUDOS_SESSION_3" : self.session.cookie['PLOUDOS_SESSION_3'],
                "PLOUDOS_SESSION_4" : self.session.cookie['PLOUDOS_SESSION_4'],
        },
        data = {
            "username" : player,
            "remove_ban" : ""
        }
        )

    def post_to_console(self, command):
        if command.startswith("/"):
            command = command[1:]


        requests.post(
            f"https://ploudos.com/manage/{self.id}/console/refresh",
            cookies = {
                "__qca" : "P0-156255044-1638389337089",
                "PLOUDOS_SESSION_1" : self.session.cookie['PLOUDOS_SESSION_1'],
                "PLOUDOS_SESSION_2" : self.session.cookie['PLOUDOS_SESSION_2'],
                "PLOUDOS_SESSION_3" : self.session.cookie['PLOUDOS_SESSION_3'],
                "PLOUDOS_SESSION_4" : self.session.cookie['PLOUDOS_SESSION_4'],
            },
            data = {"command" : command}
        )


class UncreatedPloudosServer:
    def __init__(self, id):
        self.serverName = None
        self.serverIP = None
        self.id = id
        self.session = None


class PloudosSession:

    def __init__(self, username : str, cookie : http.cookies.SimpleCookie):
        self.username = username,

        self.cookie = {
            "__qca" : "P0-156255044-1638389337089",
            "PLOUDOS_SESSION_1" : cookie['PLOUDOS_SESSION_1'].value,
            "PLOUDOS_SESSION_2" : cookie['PLOUDOS_SESSION_2'].value,
            "PLOUDOS_SESSION_3" : cookie['PLOUDOS_SESSION_3'].value,
            "PLOUDOS_SESSION_4" : cookie['PLOUDOS_SESSION_4'].value,
        }


    def get_server(self, id):

        response = requests.get(
            f"https://ploudos.com/manage/{id}/ajax2",
            cookies = {
                "__qca" : "P0-156255044-1638389337089",
                "PLOUDOS_SESSION_1" : self.cookie['PLOUDOS_SESSION_1'],
                "PLOUDOS_SESSION_2" : self.cookie['PLOUDOS_SESSION_2'],
                "PLOUDOS_SESSION_3" : self.cookie['PLOUDOS_SESSION_3'],
                "PLOUDOS_SESSION_4" : self.cookie['PLOUDOS_SESSION_4'],
            },
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
            }
        )
        response = json.loads(response.text)

        return PloudosServer(self, id, **response)


    def get_servers_with_name(self, name : str):

        servers = self.servers()

        servers = servers['owned'] + servers['shared']

        raw_servers = []
        for item in servers:
            server = item.__dict__
            server["_id"] = server["id"]
            server.pop("id")
            server.pop("session")
            raw_servers.append(server)

        raw_servers = list(filter(lambda raw_servers: raw_servers['serverName'] == name, raw_servers))

        servers = []
        for item in raw_servers:
            servers.append(PloudosServer(self, item['_id'], **item))

        return servers


    def servers(self): #web scrapes the html

        def web_scrape_servers(self, response):

            index = 0
            server_ids = []
            while index != -1:
                index = response.find('<a href="../manage/')
                response = response.replace('<a href="../manage/', '', 1)
                i = index
                endpoint = ""
                while response[i] != '/':
                    endpoint += response[i]
                    i += 1
                if not endpoint in server_ids:
                    if not "\n" in endpoint:
                        server_ids.append(endpoint)

                index = response.find('<a href="../manage/') #remove other related result
                response = response.replace('<a href="../manage/', '', 1)

            while True:
                try:
                    server_ids.remove(' <div class="server"><div class="status"><div class="online"><')
                except Exception:
                    break
            while True:
                try:
                    server_ids.remove(' <div class="server"><div class="status"><div class="offline"><')
                except Exception:
                    break

            return server_ids

        response = requests.get(
            f"https://ploudos.com/server/?force_lang=EN",
            cookies = {
                "__qca" : "P0-156255044-1638389337089",
                "PLOUDOS_SESSION_1" : self.cookie['PLOUDOS_SESSION_1'],
                "PLOUDOS_SESSION_2" : self.cookie['PLOUDOS_SESSION_2'],
                "PLOUDOS_SESSION_3" : self.cookie['PLOUDOS_SESSION_3'],
                "PLOUDOS_SESSION_4" : self.cookie['PLOUDOS_SESSION_4'],
            },
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
            }
        )

        try:
            response1, response2= response.text.split("<h1>Your Server</h1>")
        except Exception:
            if "Please disable your VPN/Proxy" in response.text:
                raise ProxyError("Your IP address is blocked by ploudos.\nIf you're using an online IDE (like replit.com), try running the code on your computer instead.")

        server_ids = web_scrape_servers(self, response1)

        my_servers = []
        for server_id in server_ids:
            try:
                my_servers.append(self.get_server(server_id))
            except Exception:
                my_servers.append(UncreatedPloudosServer(server_id))


        server_ids = web_scrape_servers(self, response2)

        shared_servers = []
        for server_id in server_ids:
            try:
                shared_servers.append(self.get_server(server_id))
            except Exception:
                continue

        return dict(
            owned = my_servers,
            shared = shared_servers
        )


def login(username, password): #logs in to the ploudos account
    response = requests.post(
        "https://ploudos.com/login/",
        data={
            "username": username,
            "password": password
        },
    )
    cookie = SimpleCookie()
    cookie.load(response.cookies)

    return PloudosSession(username, cookie)
