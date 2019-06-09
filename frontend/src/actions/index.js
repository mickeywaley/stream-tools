import * as api from '../api';


export function fetchChannels(filters) {
    return dispatch => {
        dispatch(fetchChannelsStarted());

        api
            .fetchChannels(filters)
            .then(resp => {
                dispatch(fetchChannelsSucceeded(resp.data));
            })
            .catch(err => {
                dispatch(fetchChannelsFailed(err.message));
            });
    };
}


function fetchChannelsSucceeded(channels) {
    return {
        type: 'FETCH_CHANNELS_SUCCEEDED',
        payload: {
            channels,
        },
    };
}

function fetchChannelsFailed(error) {
    return {
        type: 'FETCH_CHANNELS_FAILED',
        payload: {
            error,
        },
    };
}

function fetchChannelsStarted() {
    return {
        type: 'FETCH_CHANNELS_STARTED',
    };
}




function fetchPlayItemsSucceeded(playitems) {
    return {
        type: 'FETCH_PLAYITEMS_SUCCEEDED',
        payload: {
            playitems,
        },
    };
}

function fetchPlayItemsFailed(error) {
    return {
        type: 'FETCH_PLAYITEMS_FAILED',
        payload: {
            error,
        },
    };
}

function fetchPlayItemsStarted() {
    return {
        type: 'FETCH_PLAYITEMS_STARTED',
    };
}

export function fetchPlayItems() {
    return dispatch => {
        dispatch(fetchPlayItemsStarted());

        api
            .fetchPlayItems()
            .then(resp => {
                dispatch(fetchPlayItemsSucceeded(resp.data));
            })
            .catch(err => {
                dispatch(fetchPlayItemsFailed(err.message));
            });
    };
}

function createPlayItemSucceeded(PlayItem) {
    return {
        type: 'CREATE_PLAYITEM_SUCCEEDED',
        payload: {
            PlayItem,
        },
    };
}

export function createPlayItem({title, description, status = 'Unstarted'}) {
    return dispatch => {
        api.createPlayItem({
            title,
            description,
            status
        }).then(resp => {
            dispatch(createPlayItemSucceeded(resp.data));
        });
    };
}

function editPlayItemSucceeded(PlayItem) {
    return {
        type: 'EDIT_PLAYITEM_SUCCEEDED',
        payload: {
            PlayItem,
        },
    };
}

export function editPlayItem(id, params = {}) {
    return (dispatch, getState) => {
        const PlayItem = getPlayItemById(getState().PlayItems.PlayItems, id);
        const updatedPlayItem = Object.assign({}, PlayItem, params);
        api.editPlayItem(id, updatedPlayItem).then(resp => {
            dispatch(editPlayItemSucceeded(resp.data));
        });
    };
}

function getPlayItemById(PlayItems, id) {
    return PlayItems.find(PlayItem => PlayItem.id === id);
}
