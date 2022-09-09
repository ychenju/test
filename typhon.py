import urllib.request as req
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

RAMMB_URL = r'https://rammb-data.cira.colostate.edu/tc_realtime/storm.asp?storm_identifier='
JTWC_URL = r'https://www.metoc.navy.mil/jtwc/products/best-tracks'

JTWC_SCALE_LIST = ('DB','TD','TS','TY','ST','TC')

def get_JTWC_URL(year):
    return JTWC_URL + f'//{year}//{year}s-bwp//bwp{year}.zip'

def rammb(identifer, name, path):
    resp = req.urlopen(RAMMB_URL+identifer)
    fcsv = open(path+'\\'+identifer[-4:]+identifer[:4]+name+'.csv', 'w')
    fhtm = open(path+'\\'+'WEBSOURCE_'+identifer[-4:]+identifer[:4]+name+'.html', 'w')

    html = resp.read().decode('UTF-8')
    rec = re.compile(r'\xa9')
    html = re.sub(rec,'',html)

    print(html)
    fhtm.write(html)
    fhtm.close()

    l1 = html.find('Track History')
    r1 = html.rfind('Track History')

    l2 = html[l1:r1].find('<table>')
    r2 = html[l1:r1].rfind('</table>')

    tb = html[l1:r1][l2+1:r2]
    tb = tb.replace('<tr>','')
    tb = tb.replace('</tr>','')

    tb2 = tb.split()
    for i, s in enumerate(tb2):
        tb2[i] = s.strip('<td>')
        tb2[i] = s.strip('</td>')

    tb3 = tb2[tb2.index('Intensity')+1:]

    vd = tb3[-5::-5]
    vt = tb3[-4::-5]
    vlo = tb3[-3::-5]
    vla = tb3[-2::-5]
    vi = tb3[-1::-5]

    print(len(vi))
    data = []
    for i in range(len(vi)):
        d = str()
        d += (vd[i]+'-'+vt[i])
        d += ',\t'
        d += (vlo[i])
        d += ',\t'
        d += (vla[i])
        d += ',\t'
        d += (vi[i])
        d += '\r'
        data.append(d)
    
    r = str()
    for d in data:
        r += d

    fcsv.write(r)
    fcsv.close()

BMAP_DEFAULT_ATTRS = {
    'figsize'   :   (12,8),
    'dpi'       :   180,
    'proj'      :   'cea',
    'lon'       :   [-180.,180.],
    'lat'       :   [-60.,60.],
    'res'       :   'c',
    'latinv'    :   0.,
    'loninv'    :   0.,
    'fontsize'  :   10,
    'cmap'      :   'jet',          # default colormap
    'clcolor'   :   'k',            # coastline $color
    'cllw'      :   1.,             # coastline $linewidth
    'clbgs'     :   0.2,            # colored backgrounds $scale
    'gridc'     :   'k',       # color of parallels and meridians
    'gridlw'    :   0.5,            # linewidth of parallels and meridians
}    

