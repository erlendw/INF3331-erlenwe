import React from 'react'
import ReactDOM from 'react-dom';
import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'
import { getTemperature } from '../../actions/actions'
import { Grid, Row, Col, DropdownButton, MenuItem } from 'react-bootstrap'
import chatstyle from '../../styles/chatwindow.css'
import Chart from 'chart.js';

var myChart;


class Temperature extends React.Component {

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

        var options = { responsive: true, showTooltips: false, fill: false }

        return (<div className={"container"}>


            <canvas ref="myCanvas" />

            <Row>

                <Col>
                    <DropdownButton title={this.props.temperature.month} id="bg-nested-dropdown">
                        {months.map((val, index) => {
                            return <MenuItem key={index} onClick={() => { this.dropdownChanged(index) } }>{val}</MenuItem>
                        })}

                    </DropdownButton>
                </Col>

                <Col>
                    erlend westbye
            </Col>

            </Row>
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
    return bindActionCreators({ getTemperature: getTemperature }, dispatch)
}

export default connect(mapStateToProps, matchDispatchToProps)(Temperature);