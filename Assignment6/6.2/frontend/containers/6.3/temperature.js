import React from 'react'
import ReactDOM from 'react-dom';
import {bindActionCreators} from 'redux'
import {connect} from 'react-redux'
import {getTemperature} from '../../actions/actions'
import {Grid, Row, Col, DropdownButton, MenuItem, FormGroup, FormControl, Form, ControlLabel} from 'react-bootstrap'
import graph from '../../styles/graph.css'

var myChart;


class Temperature extends React.Component {


    constructor() {
        super();
        this.state = {

            name: '',
            shortName: '',
            displayName: '',
            displayShortName: ''

        };
    }


    updateCanvas() {
        let canvas = ReactDOM.findDOMNode(this.refs.myCanvas);
        let ctx = canvas.getContext('2d');

        if (myChart == undefined) {
            myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: this.props.temperature.years,
                    datasets: [{
                        label: 'Mean temperature in °C per year for ' + this.props.temperature.month,
                        ylabel: 'test',
                        data: this.props.temperature.meanTemperature,
                        backgroundColor: 'rgba(68, 108, 179, 0.2)',
                        borderColor: 'rgba(68, 108, 179,1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    hover: {
                        // Overrides the global setting
                        mode: 'nearest'
                    }
                }
            });
        }

        else {

            myChart.destroy()
            myChart = undefined;
            this.updateCanvas()

        }
    }

    componentWillMount() {
        this.props.getTemperature(1);
    }

    componentDidUpdate() {
        this.updateCanvas();
    }

    dropdownChanged(index) {
        this.props.getTemperature(index + 1);
    }


    render() {
        var months = ["January", "February", "March", "April", "May",
            "June", "July", "August", "September", "October", "November", "December"]

        return ( <div>

                <div className={graph.graph}>
                    <canvas ref="myCanvas"/>
                </div>

                <div className={graph.sidebar}>


                    <Form horizontal onSubmit={(e) => {
                        this.handleSubmit(e)
                    }}>

                        <FormGroup controlId="name" onSubmit={(e) => {
                            this.handleSubmit(e)
                        }}>
                            <Col componentClass={ControlLabel} sm={4}>
                                Month
                            </Col>
                            <Col sm={6}>
                                <DropdownButton title={this.props.temperature.month} id="bg-nested-dropdown">
                                    {months.map((val, index) => {
                                        return <MenuItem key={index} onClick={() => {
                                            this.dropdownChanged(index)
                                        } }>{val}</MenuItem>
                                    })}

                                </DropdownButton>

                            </Col>
                        </FormGroup>

                        <FormGroup controlId="name" onSubmit={(e) => {
                            this.handleSubmit(e)
                        }}>
                            <Col componentClass={ControlLabel} sm={4}>
                                Y min (co2)
                            </Col>
                            <Col sm={6}>
                                <FormControl value={this.state.name} onChange={(e) => {
                                    this.handleChange(e)
                                }}/>
                            </Col>
                        </FormGroup>
                        <FormGroup controlId="shortName">
                            <Col componentClass={ControlLabel} sm={4}>
                                Y max (temp)
                            </Col>
                            <Col sm={6}>
                                <FormControl value={this.state.shortName} onChange={(e) => {
                                    this.handleChange(temp)
                                }}/>
                            </Col>
                        </FormGroup>
                        <FormGroup controlId="displayName" onSubmit={(e) => {
                            this.handleSubmit(e)
                        }}>
                            <Col componentClass={ControlLabel} sm={4}>
                                X min (years)
                            </Col>
                            <Col sm={6}>
                                <FormControl value={this.state.displayName} onChange={(e) => {
                                    this.handleChange(e)
                                }}/>
                            </Col>
                        </FormGroup>
                        <FormGroup controlId="displayShortName">
                            <Col componentClass={ControlLabel} sm={4}>
                                X max (years)
                            </Col>
                            <Col sm={6}>
                                <FormControl value={this.state.displayShortName} onChange={(e) => {
                                    this.handleChange(e)
                                }}/>
                            </Col>
                        </FormGroup>

                    </Form>

                </div>


            </div>
        )
    }
}

// maps the state object to prop object

function mapStateToProps(state) {
    return {
        temperature: state.temperature
    }
}

// matches the dispatch/actions to the prop object
function matchDispatchToProps(dispatch) {
    return bindActionCreators({getTemperature: getTemperature}, dispatch)
}

export default connect(mapStateToProps, matchDispatchToProps)(Temperature);