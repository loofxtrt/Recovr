from utils import reclog

playlist_name = "shoegaze"
description = "Lorem Ipsum"
old_prefix = "#"
new_prefix = ":"

reclog.info((f"Checking for {playlist_name}", "green bold"))

reclog.info("No description found, moving on")

reclog.info((f"Current description:", "green"), description)

reclog.info((f"Prefix for {playlist_name} changed:", "green"), f"{old_prefix} {new_prefix}")

reclog.info(f"Old prefix not found in {playlist_name}, moving on")