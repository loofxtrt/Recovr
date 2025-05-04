from utils import reclog

playlist_name = "shoegaze"
description = "Lorem Ipsum"
old_prefix = "#"
new_prefix = ":"

reclog.info(label=f"Checking for b<{playlist_name}>")

reclog.info(message="No description found, moving on")

reclog.info(label=f"<Current description>green", message=description)

reclog.info(label=f"Prefix for b<{playlist_name}> changed", message=f"b<'{old_prefix}' '{new_prefix}'>")

reclog.info(message=f"Old prefix not found in {playlist_name}, moving on")