from PIL import Image, ImageDraw, ImageFont

from genetic import Gene


def comb_layers(layers):
    final = Image.new('RGBA', (120, 130), 'white')
    for im_path in layers:
        if im_path:
            im = Image.open(im_path)
            final.paste(im, mask=im)
    return final


def tail_wings_path(gene):
    PREFIX = 'assets/0-tail-wings/'
    SUFFIX = '.png'
    path = PREFIX
    if gene[0] == 0:
        TAIL_PREFIX = '0-tail/00'
        TAIL_SHAPE = '012'
        path += TAIL_PREFIX
        path += TAIL_SHAPE[gene[1]]
    elif gene[0] == 1:
        WINGS_PREFIX = '1-wings/01'
        WINGS_SHAPE = '012'
        WINGS_COLOR = '01'
        path += WINGS_PREFIX
        path += WINGS_SHAPE[gene[1]] + WINGS_COLOR[gene[2]]
    else:
        return ''
    return path + SUFFIX


def skin_path(gene):
    PREFIX = 'assets/1-skin/1'
    SUFFIX = '.png'
    SKIN_COLOR = '0123'
    return PREFIX + SKIN_COLOR[gene[0]] + SUFFIX


def clothes_path(gene):
    PREFIX = 'assets/2-clothes/2'
    SUFFIX = '.png'
    CLOTHES_SHAPE = '0123456'
    CLOTHES_COLOR_TYPE = [2, 2, 2, 3, 1, 1, 1]
    CLOTHES_COLOR = '012'
    return PREFIX + CLOTHES_SHAPE[gene[0]] + CLOTHES_COLOR[gene[1] % CLOTHES_COLOR_TYPE[gene[0]]] + SUFFIX


def hair_path(gene):
    PREFIX = 'assets/3-hair-hat/0-hat-hair/0-hair/3000'
    SUFFIX = '.png'
    HAIR_SHAPE = '012'
    if gene[0] > 4:
        return ''
    else:
        return PREFIX + HAIR_SHAPE[gene[2]] + SUFFIX


def hat_path(gene):
    PREFIX = 'assets/3-hair-hat/'
    SUFFIX = '.png'
    path = PREFIX
    if gene[0] < 4:
        path += '0-hat-hair/30'
        HAT_HAIR_SHAPE = '0123'
        HAT_HAIR_COLOR_TYPE = [1, 1, 1, 2]
        HAT_HAIR_COLOR = '01'
        return path + HAT_HAIR_SHAPE[gene[0]] + HAT_HAIR_COLOR[gene[1] % HAT_HAIR_COLOR_TYPE[gene[0]]] + SUFFIX
    elif gene[0] == 4:
        return ''
    else:
        path += '1-hat-only/31'
        hat_shape = gene[0] - 5
        HAT_HAIR_SHAPE = '012'
        HAT_HAIR_COLOR_TYPE = [2, 3, 3]
        HAT_HAIR_COLOR = '012'
        return path + HAT_HAIR_SHAPE[hat_shape] + HAT_HAIR_COLOR[gene[1] % HAT_HAIR_COLOR_TYPE[hat_shape]] + SUFFIX


def neck_path(gene):
    PREFIX = 'assets/4-neck/4'
    SUFFIX = '.png'
    NECK_SHAPE = '012345'
    NECK_COLOR_TYPE = [2, 3, 3, 2, 1, 1]
    NECK_COLOR = '012'
    return PREFIX + NECK_SHAPE[gene[0]] + NECK_COLOR[gene[1] % NECK_COLOR_TYPE[gene[0]]] + SUFFIX


def face_path(gene):
    PREFIX = 'assets/5-face/5'
    SUFFIX = '.png'
    FACE_SHAPE = '0123'
    if gene[0] == 4:
        return ''
    else:
        return PREFIX + FACE_SHAPE[gene[0]] + SUFFIX


def ear_path(gene):
    PREFIX = 'assets/6-ear/6'
    SUFFIX = '.png'
    EAR_SHAPE = '01'
    return PREFIX + EAR_SHAPE[gene[0]] + SUFFIX


def antenna_path(gene):
    return 'assets/7-antenna/70.png' if gene[0] == 0 else ''


def gen_pic(g: str):
    gene = Gene(g)
    layers = [tail_wings_path(gene.gene[3:6]),
              skin_path(gene.gene[6:7]),
              clothes_path(gene.gene[7:9]),
              hair_path(gene.gene[9:12]),
              hat_path(gene.gene[9:12]),
              neck_path(gene.gene[12:14]),
              face_path(gene.gene[14:15]),
              ear_path(gene.gene[15:16]),
              antenna_path(gene.gene[16:17])]
    
    final = comb_layers(layers)
    return final
