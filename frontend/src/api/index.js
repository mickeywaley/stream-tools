import axios from 'axios';

const API_BASE_URL = 'http://localhost:3001/freeiptv';

const client = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
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
