/**
 * Created by erlend on 02.12.2016.
 */
import React from "react";
import ReactDOM from "react-dom";
import {bindActionCreators} from "redux";
import {connect} from "react-redux";
import {getCo2, getCo2_Param_Contry} from "../../actions/actions";
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
    Button,
    Collapse,
    Well
} from "react-bootstrap";
import graph from "../../styles/graph.css";
import text from "../../styles/text.css";

var myChart;
var oldData;


class Co2 extends React.Component {


    constructor() {
        super();
        this.state = {
            year_index: 0,
            year:0,
            y_min: '',
            y_max: '',
            x_min: '',
            x_max: ''
        };
    }

    handleSubmit() {

        console.log(this.state);

        oldData = this.props.Co2;

        this.props.getCo2_Param_Contry(this.state);
        this.setState({
            updateCanvas: true
        })

    }

    handleReset() {

        this.setState({
            year: 1960,
            year_index: 0,
            updateCanvas: true,
            y_min: '',
            y_max: '',
            x_min: '',
            x_max: ''

        });

        this.props.getCo2_Param_Contry({
            year: 1960,
            year_index: 0,
            updateCanvas: true,
            y_min: '',
            y_max: '',
            x_min: '',
            x_max: ''

        });


    }

    updateCanvas() {

        let canvas = ReactDOM.findDOMNode(this.refs.myCanvas);
        let ctx = canvas.getContext('2d');

        if (myChart == undefined) {
            myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: this.props.Co2.contry,
                    datasets: [{
                        label: 'Co2 per capita',
                        data: this.props.Co2.arbitraryCo2Units,
                        backgroundColor: 'rgba(68, 108, 179, 0.2)',
                        borderColor: 'rgba(68, 108, 179,1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    hover: {
                        // Overrides the global setting
                        mode: 'nearest',
                        responsive: true
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
        this.props.getCo2_Param_Contry();
    }

    componentDidUpdate() {

        console.log(oldData === this.props.Co2)

        if (!(oldData === this.props.Co2 )) {

            this.updateCanvas();
            oldData = this.props.Co2;
        }

    }

    dropdownChanged(index) {

        console.log(index)

        this.setState({

            year: this.props.Co2.years[index],
            year_index : index,
            open: false

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

        if (this.props.Co2.years == undefined) {
            var years = []
        }
        else {
            var years = this.props.Co2.years
        }


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
                                Years
                            </Col>
                            <Col sm={6}>

                                <Button onClick={ () => this.setState({open: !this.state.open})}>
                                    {years[this.state.year_index]}
                                </Button>

                            </Col>
                        </FormGroup>


                        <Collapse in={this.state.open}>
                            <div className={text.text}>
                                <Well>
                                    <Row>
                                    {
                                        years.map((year, index) => {

                                            return (
                                                <Col md={3} className={text.clickable} onClick={() => {this.dropdownChanged(index)}}>{year}</Col>
                                            )

                                        })}
                                    </Row>

                                </Well>
                            </div>
                        </Collapse>

                        <FormGroup controlId="y_min">
                            <Col componentClass={ControlLabel} sm={4}>
                                Y min (co2)
                            </Col>
                            <Col sm={6}>
                                <FormControl type="number" value={this.state.y_min} onChange={(e) => {
                                    this.handleChange(e)
                                }}/>
                            </Col>
                        </FormGroup>
                        <FormGroup controlId="y_max">
                            <Col componentClass={ControlLabel} sm={4}>
                                Y max (co2)
                            </Col>
                            <Col sm={6}>
                                <FormControl type="number" value={this.state.y_max} onChange={(e) => {
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
function mapStateToProps(state) {
    return {
        Co2: state.co2
    }
}
// matches the dispatch/actions to the prop object
function matchDispatchToProps(dispatch) {
    return bindActionCreators({getCo2: getCo2, getCo2_Param_Contry: getCo2_Param_Contry}, dispatch)
}

export default connect(mapStateToProps, matchDispatchToProps)(Co2);