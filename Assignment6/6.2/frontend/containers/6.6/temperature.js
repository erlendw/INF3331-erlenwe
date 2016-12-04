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
            years:100
        };
    }

    handleSubmit() {

        console.log(this.state)

        oldData = this.props.temperature;

        this.props.predictTheFuture(this.state);

        this.setState({
            updateCanvas: true
        })

    }


    handleReset() {

        this.setState({
            month: 1,
            updateCanvas: true,
            years: 100

        });

        this.props.predictTheFuture(this.state)
    }

    updateCanvas() {
        let canvas = ReactDOM.findDOMNode(this.refs.myCanvas);
        let ctx = canvas.getContext('2d');

        if (myChart == undefined) {
            myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    datasets: [{
                        label: 'Temperature per year based on actual co2 data',
                        data: this.props.temperature.meanTemperature,
                        backgroundColor: 'rgba(68, 108, 179, 0.2)',
                        borderColor: 'rgba(68, 108, 179,1)',
                        borderWidth: 1
                    },
                        {
                            label: 'Temperature per year based on estimated co2 data',
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
            case 'years':
                this.setState({
                    years: e.target.value
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

                        <FormGroup controlId="years">
                            <Col componentClass={ControlLabel} sm={4}>
                                Number of years to predict
                            </Col>
                            <Col sm={6}>
                                <FormControl type="number" value={this.state.years} onChange={(e) => {
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