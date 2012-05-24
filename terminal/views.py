 # Copyright (C) 2010 Lorenzo Sfarra (lorenzosfarra@ubuntu.com)
 #
 # This program is free software; you can redistribute it and/or
 # modify it under the terms of the GNU General Public License
 # as published by the Free Software Foundation; either version 2
 # of the License, or (at your option) any later version.
 #
 # This program is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License
 # along with this program; if not, write to the Free Software
 # Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 #


from django.shortcuts import render_to_response
from django.http import HttpResponse
from commands import getoutput
import os.path

# global variable
CWD = "/home/lorenzo"

def index(request):
    return render_to_response("index.html")

def is_trusted_command(command):
    #TODO: check if it's a trusted command
    return True

def cmd(request, command):
    global CWD
    if command.startswith("cd "):
        new_path = command.split(" ")[1]
        if not new_path.startswith("/"):
            # relative path
            new_path = os.path.join(CWD, new_path)
        if os.path.isdir(new_path):
            CWD = new_path
            output = ""
        else:
            output = "cd: " + new_path + ": No such file or directory"
    elif is_trusted_command(command):
        output = getoutput("cd %s; %s" %(CWD,command))
    else:
        output = "Untrusted command."
    return HttpResponse(output);
