import React from "react";
import {bindActionCreators} from "redux";
import {connect} from "react-redux";
import {sendMessage, messageUpdated} from "../actions/actions";
import {
    Grid,
    Row,
    Col,
    FormGroup,
    FormControl,
    Navbar,
    Nav,
    NavItem,
    NavDropdown,
    MenuItem,
    Form,
    Checkbox,
    Button,
    ControlLabel,
    container,
    DropdownButton
} from "react-bootstrap";
import {browserHistory} from "react-router";


class Header extends React.Component {
    changeUrl(path){

        browserHistory.push(path)

    }

    render() {

        return (<Navbar>
            <Navbar.Header>
                <Navbar.Brand>
                    <a onClick={() => {this.changeUrl("/")}}>EW scientific</a>
                </Navbar.Brand>
            </Navbar.Header>

                <Nav>
                    <NavItem onClick={() => {this.changeUrl("/")}}>Home</NavItem>
                    <NavDropdown title="Graph versions" id="basic-nav-dropdown">
                        <MenuItem onClick={() => {this.changeUrl("/temp_62")}}>6.2 Temperature</MenuItem>
                        <MenuItem onClick={() => {this.changeUrl("/co2_62")}}>6.2 Co2</MenuItem>
                        <MenuItem onClick={() => {this.changeUrl("/temp_63")}}>6.3 Temperature</MenuItem>
                        <MenuItem onClick={() => {this.changeUrl("/co2_63")}}>6.3 Co2</MenuItem>
                        <MenuItem onClick={() => {this.changeUrl("/co2_contry")}}>6.4 Co2 by contry</MenuItem>
                    </NavDropdown>
                    <NavDropdown title="Docs" id="basic-nav-dropdown">
                        <div><a href="/docs/temperature_CO2_plotter">temperature_CO2_plotter</a></div>
                        <div><a href="/docs/web_visualization">/docs/web_visualization</a></div>
                        <div><a href="/static/docs/index.html">Javascript</a></div>
                    </NavDropdown>
                </Nav>



        </Navbar>)


    }

}

export default Header;