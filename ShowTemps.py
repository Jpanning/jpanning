#influx -execute 'use temperatures'
#influx -execute 'precision rfc3339'
#influx -execute 'SELECT airtemp, ambtemp, fermtemp FROM "temp_info" WHERE time > 2021-12-20 tz("America/Detroit")' -database="temperatures" -precision=rfc3339
influx -execute 'SELECT airtemp, ambtemp, fermterm FROM "temp_info" LIMIT 5' -database="temperatures" -precision=rfc3339
