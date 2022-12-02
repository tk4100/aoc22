#!/bin/sh

awk 'BEGIN{sum=0} { if($2=="X"){ playval=1; if($1=="A"){winval=3} else if($1=="B"){winval=0} else if($1=="C"){winval=6} } else if($2=="Y"){ playval=2; if($1=="A"){winval=6} else if($1=="B"){winval=3} else if($1=="C"){winval=0} } else if($2=="Z"){ playval=3; if($1=="A"){winval=0} else if($1=="B"){winval=6} else if($1=="C"){winval=3} }; sum = sum + playval + winval } END { print sum }' input.txt
