export default (state = [], action) => {
    switch (action.type){
        case 'CO2_LOADING':
            return action.payload;
        case 'CO2_UPDATED':
            return action.payload
        default : return state;

    }
};