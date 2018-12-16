from enum import Enum


class AnnotationKey(Enum):
    cpg = 'ID_REF'
    chr = 'CHR'
    map_info = 'MAPINFO'
    Probe_SNPs = 'Probe_SNPs'
    Probe_SNPs_10 = 'Probe_SNPs_10'
    gene = 'UCSC_REFGENE_NAME'
    probe_class = 'Class'
    geo = 'RELATION_TO_UCSC_CPG_ISLAND'
    bop = 'BOP'
    cross_reactive = 'CROSS_R'


class Exclude(Enum):
    none = 'none'
    cluster = 'cluster'


class CrossReactive(Enum):
    any = 'any'
    exclude = 'exclude'


class SNP(Enum):
    any = 'any'
    exclude = 'exclude'


class Chromosome(Enum):
    any = 'any'
    non_gender = 'non_gender'
    X = 'X'
    Y = 'Y'


class GeneRegion(Enum):
    any = 'any'
    yes = 'yes'
    no = 'no'


class Geo(Enum):
    any = 'any'
    shores = 'shores'
    shores_s = 'shores_s'
    shores_n = 'shores_n'
    islands = 'islands'
    islands_shores = 'islands_shores'


class ProbeClass(Enum):
    any = 'any'
    class_a = 'ClassA'
    class_b = 'ClassB'
    class_c = 'ClassC'
    class_d = 'ClassD'
    class_ab = 'ClassAB'