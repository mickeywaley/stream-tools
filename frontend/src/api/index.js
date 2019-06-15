import axios from 'axios';

import https from 'https';

const API_BASE_URL = 'http://freeiptv.cn/backend';
//const API_BASE_URL = 'http://localhost:5000';

const agent = new https.Agent({
    rejectUnauthorized: false
});

const client = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"

    },
    httpsAgent: agent
});

export function fetchPlayItems(filters) {

    var params = {};

    if (filters)
    {
        params.keyword = filters.keyword;

        params.pageSize = filters.pageSize;

        params.pageNum = filters.pageNum;
    }

    return client.get('/playitems', {params});
}


export function createPlayItem(params) {
    return client.post('/playitems', params);
}

export function editPlayItem(id, params) {
    return client.put(`/playitems/${id}`, params);
}

export function fetchChannels(filters) {

    var params = {};

    if (filters)
    {
        params.keyword = filters.keyword;
        params.type  =filters.type;

        params.pageSize = filters.pageSize;

        params.pageNum = filters.pageNum;
    }

    console.log(params)
    return client.get('/channels', {params});

}
