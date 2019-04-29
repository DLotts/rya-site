#!/usr/bin/env python
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# This is confluenceuser.cgi
import sys
import cgi
import os
import subprocess
import sscommon

def userExists(username):
    os.chdir(sscommon.clipath)
    
    try:
        subprocess.check_output([
        '/usr/bin/java', '-jar', sscommon.cwikijar,
        '-v',
        '--server', 'https://cwiki.apache.org/confluence',
        '--user', sscommon.config['jira']['username'],
        '--password', sscommon.config['jira']['password'],
        '--action', 'getUser',
        '--userId', username,
        ], stderr=subprocess.STDOUT
        )
        return True
    except subprocess.CalledProcessError as e:
        sys.stderr.write(e.output + "\n")
        sys.stderr.flush()
        return False
    
# CGI interface
xform = cgi.FieldStorage();

username = xform.getvalue('username')
for user in username.split(","):
    if not userExists(user):
        print("Status: 404\r\n\r\nUser %s does not exist!" % user)
        sys.exit(0)

print("Status: 200\r\n\r\nUser exists")
