def cleanDataFromDF(DF_toClean):
    import re
    from unidecode import unidecode

    for cD in DF_toClean.columns:
        DF_toClean[cD] = DF_toClean[cD].map(lambda x: re.sub('[,\.!?·:#()]',' ', str(x)))# Convert the titles to lowercase
        DF_toClean[cD] = DF_toClean[cD].map(lambda x: re.sub('[&]','', str(x)))# eliminar &
        DF_toClean[cD] = DF_toClean[cD].map(lambda x: re.sub('[;]','', str(x)))#eliminar ;
        DF_toClean[cD] = DF_toClean[cD].map(lambda x: re.sub('<[^<]+?>',' ', str(x)))#eliminar HTML
        DF_toClean[cD] = DF_toClean[cD].apply(unidecode)
        DF_toClean[cD] = DF_toClean[cD].map(lambda x: re.sub('{|acute|}','', str(x)))
        DF_toClean[cD] = DF_toClean[cD].map(lambda x: re.sub('{|\n|}', '', str(x)))
        DF_toClean[cD] = DF_toClean[cD].map(lambda x: re.sub('{|\[\'|}', '', str(x)))
        DF_toClean[cD] = DF_toClean[cD].map(lambda x: re.sub('{|\'\]|}', '', str(x)))
        DF_toClean[cD] = DF_toClean[cD].map(lambda x: re.sub('{|\'|}', '', str(x)))
        DF_toClean[cD] = DF_toClean[cD].map(lambda x: re.sub('{|\"|}', '', str(x)))
        DF_toClean[cD] = DF_toClean[cD].map(lambda x: re.sub('{|nan|}','', str(x)))
        DF_toClean[cD] = DF_toClean[cD].map(lambda x: re.sub('{|tilde|}','', str(x)))
        DF_toClean[cD] = DF_toClean[cD].map(lambda x: re.sub('{|nbsp|}','', str(x)))
        DF_toClean[cD] = DF_toClean[cD].map(lambda x: re.sub('{|iquest|}','', str(x)))
        DF_toClean[cD] = DF_toClean[cD].map(lambda x: re.sub('{|13|}','', str(x)))
        #DF_toClean[cD] = DF_toClean[cD].map(lambda x: re.sub('[?P=ntilde]',' ', str(x)))
        DF_toClean[cD] = DF_toClean[cD].map(lambda x: x.lower())# Print out the first rows of papers
    DF_toClean[cD].head()
    return DF_toClean