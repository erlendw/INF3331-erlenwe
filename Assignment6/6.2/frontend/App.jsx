import React from 'react';
import { Navbar, Nav, NavItem, NavDropdown, MenuItem, Form, FormGroup, Col, FormControl, Checkbox, Button, ControlLabel, container } from 'react-bootstrap';
import superagent from 'superagent';


import header from './styles/header.css'
import text from './styles/text.css'

import Header from './containers/header';

import Temperature_62 from './containers/6.2/Temperature';
import Co2_62 from './containers/6.2/Co2';


import Temperature_63 from './containers/6.3/Temperature';
import Co2_63 from './containers/6.3/Co2';

import Co2_Contry from './containers/6.4/co2_contry';

import {Router,Route, browserHistory } from 'react-router';




class App extends React.Component {

    render() {
        return (
            <div>
            <div className={header.header}></div>
            <Router history={browserHistory}>
                <Route>
                    <Route path="/temp_62" component={Temperature_62}/>
                    <Route path="/co2_62"  component={Co2_62}/>
                    <Route path="/temp_63" component={Temperature_63}/>
                    <Route path="/co2_63"  component={Co2_63}/>
                    <Route path="/co2_contry"  component={Co2_Contry}/>
                </Route>
            </Router>
            </div>
        );
    }
}

export default App;