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
    DropdownButton,
    Jumbotron
} from "react-bootstrap";
import {browserHistory} from "react-router";


class Start extends React.Component {
    changeUrl(path) {

        browserHistory.push(path)

    }

    render() {



        return (<div className="container">


            <Jumbotron>
                <h1>Welcome!</h1>
                <p>Welcome to EW scientific, this is where the rendering of our ready crunched data happens</p>
                <p>All graph attributes can be changed in no perticular order, feel free to test it out! The graphs are in the header option "graph versions"</p>
                <p>The documentation for the python and js files are linked under docs in the header</p>
                <p>This webpage was built using react-js, charts are rendered by <a href="http://www.chartjs.org/">charts.js</a>, documentation is built with
                    <a href="https://github.com/BurntSushi/pdoc"> pdoc</a>  for python and <a href="https://mr-doc.github.io/">mr-doc</a>  for js</p>
                <p>Select the graph you want to view in the dropdown below</p>
                <p> <DropdownButton title="Graph versions" id="basic-nav-dropdown">
                        <MenuItem onClick={() => {this.changeUrl("/temp_62")}}>6.2 Temperature</MenuItem>
                        <MenuItem onClick={() => {this.changeUrl("/co2_62")}}>6.2 Co2</MenuItem>
                        <MenuItem onClick={() => {this.changeUrl("/temp_63")}}>6.3 Temperature</MenuItem>
                        <MenuItem onClick={() => {this.changeUrl("/co2_63")}}>6.3 Co2</MenuItem>
                        <MenuItem onClick={() => {this.changeUrl("/co2_contry")}}>6.4 Co2 by contry</MenuItem>
                        <MenuItem onClick={() => {this.changeUrl("/temp_prediction")}}>6.6 Proprietary Temperature prediction algorythm</MenuItem>
                    </DropdownButton></p>
            </Jumbotron>


        </div>)


    }

}

export default Start;