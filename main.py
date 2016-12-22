import threading
from Queue import Queue
from spider import Spider
from domain import *
from general import *

# Set the defaults
PROJECT_NAME = 'thenewboston'
HOMEPAGE = 'https://thenewboston.com/'

# Enabling user input
PROJECT_NAME = raw_input("Enter the project name\n")
HOMEPAGE = raw_input("Enter the website name\n")

DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
NUMBER_OF_THREADS = int(raw_input("Enter the number of threads to crawl this website\n"))
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name,url)
        queue.task_done()

# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

# Check for items in queue. If yes, crawl them
def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print str(len(queued_links))+" links in the current queue"
        create_jobs()

# Call all the functions
create_workers()
crawl()
