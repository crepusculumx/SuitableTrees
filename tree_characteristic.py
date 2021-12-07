from json_tool import *


# 检测耐碱性
def check_alkali(tree, feature) -> bool:
    prop = feature['properties']
    if 1 in tree['耐碱性']:
        if prop['UPH1_mean'] < 8.5 and prop['URZ1_mean'] > 1.4 and prop['综合立地评价'] <= 4:
            return True
    if 2 in tree['耐碱性']:
        if prop['UPH1_mean'] < 8.5 and prop['综合立地评价'] <= 4:
            return True
    if 3 in tree['耐碱性']:
        if prop['UPH1_mean'] < 8.5:
            return True
        if prop['UPH1_mean'] >= 8.5 and prop['URZ1_mean'] > 1.4:
            return True
    if 4 in tree['耐碱性']:
        return True

    return False


# 检测耐旱性
def check_drought(tree, feature) -> bool:
    prop = feature['properties']
    if 1 in tree['耐旱性'] or 2 in tree['耐旱性'] or 3 in tree['耐旱性']:
        if prop['UWH1_mean'] >= 0.2:
            return True
    if 4 in tree['耐旱性']:
        return True

    return False


# 检测耐瘠性
def check_barren(tree, feature) -> bool:
    prop = feature['properties']
    if 1 in tree['耐瘠性'] or 2 in tree['耐瘠性']:
        if prop['土壤分级']['UMOC1'] <= 4:
            return True
    if 3 in tree['耐瘠性']:
        return True

    return False


def check(tree, xb) -> bool:
    try:
        alkali = check_alkali(tree, xb)
        drought = check_drought(tree, xb)
        barren = check_barren(tree, xb)
    except TypeError:
        return False
    else:
        return alkali and drought and barren


def get_suitable(tree, xb):
    tree_name = tree['名称']
    print(tree_name)
    for feature in xb['features']:
        if '适地适树' not in feature['properties']:
            feature['properties']['适地适树'] = {}

        feature['properties']['适地适树'][tree_name] = 0
        if check(tree, feature):
            feature['properties']['适地适树'][tree_name] = feature['properties']['综合立地评价']


def work():
    tree_characteristics = read_json('tree_characteristics.json')
    xb = read_json('fn_fq.geojson')
    for tree in tree_characteristics:
        get_suitable(tree, xb)
    write_json('FN_features.geojson', xb)


if __name__ == '__main__':
    work()
