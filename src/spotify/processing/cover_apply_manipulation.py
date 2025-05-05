import importlib
import base64
from io import BytesIO

from utils import reclog
from utils.extract_playlist_id import extract_playlist_id
from manipulate.grayscale import grayscale
from spotify.download_playlist_cover import download_playlist_cover

def cover_apply_manipulation(spot, playlist_url, method_name):
    # importar a função de manipulação correspondente ao nome passado pra função
    module = importlib.import_module(f"manipulate.{method_name}")
    manipulation_method = getattr(module, method_name)

    # extrair o id da url da playlist
    playlist_id = extract_playlist_id(playlist_url)

    # buffer pra salvar temporariamente a imagem
    buffer = BytesIO()

    # baixar a capa da playlist, aplicar a manipulação e salvar
    cover = download_playlist_cover(spot=spot, playlist_id=playlist_id)
    cover = manipulation_method(cover)
    cover.save(buffer, format='JPEG')

    data_bytes = buffer.getvalue()
    if len(data_bytes) > 256000:
        raise ValueError("Image exceeds 256KB")

    # passar a imagem pra base64 e aplicar na playlist
    cover = base64.b64encode(data_bytes).decode('utf-8')
    spot.playlist_upload_cover_image(playlist_id=playlist_id, image_b64=cover)

    reclog.info(f"Manipulated current cover using {method_name}")