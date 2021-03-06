"""The constants used in translation."""

LINENUMBERS = [
    1, 2, 5, 6, 7, 8, 10, 11, 12, 15, 16, 31, 50, 51, 52, 1200, 1203, 1204, 1210, 1211, 1212,
    1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1227,
    1228, 1229, 1230, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1240, 1241, 1242, 1243,
    1244, 1245, 1246, 1247, 1248, 1249, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1258,
    1259, 1260, 1261, 1262, 1263, 1264, 1265, 1266, 1267, 1268, 1269, 1270, 1271, 1272, 1273,
    1274, 1275, 1276, 1277, 1278, 1279, 1280, 1281, 1282, 1283, 1284, 1285, 1286, 1287, 1288,
    1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297, 1298, 1299, 1305, 1306, 1307, 1308,
    1309, 1310, 1320, 1321, 1322, 1323, 1324, 1325, 1328, 1329, 1330, 1331, 1332, 1333, 1334,
    1335, 1336, 1337, 1338, 1339, 1340, 1341, 1342, 1343, 1344, 2501, 4270, 4271, 4272, 81700,
    81701, 81702, 81703, 81704, 81705, 81706, 81707, 81708, 81709, 81710, 81711, 81712, 81713,
    81714, 81715, 81716, 81717, 81718, 81719, 81720
]

SAMPLEPATTERN = {
    'drive': None,
    'settings': {
        'Read mode': 1234,
        'Accurate stream': 1297,
        'Audio cache': 1298,
        'C2 pointers': 1296,
        'Drive offset': 1256,
        'Fill missing offset samples with silence': 1264,
        'Deleting silent blocks': 1265,
        'Null samples': 1338,
        'Gap handling': 1320,
        'ID3 tags': 1309
    },
    'bad settings': {
        'Normalization': 1266,
        'Compression offset': 1262,
        'Combined offset': 1255
    },
    'proper settings': {
        'Read mode': 1295,
        'Accurate stream': 15,
        'Audio cache': 15,
        'C2 pointers': 16,
        'Fill missing offset samples with silence': 15,
        'Deleting silent blocks': 16,
        'Null samples': 15,
        'Gap handling': 1322,
        'ID3 tags': 16
    },
    'toc': 1289,
    'range': 1210,
    'htoa': None,
    'track': 1226,
    'track settings': {
        'filename': 1269,
        'pregap': 1270,
        'peak': 1217,
        'test crc': 1271,
        'copy crc': None
    },
    'track errors': {
        'Aborted copy': 1228,
        'Timing problem': 1212,
        'Missing samples': 1214,
        'Suspicious position': 1213
    },
    'accuraterip': {
        'match': 1281,
        'no match': 1330,
        'bad match': 1282,
        'no result': 1283,
        'not ripped': 1280
    },
    'range accuraterip': {
        'match': None,
        'no match': None,
        'no result': None
    },
    'footer': 1225,
    'checksum': None
}
