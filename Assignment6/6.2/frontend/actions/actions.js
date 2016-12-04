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


export const getTemperature_Param = (obj) => {

    var dataToSend = {}

    for(var key in obj){

        console.log(key)

        if(obj.hasOwnProperty(key)){

                console.log(typeof  obj[key])


                if(obj[key] != undefined){
                    if(typeof obj[key] == "string"){
                        if(obj[key].length>0){
                            dataToSend[key] = obj[key]
                        }
                    }
                    if(typeof obj[key] == "number"){
                        dataToSend[key] = obj[key]
                    }
                }


        }
    }

    console.log(dataToSend);


    return (dispatch) => {
        return superagent.post("http://localhost:5000/getTemp").set('Content-Type', 'application/json').send(JSON.stringify(dataToSend)).end((error, response) => {
            if (!error && response) {
                //localStorage.setItem('response', JSON.stringify(response.body))

                var inData = JSON.parse(response.text);

                dispatch(tempUpdated(inData))

            } else {
                console.log('There was an error fetching from GitHub', error);
            }
        });
    }




};

export const getCo2_Param = (obj) => {

    var dataToSend = {}

    for(var key in obj){

        console.log(key)

        if(obj.hasOwnProperty(key)){

                console.log(typeof  obj[key])

                if(obj[key] != undefined){
                    if(typeof obj[key] == "string"){
                        if(obj[key].length>0){
                            dataToSend[key] = obj[key]
                        }
                    }
                    if(typeof obj[key] == "number"){
                        dataToSend[key] = obj[key]
                    }
                }


        }
    }

    console.log(dataToSend);


    return (dispatch) => {
        return superagent.post("http://localhost:5000/getCo2").set('Content-Type', 'application/json').send(JSON.stringify(dataToSend)).end((error, response) => {
            if (!error && response) {
                //localStorage.setItem('response', JSON.stringify(response.body))

                var inData = JSON.parse(response.text);

                dispatch(co2Updated(inData))

            } else {
                console.log('There was an error fetching from GitHub', error);
            }
        });
    }
};


export const getCo2_Param_Contry = (obj) => {

    var dataToSend = {}

    for(var key in obj){

        if(obj.hasOwnProperty(key)){

                console.log(typeof  obj[key])

                if(obj[key] != undefined){
                    if(typeof obj[key] == "string"){
                        if(obj[key].length>0){
                            dataToSend[key] = obj[key]
                        }
                    }
                    if(typeof obj[key] == "number"){
                        dataToSend[key] = obj[key]
                    }
                }


        }
    }


    return (dispatch) => {
        return superagent.post("http://localhost:5000/getCo2ByContry").send(JSON.stringify(dataToSend)).set('Content-Type', 'application/json').end((error, response) => {
            if (!error && response) {
                //localStorage.setItem('response', JSON.stringify(response.body))

                var inData = JSON.parse(response.text);

                dispatch(co2Updated(inData))

            } else {
                console.log('There was an error fetching from GitHub', error);
            }
        });
    }
};

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

export const predictTheFuture = () => {
    return (dispatch) => {
        return superagent.get("http://localhost:5000/predictingTheFuture").set('Content-Type', 'application/json').end((error, response) => {
            if (!error && response) {
                //localStorage.setItem('response', JSON.stringify(response.body))

                var inData = JSON.parse(response.text)

                console.log(inData.years.indexOf(inData.finalrealyear))
                var real_cutoff = inData.years.indexOf(inData.finalrealyear)



                var real_years = inData.years.slice(0,real_cutoff+1)
                var real_temperatures = inData.meanTemperature.slice(0, real_cutoff+1)

                var predicion_years = inData.years.slice(real_cutoff+1)
                var prediction_temperatures =     inData.meanTemperature.slice(real_cutoff+1)





                /*inData.years = real_years;*/
                inData.meanTemperature = real_temperatures;

                var real_scatter = []


                for(var i = 0; i < inData.meanTemperature.length; i++){

                    var scatterpiont = {x: real_years[i],y:real_temperatures[i]}

                    real_scatter.push(scatterpiont)

                }

                var predicted_scatter = []


                for(var i = 0; i < inData.meanTemperature.length; i++){

                    var scatterpiont = {x: predicion_years[i],y:prediction_temperatures[i]}

                    predicted_scatter.push(scatterpiont)

                }

                console.log(real_scatter)


                inData.meanTemperature = real_scatter
                inData.predictedMeanTemperatures = predicted_scatter


                dispatch(tempUpdated(inData))

            } else {
                console.log('There was an error fetching from GitHub', error);
            }
        });
    }
};

