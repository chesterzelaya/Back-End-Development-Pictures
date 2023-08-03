data = [{"event_city":"Washington","event_country":"United States","event_date":"11/16/2022","event_state":"District of Columbia","id":1,"pic_url":"http://dummyimage.com/136x100.png/5fa2dd/ffffff"},{"event_city":"Naples","event_country":"United States","event_date":"11/2/2022","event_state":"Florida","id":2,"pic_url":"http://dummyimage.com/230x100.png/dddddd/000000"},{"event_city":"Youngstown","event_country":"United States","event_date":"7/11/2022","event_state":"Ohio","id":3,"pic_url":"http://dummyimage.com/123x100.png/5fa2dd/ffffff"},{"event_city":"Anaheim","event_country":"United States","event_date":"3/10/2022","event_state":"California","id":4,"pic_url":"http://dummyimage.com/175x100.png/dddddd/000000"},{"event_city":"Newark","event_country":"United States","event_date":"12/25/2022","event_state":"New Jersey","id":5,"pic_url":"http://dummyimage.com/167x100.png/ff4444/ffffff"},{"event_city":"Charlotte","event_country":"United States","event_date":"8/2/2022","event_state":"North Carolina","id":6,"pic_url":"http://dummyimage.com/232x100.png/5fa2dd/ffffff"},{"event_city":"San Antonio","event_country":"United States","event_date":"4/1/2022","event_state":"Texas","id":7,"pic_url":"http://dummyimage.com/237x100.png/ff4444/ffffff"},{"event_city":"Orlando","event_country":"United States","event_date":"7/12/2022","event_state":"Florida","id":8,"pic_url":"http://dummyimage.com/152x100.png/cc0000/ffffff"},{"event_city":"Los Angeles","event_country":"United States","event_date":"8/6/2022","event_state":"California","id":9,"pic_url":"http://dummyimage.com/188x100.png/ff4444/ffffff"},{"event_city":"Miami Beach","event_country":"United States","event_date":"11/19/2022","event_state":"Florida","id":10,"pic_url":"http://dummyimage.com/187x100.png/5fa2dd/ffffff"}]

# print out all the id's and pic_url's from data
sub_data = []
for item in data:
    temp = [item['id'], item['pic_url']]
    sub_data.append(temp)

print(data[1]['pic_url'])


#[[1, 'http://dummyimage.com/136x100.png/5fa2dd/ffffff'], 
#[2, 'http://dummyimage.com/230x100.png/dddddd/000000'], 
#[3, 'http://dummyimage.com/123x100.png/5fa2dd/ffffff'], 
#[4, 'http://dummyimage.com/175x100.png/dddddd/000000'], 
#[5, 'http://dummyimage.com/167x100.png/ff4444/ffffff'], 
#[6, 'http://dummyimage.com/232x100.png/5fa2dd/ffffff'], 
#[7, 'http://dummyimage.com/237x100.png/ff4444/ffffff'], 
#[8, 'http://dummyimage.com/152x100.png/cc0000/ffffff'], 
#[9, 'http://dummyimage.com/188x100.png/ff4444/ffffff'], 
#[10, 'http://dummyimage.com/187x100.png/5fa2dd/ffffff']]