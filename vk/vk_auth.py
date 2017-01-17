# -*- coding: utf-8 -*-

import http.cookiejar
from html.parser import HTMLParser
import urllib
from urllib import parse

class FormParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.url = None
        self.params = {}
        self.in_form = False
        self.form_parsed = False
        self.method = "GET"

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag == "form":
            if self.form_parsed:
                raise RuntimeError("Second form on page")
            if self.in_form:
                raise RuntimeError("Already in form")
            self.in_form = True
        if not self.in_form:
            return
        attrs = dict((name.lower(), value) for name, value in attrs)
        if tag == "form":
            self.url = attrs["action"]
            if "method" in attrs:
                self.method = attrs["method"].upper()
        elif tag == "input" and "type" in attrs and "name" in attrs:
            if attrs["type"] in ["hidden", "text", "password"]:
                self.params[attrs["name"]] = attrs["value"] if "value" in attrs else ""

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "form":
            if not self.in_form:
                raise RuntimeError("Unexpected end of <form>")
            self.in_form = False
            self.form_parsed = True

def auth(email, password, client_id, scope):
    def split_key_value(kv_pair):
        kv = kv_pair.split("=")
        return kv[0], kv[1]

    # Authorization form
    def auth_user(email, password, client_id, scope, opener):
        response = opener.open(
            "https://oauth.vk.com/oauth/authorize?" + \
            "redirect_uri=http://oauth.vk.com/blank.html&response_type=token&v=5.52&" + \
            "client_id=%s&scope=%s&display=wap" % (client_id, ",".join(scope))
            )

        # Пример запроса
        # https://oauth.vk.com/authorize?client_id=5703171&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=wall&response_type=token&v=5.52

        doc = response.read()
        vkparser = FormParser()
        vkparser.feed(doc.decode('utf-8'))
        vkparser.close()
        if not vkparser.form_parsed or vkparser.url is None or "pass" not in vkparser.params or \
          "email" not in vkparser.params:
              raise RuntimeError("Something wrong")
        vkparser.params["email"] = email
        vkparser.params["pass"] = password
        if vkparser.method == "POST":
            req_params = parse.urlencode(vkparser.params).encode("utf-8")
            response = opener.open(vkparser.url, req_params)
        else:
            raise NotImplementedError("Method '%s'" % vkparser.method)
        return response.read(), response.geturl()

    # Permission request form
    def give_access(doc, opener):
        vkparser = FormParser()
        vkparser.feed(doc)
        vkparser.close()
        if not vkparser.form_parsed or vkparser.url is None:
              raise RuntimeError("Something wrong")
        if vkparser.method == "POST":
            req_params = parse.urlencode(vkparser.params).encode("utf-8")
            response = opener.open(vkparser.url, req_params)
        else:
            raise NotImplementedError("Method '%s'" % vkparser.method)
        return response.geturl()


    if not isinstance(scope, list):
        scope = [scope]
    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()),
        urllib.request.HTTPRedirectHandler())
    doc, url = auth_user(email, password, client_id, scope, opener)
    if parse.urlparse(url).path != "/blank.html":
        # Need to give access to requested scope
        url = give_access(doc, opener)
    if parse.urlparse(url).path != "/blank.html":
        raise RuntimeError("Expected success here")
    answer = dict(split_key_value(kv_pair) for kv_pair in parse.urlparse(url).fragment.split("&"))
    if "access_token" not in answer or "user_id" not in answer:
        raise RuntimeError("Missing some values in answer")
    return answer["access_token"], answer["user_id"]

#Пример запроса
#https://oauth.vk.com/authorize?client_id=5703171&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=wall&response_type=token&v=5.52

#Пример ответа
#https://oauth.vk.com/blank.html#access_token=b61d9b1104aa4167b6d78f808777d3d26e3d8c7c2d3a53c802c62b5236cc93bc50edeea81eae594b3ee8e&expires_in=86400&user_id=163222298