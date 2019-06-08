const initialState = {
    channels: [],
    isLoading: false,
    error: null,
};

export default function channels(state = initialState, action) {
    switch (action.type) {
    case 'FETCH_CHANNELS_STARTED': {
        return {
            ...state,
            isLoading: true,
        };
    }
    case 'FETCH_CHANNELS_SUCCEEDED': {


        var items = action.payload.channels;

        return {
            ...state,
            channels: action.payload.channels,
            isLoading: false,
        };
    }
    case 'FETCH_CHANNELS_FAILED': {
        return {
            ...state,
            isLoading: false,
            error: action.payload.error,
        };
    }
    case 'CREATE_CHANNEL_SUCCEEDED': {
        return {
            ...state,
            channels: state.channels.concat(action.payload.channel),
        };
    }
    case 'EDIT_CHANNEL_SUCCEEDED': {
        const {payload} = action;
        const nextChannels = state.channels.map(channel => {
            if (channel._id === payload.channel._id) {
                return payload.channel;
            }

            return channel;
        });
        return {
            ...state,
            channels: nextChannels,
        };
    }
    default: {
        return state;
    }
    }
}
