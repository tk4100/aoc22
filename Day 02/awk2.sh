#!/bin/sh

awk 'BEGIN{sum=0} { if($2=="X"){ winval=0; if($1=="A"){playval=3} else if($1=="B"){playval=1} else if($1=="C"){playval=2} } else if($2=="Y"){ winval=3; if($1=="A"){playval=1} else if($1=="B"){playval=2} else if($1=="C"){playval=3} } else if($2=="Z"){ winval=6; if($1=="A"){playval=2} else if($1=="B"){playval=3} else if($1=="C"){playval=1} }; sum = sum + playval + winval } END { print sum }' input.txt
