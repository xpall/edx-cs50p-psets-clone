import re


username = input("URL or username: ").strip()


if username := re.search(r"^(?:(?:(?:https?)?://(?:www\.)?)?twitter\.com/)?(.+)$", username, re.IGNORECASE):
    username = username.group(1)


print(f"username: {username}")