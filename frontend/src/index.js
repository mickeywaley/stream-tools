// import serviceWorker from './serviceWorker';

import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

import Channel from './views/channel';

import Contact from './views/contact';
import Legal from './views/legal';
import About from './views/about';


const store = configureStore()

ReactDOM.render(
    <Provider store={ store }>
        <ConnectedRouter history={ history }>
            <Switch>
                <Route path='/' component={ App }>
                    <Route exact path="/" component={ Home } />


                    <Route exact path='/channel' component={ Channel } />


                    <Route exact path='/contact' component={ Contact } />

                    <Route exact path='/about' component={ About } />

                    <Route exact path='/legal' component={ Legal } />

                </Route>
            </Switch>
        </ConnectedRouter>
    </Provider>,
    document.getElementById('root')
)

// import { createStore, applyMiddleware } from 'redux';
// import thunk from 'redux-thunk';
// import { Provider } from 'react-redux';
// import { composeWithDevTools } from 'redux-devtools-extension';
// import PlayItemsReducer from './reducers';
// import App from './App';
// import './index.css';

// const rootReducer = (state = {}, action) => {
//   return {
//     PlayItems: PlayItemsReducer(state.PlayItems, action),
//   };
// };

// const store = createStore(
//   rootReducer,
//   composeWithDevTools(applyMiddleware(thunk))
// );

// ReactDOM.render(
//   <Provider store={store}>
//     <App />
//   </Provider>,
//   document.getElementById('root')
// );

// if (module.hot) {
//   module.hot.accept('./App', () => {
//     const NextApp = require('./App').default;
//     ReactDOM.render(
//       <Provider store={store}><NextApp /></Provider>,
//       document.getElementById('root')
//     );
//   });

//   module.hot.accept('./reducers', () => {
//     const nextRootReducer = require('./reducers').default;
//     store.replaceReducer(nextRootReducer);
//   });
// }

// serviceWorker.unregister();




