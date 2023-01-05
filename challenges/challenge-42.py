#!/usr/bin/env python3


challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

print(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}!")

print(f"My {trial[2].get('goggles')}! The {trial[2].get('eyes')} do {trial[3]}!")

print(f"My {nightmare[0].get('user').get('name').get('first')}! The {nightmare[0].get('kumquat')} do {nightmare[0].get('d')}!")

