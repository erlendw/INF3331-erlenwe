import React from 'react'
import ReactDOM from 'react-dom';
import { bindActionCreators } from 'redux'
import { connect } from 'react-redux'
import {getCo2} from '../../actions/actions'
import { Grid, Row, Col } from 'react-bootstrap'
import chatstyle from '../../styles/graph.css'

var myChart;

class Co2 extends React.Component{

    updateCanvas() {
        let canvas = ReactDOM.findDOMNode(this.refs.myCanvas);
        let ctx = canvas.getContext('2d');

        if(myChart == undefined){
            myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: this.props.Co2.years,
                datasets: [{
                    label: 'Co2 per year',
                    data: this.props.Co2.arbitraryCo2Units,
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

        else{

            myChart.destroy()
            myChart = undefined;
            this.updateCanvas()

        }
    }

    componentWillMount() {
        this.props.getCo2();
    }

    componentDidUpdate(){
        this.updateCanvas();
    }

    render() {


        return (<div className={graph.inline}>

                <div className={graph.graph}>

                    <canvas ref="myCanvas" />


                </div>

                <div className={graph.sidebar}></div>


        </div>
        )
    }
}

// maps the state object to prop object

function mapStateToProps(state) {
    return {
        Co2 : state.co2
    }
}

// matches the dispatch/actions to the prop object
function matchDispatchToProps(dispatch) {
    return bindActionCreators({getCo2: getCo2}, dispatch)
}

export default connect(mapStateToProps, matchDispatchToProps)(Co2);