import axios from 'axios';

//const API_BASE_URL = 'http://localhost:5000';

const API_BASE_URL = 'https://freeiptv.cn/backend';

const client = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"

    },
});

export function fetchPlayItems() {
    return client.get('/playitems');
}


export function createPlayItem(params) {
    return client.post('/playitems', params);
}

export function editPlayItem(id, params) {
    return client.put(`/playitems/${id}`, params);
}

export function fetchChannels(keyword) {

    var params = {};

    if (keyword)
    {
        console.log(keyword)
        params.keyword = keyword;
    }

    console.log(params)
    return client.get('/channels', {params});

}
