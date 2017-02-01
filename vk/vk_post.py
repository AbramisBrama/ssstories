# -*- coding: UTF-8 -*-

import vk.vk_auth
import json
import urllib
from urllib import parse
import os
import getpass
import sys
import vk.vk_conf
import text.generator


def call_api(method, params, token):
    params.append(("access_token", token))
    params.append(("v", "5.60"))
    encoded_params = parse.urlencode(params)
    #url = "https://api.vk.com/method/%s?%s" % (method, encoded_params)
    #return json.loads(urllib.request.urlopen(url).read().decode("utf-8"))["response"]
    url = "https://api.vk.com/method/%s?" % method
    req = urllib.request.Request(url,encoded_params)
    with urllib.request.urlopen(req) as response:
        result = response.read().decode("utf-8")
    return json.loads(result)["response"]

def wallpost():
    directory = None
    if len(sys.argv) == 2:
        directory = sys.argv[1]
    email = vk.vk_conf.credentials.get('email')
    # password = getpass.getpass()
    password = vk.vk_conf.credentials.get('passwd')
    client_id = "5703171"  # Vk application ID
    group_id = "-106824176"
    message = text.generator.get_text()
    post_auth = "1"
    token, user_id = vk.vk_auth.auth(email, password, client_id, "wall")
    result = call_api("wall.post", [("owner_id", group_id),("message",message),("from_group",post_auth)], token)
    return result



post_result=wallpost()
print(post_result)
# https://api.vk.com/method/wall.post?owner_id=-106824176&message="АВТОМАТИЧЕСКИЕ ПРИВЕТИКИ"&from_group=1&access_token=a329408415dc02dffa04b622d668f722e182f3acfdabbe74b8363d11f23fb117359a7577ff93a674614b5&v=5.60