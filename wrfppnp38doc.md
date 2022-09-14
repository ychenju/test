<!DOCTYPE html>

<html>
    <head>
        <meta charset="UTF-8">
        <title>
            WRFPPNP38文档
        </title>
    </head>
    <body>
        <h2>
            WRF python processing noob pack for python 3.8 (WRFPPNP38) 文档
        </h2>
        <br /><hr /><hr /><br />
        <h3>
            一般函数与常量
        </h3>
        <hr />
        <h4>
            datafilter(filtee, sifter, func):
        </h4>
        <p style="padding-left: 4em;">
            基于过滤器函数中的二元函数对数据进行过滤.
        </p>
        <ul style="padding-left: 4em;">
            <li>
                filtee: 待过滤的二维数据表，其元素作为过滤器函数的第1个参数.
            </li>
            <li>
                sifter: 作为筛选器的二维数据表，其元素作为过滤器函数的第2个参数.
            </li>
            <li>
                func: 用于过滤的二元函数，一般从filterf类的方法中选取.
            </li>
        </ul>
        <div style="padding-left: 4em;">
            <a href="JAVASCRIPT:;">详细：</a>
        </div>
        <h4>
            FRAME_DEFAULT_FLAGS:
        </h4>
        <p style="padding-left: 4em;">
            用于初始化frame类及其各派生类的_flag字典的常量字典.
        </p>
        <br />
        <h3>
            静态方法类filterf
        </h3>
        <hr />
        <p style="padding-left: 4em;">
           过滤器函数集，一般用于前述的<code>datafilter()</code>函数或者python的<code>filter()</code>函数.所有方法均为静态方法.
        </p>
        <h4>
            <c style='color:green'>【静态】</c> nansync(x, f):
        </h4>
        <p style="padding-left: 4em;">
           NaN同步函数.若f为NaN，则返回NaN，否则返回x的值.
        </p>
        <h4>
            <c style='color:green'>【静态】</c> falsetonan(x, f):
        </h4>
        <p style="padding-left: 4em;">
           NaN赋值函数.若条件f为假，则返回NaN，否则返回x的值.
        </p>
        <h4>
            <c style='color:green'>【静态】</c> isnan(f):
        </h4>
        <p style="padding-left: 4em;">
           NaN判断函数.若f为NaN，则返回1，否则返回0.
        </p>
        <br />
        <h3>
            wrfout文件对象类wrfout
        </h3>
        <hr />
        <h4>
            <c style='color:brown'>【类属】</c> ncfile
        </h4>
        <p style="padding-left: 4em;">
            初始化实例对象时用xarray读取wrfout文件后生成的对象.
        </p>
        <h4>
            <c style='color:blue'>【特殊】</c> __init__(self, path):
        </h4>
        <p style="padding-left: 4em;">
            通过<code>xarray.open_dataset()</code>函数，读取<code>path</code>表示的wrfout文件，从而初始化实例.
        </p>
        <h4>
            【方法】 extract(self, *keys):
        </h4>
        <div style="padding-left: 4em;">
            使用frame类的标准初始化函数<code>frame.__init__(self, source, *keys)</code>从wrfout文件中提取数据并返回一个frame对象.
        </div>
        <div style="padding-left: 4em;">
            其中参数<code>source=self.ncfile</code>，<code>*keys=*keys</code>.
        </div>
        <h4>
            <c style='color:blue'>【特殊】</c> __getitem__(self, key):
        </h4>
        <div style="padding-left: 4em;">
            重载索引查找运算符<q><code>[]</code></q>.可以通过<q>对象名<code>[key]</code></q>的方式访问wrfout文件中标签名为key的数据表，并在打开时处理为二维numpy.ndarray格式.
        </div>
        <div style="padding-left: 4em;">
            这对于部分方法如<code>frame.load()</code>是重要的.
        </div>
        <br />
        <h3>
            dataframe文件对象类frame
        </h3>
        <hr />
        <h4>
            <c style='color:brown'>【类属】</c> lat
        </h4>
        <div style="padding-left: 4em;">
            纬度表.为二维np.ndarray对象.frame对象初始化时所必需的参数表.
        </div>
        <h4>
            <c style='color:brown'>【类属】</c> long
        </h4>
        <div style="padding-left: 4em;">
            经度表.为二维np.ndarray对象.frame对象初始化时所必需的参数表.
        </div>
        <h4>
            <c style='color:brown'>【类属】</c> time
        </h4>
        <div style="padding-left: 4em;">
            frame对象对应的时间.
        </div>
        <h4>
            <c style='color:blue'>【特殊】</c> __init_(self, source, *keys):
        </h4>
        <div style="padding-left: 4em;">
            在这里插入内容.
        </div>
        <ul style="padding-left: 4em;">
            <li>
                在这里插入内容
            </li>
            <li>
                在这里插入内容<code>在这里插入代码</code>, <code>在这里插入代码</code>.
            </li>
        </ul>
        <h4>
            <c style='color:orange'>【实属】</c> _data:
        </h4>
        <div style="padding-left: 4em;">
            用于存放从wrfout文件中提取并展开一次后得到的二维numpy.ndarray格式的数据表（经纬度及时间除外）的字典，为frame类的核心实例属性.
        </div>
        <div style="padding-left: 4em;">
            <code>frame[key]</code>等操作已被重载为<code>frame._data[key]</code>.
        </div>
        <h4>
            <c style='color:orange'>【实属】</c> _flag:
        </h4>
        <div style="padding-left: 4em;">
            实例标记及标记变量的集合字典.
        </div>
        <div style="padding-left: 4em;">
            这些变量在执行某些方法时将会改变，标志实例已经经过了某些变换操作而导致属性发生了一些变化，这些变化会影响到某些方法的行为. 
            例如执行<code>removewater()</code>函数后，<code>_flag['removewater']</code>将由False变为True，从而影响<code>planefit()</code>方法的执行过程.
        </div>
        <div style="padding-left: 4em;">
            实例初始化时，这些变量将会用一个常量字典初始化. 
        </div>
        <h4>
            <c style='color:orange'>【实属】</c> _chara:
        </h4>
        <div style="padding-left: 4em;">
            实例特征量的集合字典.
        </div>
        <div style="padding-left: 4em;">
            这些特征量如sigma值，通常是通过计算得到的，因此这个对象不设赋值函数.
        </div>
        <h4>
            <c style='color:black'>【方法】</c> load(self, source, *keys):
        </h4>
        <div style="padding-left: 4em;">
            从<code>source</code>通过索引名向_data中载入数据表.
        </div>
        <ul style="padding-left: 4em;">
            <li>
                在这里插入内容
            </li>
            <li>
                在这里插入内容<code>在这里插入代码</code>, <code>在这里插入代码</code>.
            </li>
        </ul>
        <h4>
            <c style='color:black'>【方法】</c> params(self):
        </h4>
        <div style="padding-left: 4em;">
            获取所有已导入和生成的数据表的索引组成的list.
        </div>
        <h4>
            <c style='color:black'>【方法】</c> get(self, key):
        </h4>
        <div style="padding-left: 4em;">
            返回数据表key（即_data[key]指向的数据）.
        </div>
        <h4>
            <c style='color:blue'>【特殊】</c> __getitem__(self, key):
        </h4>
        <div style="padding-left: 4em;">
            对索引运算符[]进行重载，使得frame[key]将返回frame.get(key).
        </div>
        <h4>
            <c style='color:black'>【方法】</c> getall(self):
        </h4>
        <div style="padding-left: 4em;">
            返回整个_data字典.
        </div>
        <h4>
            <c style='color:black'>【方法】</c> set(self, key, value):
        </h4>
        <div style="padding-left: 4em;">
            使用value数据表更新数据表key（即_data[key]指向的数据）.
        </div>
        <h4>
            <c style='color:blue'>【特殊】</c> __setitem__(self, key, value):
        </h4>
        <div style="padding-left: 4em;">
            对赋值运算符[]=进行重载，使得frame[key]=value将返回frame.set(key, value).
        </div>
        <h4>
            <c style='color:black'>【方法】</c> delete(self, key):
        </h4>
        <div style="padding-left: 4em;">
            删除数据表key（即_data[key]指向的数据表）.
        </div>
        <h4>
            <c style='color:blue'>【特殊】</c> __delitem__(self, key):
        </h4>
        <div style="padding-left: 4em;">
            对删除运算符del []进行重载，使得del frame[key]将返回frame.delete(key).
        </div>
        <h4>
            <c style='color:black'>【方法】</c> getflag(self, key):
        </h4>
        <div style="padding-left: 4em;">
            返回_flag[key]. 用于查找标记或标记属性.
        </div>
        <h4>
            <c style='color:black'>【方法】</c> setflag(self, key, value):
        </h4>
        <div style="padding-left: 4em;">
            设置_flag[key]的值为value. 用于设置或改变标记或标记属性.
        </div>
        <h4>
            <c style='color:black'>【方法】</c> getchara(self, key):
        </h4>
        <div style="padding-left: 4em;">
            返回_chara[key]. 用于查找特征量.
        </div>
        <h4>
            <c style='color:green'>【静态】</c> cp2dattr(attr):
        </h4>
        <div style="padding-left: 4em;">
            返回一个对二维numpy.ndarray对象attr进行的拷贝，常用于初始化赋值. 注意attr不可为二维列表.
        </div>
        <h4>
            <c style='color:black'>【方法】</c> removewater(self):
        </h4>
        <div style="padding-left: 4em;">
            以<code>self['LANDMASK']</code>为判断标准，将_data中的所有数据表中，'LANDMASK'=0（表征水域）的所有数据点的值移除（设为numpy.NaN）. 
        </div>
        <div style="padding-left: 4em;">
            此方法用于移除除经纬度以外的数据中，位于水域的数据. 执行此方法前需确保'LANDMASK'已经载入. <a href="JAVASCRIPT:;">详细：</a>
        </div>
        <h4>
            <c style='color:black'>【方法】</c> planefit(self, key):
        </h4>
        <div style="padding-left: 4em;">
            通过矩阵本征值分解法，对<code>self[key]</code>数据进行平面拟合（调用sigmacalc模块）.
        </div>
        <div style="padding-left: 4em;">
            拟合结果及残差将被添加至_data中，分别为 <code>self._data['PF_'+key+'_1']</code> 和 <code>self._data['PF_'+key+'_r']</code>，同时这两个变量将作为返回值输出.
        </div>
        <h4>
            <c style='color:black'>【方法】</c> sigma(self, key):
        </h4>
        <div style="padding-left: 4em;">
            计算<code>self[key]</code>数据的σ值（调用sigmacalc模块）.
        </div>
        <div style="padding-left: 4em;">
            σ值定义为变量作平面拟合后所得残差数据的总体标准差，单位与原数据单位相同，用于衡量一个物理量的空间波动性. 
        </div>
        <div style="padding-left: 4em;">
            σ值的计算结果将保存在<code>self._chara[key+'_SIGMA']</code>中，同时作为返回值输出.
        </div>
        <h4>
            <c style='color:black'>【方法】</c> quickshow(self, key):
        </h4>
        <div style="padding-left: 4em;">
            调用emap模块快速作<code>self[key]</code>变量的等值填充地图. 用于调试目的. <a href="JAVASCRIPT:;">详细：</a>
        </div>
        <h4>
            <c style='color:black'>【方法】</c> get3x3(self, key, x, y):
        </h4>
        <div style="padding-left: 4em;">
            获取<code>self[key]</code>数据表中，<code>self[key][x,y]</code>点及其周围距离最近的8个点的数据，返回含有9个数值的一维numpy.ndarray对象. 作为其他函数的中间方法，一般不单独使用.
        </div>
        <h4>
            <c style='color:black'>【方法】</c> mean3x3(self):
        </h4>
        <div style="padding-left: 4em;">
            对数据表进行<q>3x3网格平均</q>操作. 该操作将生成一个新的voidFrame对象，此对象与原对象相比：
        </div>
        <ul style="padding-left: 4em;">
            <li>
                lat, long, time的值不变.
            </li>
            <li>
                _data的所有数据表中，最外层的值保持不变，其余值取原对象该数据表中，该点及其周围8个点，共9个值的平均. 
                若9个值中，出现NaN的比例超过一半，则平均后的值取NaN，否则取忽略NaN平均的返回值.
            </li>
            <li>
                _flag不变, _chara清空.
            </li>
        </ul>
        <div style="padding-left: 4em;">
            <a href="JAVASCRIPT:;">详细：</a>
        </div>
        <h4>
            <c style='color:black'>【方法】</c> crop(self, interv=3, fromx=1, tox=-1, fromy=1, toy=-1):
        </h4>
        <div style="padding-left: 4em;">
            对数据表进行<q>等距采样</q>操作. 该操作将生成一个新的voidFrame对象，此对象中包括经纬度的所有数据表将通过等距采样切片法生成.
        </div>
        <div style="padding-left: 4em;">
            执行该方法后，<code>_flag['RES']</code>将会扩大到原来的三倍.
        </div>
        <div style="padding-left: 4em;">
            <a href="JAVASCRIPT:;">详细：</a>
        </div>
        <h4>
            <c style='color:black'>【方法】</c> lowres3(self, fromx=1, tox=-1, fromy=1, toy=-1):
        </h4>
        <div style="padding-left: 4em;">
            对数据表进行平均采样操作以获得低分辨率的数据表. 生成的数据表的网格长度是原来的3倍. 参数与crop方法的参数相同.
        </div>
        <div style="padding-left: 4em;">
            该方法首先执行<code>mean3x3()</code>方法，并使用其返回值执行<code>crop(interv=3)</code>方法.
        </div>
        <h4>
            <c style='color:black'>【方法】</c> res(self):
        </h4>
        <div style="padding-left: 4em;">
            返回分辨率标记值（即_flag['res']）.
        </div>
        <h4>
            <c style='color:purple'>【子类】</c> voidFrame:
        </h4>
        <div style="padding-left: 4em;">
            使用拷贝属性的方法，而不是从wrfout获取数据而生成的frame子类. 其余与frame类没有区别.
        </div>
        <h4>
            <c style='color:blue'>【子类特殊】</c> __init__(self, lat, long, time):
        </h4>
        <div style="padding-left: 4em;">
            使用变量作为lat, long, 和time, 对frame进行初始化的初始化方法. 
        </div>
        <div style="padding-left: 4em;">
            其余属性需要在实例生成后，通过<code>set()</code>方法或重载后的赋值语句获得.
        </div>
    </body>
</html>

