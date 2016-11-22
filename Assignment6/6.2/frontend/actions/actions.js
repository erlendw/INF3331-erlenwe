import superagent from 'superagent';

// action has two parts
// 

//first is the type, these are specified as constants i.e 
// "SEND_MESSAGE"

//the other one is the payload, or any information that the app
//needs to have

//the entire function is called the action creator

export const tempUpdated = (data) => {
    //this returns the action
    console.log(data)
    return {
        type: "TEMPERATURE_UPDATED", //type of action
        payload: data //payload contains the data that will be passed to the event handler
    }
}

export const co2Updated = (data) => {
    //this returns the action
    return {
        type: "CO2_UPDATED", //type of action
        payload: data //payload contains the data that will be passed to the event handler
    }
}




export const getTemperature = (month) => {
    return (dispatch) => {
        return superagent.get("http://localhost:5000/getTemp/" + month).set('Content-Type', 'application/json').end((error, response) => {
            if (!error && response) {
                //localStorage.setItem('response', JSON.stringify(response.body))

                var inData = JSON.parse(response.text)


                var label = []

                inData.years.map((year,index)=>{

                    if(index % 3 == 0){

                        label.push(year)

                    }else{
                        label.push("")
                    }

                })


            
                dispatch(tempUpdated(inData))





                
            } else {
                console.log('There was an error fetching from GitHub', error);
            }
        });
    }
};


export const getCo2 = () => {
    return (dispatch) => {
        return superagent.get("http://localhost:5000/getCo2").set('Content-Type', 'application/json').end((error, response) => {
            if (!error && response) {
                //localStorage.setItem('response', JSON.stringify(response.body))

                var inData = JSON.parse(response.text)

             
            
                dispatch(co2Updated(inData))





                
            } else {
                console.log('There was an error fetching from GitHub', error);
            }
        });
    }
};
