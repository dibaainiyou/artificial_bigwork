import mapcreate
import search
import shuchuditu
import shuchutd
Map=mapcreate.createmap()       #创建随机地图

shuchuditu.shuchuditu(Map)      #将地图放到EXCEL中
shuchutd.shuchutd(search.mapsearch(Map))   #寻找路线并输出到EXCEL中

