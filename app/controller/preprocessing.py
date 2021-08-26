class preprocessing:

    def remove_punctuation(text):
        return text.translate(str.maketrans('', '', string.punctuation))

    def jaro_distance(sentence,dictionary):
        for k in range(len(sentence)):
            wordx = ["a",0]
            for x, w_dic in enumerate(dictionary):
                jaro_dist = distance.get_jaro_distance(sentence[k], w_dic, winkler=True, scaling=0.1)
                if(jaro_dist > wordx[1]):
                    wordx[1] = jaro_dist
                    wordx[0] = w_dic
            sentence[k] = wordx[0]
        return " ". join(sentence)

    def normalization_per_word(word,dictionary):
        Kata_nonformal = {
            1 : {
            "slang" : ["gak","nda","gk","ndak","nd","tdk","no","nope","g"],
            "baku"    : "tidak"
            },
            2 : {
            "slang" : ["makasih","maasih","makasi","thank","thanks"],
            "baku"    : "terima kasih"
            },
            3 : {
            "slang" : ["kntl","ktl"],
            "baku"    : "kontol"
            },
            4 : {
            "slang" : ["dgn"],
            "baku"    : "dengan"
            },
            5 : {
            "slang" : ["dlm"],
            "baku"    : "dalam"
            },
            6 : {
            "slang" : ["boong"],
            "baku"    : "bohong"
            },
            7 : {
            "slang" : ["jd","jdii","jdinya"],
            "baku"    : "jadi"
            },
            8 : {
            "slang" : ["sj","doang"],
            "baku"    : "saja"
            },
            9 : {
            "slang" : ["jgn","tjangan"],
            "baku"    : "jangan"
            },
            10 : {
            "slang" : ["jg","jga"],
            "baku"    : "juga"
            },
            11 : {
            "slang" : ["banget","bet"],
            "baku"    : "sangat"
            },
            12 : {
            "slang" : ["makin"],
            "baku"    : "semakin"
            }
        }
        jaro = ["a",0]
        for x in enumerate(Kata_nonformal):
            for y in enumerate(Kata_nonformal[x[1]]["slang"]):
                if(word == y[1]):
                    return Kata_nonformal[x[1]]["baku"]

        for x, w_dic in enumerate(dictionary):
            jaro_dist = distance.get_jaro_distance(word, w_dic, winkler=True, scaling=0.1)
            if(jaro_dist > jaro[1]):
                jaro[1] = jaro_dist
                jaro[0] = w_dic
        return jaro[0]

    def normalization(sentence,dictionary):
        for k in range(len(sentence)):
            sentence[k] = preprocessing.normalization_per_word(sentence[k],dictionary)
        return " ". join(sentence)

    def stemming_create():
        factory = StemmerFactory()
        return factory.create_stemmer()

    def stopword_removal(text):
        file1 = open("stopword.txt","r")
        stop_words = set(word_tokenize(file1.read()))
        file1.close()
        filtered_text = [w for w in text if not w in stop_words]
        return filtered_text
    
