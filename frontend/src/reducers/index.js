import { combineReducers } from 'redux'
import { connectRouter } from 'connected-react-router'

import playitems from './playitems'

export default (history) => combineReducers({
    router: connectRouter(history),
    playitems,
})