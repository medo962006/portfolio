import webbrowser as c
import time

link = input("enter the youtube link to visit : ")
times = int(input("how many times do you want to repeat per one turn : "))
time_per_turn = int(input("how much time delay between every turn"))

def open( link):
    c.open(link)


def repeat_in_new_tab( times, link):
    for i in range(times):
        c.open_new_tab(link)


    for i in range(times):
        open(link)
        repeat_in_new_tab(int(times), link)
        time.sleep(10)
        c.open(link)
        time.sleep(600)
