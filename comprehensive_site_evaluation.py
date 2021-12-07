import pymongo

from json_tool import *


# 有机质
def UMOC_rank(num):
    if num is None:
        return None
    if num > 40:
        return 1
    if 30 < num <= 40:
        return 2
    if 20 < num <= 30:
        return 3
    if 10 < num <= 20:
        return 4
    if 6 < num <= 10:
        return 5
    if num <= 6:
        return 6


# 全氮含量
def UTN_rank(num):
    if num is None:
        return None
    if num > 2:
        return 1
    if 1.5 < num <= 2:
        return 2
    if 1 < num <= 1.5:
        return 3
    if 0.75 < num <= 1:
        return 4
    if 0.5 < num <= 0.75:
        return 5
    if num <= 0.5:
        return 6


# 碱解氮
def UAN_rank(num):
    if num is None:
        return None
    if num > 150:
        return 1
    if 120 < num <= 150:
        return 2
    if 90 < num <= 120:
        return 3
    if 60 < num <= 90:
        return 4
    if 30 < num <= 60:
        return 5
    if num <= 30:
        return 6


# 全磷
def TP_rank(num):
    if num is None:
        return None
    if num > 2:
        return 1
    if 1.5 < num <= 2:
        return 2
    if 1 < num <= 1.5:
        return 3
    if 0.75 < num <= 1:
        return 4
    if 0.5 < num <= 0.75:
        return 5
    if num <= 0.5:
        return 6


# 速效磷
def UAP_rank(num):
    if num is None:
        return None
    if num > 40:
        return 1
    if 20 < num <= 40:
        return 2
    if 10 < num <= 20:
        return 3
    if 5 < num <= 10:
        return 4
    if 3 < num <= 5:
        return 5
    if num <= 3:
        return 6


# 全钾
def TK_rank(num):
    if num is None:
        return None
    if num > 20:
        return 1
    if 15 < num <= 20:
        return 2
    if 10 < num <= 15:
        return 3
    if 5 < num <= 10:
        return 4
    if 3 < num <= 5:
        return 5
    if num <= 3:
        return 6


# 速效钾
def UAK_rank(num):
    if num is None:
        return None
    if num > 200:
        return 1
    if 150 < num <= 200:
        return 2
    if 100 < num <= 150:
        return 3
    if 50 < num <= 100:
        return 4
    if 30 < num <= 50:
        return 5
    if num <= 30:
        return 6


def comprehensive_site_evaluation(xb):
    for feature in xb['features']:
        if not feature['properties'].has_key('土壤分级'):
            feature['properties']['土壤分级'] = {}
        UMOC_c = feature['properties']['土壤分级']['UMOC1'] = UMOC_rank(feature['properties']['UMOC1_mean'])  # 有机质
        UTN_c = feature['properties']['土壤分级']['UTN1'] = UTN_rank(feature['properties']['UTN_mean'])  # 全氮含量
        TP_c = feature['properties']['土壤分级']['TP1'] = TP_rank(feature['properties']['TP1_mean'])  # 全磷
        UAP_c = feature['properties']['土壤分级']['UAP1'] = UAP_rank(feature['properties']['UAP1_mean'])  # 速效磷
        TK_c = feature['properties']['土壤分级']['TK1'] = TK_rank(feature['properties']['TK1_mean'])  # 全钾
        UAK_c = feature['properties']['土壤分级']['UAK1'] = UAK_rank(feature['properties']['UAK1_mean'])  # 速效钾
        soil_features = [UMOC_c, UTN_c, TP_c, UAP_c, TK_c, UAK_c]
        if None in soil_features:
            continue
        feature['properties']['综合立地评价'] = (UMOC_c + UTN_c + TP_c + UAP_c + TK_c + UAK_c) / 6


def json_run():
    FN_xb = read_json('fn_fq.geojson')
    comprehensive_site_evaluation(FN_xb)
    write_json('fn_fq_new.geojson', FN_xb)


def db_run():
    client = pymongo.MongoClient()
    db = client["Xiongan-forest"]
    col = db["FN-features"]


if __name__ == '__main__':
    db_run()
