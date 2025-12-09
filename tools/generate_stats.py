#!/usr/bin/env python3
# tools/generate_stats.py
import os
import sys
import argparse
import requests
from PIL import Image, ImageDraw, ImageFont
from collections import Counter

GITHUB_API = "https://api.github.com"

def get_repos(user, token=None):
    repos = []
    page = 1
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"token {token}"
    while True:
        r = requests.get(f"{GITHUB_API}/users/{user}/repos", params={"per_page":100,"page":page}, headers=headers)
        r.raise_for_status()
        batch = r.json()
        if not batch:
            break
        repos.extend(batch)
        page += 1
    return repos

def top_languages(repos):
    langs = []
    for r in repos:
        if r.get("language"):
            langs.append(r["language"])
    c = Counter(langs)
    return c.most_common(6)

def generate_stats_image(data, outpath):
    W, H = 900, 260
    bg = (11,18,32)
    fg = (230,238,248)
    accent = (47,128,237)

    img = Image.new("RGB",(W,H),bg)
    d = ImageDraw.Draw(img)
    try:
        f = ImageFont.truetype("DejaVuSans.ttf", 20)
        f_title = ImageFont.truetype("DejaVuSans.ttf", 28)
    except:
        f = ImageFont.load_default()
        f_title = f

    d.text((24,20),"GitHub Overview — {}".format(data["user"]), font=f_title, fill=fg)
    d.text((24,64), f'Total public repos: {data["total_repos"]}', font=f, fill=fg)
    d.text((24,96), f'Total stars (sum): {data["total_stars"]}', font=f, fill=fg)
    d.text((24,128), f'Followers: {data["followers"]}', font=f, fill=fg)

    # draw top languages
    d.text((24,174), "Top languages:", font=f, fill=fg)
    x = 160
    y = 172
    for lang, count in data["top_langs"]:
        d.rectangle([x, y, x+ (count*26), y+22], fill=accent)
        d.text((x+6, y+2), f"{lang} ({count})", font=f, fill=(255,255,255))
        y += 34
        if y > 230:
            x += 260
            y = 172

    img.save(outpath, optimize=True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", required=True)
    parser.add_argument("--out", default="assets")
    args = parser.parse_args()
    token = os.environ.get("GITHUB_TOKEN")
    repos = get_repos(args.user, token)
    total_stars = sum(r.get("stargazers_count",0) for r in repos)
    top = top_languages(repos)
    # get user info
    u = requests.get(f"{GITHUB_API}/users/{args.user}", headers={"Accept":"application/vnd.github.v3+json"})
    u.raise_for_status()
    user_info = u.json()
    data = {
        "user": args.user,
        "total_repos": len(repos),
        "total_stars": total_stars,
        "followers": user_info.get("followers",0),
        "top_langs": top
    }
    os.makedirs(args.out, exist_ok=True)
    generate_stats_image(data, os.path.join(args.out,"stats.png"))
    print("Generated:", os.path.join(args.out,"stats.png"))

if __name__ == "__main__":
    main()