class bmap:
    # __attr = {  'figsize'   :   (12,8),
    #             'dpi'       :   180,
    #             'proj'      :   'cea',
    #             'lon'       :   [-180.,180.],
    #             'lat'       :   [-60.,60.],
    #             'res'       :   'c',
    #             'latinv'    :   0.,
    #             'loninv'    :   0.,
    #             'fontsize'  :   10,
    #             'cmap'      :   'jet',
    #             }

    # __base = None

    def __init__(self, **kw):
        self.__attr = BMAP_DEFAULT_ATTRS
        # self.__attr = {
        #     'figsize'   :   (12,8),
        #         'dpi'       :   180,
        #         'proj'      :   'cea',
        #         'lon'       :   [-180.,180.],
        #         'lat'       :   [-60.,60.],
        #         'res'       :   'c',
        #         'latinv'    :   0.,
        #         'loninv'    :   0.,
        #         'fontsize'  :   10,
        #         'cmap'      :   'jet',
        # }
        self.__base = None
        for k in kw:
            self.__attr[k] = kw[k]

    def resetall(self):
        self.__attr = BMAP_DEFAULT_ATTRS
        self.__base = None

    def reset(self, **kw):
        self.resetall()
        for k in kw:
            self.__attr[k] = kw[k]
    
    def set(self, **kw):
        for k in kw:
            self.__attr[k] = kw[k]
    

    def bg(self):
        plt.figure(figsize=self.__attr['figsize'], dpi=self.__attr['dpi'])
        self.__base = Basemap(projection=self.__attr['proj'], llcrnrlon = self.__attr['lon'][0], llcrnrlat = self.__attr['lat'][0], 
                    urcrnrlon = self.__attr['lon'][1], urcrnrlat = self.__attr['lat'][1], resolution=self.__attr['res'])
        self.__base.drawcoastlines(color=self.__attr['clcolor'], linewidth=self.__attr['cllw'])

        if int(self.__attr['latinv']):
            self.__base.drawparallels(np.arange(self.__attr['lat'][0], self.__attr['lat'][1], self.__attr['latinv']), labels=[1,0,0,0],
                                        color=self.__attr['gridc'], linewidth=self.__attr['gridlw'], fontsize=self.__attr['fontsize'])
        if int(self.__attr['loninv']):
            self.__base.drawmeridians(np.arange(self.__attr['lon'][0], self.__attr['lon'][1], self.__attr['loninv']), labels=[0,0,0,1],
                                        color=self.__attr['gridc'], linewidth=self.__attr['gridlw'], fontsize=self.__attr['fontsize'])

    def colorbg(self, style=None):
        if style == 'bluemarble':
            self.__base.bluemarble(scale=self.__attr['clbgs'])
        if style == 'shadedrelief':
            self.__base.shadedrelief(scale=self.__attr['clbgs'])
        if style == 'etopo':
            self.__base.etopo(scale=self.__attr['clbgs'])

    def fitboundaries(self, source):
        self.__attr['lon'] = [source.long[0,:].min(), source.long[0,:].max()]
        self.__attr['lat'] = [source.lat[:,0].min(), source.lat[:,0].max()]
    
    def womesh(self, source):
        _lon, _lat = np.meshgrid(source.long[0,:], source.lat[:,0])
        return self.__base(_lon, _lat)

    def quickcountourf(self, source, key):
        self.fitboundaries(source)
        self.bg()
        _X, _Y = self.womesh(source)
        if 'levels' in self.__attr.keys():
            self.__base.contourf(_X,_Y,source.get(key),cmap=self.__attr['cmap'],levels=self.__attr['levels'])
        else:
            self.__base.contourf(_X,_Y,source.get(key),cmap=self.__attr['cmap'])

class tymap(bmap):

    def __boundaries(self, track):
        self._bmap__attr['lat'] = [max(track[1].min()-5.,-70), min(track[1].max()+5.,70)]
        self._bmap__attr['lon'] = [track[2].min()-10., track[2].max()+10.]

    def __sshws(self, inten):
        if inten < 25:      # DIST
            return np.array([128,204,255])/256.
        elif inten < 34:    # TD
            return np.array([ 94,186,255])/256.
        elif inten < 64:    # TS
            return np.array([  0,255,244])/256.
        elif inten < 82:    # C1
            return np.array([255,255,204])/256.
        elif inten < 96:    # C2
            return np.array([255,231,117])/256.
        elif inten < 112:   # C3
            return np.array([255,193, 64])/256.
        elif inten < 137:   # C4
            return np.array([255,143, 32])/256.
        else:               # C5
            return np.array([255, 96, 96])/256.
    
    def __plotd(self, track, i):
        # _lon, _lat = np.meshgrid(track[1][i], track[2][i])
        # _lon2, _lat2 = self._bmap__base(_lon, _lat)
        plt.plot(track[2][i], track[1][i], '.', c=self.__sshws(track[3][i]), ms=7.5, zorder=100)

    def plot(self, track):
        self._bmap__attr['proj'] = 'cyl'
        self._bmap__attr['cllw'] = .25
        self._bmap__attr['latinv'] = 0
        self._bmap__attr['loninv'] = 0
        self._bmap__attr['gridc'] = 'darkgrey'
        self._bmap__attr['gridlw'] = .25
        self.__boundaries(track)
        self.set(clbgs=1., res='i')
        self.bg()
        self.colorbg('bluemarble')
        self._bmap__base.drawparallels(np.arange(-90,90,10), labels=[1,0,0,0], 
                                        color=self._bmap__attr['gridc'], linewidth=self._bmap__attr['gridlw'], fontsize=self._bmap__attr['fontsize'])
        self._bmap__base.drawmeridians(np.arange(-180,180,10), labels=[0,0,0,1], 
                                        color=self._bmap__attr['gridc'], linewidth=self._bmap__attr['gridlw'], fontsize=self._bmap__attr['fontsize'])
        _r = range(min([len(j) for j in track]))
        for i in _r:
            self.__plotd(track, i)
            if i < _r[-1]:
                self._bmap__base.drawgreatcircle(track[2][i],track[1][i],track[2][i+1],track[1][i+1],linewidth=.5,color='w')
        print(f'ACE: {ace(track)}')


