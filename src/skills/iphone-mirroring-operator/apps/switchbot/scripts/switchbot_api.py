"""SwitchBot Open API v1.1 helper: list devices and scenes, read status, run a scene.

The token and secret come from the SWITCHBOT_TOKEN / SWITCHBOT_SECRET
environment variables and are never printed.

  switchbot_api.py devices          # each device and its status
  switchbot_api.py scenes           # scene ids and names
  switchbot_api.py run <scene>      # run a scene by id or exact name, then print light status
"""
from __future__ import annotations

import base64
import hashlib
import hmac
import json
import os
import sys
import time
import urllib.request
import uuid

BASE = "https://api.switch-bot.com/v1.1"


def call(path: str, method: str = "GET") -> dict:
    token = os.environ["SWITCHBOT_TOKEN"].strip()
    secret = os.environ["SWITCHBOT_SECRET"].strip()
    t = str(int(time.time() * 1000))
    nonce = uuid.uuid4().hex
    sign = base64.b64encode(
        hmac.new(secret.encode(), (token + t + nonce).encode(), hashlib.sha256).digest()
    ).decode()
    req = urllib.request.Request(
        BASE + path,
        method=method,
        data=b"{}" if method == "POST" else None,
        headers={"Authorization": token, "sign": sign, "t": t, "nonce": nonce,
                 "Content-Type": "application/json; charset=utf8"},
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.load(r)


def print_devices() -> None:
    for d in call("/devices")["body"].get("deviceList", []):
        b = call(f"/devices/{d['deviceId']}/status").get("body", {})
        print(f"{d['deviceName']} ({d['deviceType']}): power={b.get('power')} "
              f"brightness={b.get('brightness')} colorTemperature={b.get('colorTemperature')} "
              f"color={b.get('color')}")


def scenes() -> list[dict]:
    return call("/scenes").get("body", [])


def main(argv: list[str]) -> int:
    if not argv or argv[0] not in {"devices", "scenes", "run"}:
        print(__doc__)
        return 2
    if argv[0] == "devices":
        print_devices()
    elif argv[0] == "scenes":
        for s in scenes():
            print(f"{s['sceneId']}  {s['sceneName']}")
    else:
        if len(argv) < 2:
            print("run needs a scene id or name")
            return 2
        target = argv[1]
        match = [s for s in scenes() if target in (s["sceneId"], s["sceneName"])]
        if len(match) != 1:
            print(f"scene not found or ambiguous: {target}")
            return 1
        r = call(f"/scenes/{match[0]['sceneId']}/execute", "POST")
        print(f"run {match[0]['sceneName']}: {r.get('statusCode')} {r.get('message')}")
        time.sleep(8)
        print_devices()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
