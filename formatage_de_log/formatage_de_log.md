# Formatage de log

## Consignes

Vous avez ici un fichier `access_200.log` qui contient des informations sous le format common log format (CLF).

**Exemple**:
```
13.66.139.0 - - [19/Dec/2020:13:57:26 +0100] "GET /index.php?option=com_phocagallery&view=category&id=1:almhuette-raith&Itemid=53 HTTP/1.1" 200 32653 "-" "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)" "-"
```

Il vous faut collecter et énumérer les addresses IP présente et déterminer combien de fois apparaît chaque addresse IP.

Pour chaque addresse IP, il faut déterminer combien de fois celle-ci apparait et lui attribuer ce nombre.

Il faut de préférence stocker ces informations dans un fichier `access.json`.

**Exemple**:
```
{
"13.66.139.0" : 7,
"123.12.14.8" : 3,
...
}
```


