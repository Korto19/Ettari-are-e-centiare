from qgis.core import *
from qgis.gui import *
import math

@qgsfunction(group='CATASTO', referenced_columns=[])
def cat_area(value, a_unit):
    """
    Calculate the area of ​​the parcel in "Ha", "a" or "ca" or all together
    <h3>Syntax</h3>
        <p><b style="color:#4863A0;">cat_area</b>(<i style="color:#9F000F;">value, a_unit</i>)
    <h3>Arguments</h3>
<pre>
<i style="color:#9F000F;">value</i>    <h0>value like 112233.45 to convert</h0>
<i style="color:#9F000F;">a_unit</i>    <h0>unit selected from those below</h0>
</pre>
    <ul>
        <li><b>Ha</b> only ettari
        <li><b>a</b>  only are
        <li><b>ca</b> only centiare
        <li><b>all</b> ettari, are, centiare
    </ul>
    <h3>Example usage:</h3>
    <ul>
        <li>cat_area(112233.41,'Ha') -> 11</li>
        <li>cat_area(112233.41,'a')  -> 22</li>
        <li>cat_area(112233.41,'ca') -> 33</li>
        <li>cat_area(112233.41,'all')-> '11 22 33' <b>This is a string</b></li>
    </ul>
    """
    
    Ha = math.modf(value/10000)
    a = math.modf((value - Ha[1]*10000)/100)
    ca  = math.modf(value - Ha[1]*10000 - a[1]*100)
    all = str(int(Ha[1])) + " " + str(int(a[1])) + " " + str(int(ca[1]))
    
    cat_area = {'Ha': int(Ha[1]), 'a':int(a[1]), 'ca':int(ca[1]), 'all': all}
    
    return cat_area[a_unit]
