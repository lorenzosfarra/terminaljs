/* Copyright (C) 2010 Lorenzo Sfarra (lorenzosfarra@ubuntu.com)
 
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. * See the
 * GNU General Public License for more details.
 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA * 02110-1301, USA.
 */



// The command line prompt
var cliPrompt = "lorenzo@josie:~$ ";

// the server address where the real console exists
var cliHost = "http://localhost:8000/";

function isTrustedCommand(command) {
    /** 
     * Function to check that the given command is trusted.
     * @param command the command to check
     * @return boolean
     */
    // TODO: check that this is a trusted command!
    return true;
}

function executeCommand(text, cliPrompt, command) {
    /**
     * Function to execute the given command through an AJAX call
     * and retrieve the result to update the textarea value.
     * @param text the current textarea value
     * @param cliPrompt the prompt
     * @param command the command to execute
     */
    // build the URL for the command
    remoteCommand = cliHost + "cmd/" + command;
    output = "";
    // Perform the AJAX call
    $.ajax({
        url: remoteCommand,
        type: 'GET',
        dataType: 'text',
        error: function(data, textStatus, errorThrown) {
            // readyState == 4? Error.
            if (data.readyState == 4) {
                output = "Connection error.\n"
            }
        },
        success: function(data) {
            output = data + "\n";
            $("#commandline").val([text, output, cliPrompt].join("\n"));
            // Textarea with focus at bottom
            $("#commandline").animate({ scrollTop: 99999}, 10);
        }
    });

}

function onEnterKey() {
    /* Function called when a user press the Enter key on its keyboard. */
    text = $("#commandline").val();
    // Get the command
    promptIndex = text.lastIndexOf(cliPrompt);
    // build the command
    command = text.substring(promptIndex + cliPrompt.length);
    if (command == "clear") {
        // simply clear the textarea value
        $("#commandline").val(cliPrompt);
    } else if (isTrustedCommand(command)) {
        executeCommand(text, cliPrompt, command);
    } else {
        output = "Invalid command.";
        $("#commandline").val([text,output,cliPrompt].join("\n"));
    }
}

