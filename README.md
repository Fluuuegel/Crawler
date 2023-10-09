# Crawler for 3D Warehouse

A small but not smart crawler

[3D Warehouse](https://3dwarehouse.sketchup.com/search/products)

## How to use

## Install

1. Install Chrome and corresponding version of Chrome WebDriver then configure PATH
2. ```pip
   Install selenium
   pip install selenium
   ```

## Edit

Get profile path (type `chrom://version/`  in Chrome to get the profile path) and replace line 16 of `spider.py`

**Change the default download dir in the Chrome** and range of accounts in `spider.py` at your ease

`index.txt` records download index

## Dump Cookies

Run `dump_cookies.py` -> Login account -> Rename cookies.pkl and throw it into the cookies directory

Every account can download 100 file from the website due to a server limitation

## Run

Run `spider.py`
