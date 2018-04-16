#! /usr/bin/python3

### REQUIRES python 3 !!!!

## Run:  ./sample.py
## Reads from stdin and writes to stdout
## For example:
##     ./sample.py <test.txt >test_out.txt

#~ import freeling
from Preprocesamiento.utilities import freeling
import sys, re

## ----------------------------------------------
## -------------    MAIN PROGRAM  ---------------
## ----------------------------------------------

## Modify this line to be your FreeLing installation directory
FREELINGDIR = "/usr/local";

DATA = FREELINGDIR+"/share/freeling/";
LANG="es";

freeling.util_init_locale("default");

# create language analyzer
la=freeling.lang_ident(DATA+"common/lang_ident/ident.dat");

# create options set for maco analyzer. Default values are Ok, except for data files.
op= freeling.maco_options("es");
op.set_data_files( "", 
                   DATA + "common/punct.dat",
                   DATA + LANG + "/dicc.src",
                   DATA + LANG + "/afixos.dat",
                   "",
                   DATA + LANG + "/locucions.dat", 
                   DATA + LANG + "/np.dat",
                   DATA + LANG + "/quantities.dat",
                   DATA + LANG + "/probabilitats.dat");

# create analyzers
tk=freeling.tokenizer(DATA+LANG+"/tokenizer.dat");
sp=freeling.splitter(DATA+LANG+"/splitter.dat");
sid=sp.open_session();
mf=freeling.maco(op);

# activate mmorpho odules to be used in next call 
mf.set_active_options(False, # Usermap 
                      False,  # NumbersDetection
                      True,  # PunctuationDetection
                      False,  # DatesDetection
                      True,  # DictionarySearch
                      True,  # AffixAnalysis 
                      False, # CompoundFile
                      True,   
                      True,  # MultiwordsDetection
                      True,  # NE Recognition 
                      True,  # QuantitiesDetection 
                      True   # ProbabilityAssignment
                      ); 

#~ umap: 'bool', num: 'bool', pun: 'bool', dat: 'bool', dic: 'bool', aff: 'bool', comp: 'bool', rtk: 'bool', mw: 'bool', ner: 'bool', qt: 'bool', prb: 'bool'
                      
0,# UserMap
						#~ 1,# AffixAnalysis
						#~ 1,# MultiwordsDetection
						#~ 0,# NumbersDetection
						#~ 1,# PunctuationDetection
						#~ 0,# DatesDetection
						#~ 1,# QuantitiesDetection
						#~ 1,# DictionarySearch
						#~ 1,# ProbabilityAssignment
						#~ 1);# NE Recognition

# create tagger, sense anotator, and parsers
tg=freeling.hmm_tagger(DATA+LANG+"/tagger.dat",True,2);
sen=freeling.senses(DATA+LANG+"/senses.dat");
parser= freeling.chart_parser(DATA+LANG+"/chunker/grammar-chunk.dat");
dep=freeling.dep_txala(DATA+LANG+"/dep_txala/dependences.dat", parser.get_start_symbol());


def lematizar(linea):		
	cadena = ''
	palabras = linea.split()
	#~ print (palabras)
	for palabra in palabras:
		#~ print (palabra)
		if re.search(r"[^a-zA-ZáéíóúñüÁÉÍÓÚÑÜçàèìòùÀÈÌÒÙäëïöüÄËÏÖÜňù]", palabra):#Las palabras que no contengan sólo letras
			cadena += palabra + ' '
		else:
			if re.search(r"[a-zA-ZáéíóúñüÁÉÍÓÚÑÜçàèìòùÀÈÌÒÙäëïöüÄËÏÖÜňù]{2,}", palabra):#Las palabras que contengan sólo letras
				l = tk.tokenize(palabra + '.')#Se agrega el punto final para que Freeling pueda analizar la palabra
				ls = sp.split(sid,l,False)
				ls = mf.analyze(ls)
				resultado = ''
				for s in ls :
					ws = s.get_words()
					for w in ws :
							resultado += w.get_lemma() + ' '   
				resultado = re.sub('\.', '', resultado)
				cadena += resultado
			else:#Contempla el caso de una sola letra, como una sigla con una sóla letra. Por ejemplo: a quien identifican únicamente como Arne “N” --> En este caso es la N la que entra aquí
				cadena += palabra + ' '
		#~ print (cadena)
	cadena = re.sub('\s+', ' ', cadena)
	return cadena  
	
