const initialState = {
    playitems: [],
    isLoading: false,
    error: null,
};

export default function playitems(state = initialState, action) {
    switch (action.type) {
    case 'FETCH_PLAYITEMS_STARTED': {
        return {
            ...state,
            isLoading: true,
        };
    }
    case 'FETCH_PLAYITEMS_SUCCEEDED': {


        var items = action.payload.playitems;

        var i;
        for (i in items){
            items[i].status = "IN_CHANNEL";
        }

        return {
            ...state,
            playitems: action.payload.playitems,
            isLoading: false,
        };
    }
    case 'FETCH_PLAYITEMS_FAILED': {
        return {
            ...state,
            isLoading: false,
            error: action.payload.error,
        };
    }
    case 'CREATE_PLAYITEM_SUCCEEDED': {
        return {
            ...state,
            playitems: state.playitems.concat(action.payload.playitem),
        };
    }
    case 'EDIT_PLAYITEM_SUCCEEDED': {
        const {payload} = action;
        const nextPlayItems = state.playitems.map(playitem => {
            if (playitem.id === payload.playitem.id) {
                return payload.playitem;
            }

            return playitem;
        });
        return {
            ...state,
            playitems: nextPlayItems,
        };
    }
    default: {
        return state;
    }
    }
}
