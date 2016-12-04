import React from "react";
import ReactDOM from "react-dom";
import {bindActionCreators} from "redux";
import {connect} from "react-redux";
import {predictTheFuture} from "../../actions/actions";
import {
    Grid,
    Row,
    Col,
    DropdownButton,
    MenuItem,
    FormGroup,
    FormControl,
    Form,
    ControlLabel,
    Button
} from "react-bootstrap";
import graph from "../../styles/graph.css";

var myChart;
var oldData;


class Temperature extends React.Component {


    constructor() {
        super();
        this.state = {
            month: 1,
            updateCanvas: true,
            y_min: '',
            y_max: '',
            x_min: '',
            x_max: ''
        };
    }

    handleSubmit() {

        console.log(this.state)

        oldData = this.props.temperature;

        this.props.getTemperature_Param(this.state);
        this.setState({
            updateCanvas: true
        })

    }


    handleReset() {

        this.setState({
            month: 1,
            updateCanvas: true,
            y_min: '',
            y_max: '',
            x_min: '',
            x_max: ''

        });

        this.props.predictTheFuture(1)
    }

    updateCanvas() {
        let canvas = ReactDOM.findDOMNode(this.refs.myCanvas);
        let ctx = canvas.getContext('2d');

        if (myChart == undefined) {
            myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    datasets: [{
                        label: 'Based on actual co2 data',
                        data: this.props.temperature.meanTemperature,
                        backgroundColor: 'rgba(68, 108, 179, 0.2)',
                        borderColor: 'rgba(68, 108, 179,1)',
                        borderWidth: 1
                    },
                        {
                            label: 'Based on estimated co2 data',
                            data: this.props.temperature.predictedMeanTemperatures,
                            backgroundColor: 'rgba(207, 0, 15, 0.2)',
                            borderColor: 'rgba(207, 0, 15, 1)',
                            borderWidth: 1

                        }
                    ]
                },
                options: {
                    scales: {
                        xAxes: [{
                            type: 'linear',
                            position: 'bottom'
                        }]
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
        this.props.predictTheFuture();
    }

    componentDidUpdate() {

        console.log(oldData === this.props.temperature)

        if (!(oldData === this.props.temperature )) {

            this.updateCanvas();
            oldData = this.props.temperature;
        }

    }

    dropdownChanged(index) {
        this.setState({

            month: (index + 1)

        });

        console.log(this.state)
    }

    handleChange(e) {

        switch (e.target.id) {

            case 'y_min':

                this.setState({
                    y_min: e.target.value
                });
                break;
            case 'y_max':

                this.setState({
                    y_max: e.target.value
                });
                break;
            case 'x_min':

                this.setState({
                    x_min: e.target.value
                });
                break;
            case 'x_max':

                this.setState({
                    x_max: e.target.value
                });
                break;
        }
    }


    render() {
        var months = ["January", "February", "March", "April", "May",
            "June", "July", "August", "September", "October", "November", "December"]

        return ( <div>

                <div className={graph.graph}>
                    <canvas ref="myCanvas"/>
                </div>

                <div className={graph.sidebar}>


                    <Form horizontal>

                        <FormGroup controlId="month">
                            <Col componentClass={ControlLabel} sm={4}>
                                Month
                            </Col>
                            <Col sm={6}>

                                <DropdownButton title={months[this.state.month - 1]} id="bg-nested-dropdown">
                                    {months.map((val, index) => {
                                        return <MenuItem key={index} onClick={() => {
                                            this.dropdownChanged(index)
                                        } }>{val}</MenuItem>
                                    })}

                                </DropdownButton>

                            </Col>
                        </FormGroup>

                        <FormGroup controlId="y_min">
                            <Col componentClass={ControlLabel} sm={4}>
                                Y min (temp)
                            </Col>
                            <Col sm={6}>
                                <FormControl type="number" value={this.state.y_min} onChange={(e) => {
                                    this.handleChange(e)
                                }}/>
                            </Col>
                        </FormGroup>
                        <FormGroup controlId="y_max">
                            <Col componentClass={ControlLabel} sm={4}>
                                Y max (temp)
                            </Col>
                            <Col sm={6}>
                                <FormControl type="number" value={this.state.y_max} onChange={(e) => {
                                    this.handleChange(e)
                                }}/>
                            </Col>
                        </FormGroup>
                        <FormGroup controlId="x_min">
                            <Col componentClass={ControlLabel} sm={4}>
                                X min (year)
                            </Col>
                            <Col sm={6}>
                                <FormControl type="number" value={this.state.x_min} onChange={(e) => {
                                    this.handleChange(e)
                                }}/>
                            </Col>
                        </FormGroup>
                        <FormGroup controlId="x_max">
                            <Col componentClass={ControlLabel} sm={4}>
                                X max (year)
                            </Col>
                            <Col sm={6}>
                                <FormControl type="number" value={this.state.x_max} onChange={(e) => {
                                    this.handleChange(e)
                                }}/>
                            </Col>
                        </FormGroup>


                        <FormGroup controlId="buttons">

                            <Col componentClass={ControlLabel} sm={4}>
                                Submit
                            </Col>
                            <Col sm={6}>
                                <Button
                                    onClick={() => {
                                        this.handleSubmit()
                                    }}
                                >Update chart</Button>
                            </Col>


                        </FormGroup>

                        <FormGroup controlId="Reset">

                            <Col componentClass={ControlLabel} sm={4}>
                                Submit
                            </Col>
                            <Col sm={6}>
                                <Button
                                    onClick={() => {
                                        this.handleReset()
                                    }}
                                >Reset chart</Button>
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
    return bindActionCreators({predictTheFuture: predictTheFuture}, dispatch)
}

export default connect(mapStateToProps, matchDispatchToProps)(Temperature);