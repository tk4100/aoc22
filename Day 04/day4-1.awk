BEGIN{FS=",|-";numenv=0}{if(($1 >= $3 && $2 <= $4) || ($1 <= $3 && $2 >= $4)) numenv+=1 }END{print numenv}
