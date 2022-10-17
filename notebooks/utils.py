class structs:
    '''
    SemEval 2022 data format 
    '''
    def ReviewDict():
        return {
            'review_id':'', 
            'sent_id':'',          # extra, to keep the review-sentences structure in SemEval 2016 
            'text':'',
            'overall_polarity':'', # extra, to keep the Yelp star rating 
            'opinions':[]          # a list of OpnDict objects
        }
    def OpnDict():
        return {
        'Source':[[],[]],
        'Target':[[],[]],
        'Polar_expression':[[],[]],
        'Polarity':'',
        'Intensity':'',
        'Category': '', # extra, to keep the gold label of category in SemEval 2016, eg."FOOD#QUALITY" 
    }