class track:

    @classmethod
    def simple(self, path):
        dframe = pd.read_csv(path, header=None)
        return np.array(dframe.iloc[:,:]).T
        
def ace(track):
    _r = []
    for inten in track[3]:
        if inten > 34:
            _r.append(inten)
    _r2 = np.array(_r)
    return (_r2**2).sum()/1e4

def report(name, track, path):
    _r = []
    for inten in track[3]:
        if inten > 34:
            _r.append(inten)
    _r2 = np.array(_r)
    with open(path, 'a') as f:
        f.write(f'{name}\t\t,\t{len(_r2)}\t,\t{max(track[3])}\t,\t{(_r2**2).sum()/1e4}\r')

def coorproc(t, *args):
    for arg in args:
        for tl in t:
            _r = list(tl[arg])
            _r.pop()
            _r.insert(-1,'.')
            tl[arg] = ''.join(_r)
    return t

def readjtwc(ipath, opath):
    with open(ipath, 'r') as trf:
        trc = trf.read()
    trx = np.array(trc.split('\n'))
    trx = [trxl for trxl in trx if trxl.find('BEST') + 1]
    trx = [trxl.split(',') for trxl in trx]
    trx = [trxl[:3] + trxl[6:11] for trxl in trx if int(trxl[11]) < 35]
    trx = [trxl for trxl in trx if not int(trxl[2][-2:])%6]
    trx = [trxl for trxl in trx if max([trxl[-1].find(sx)+1 for sx in JTWC_SCALE_LIST])]
    trx = coorproc(trx, 3, 4)
    trx = [[x if i else trxl[0]+trxl[1]+trxl[2] for i, x in enumerate(trxl[2:])] for trxl in trx]
    _p = pd.DataFrame(trx)
    _p.to_csv(opath,index=None, header=None)

def readjtwc(ipath, opath):
    with open(ipath, 'r') as trf:
        trc = trf.read()
    trx = np.array(trc.split('\n'))
    #   trx = [trxl for trxl in trx if trxl.find('BEST') + 1]
    trx = filter(lambda _x: _x.find('BEST') + 1, trx)
    trx = [trxl.split(',') for trxl in trx]
    trx = [trxl[:3] + trxl[6:11] for trxl in trx if int(trxl[11]) < 35]

    trx = [trxl for trxl in trx if not int(trxl[2][-2:])%6]
    trx = filter(lambda _x: not int(_x[2][-2:])%6, trx)

    # trx = [trxl for trxl in trx if max([trxl[-1].find(sx)+1 for sx in JTWC_SCALE_LIST])]
    #   trx = filter(lambda _x: max([_x[-1].find(sx)+1 for sx in JTWC_SCALE_LIST]), trx)

    trx = coorproc(trx, 3, 4)
    trx = [[x if i else trxl[0]+trxl[1]+trxl[2] for i, x in enumerate(trxl[2:])] for trxl in trx]
    _p = pd.DataFrame(trx)
    _p.to_csv(opath,index=None, header=None)