import React from 'react';
import ReactDOM from 'react-dom';
import App from './App.jsx';
import {createStore, applyMiddleware, compose} from 'redux';
import {Provider} from 'react-redux'
import thunk from 'redux-thunk'
import chatApp from './reducers/reducers'

//creates one true store, this saves the state for the entire application
const store = createStore(chatApp, applyMiddleware(thunk))


ReactDOM.render(<Provider store={store}><App /></Provider>, document.getElementById('app'));