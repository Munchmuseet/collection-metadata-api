# Introduction
REST API for the Munch Museum. The API contains drawings and sketches by Edward Munch.

The API is also documented with [Postman](https://documenter.getpostman.com/view/2789837/S1TYUbGW).

# Overview
Base URL for the API is https://munch.emuseum.com.
The API only supports the GET method.

Available modules are:
* objects
* people

# Authentication
The API requires an API key. To request a key please contact the [Munch Museum][1].

# General Parameter Summary:
| URL Element | Required | Description |
| --- | --- | --- |
| {module} | Yes | The module to list records from. |
| {view} | No - defaults to configuration | The view to display records in. |
| {id} | No | The unique ID of a single record, if only a single record should be returned. |
| {slug} | No | The title or name of the single record. Not required in most cases. |
| {related-module} | No | The module that should be used to display related records to the given {module}. Not available for all modules. |
| {api-format} | No | The preconfigured API format that the data should be returned in. Default formats are JSON, XML and RDF. |

# Search Parameter Summary:
| URL | Element | Required Description |
| --- | --- | --- |
| /search | Yes | The base of the keyword search. |
| {keyword} | No - defaults to "*" | The word(s) to be used for the keyword search. |
| {module} | No - returns all modules | The module to query records from. |
| {view} | No - defaults to configuration | The view to display queried records in. |
| {api-format} | No | The preconfigured API format that the data should be returned in. |

# Advanced Search Parameter Summary:
| URL | Element | Required Description |
| --- | --- | --- |
| /advancedsearch | Yes | The base of the advanced search. |
| {module} | Yes | The module to search in. |
| {field} | Yes | The field to search on. |
| {field-value} | Yes | The value to search a given field with |
| {view} | No - defaults to configuration | The view to display queried records in. |
| {api-format} | No | The preconfigured API format that the data should be returned in. |

# Result Modifier Parameter Summary:
| URL Element | Required |
| --- | --- |
| ?filter | No |
| ?page | No |
| ?sort | No |
| ?key | When key is required in configuration |

# Searchable fields:
* thesadvsearch
* title
* titleEN

# Filters:
people:
* A list of people who are either artists or depicted. Available people are:
    * Edvard Munch
    * Ingeborg Kaurin
    * Annie Fjeldbu
    * Hildur Christensen
    * Birgit Prestøe
    * Gunnar Heiberg
    * Frøydis Mjølstad
    * Børre Eriksen
    * Eva Kittelsen
    * Hanna Brieschke
    * Karen Bjølstad
    * Helga Rogstad
    * Inger Munch
    * Peter Andreas Munch
    * Sigurd Bødtker
    * Christian Munch
    * Laura Cathrine Munch
    * Claude de Beriot
    * Erik Pedersen
    * Fredrik Stang
    * Hans Jæger
    * Jappe Nilssen
    * August Strindberg
    * Bjørnstjerne Bjørnson
    * Christian Krohg
    * Ellef Larssen
    * Friedrich Nietzsche
    * Karl Wefring
    * Rolf Hansen
    * Annie Stenersen
    * Dorothy Boleyn Drewry
    * Frederick Delius
    * Helge Rode
    * Johan Martin Stenersen
    * Kristian Schreiner
    * Max Dauthendey
    * Nicolai Rygg
    * Nils Hansteen
    * Rosa Meissner
    * Tulla Larsen
    * Andreas Bjølstad
    * Curt Glaser
    * Dagny Konow
    * Fritz Frølich
    * Gerhard Munthe
    * Henrik Ibsen
    * Hermann Schlittgen
    * Hieronymus Heyerdahl
    * Karen Haugen
    * Käte Perls
    * Maggie Torkildsen
    * Sten Stenersen
    * Tupsy Jebe
    * Annie Dauthendey
    * Botho Graf von Schwerin
    * Christian Gierløff
    * Dr. Christopher  Munthe
    * Ebba Ridderstad
    * Eberhard Grisebach
    * Elisabeth Förster-Nietzsche
    * Elsa Glaser
    * Harry Kessler
    * Henriette Olsen
    * Hjørdis Gierløff
    * Holger Drachmann
    * Inger Barth
    * Katja Wallier
    * Laura Munch
    * Line Dedichen
    * Ludwig Justi
    * Marie Linde
    * Marika Pauli
    * Meisse Dørnberger
    * Ole Thingstad
    * Olga Buhre
    * Olga Meissner
    * Pernille Anker Kirkeby
    * Peter Munch
    * Sigbjørn Obstfelder
    * Sophie Munch
    * Thorvald Løchen
    * Aase  Nørregaard
    * Akseli Gallen-Kallela
    * Albert Kollmann
    * Alfred Rütschi
    * Anna Munch
    * Arturo Ciacelli
    * Arve Arvesen
    * Bjarne Falk
    * Cally Monrad
    * Christen Sandberg
    * Christian Skredsvig
    * Céline Cuvelier
    * Daniel Jacobson
    * Edvard Diriks
    * Edvard Storm Munch
    * Else Erichsen (frøken)
    * Emanuel Goldstein
    * Erik Krafft
    * Frida Uhl
    * Frøken Seiersted
    * Georg Brandes
    * Gustaf Uddgren
    * Gustav 2 Adolf
    * Gustav Schiefler
    * Gustav Vigeland
    * Haakon Nyhuus
    * Harald Nørregaard
    * Heggelund
    * Heinrich Hudtwalcker
    * Helge Bäckström
    * Helma Meyer
    * Henrik Dedichen
    * Henry van de Velde
    * Hugo Perls
    * Ingeborg Thingstad
    * Ingse Vibe
    * Jens Thiis
    * Johanne Sophie Munch
    * Josephine Roll
    * Jørgen Engelaug
    * Jørgen Engelhart
    * Karl Jensen-Hjell
    * Kristoffer Stoa
    * Lally Horstmann
    * Louise  Munthe
    * Lucien Dedichen
    * Ludvig Karsten
    * Ludvig Ravensberg
    * Maja Munthe
    * Maria Hudtwalcker
    * Marit Nørregaard
    * Marta Sandal
    * Minchen Torkildsen
    * Nils Collet Vogt
    * Nils Gude
    * Nils Onsager
    * Oda Krohg
    * Oline Mjølstad
    * Ottilie Schiefler
    * Peter Munch Tronhus
    * Professor Caspary
    * Ragnvald Munch
    * Richard Strauss
    * Tor Hedberg
    * Walter Rathenau
    * Wilhelm  Larsen
    * Wilhelm Wartmann

classifications:
* Tegninger
* Malerier
* Brev og notater
* Grafikk
* Frottasje
* Skisse- og notatbøker
* Varia

displayDate:
* Number between 1889-1943

department:
* Munch-samlingen
* Andre eiere. Malerier
* Andre eiere. Tegninger
* Andre eiere. Brev og notater
* Rolf E. Stenersens gave til Oslo by

thesfilter:
* Thesaurus with codes for motifs that can be used as a filter. The available motifs are:
    * 1545220=Mann
    * 1545219=Kvinne
    * 1545272=Stående
    * 1545269=Helfigur
    * 1545271=Sittende
    * 1545217=Menneske
    * 1545240=Landskap
    * 1545237=Tre
    * 1545270=Halvfigur
    * 1545208=Kvinnelig akt
    * 1545227=Bygning
    * 1545335=Liggende
    * 1545279=Kvinnelig
    * 1545373=Hus
    * 1545256=Interiør
    * 1545492=Naken
    * 1545355=Gående
    * 1545257=Bord
    * 1545364=Symbolsk motiv
    * 1545282=Mannsportrett
    * 1545293=Karikatur
    * 1545253=Skog
    * 1545338=Par
    * 1545250=Fjell
    * 1545539=Barnetegninger
    * 1545226=Hest
    * 1545204=Kvinneportrett
    * 1545218=Barn
    * 1545254=Strand
    * 1545244=Gate
    * 1545307=Værelse
    * 1545547=Aula
    * 1545252=Hav
    * 1545110=Ekely
    * 1545225=Hund
    * 1545224=Fauna
    * 1545365=Studiehode
    * 1545264=Arbeider
    * 1545267=Vindu
    * 1545286=Peer Gynt
    * 1545274=Båt
    * 1545325=Livsfrisetematikk
    * 1545339=Vei
    * 1545222=Gutt
    * 1545207=Akt
    * 1545441=Atelier
    * 1545249=Kyst
    * 1545280=Mannlig
    * 1545309=Vann
    * 1545509=Stol
    * 1545495=Annet
    * 1545281=Mannlig akt
    * 1545205=Selvportrett
    * 1545311=Sol
    * 1545247=Jorde
    * 1545295=Kafé
    * 1545268=Figur
    * 1545258=Flaske
    * 1545548=Alma Mater
    * 1545228=Kirke
    * 1545371=Seng
    * 1545296=By
    * 1545245=Hage
    * 1545328=Sykdom/død
    * 1545382=Studietegning
    * 1545342=Skulpturskisse
    * 1545324=Familien
    * 1545343=Krig
    * 1545263=Jordbruk
    * 1545340=Bading
    * 1545259=Glass
    * 1545289=Kongs-Emnerne
    * 1545337=Fugl
    * 1545203=Portrett
    * 1545255=Svaberg
    * 1545514=Dans
    * 1545221=Jente
    * 1545287=John Gabriel Borkman
    * 1545124=Kragerø
    * 1545212=Vinter
    * 1545354=Bygningsarbeider
    * 1545359=Monumentale utkast
    * 1545109=Oslo
    * 1545553=Rådhusutkast
    * 1545549=Historien
    * 1545436=Fjord
    * 1545209=Dobbeltakt
    * 1545284=Illustrasjon
    * 1545322=Bohem
    * 1545261=Spilling
    * 1545366=Vogn
    * 1545243=Blomst
    * 1545358=Øyesykdom
    * 1545260=Gjøremål
    * 1545540=Gunneruds hund
    * 1545215=Venneportrett
    * 1545318=Snø
    * 1545554=Menneskeberget
    * 1545112=Åsgårdstrand
    * 1545368=Sammenkomst
    * 1545424=Utstillingsskisse
    * 1545551=Bergen Børs
    * 1545278=Modell
    * 1545516=Kjærlighet
    * 1545533=Sjalusi
    * 1545229=Bro
    * 1545283=Familieportrett
    * 1545425=Foss
    * 1545491=Uidentifisert motiv
    * 1545288=Når vi døde vågner
    * 1545251=Park
    * 1545433=Tiger
    * 1545552=Freia-frisen
    * 1545300=Kabaret
    * 1545310=Måne
    * 1545113=Hvitsten
    * 1545233=Flora
    * 1545515=Ridning
    * 1545265=Forestilling
    * 1545319=Munch-temaer
    * 1545555=Regnbuen/Freden
    * 1545556=Stormen/Krigen
    * 1545231=Låve
    * 1545242=Elv
    * 1545315=Natt
    * 1545542=Kunnskapens tre
    * 1545381=Gardermoen
    * 1545213=Sommer
    * 1545290=Gengangere
    * 1545432=Løve
    * 1545541=Sofa
    * 1545131=Karl Johans gate
    * 1545206=Dobbeltportrett
    * 1545246=Havn
    * 1545427=Gris
    * 1545532=Aske
    * 1545550=Solen
    * 1545216=Kunstnerportrett
    * 1545234=Frukt
    * 1545235=Eple
    * 1545241=Bekk
    * 1545292=Quickborn
    * 1545370=Øy
    * 1545125=Grünerløkka
    * 1545127=St. Cloud
    * 1545330=Barneportrett
    * 1545527=Stoffveksling
    * 1545299=Berlin
    * 1545544=Kabaret
    * 1545239=Furu
    * 1545291=Charles Baudelaire
    * 1545308=Hedmark
    * 1545530=Vampyr
    * 1545276=Italia
    * 1545344=Eik
    * 1545363=Den fri kjærlighets by
    * 1545374=Thorvald Meyers gate 48
    * 1545385=Hamar
    * 1545115=Warnemünde
    * 1545138=Maridalen
    * 1545140=Nice
    * 1545162=Gamle Aker kirke
    * 1545297=Alm
    * 1545369=Regnbue
    * 1545375=Fossveien 7
    * 1545505=Sirkus
    * 1545535=Kvinnen. Sfinx
    * 1545165=Paris
    * 1545312=Stjerner
    * 1545528=Stemmen
    * 1545536=Løsrivelse
    * 1545116=Bergen
    * 1545137=Oslo omegn
    * 1545139=Nordmarka
    * 1545273=Transport
    * 1545316=Kveld
    * 1545357=Ragnarokk
    * 1545384=Gran
    * 1545521=Skrik
    * 1545534=Melankoli
    * 1545108=Norge
    * 1545301=Teater
    * 1545431=Høns
    * 1545531=Kyss
    * 1545145=Hakloa
    * 1545303=Skøyen
    * 1545326=Marat
    * 1545524=Ved dødssengen
    * 1545537=Tiltrekning
    * 1545121=Bygdøy
    * 1545129=Bad Kösen
    * 1545232=Sykehus
    * 1545248=Kanal
    * 1545285=Henrik Ibsen
    * 1545386=Ringerike
    * 1545525=Døden i sykeværelset
    * 1545529=Madonna
    * 1545114=Tyskland
    * 1545117=Jeløy
    * 1545136=Akerselva
    * 1545214=Vår
    * 1545298=Hedda Gabler
    * 1545367=Bil
    * 1545435=Svane
    * 1545123=Helgelandsmoen
    * 1545132=Thüringen
    * 1545135=Roma
    * 1545211=Høst
    * 1545302=Grønland
    * 1545430=Kalkuner
    * 1545513=Allé
    * 1545517=Angst
    * 1545520=Aften på Karl Johan
    * 1545128=Lübeck
    * 1545130=Elgersburg
    * 1545154=Frankrike
    * 1545158=Ålerud
    * 1545160=København
    * 1545161=Telthusbakken
    * 1545294=Dyrehage
    * 1545333=Det grønne værelset
    * 1545356=Wiesbaden
    * 1545428=Ender
    * 1545526=Den døde mor
    * 1545111=Nordstrand
    * 1545142=Moss
    * 1545143=Grimsrød
    * 1545144=Vestre Aker
    * 1545223=Gruppeportrett
    * 1545230=Bordell
    * 1545388=München
    * 1545389=Weimar
    * 1545429=Gjess
    * 1545448=England
    * 1545519=Angst
    * 1545522=Pubertet
    * 1545134=Olaf Ryes plass 4
    * 1545147=Sandvika
    * 1545148=Asker
    * 1545164=Rivieraen
    * 1545236=Grønnsak
    * 1545238=Bjørk
    * 1545277=Danmark
    * 1545321=Blodblomst
    * 1545323=Eventyrskogen
    * 1545329=Reinhardt-frisen
    * 1545376=Fossveien 9
    * 1545394=Hamburg
    * 1545395=Sveits
    * 1545400=Spania
    * 1545402=Russland
    * 1545444=Antwerpen
    * 1545460=Monaco
    * 1545523=Det syke barn
    * 1545538=Måneskinn

mediaExistence:
* True
* False

# Sortable fields:
* displayDate
* Relevance
* invno

[1]: mailto:christer.gimse@munchmuseet.no?subject=API-key "DBA"
