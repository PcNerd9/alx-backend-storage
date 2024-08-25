-- querys the metal_bands table to ranks country origin
-- of bands and order them by number of fans

SELECT origin, SUM(fans) AS nb_fans 
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
