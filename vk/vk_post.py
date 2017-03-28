# -*- coding: UTF-8 -*-

import vk.vk_auth
import json
import urllib
from urllib import parse
import sys
import vk.vk_conf
import text.generator


def call_api(method, params, token):
    params.append(("access_token", token))
    params.append(("v", "5.60"))
    encoded_params = bytes(urllib.parse.urlencode(params).encode())
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
    password = vk.vk_conf.credentials.get('passwd')
    client_id = "5703171"  # Vk application ID
    group_id = "-106824176"
    post = text.generator.get_text()
    ss_sentence = text.generator.get_ss_sentence(post)
    message = text.generator.get_printable_sentence(ss_sentence)
    post_auth = "1"
    token, user_id = vk.vk_auth.auth(email, password, client_id, "wall")
    result = call_api("wall.post", [("owner_id", group_id),("message",message),("from_group",post_auth)], token)
    return result