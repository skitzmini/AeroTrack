MAJOR_AIRPORTS=[
 {'id':1,'iata':'GRU','icao':'SBGR','name':'Aeroporto Internacional de São Paulo/Guarulhos','city':'São Paulo','country':'Brasil','latitude':-23.4356,'longitude':-46.4731},
 {'id':2,'iata':'GIG','icao':'SBGL','name':'Aeroporto Internacional do Rio de Janeiro/Galeão','city':'Rio de Janeiro','country':'Brasil','latitude':-22.809,'longitude':-43.2506},
 {'id':3,'iata':'JFK','icao':'KJFK','name':'Aeroporto Internacional John F. Kennedy','city':'Nova York','country':'Estados Unidos','latitude':40.6413,'longitude':-73.7781},
 {'id':4,'iata':'LAX','icao':'KLAX','name':'Aeroporto Internacional de Los Angeles','city':'Los Angeles','country':'Estados Unidos','latitude':33.9416,'longitude':-118.4085},
 {'id':5,'iata':'ATL','icao':'KATL','name':'Aeroporto Internacional Hartsfield–Jackson Atlanta','city':'Atlanta','country':'Estados Unidos','latitude':33.6407,'longitude':-84.4277},
 {'id':6,'iata':'ORD','icao':'KORD','name':'Aeroporto Internacional O’Hare','city':'Chicago','country':'Estados Unidos','latitude':41.9742,'longitude':-87.9073},
 {'id':7,'iata':'MIA','icao':'KMIA','name':'Aeroporto Internacional de Miami','city':'Miami','country':'Estados Unidos','latitude':25.7959,'longitude':-80.287},
 {'id':8,'iata':'YYZ','icao':'CYYZ','name':'Aeroporto Internacional Toronto Pearson','city':'Toronto','country':'Canadá','latitude':43.6777,'longitude':-79.6248},
 {'id':9,'iata':'MEX','icao':'MMMX','name':'Aeroporto Internacional da Cidade do México','city':'Cidade do México','country':'México','latitude':19.4361,'longitude':-99.0719},
 {'id':10,'iata':'LHR','icao':'EGLL','name':'Aeroporto de Londres Heathrow','city':'Londres','country':'Reino Unido','latitude':51.47,'longitude':-0.4543},
 {'id':11,'iata':'CDG','icao':'LFPG','name':'Aeroporto Paris Charles de Gaulle','city':'Paris','country':'França','latitude':49.0097,'longitude':2.5479},
 {'id':12,'iata':'FRA','icao':'EDDF','name':'Aeroporto de Frankfurt','city':'Frankfurt','country':'Alemanha','latitude':50.0379,'longitude':8.5622},
 {'id':13,'iata':'AMS','icao':'EHAM','name':'Aeroporto de Amsterdã Schiphol','city':'Amsterdã','country':'Países Baixos','latitude':52.3105,'longitude':4.7683},
 {'id':14,'iata':'MAD','icao':'LEMD','name':'Aeroporto Adolfo Suárez Madrid–Barajas','city':'Madri','country':'Espanha','latitude':40.4983,'longitude':-3.5676},
 {'id':15,'iata':'LIS','icao':'LPPT','name':'Aeroporto Humberto Delgado','city':'Lisboa','country':'Portugal','latitude':38.7742,'longitude':-9.1342},
 {'id':16,'iata':'DXB','icao':'OMDB','name':'Aeroporto Internacional de Dubai','city':'Dubai','country':'Emirados Árabes Unidos','latitude':25.2532,'longitude':55.3657},
 {'id':17,'iata':'DOH','icao':'OTHH','name':'Aeroporto Internacional Hamad','city':'Doha','country':'Catar','latitude':25.2731,'longitude':51.6081},
 {'id':18,'iata':'IST','icao':'LTFM','name':'Aeroporto de Istambul','city':'Istambul','country':'Turquia','latitude':41.2753,'longitude':28.7519},
 {'id':19,'iata':'HND','icao':'RJTT','name':'Aeroporto Internacional de Tóquio Haneda','city':'Tóquio','country':'Japão','latitude':35.5494,'longitude':139.7798},
 {'id':20,'iata':'NRT','icao':'RJAA','name':'Aeroporto Internacional de Narita','city':'Tóquio','country':'Japão','latitude':35.772,'longitude':140.3929},
 {'id':21,'iata':'SIN','icao':'WSSS','name':'Aeroporto de Singapura Changi','city':'Singapura','country':'Singapura','latitude':1.3644,'longitude':103.9915},
 {'id':22,'iata':'HKG','icao':'VHHH','name':'Aeroporto Internacional de Hong Kong','city':'Hong Kong','country':'China','latitude':22.308,'longitude':113.9185},
 {'id':23,'iata':'PEK','icao':'ZBAA','name':'Aeroporto Internacional de Pequim Capital','city':'Pequim','country':'China','latitude':40.0799,'longitude':116.6031},
 {'id':24,'iata':'SYD','icao':'YSSY','name':'Aeroporto de Sydney','city':'Sydney','country':'Austrália','latitude':-33.9399,'longitude':151.1753},
 {'id':25,'iata':'JNB','icao':'FAOR','name':'Aeroporto Internacional O. R. Tambo','city':'Joanesburgo','country':'África do Sul','latitude':-26.1367,'longitude':28.2411},
]

def search_major_airports(query:str)->list[dict]:
    term=query.strip().casefold()
    if not term:return MAJOR_AIRPORTS
    return [airport for airport in MAJOR_AIRPORTS if term in ' '.join(str(value) for value in airport.values()).casefold()]
