# Snort
 
## C'est quoi ?
 
 - IDS
 - IPS

## Les modes chez snort

- Packet sniffer
- Packet logger
- IDS 

## Snort component

![](images/snort_architecture.png)

## Mode Packet sniffer
 

###Classique  
```
snort 
```

###Verbeux  
```
snort --v
```

### Données  

```
snort -d
```

## Mode Packet logger

```
snort -l <logfolder> -b
```

## Lecture de packet

```
snort -r <file>
```

## Mode IDS

```
snort -c <configuration_file>
```

```
snort -c <configuration_file> -R <rule_file>
```

## Les règles Snort

### Syntax
```
[Action] [Protocol] [IP1] [Port1] -> [IP2] [Port2] [([Option1, Option2, etc.])]
```

### Exemple
```
alert ip any any -> any any (msg: "IP Packet detected";)
```

## Actions

- alert 
- log
- pass
- drop
- reject

## Protocoles

- ip
- icmp
- tcp
- udp
- ...

## Options

- msg
- flow (to_server, from_client, established,...)
- content
- pcre
- threshold
- sid
- rev


### Matcher une chaîne

```bash
content: "TALOS";
```

### Match négatif:

```bash
content: !"TALOS";
```

### Nous avons les offsets qui permettent de définir le début du scan du packet:

```bash
content: "TALOS"; offset:5;
```

Indique 5 bytes après le début du package.

### Le depth indique la longueur du packer
```bash
content: "TALOS"; offset:5; depth:19;
```

Distance et within sont utilisé pour détecter 
strictement une valeur (distance:[byte];)
non strictement une valeur (within:[byte];)


### fast_pattern permet de mettre la priorité d'évaluation et l'éligibilité à une analise supplémentaire.

```bash
content: "TALOS"; offset:5; depth:19;content:"WORD"; fast_pattern;
```

Comme word est en fast_pattern, l'évaluation commence d'abord par là puis reprend la lecture de gauche à droite normalement si word match.

### Alternative data buffers

- http_*
- file_data
- raw
- sip

### file_data detection 
Spécifique pour détecter les fichiers téléchargé (généralement des page javascript)

```bash
file_data;content:"CollectGarbage";fast_pattern:only;
```

### Trouve un fichier qui contient "CollectGarbage" (souvent utilisé en javascript)

## binary operation:

byte_jump
byte_extract
byte_test
byte_math
