from django.shortcuts import render
import subprocess
import os
import re
import sys
from multiprocessing import Process

def start_server():
    os.system('node /home/daniel/djangoSocketIo/server_monitor/serverSockets_iO.js')
    


def home(request):
    p = Process(target=start_server).start()
    return render(request,'index.html')


