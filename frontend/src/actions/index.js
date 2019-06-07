import * as api from '../api';

function fetchPlayItemsSucceeded(PlayItems) {
    return {
        type: 'FETCH_PlayItemS_SUCCEEDED',
        payload: {
            PlayItems,
        },
    };
}

function fetchPlayItemsFailed(error) {
    return {
        type: 'FETCH_PlayItemS_FAILED',
        payload: {
            error,
        },
    };
}

function fetchPlayItemsStarted() {
    return {
        type: 'FETCH_PlayItemS_STARTED',
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
        type: 'CREATE_PlayItem_SUCCEEDED',
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
        type: 'EDIT_PlayItem_SUCCEEDED',
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
