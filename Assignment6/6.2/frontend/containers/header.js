import React from 'react'
import { bindActionCreators } from 'redux'
import FontAwesome from 'react-fontawesome'
import { connect } from 'react-redux'
import chatstyle from '../styles/graph.css'
import text from '../styles/text.css'
import { sendMessage, messageUpdated } from '../actions/actions'
import { Grid, Row, Col, FormGroup, FormControl, Navbar, Nav, NavItem, NavDropdown, MenuItem, Form, Checkbox, Button, ControlLabel, container } from 'react-bootstrap'



class Header extends React.Component {

    render() {

        return (<Navbar>
            <Navbar.Header>
                <Navbar.Brand>
                    <a href="#">React-Bootstrap</a>
                </Navbar.Brand>
            </Navbar.Header>
            <Nav>
                <NavItem eventKey={1} href="#">Link</NavItem>
                <NavItem eventKey={2} href="#">Link</NavItem>
                <NavDropdown eventKey={3} title="Dropdown" id="basic-nav-dropdown">
                    <MenuItem eventKey={3.1}>Action</MenuItem>
                    <MenuItem eventKey={3.2}>Another action</MenuItem>
                    <MenuItem eventKey={3.3}>Something else here</MenuItem>
                    <MenuItem divider />
                    <MenuItem eventKey={3.3}>Separated link</MenuItem>
                </NavDropdown>
            </Nav>
        </Navbar>)



    }

}

export default Header;