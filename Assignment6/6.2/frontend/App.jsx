import React from 'react';
import { Navbar, Nav, NavItem, NavDropdown, MenuItem, Form, FormGroup, Col, FormControl, Checkbox, Button, ControlLabel, container } from 'react-bootstrap';
import superagent from 'superagent';


import Header from './containers/header';
import text from './styles/text.css'

import Temperature from './containers/Temperature';
import Co2 from './containers/Co2';

import {Router,Route, browserHistory } from 'react-router';




class App extends React.Component {

    render() {
        return (
            <div>
            <Header/>
            <Router history={browserHistory}>
                <Route>
                    <Route path="temp" component={Temperature}/>
                    <Route path="co2"  component={Co2}/>
                </Route>
            </Router>
            </div>
        );
    }
}

export default App;