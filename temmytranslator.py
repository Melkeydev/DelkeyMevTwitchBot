def replace(cont,a,b):
    	ret = ""; ret = cont;
	
	if ret.find(a + " "):
		ret = ret.replace(a + " ",b + " ");
	if ret.find(" " + a + " "):
		ret = ret.replace(" " + a + " "," " + b + " ");
	if ret.find("--" + a + "--"):
		ret = ret.replace("--" + a + "--","--" + b + "--");
	
	if ret.find('"' + a):
		ret = ret.replace('"' + a, '"' + b);
	if ret.find('"' + a + ","):
		ret = ret.replace('"' + a + ",",'"' + b + ",");
	if ret.find('"' + a + '"'):
		ret = ret.replace('"' + a + '"', '"' + b + '"');
	if ret.find('"' + a + " "):
		ret = ret.replace('"' + a + " ",'"' + b + " ");

	if ret.find("“" + a):
		ret = ret.replace("“" + a,"“" + b);
	if ret.find("“" + a + " "):
		ret = ret.replace("“" + a + " ","“" + b + " ");

	return ret;

def temmytranslate(content):
     ret = ""; ret = content;
     
     ret = replace(ret,"me","meh"); ret = replace(ret,"ME","meh");
     ret = replace(ret,"Me","meh");
     
     ret = replace(ret,"you","U");
     ret = replace(ret,"You","U");
     
     ret = replace(ret,"hello","hOI!!!"); ret = replace(ret,"HELLO","hOI!!!");
     ret = replace(ret,"Hello","hOI!!!");
     
     ret = replace(ret,"hi","hOI!!!"); ret = replace(ret,"HI","hOI!!!");
     ret = replace(ret,"Hi","hOI!!!");
     
     ret = replace(ret,"to","tu"); ret = replace(ret,"TO","tu");
     ret = replace(ret,"To","tu");
     
     ret = replace(ret,"we","WE"); ret = replace(ret,"WE","WE");
     ret = replace(ret,"We","WE");
     
     ret = replace(ret,"like","liek"); ret = replace(ret,"LIKE","liek");
     ret = replace(ret,"Like","liek");
     
     ret = replace(ret,"the","da"); ret = replace(ret,"THE","da");
     ret = replace(ret,"The","da");
     
     ret = replace(ret,"would","wud"); ret = replace(ret,"WOULD","wud");
     ret = replace(ret,"Would","wud");
     
     ret = replace(ret,"human","hooman"); ret = replace(ret,"HUMAN","hooman");
     ret = replace(ret,"Human","hooman");
     ret = replace(ret,"that","dat"); ret = replace(ret,"THAT","dat");
     ret = replace(ret,"That","dat");
     
     ret = replace(ret,"i","tem");
     ret = replace(ret,"I","tem");
     
     ret = replace(ret,"is","iz"); ret = replace(ret,"IS","iz");
     ret = replace(ret,"Is","iz");
      
     ret = replace(ret,"that","dat"); ret = replace(ret,"THAT","dat");
     ret = replace(ret,"That","dat");
     
     ret = replace(ret,"my","ma"); ret = replace(ret,"MY","ma");
     ret = replace(ret,"My","ma");
     
     ret = replace(ret,"im","am"); ret = replace(ret,"IM","am");
     ret = replace(ret,"Im","am");

     ret = replace(ret,"i'm","am"); ret = replace(ret,"M'M","am");
     ret = replace(ret,"I'm","am");
     
     ret = replace(ret,"food","FOOB"); ret = replace(ret,"FOOD","FOOB");
     ret = replace(ret,"Food","FOOB");
     
     ret = replace(ret,"why","y"); ret = replace(ret,"WHY","y");
     ret = replace(ret,"Why","y");
     
     ret = replace(ret,"are","r"); ret = replace(ret,"ARE","r");
     ret = replace(ret,"Are","r");
     
     ret = replace(ret,"with","wit"); ret = replace(ret,"WITH","wit");
     ret = replace(ret,"With","wit");
     
     ret = replace(ret,"then","den"); ret = replace(ret,"THEN","den");
     ret = replace(ret,"Then","den");
     
     ret = replace(ret,"your","ur"); ret = replace(ret,"YOUR","ur");
     ret = replace(ret,"Your","ur");
     
     ret = replace(ret,"stuff","stuf"); ret = replace(ret,"STUFF","stuf");
     ret = replace(ret,"Stuff","stuf");
     
     ret = replace(ret,"some","sum"); ret = replace(ret,"SOME","sum");
     ret = replace(ret,"Some","sum");
     
     ret = replace(ret,"thing","THIN"); ret = replace(ret,"THING","THIN");
     ret = replace(ret,"Thing","THIN");
     
     ret = replace(ret,"speak","spek"); ret = replace(ret,"SPEAK","spek");
     ret = replace(ret,"Speak","spek");
     
     ret = replace(ret,"her","hur"); ret = replace(ret,"HER","hur");
     ret = replace(ret,"her","hur");
     
     ret = replace(ret,"money","MONEE FOR COLLEG"); ret = replace(ret,"MONEY","MONEE FOR COLLEG");
     ret = replace(ret,"money","MONEE FOR COLLEG");
     
     ret = replace(ret,"snow","COLD FLAKES"); ret = replace(ret,"SNOW","COLD FLAKES");
     ret = replace(ret,"Snow","COLD FLAKES");
     
     ret = replace(ret,"water","waters"); ret = replace(ret,"WATER","waters");
     ret = replace(ret,"Water","waters");
     
     ret = replace(ret,"town","tem village"); ret = replace(ret,"TOWN","tem village");
     ret = replace(ret,"Town","tem village");
     
     ret = replace(ret,"home","temmie village"); ret = replace(ret,"HOME","temmie village");
     ret = replace(ret,"Home","temmie village");
     
     ret = replace(ret,"village","tem village"); ret = replace(ret,"VILLAGE","tem village");
     ret = replace(ret,"Village","tem village");
     
     ret = replace(ret,"city","tem village"); ret = replace(ret,"CITY","tem village"); 
     ret = replace(ret,"City","tem village");
     
     ret = replace(ret,"dog","annoyin doggy"); ret = replace(ret,"DOG","annoyin doggy");
     ret = replace(ret,"Dog","annoyin doggy");
     
     ret = replace(ret,"mom","Toriel"); ret = replace(ret,"MOM","Toriel"); 
     ret = replace(ret,"Mom","Toriel");
     
     ret = replace(ret,"toriel","GOAT MOM"); ret = replace(ret,"TORIEL","GOAT MOM");
     ret = replace(ret,"Toriel","GOAT MOM");
     
     ret = replace(ret,"bob","Bob's really cool"); ret = replace(ret,"BOB","Bob's really cool");
     ret = replace(ret,"Bob","Bob's really cool");
     
     ret = replace(ret,"big","BIGS"); ret = replace(ret,"BIG","BIGS");
     ret = replace(ret,"Big","BIGS");
     
     ret = replace(ret,"small","SMOL"); ret = replace(ret,"SMALL","SMOL");
     ret = replace(ret,"Small","SMOL");
     
     ret = replace(ret,"will","wil"); ret = replace(ret,"WILL","wil");
     ret = replace(ret,"Will","wil");
     
     ret = replace(ret,"you","u"); ret = replace(ret,"YOU","u");
     ret = replace(ret,"You","u");
     
     ret = replace(ret,"your","ur"); ret = replace(ret,"YOUR","ur");
     ret = replace(ret,"Your","ur");
     
     ret = replace(ret,"i'll","tem"); ret = replace(ret,"I'LL","tem");
     ret = replace(ret,"I'll","tem");
     
     ret = replace(ret,"i've","tem"); ret = replace(ret,"I'VE","tem");
     ret = replace(ret,"I've","tem");
     
     ret = replace(ret,"your's","ur's"); ret = replace(ret,"YOUR'S","ur's");
     ret = replace(ret,"Your's","ur's");
     ret = replace(ret,"yours","ur's");
     ret = replace(ret,"Yours","ur's"); ret = replace(ret,"YOURS","ur's");

     
     ret = replace(ret,"your'","yer'"); ret = replace(ret,"YOUR'","yer'");
     ret = replace(ret,"Your'","yer'");
     
     ret = replace(ret,"what","WHAT");
     ret = replace(ret,"What","WHAT");
     
     ret = replace(ret,"wat","WHAT"); ret = replace(ret,"WAT","WHAT");
     ret = replace(ret,"Wat","WHAT");    
     
     ret = replace(ret,"shop","tem shop"); ret = replace(ret,"SHOP","tem shop");
     ret = replace(ret,"Shop","tem shop");
     
     ret = replace(ret,"store","tem shop"); ret = replace(ret,"STORE","tem shop");
     ret = replace(ret,"Store","tem shop");

     ret = replace(ret,"u/temmie_bot","tEMMIE");

     return ret;