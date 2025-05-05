import base64
from io import BytesIO

from utils import reclog
from utils.extract_playlist_id import extract_playlist_id
from pillow.grayscale import grayscale
from spotify.utils.download_playlist_cover import download_playlist_cover

def cover_grayscale(spot, playlist_url):
    playlist_id = extract_playlist_id(playlist_url) # extrair o id da url da playlist
    buffer = BytesIO() # buffer pra salvar temporariamente a imagem

    # baixar a capa da playlist e converter pra grayscale
    cover = grayscale(download_playlist_cover(spot=spot, playlist_id=playlist_id))
    cover.save(buffer, format='JPEG')

    # fallback
    data_bytes = buffer.getvalue()
    if len(data_bytes) > 256000:
        raise ValueError("Image exceeds 256KB")

    # passar a imagem pra base64 e aplicar na playlist
    cover_64 = base64.b64encode(data_bytes).decode('utf-8')
    spot.playlist_upload_cover_image(playlist_id=playlist_id, image_b64=cover_64)

    reclog.info("Converted current cover to to grayscale")