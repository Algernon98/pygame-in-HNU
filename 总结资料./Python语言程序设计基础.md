# 《Python语言程序设计基础》
## 程序实例

### python蟒蛇绘制

```bash
import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
```
 ## 基本数据类型
### math库解析
#### 数学常数

|常数|  描述|
|--|--|
|math.pi  | Π，圆周率，值为3.141592653589793 |
| math.e |e,自然对数，值为2.718281828459045
|math.inf|正无穷大|
| math.nan | 非浮点数标记，NaN(Not a Number) |
#### 数值表示函数
|math.fabs(x)  |  返回x的绝对值|
|--|--|
| math.fmod(x,y) |x%y,返回x与y的模  |
| math.fsum([x,y,...]) |x+y+···,浮点数精确求和
|math.ceil(x)|**向上**取整，返回不小于x的最小整数|
| math.floor(x)|  **向下**取整，返回不大于x的最大整数|
| math.factorial(x) |x!，返回x的阶乘，如果x是小数或负数，返回ValueError
|math.gcd(a,b)|返回a与b的最大公约数|
|  math.frexp(x)| $x$=$m$x$2^e$,返回(m,e)，当x=0，返回（0.0，0） |
| math.ldexp(x,i) |返回$x$x$2^i$运算值，math.frexp(x)函数的反运算。  |
|math.modf(x)|返回x的小数和整数部分
|math.trunc(x)  |  返回x的整数部分|


math包含8个幂对数函数
|  函数| 描述 |
|--|--|
| math.pow(x,y) |  $x^y$,返回x的y次幂|
| math.exp(x) | $e^x$,返回e的x次幂，e是自然对数 |
|math.sqrt(x)|返回x的平方根|
|  math.log(x[,base])| $\log_{base} {x}$，返回x的对数值，只输入x时，返回自然对数，即lnx |
| math.log1p(x) |  ln(1+x),返回1+x的自然对数值|
|math.log2(x)|l$og_2x$,返回x的2对数值|
|  math.log10(x)|  $log_{10}x$,返回x的10对数值|

#### 高等特殊函数
| 函数 | 描述 |
|--|--|
|  math.erf(x)|  高斯误差函数，应用于概率论、统计学等领域|
| math.erfc(x) | 余补高斯误差函数，math.erfc(x)=1-math.erf(x) |
|math.gamma(x)|伽马函数，也叫欧拉第二积分函数|
|math.lgamma(x)  | 伽马函数的自然对数 |

可以利用伽马函数计算浮点数的阶乘

### 字符串
#### 基本的字符串操作符
|操作符  | 描述 |
|--|--|
|  x+y| 连接两个字符串x与y |
| $x*n$或$n*x$ |  复制|
|x in s|如果x是s的子串，返回True,否则返回False|
|  str[i]|索引，返回第i个字符  |
|str[N:M]  |切片，返回索引第N到第M的子串，其中不包含M  |

#### 内置的字符串处理函数
|函数| 描述 |
|--|--|
| len(x) |  返回字符串x的长度|
|  str(x)|  返回任意类型x所对应的字符串形式|

## 程序的控制结构
### 异常处理：try-except语句

```bash
try:
   <语句块1>
except <异常类型>:
    <语句块2>
```
## 科学计算与可视化
### numpy
引用numpy
```bash
import numpy as np
```
#### 创建数组函数
| 函数 | 描述 |
|--|--|
| np.array([x,y,z],dtype=int) | 从python列表和元组创造数组 |
| np.arange(x,y,i) | 创建一个由x到y，以i为步长的数组 |
|np.linspace(x,y,n）|创建一个由x到y，等分成n个元素的数组|
|np.indices((m,n))  |创建一个m行n列的矩阵  |
|np.random.rand(m,n)  | 创建一个m行n列的随机数组 |
|np.ones((m,n),dtype)|创建一个m行n列全1的数组，dtype是数据类型|
| np.empty((m,n),dtype) |  创建一个m行n列全0的数组，dtype是数据类型|


#### 算数运算函数
| 函数 |描述  |
|--|--|
| np.add(x1,x2[,y]) |  y=x1+x2|
| np.subtract(x1,x2[,y]) |  y=x1-x2|
| np.multiply(x1,x2[,y]) |  y=x1*x2|
| np.divide(x1,x2[,y]) |  y=x1/x2|
| np floor_divide(x1,x2[,y]) |  y=x1//x2,返回值取整|
| np.negative(x[,y]) |  y=-x|
| np.power(x1,x2[,y]) |  y=x1**x2|
| np.remainder(x1,x2[,y]) |  y=x1%x2|

## 网络爬虫和自动化
