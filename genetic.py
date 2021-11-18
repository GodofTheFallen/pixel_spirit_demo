from datetime import timedelta
from random import random, randint

import toml


class Gene:
    """
    基因类
    """
    CONFIG = toml.load('config.toml').get('GENE')  # 从配置中读取基本参数
    
    def __init__(self, s: str):
        """
        从字符串初始化基因
        :param s: 基因字符串，每一位一个数字代表该位点基因类型
        """
        assert len(s) == self.CONFIG['LENGTH'], self.CONFIG['LENGTH_ASSERR_MSG'].format(self.CONFIG['LENGTH'], len(s))
        self.gene = []
        for i, ch in enumerate(s):
            locus = ord(ch) - ord('0')
            assert 0 <= locus < self.CONFIG['TYPE'][i], \
                self.CONFIG['TYPE_ASSERR_MSG'].format(self.CONFIG['TYPE'][i] - 1, locus)
            self.gene.append(locus)
    
    def __str__(self) -> str:
        """
        从基因转化为字符串
        :return: 基因字符串
        """
        s = ''
        for locus in self.gene:
            s += str(locus)
        return s


def rand_gene_str() -> str:
    """
    返回完全随机的基因
    :return:
    """
    s = ''
    for i in range(Gene.CONFIG['LENGTH']):
        s += str(randint(0, Gene.CONFIG['TYPE'][i] - 1))
    return s


def reproduce(father_s: str, mother_s: str) -> str:
    """
    计算繁殖后的子代基因
    :param father_s: 父亲的基因串
    :param mother_s: 母亲的基因串
    :return: 子代的基因串
    """
    s = ''
    parents = (Gene(father_s), Gene(mother_s))
    for i in range(Gene.CONFIG['LENGTH']):
        if random() < Gene.CONFIG['MUTATION_RATE']:  # 是否发生突变
            s += str(randint(0, Gene.CONFIG['TYPE'][i] - 1))
        else:
            s += str(parents[randint(0, 1)].gene[i])
    return s


def get_life_length(gene: Gene) -> timedelta:
    """
    根据基因计算寿命长度，由前两位决定，120~360小时
    :param gene: 基因
    :return: 寿命长度
    """
    life_hours = (gene.gene[0] * Gene.CONFIG['TYPE'][0] + gene.gene[1]) * 16 + 120
    return timedelta(hours=life_hours)


def get_cd_length(gene: Gene) -> timedelta:
    """
    根据基因计算繁殖冷却时间，由第三位决定，5~20分钟
    :param gene: 基因
    :return: 繁殖冷却时间
    """
    cd_minutes = gene.gene[2] + 1
    return timedelta(minutes=cd_minutes)
