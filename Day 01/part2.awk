BEGIN{largest=0;largest2=0;largest3=0;sum=0}{ if(NF){sum=sum+$1}else{ if(sum>largest){if(largest>largest2){if(largest2>largest3){largest3=largest2}largest2=largest}largest=sum} else if(sum>largest2){ if(largest2>largest3){largest3=largest2} largest2=sum} else if(sum>largest3){largest3=sum} sum=0 }} END{ print largest,largest2,largest3; print largest+largest2+largest3 }