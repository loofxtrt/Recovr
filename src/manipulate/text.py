from PIL import Image, ImageDraw, ImageFont

def text(cover, text, color):
    cover = cover.convert("RGBA") # converter pra rgba pra manter a qualidade
    draw_obj = ImageDraw.Draw(cover) # criar o objeto de draw

    # configurar o texto
    font = ImageFont.truetype("/media/luan/seagate/workspace/coding/projects/software/recovr/media/fonts/helmet/Helmet-Regular.ttf", 160)
    pos = (20, 475)

    # desenhar o texto e retornar a capa atualizada
    draw_obj.text(pos, text=text, font=font, fill=color)
    return cover