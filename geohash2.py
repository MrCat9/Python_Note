# -*- coding: utf-8 -*-

import geohash2

if __name__ == "__main__":
    # geohash2.encode(latitude, longitude, precision)
    # geohash2.decode(geohash)
    
    latitude = "26.082294"    #纬度
    longitude = "119.303822"    #经度
    geohash_code = "wssu6u4kks12"
    
    print(geohash2.encode(float(latitude), float(longitude)))    # wssu6u4kks12
    print(geohash2.encode(float(latitude), float(longitude)).__class__)    # <class 'str'>

    print(geohash2.encode(26.082294, 119.303822))    # wssu6u4kks12
    print(geohash2.encode(26.082294, 119.303822).__class__)    # <class 'str'>
    
    print(geohash2.decode(geohash_code))    # ('26.082294', '119.303822')
    print(geohash2.decode(geohash_code).__class__)    # <class 'tuple'>
